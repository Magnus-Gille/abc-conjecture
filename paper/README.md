# Reproduction guide

## Files

- `main-v5.tex` — current reference-audited manuscript source.
- `main-v4.tex` — historical Phase 3 candidate superseded after the second
  Opus 5 review of PR #1.
- `main-v3.tex` — historical Phase 3 candidate superseded after the Opus 5
  review of PR #1.
- `main-v2.tex` — historical Phase 2 candidate whose exact-hash dual
  signatures were suspended by the later reference audit.
- `main.tex` — historical v1 draft retained at its original path because
  mailbox messages 0027--0031 refer to it. It is not the source of
  `../output/pdf/main.pdf`, which is the canonical v5 PDF.
- `check_square_lifts.py` — standard-library Python program used for
  Proposition 11.

The article does **not** claim to prove or disprove the \(abc\) conjecture.
Its contribution is the exact whole-orbit radical identity and the
aggregate repeated-prime quality criterion stated in the manuscript.

## Build

The final PDF was built with Tectonic:

```sh
tectonic --keep-logs --keep-intermediates --outdir ../output/pdf main-v5.tex
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

## Current frozen candidate

The reference-audited v5 candidate has these SHA-256 digests:

```text
a94309b910edb8791ec754fd2da1f013588527d8b50b7efb3080e05c89182c6c  main-v5.tex
7f76868650d478a08d5633b5e37dd99042a75f0bc66d07a6435ca6460e014ec7  main-v5.pdf
1b50506daed1b3cd1f8b1a89989407c619129245642158ba67ade946c85e6056  check_square_lifts.py
```

The v3 approval is Codex-only at Magnus's explicit direction; see
`../mailbox/0062-codex.md`. Opus 5 subsequently requested changes on PR #1
in `../mailbox/0063-claude.md`, and a second pass requested the consistency
fixes recorded in `../mailbox/0065-claude.md`. Version 5 resolves both rounds
and awaits an exact-hash Opus 5 re-review. The historical Phase 2 dual
approvals are preserved in the mailbox but are not signatures on the v5
hashes.

Before submission, the named human author must personally validate the
proofs, sources, code, rendered PDF, and AI-use statement and accept
responsibility for the work.
