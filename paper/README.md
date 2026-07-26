# Reproduction guide

## Files

- `main-v2.tex` — manuscript source.
- `check_square_lifts.py` — standard-library Python program used for
  Proposition 11.

The article does **not** claim to prove or disprove the \(abc\) conjecture.
Its contribution is the exact whole-orbit radical identity and the
aggregate repeated-prime quality criterion stated in the manuscript.

## Build

The final PDF was built with Tectonic:

```sh
tectonic --keep-logs --keep-intermediates --outdir ../output/pdf main-v2.tex
```

The final build completed without TeX warnings, overfull or underfull
boxes, undefined references, or errors.

## Reproduce the finite search

Python 3.10 or newer is recommended. The program has no third-party
dependencies.

```sh
python3 check_square_lifts.py --prime-limit 10000000 --max-j 50
```

Expected output:

```text
prime_limit=10000000
max_j=50
tested_primes=664577
square_lifts=0
```

The program first performs a deterministic exact-versus-modular self-check.
The finite search is not an input to any proof.

## Frozen candidate

The cross-reviewed candidate has these SHA-256 digests:

```text
a42b5458fa94dad482be1db199d9b0d9d81fa2a6e31e19e752c1c51f6a14b9e0  main-v2.tex
1a6c0b77f43a5a7e1a2e86c03ef5bd50413351231c2bd6c0e24db1d587eaa53f  main-v2.pdf
1b50506daed1b3cd1f8b1a89989407c619129245642158ba67ade946c85e6056  check_square_lifts.py
```

Before submission, the named human author must personally validate the
proofs, sources, code, rendered PDF, and AI-use statement and accept
responsibility for the work.

