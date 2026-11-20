"""Certify the density of the union of specified simple-prime events."""
from collections import defaultdict
from math import isqrt

from abc_odd_rank_squareclass_support import (
    division_values, largest_prime_factors, multiple, odd_prime_divisors_above_three,
)


def ceiling_ratio(numerator, denominator):
    return (numerator + denominator - 1) // denominator


def collect_edges(bound, factors):
    edges = defaultdict(list)
    for a in range(1, isqrt(bound) + 1, 2):
        for b in range(1, isqrt((bound - a*a)//2) + 1):
            p = a*a + 2*b*b
            if factors[p] != p:
                continue
            possible = set()
            for group_order in (p + 1 - 2*a, p + 1 + 2*a):
                for q in odd_prime_divisors_above_three(group_order, factors):
                    possible.add(q)
                    if group_order % 3 == 0:
                        possible.add(3*q)
            w = division_values(p)
            if w(3) != 0:
                for rank in sorted(possible):
                    if w(rank) != 0:
                        continue
                    # Sorted order tests q before 3q. The only other proper
                    # orders would be one or three, both already excluded.
                    if division_values(p*p)(rank) != 0:
                        edges[rank].append(p)
                    break
            w.cache_clear()
    return edges


def miss_probability(edges, contains_three, scale, round_up):
    divide = ceiling_ratio if round_up else lambda a, b: a // b
    children = defaultdict(list)
    child_set = set()
    for rank, primes in edges.items():
        if rank % 3 == 0 and not contains_three:
            continue
        # In the 3|n branch, node 3 denotes the independent event 9|n,
        # of conditional probability 1/3.
        node = rank // 3 if rank % 3 == 0 else rank
        for p in primes:
            assert p > node and p not in child_set
            children[node].append(p)
            child_set.add(p)
    subtree = {}
    included = {}
    for node in sorted(set(children) | child_set, reverse=True):
        unrestricted = must_include = scale
        for child in children.get(node, []):
            unrestricted = divide(unrestricted * subtree[child], scale)
            must_include = divide(must_include * included[child], scale)
        included[node] = divide(must_include, node)
        subtree[node] = included[node] + divide((node-1) * unrestricted, node)
    total = scale
    for root in sorted(set(children) - child_set):
        total = divide(total * subtree[root], scale)
    return total


def main():
    bound = 10**7
    factors = largest_prime_factors(bound + 3 + 2 * isqrt(bound))
    edges = collect_edges(bound, factors)
    assert sum(1 for rank in edges if rank % 3) == 22716
    denominator_squared = multiple(9)[0].denominator
    denominator = isqrt(denominator_squared)
    assert denominator**2 == denominator_squared
    assert denominator == 3**3 * 11 * 67 * 13411
    assert all(factors[p] == p for p in (11, 67, 13411))
    edges[9] = [11, 67, 13411]

    scale = 10**24
    misses = []
    for round_up in (False, True):
        outside = miss_probability(edges, False, scale, round_up)
        inside = miss_probability(edges, True, scale, round_up)
        numerator = 2*outside + inside
        misses.append(ceiling_ratio(numerator, 3) if round_up else numerator//3)
    lo, hi = scale - misses[1], scale - misses[0]
    assert lo * 1000000 > 754723 * scale
    assert hi * 1000000 < 754724 * scale
    print("Certified lower and upper numerators for the event density:", lo, hi)
    print("Common denominator:", scale)
    print("Witness primes:", sum(map(len, edges.values())))


if __name__ == "__main__":
    main()
