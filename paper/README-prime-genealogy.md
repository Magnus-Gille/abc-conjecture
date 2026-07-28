# Prime-genealogy proposal: audit and reproduction

## Status

This is a research-development package for the proposed paper
“Prime genealogy in Chebyshev \(abc\)-orbits.” It is not peer reviewed,
priority certified, or approved for submission.

Commit `6bf6864` preserves the manuscript and CLI supplied by Magnus from a
ChatGPT Pro session. The current task branch contains Codex's proof and
software audit plus an independent GPT-5.5 cross-model review.

## Files

- `prime-genealogy-draft.md`: audited working manuscript.
- `chebyshev_abc.py`: supplied research CLI with input-validation hardening.
- `test_chebyshev_abc.py`: independent regression tests.
- `verify_prime_genealogy.py`: deterministic reproduction harness.
- `verification-results-prime-genealogy.json`: recorded harness output.
- `render_prime_genealogy.py`: deterministic review-PDF renderer.
- `prime-genealogy-draft.tex`: generated LaTeX review source.
- `../output/pdf/prime-genealogy-draft.pdf`: rendered review PDF.
- `../notes/codex/prime-genealogy-audit.md`: proof findings and remaining
  publication risks.

## Commands

Run the supplied self-test:

```sh
python3 chebyshev_abc.py self-test
```

Run the independent regression suite:

```sh
python3 -m unittest -v test_chebyshev_abc.py
```

Reproduce the recorded finite verification:

```sh
python3 verify_prime_genealogy.py
```

Regenerate the review PDF from the audited Markdown:

```sh
python3 render_prime_genealogy.py
tectonic prime-genealogy-draft.tex \
  --outdir ../output/pdf \
  --keep-logs \
  --keep-intermediates
```

Expected headline results:

```text
orbit_count=278
orbit_assertions=11398
local_case_count=12
local_root_count=110
hensel_lift_count=110
```

All programs use only the Python standard library.

## Interpretation

The computations test finite instances and guard the implementation. They do
not prove the universal theorems. The central proof chain has no known
counterexample after the Codex audit and an independent cross-model review,
but it still requires specialist human review, especially Proposition 15,
Corollary 16, and Theorem 17. Novelty language must remain qualified until
that review and a broader priority search are complete.
