"""Check the degree-eight minimum for the pair of conjugate points of order two.

Run with the path to the upstream BelyiDB git archive (.tar.gz). Only Python's
standard library is required. The scan stops after all degree-seven records.
"""

import argparse
import ast
import itertools
import re
import tarfile
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import PurePosixPath


COMMIT = "aa663d2aded41c6844f3237ac26f687f7382bda3"
MISSING = "7T7-[6,6,4]-61-61-421-g1.m"


@lru_cache(maxsize=None)
def expression(text):
    return ast.parse(text.replace("^", "**"), mode="eval").body


def evaluate(node, root, prime):
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return node.value % prime
    if isinstance(node, ast.Name) and node.id == "x":
        return root
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -evaluate(node.operand, root, prime) % prime
    if not isinstance(node, ast.BinOp):
        raise ValueError(ast.dump(node))
    a = evaluate(node.left, root, prime)
    if isinstance(node.op, ast.Pow):
        assert isinstance(node.right, ast.Constant) and type(node.right.value) is int
        return pow(a, node.right.value, prime)
    b = evaluate(node.right, root, prime)
    if isinstance(node.op, ast.Add):
        return (a + b) % prime
    if isinstance(node.op, ast.Sub):
        return (a - b) % prime
    if isinstance(node.op, ast.Mult):
        return (a * b) % prime
    if isinstance(node.op, ast.Div):
        if not b:
            raise ZeroDivisionError
        return a * pow(b, -1, prime) % prime
    raise ValueError(ast.dump(node))


def coefficient_witness(coefficients, defining_polynomial):
    """A nonzero residue certifies c4^3 - 8000*Delta != 0 in characteristic 0."""
    for p in range(11, 2000):
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            continue
        if any(q.denominator % p == 0 for q in defining_polynomial):
            continue
        mod_poly = [q.numerator * pow(q.denominator, -1, p) % p
                    for q in defining_polynomial]
        for r in range(p):
            value = 0
            for a in reversed(mod_poly):
                value = (value * r + a) % p
            if value:
                continue
            try:
                a1, a2, a3, a4, a6 = (evaluate(e, r, p) for e in coefficients)
            except ZeroDivisionError:
                continue
            b2, b4, b6 = a1*a1 + 4*a2, a1*a3 + 2*a4, a3*a3 + 4*a6
            b8 = (b2*b6 - b4*b4) * pow(4, -1, p) % p
            c4 = (b2*b2 - 24*b4) % p
            delta = (-b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6) % p
            if delta and (c4**3 - 8000*delta) % p:
                return p, r
    raise ValueError("No modular certificate found for this model")


def cycle_type(perm):
    unseen = set(range(len(perm)))
    lengths = []
    while unseen:
        i = next(iter(unseen))
        length = 0
        while i in unseen:
            unseen.remove(i)
            i = perm[i]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def inverse(perm):
    result = [0] * len(perm)
    for i, j in enumerate(perm):
        result[j] = i
    return tuple(result)


def compose(left, right):
    return tuple(left[i] for i in right)


def transitive(a, b):
    orbit = {0}
    while True:
        more = orbit | {a[i] for i in orbit} | {b[i] for i in orbit}
        if more == orbit:
            return len(orbit) == len(a)
        orbit = more


def permutation_census(d):
    """Count dessins for one ordering of each multiset of branch partitions."""
    permutations = list(itertools.permutations(range(d)))
    types = {s: cycle_type(s) for s in permutations}
    representatives = {t: s for s, t in types.items()}
    result = Counter()
    for ta, a in representatives.items():
        centralizer = [(g, inverse(g)) for g in permutations if compose(g, a) == compose(a, g)]
        seen = set()
        for b in permutations:
            tb = types[b]
            if b in seen or ta > tb or len(ta) + len(tb) >= d:
                continue
            tc = types[compose(a, b)]
            if tb > tc or len(ta) + len(tb) + len(tc) != d or not transitive(a, b):
                continue
            result[ta, tb, tc] += 1
            seen.update(compose(g, compose(b, gi)) for g, gi in centralizer)
    return result


def check_archive(path):
    by_partition = defaultdict(Counter)
    model_counts = Counter()
    missing = []
    primes = []
    with tarfile.open(path, "r|gz") as archive:
        for member in archive:
            parts = PurePosixPath(member.name).parts
            if len(parts) < 3 or parts[1] != "belyi_db" or not parts[2].isdigit():
                continue
            degree = int(parts[2])
            if degree > 7:
                break
            if len(parts) != 4 or not parts[3].endswith("-g1.m"):
                continue
            assert archive.pax_headers.get("comment") == COMMIT
            name = parts[3]
            text = archive.extractfile(member).read().decode()
            size = int(re.search(r"BelyiDBSize := (\d+);", text)[1])
            profile = re.search(r"\]-([0-9]+)-([0-9]+)-([0-9]+)-g1", name)
            partition = tuple(sorted(tuple(sorted(map(int, block), reverse=True))
                                     for block in profile.groups()))
            by_partition[degree][partition] += size
            entries = re.findall(r"aInvs(\d+) := \[(.*?)\];", text, re.S)
            assert len(entries) == len(re.findall(r"base_field_data_\d+ := ", text))
            assert len(entries) == len(re.findall(r"Append\(~maps, phi\d+\);", text))
            if len(entries) != size:
                missing.append((name, size, len(entries)))
            for k, row in entries:
                model_counts[degree] += 1
                label = "K" + k + "<nu" + k + "> := "
                pattern = re.escape(label) + r"NumberField\(Polynomial\(\[RationalField\(\) \| (.*?)\]\)\)"
                field = re.search(pattern, text, re.S)
                if field:
                    polynomial = tuple(Fraction(v.strip()) for v in field[1].split(","))
                else:
                    assert label + "RationalsAsNumberField();" in text
                    polynomial = (Fraction(0), Fraction(1))
                assert polynomial[-1] == 1
                expressions = [expression(v.strip().replace("nu" + k, "x").replace("K.1", "x"))
                               for v in row.split(",")]
                p, _ = coefficient_witness(expressions, polynomial)
                primes.append(p)
    for d in range(3, 8):
        assert permutation_census(d) == by_partition[d], (d, by_partition[d])
        print(d, sum(by_partition[d].values()), model_counts[d])
    assert missing == [(MISSING, 32, 0)]
    assert len(primes) == 493
    print("Largest witness prime", max(primes))
    print("Missing passport", MISSING, "(32 classes)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", help="BelyiDB git archive at the pinned commit")
    check_archive(parser.parse_args().archive)
