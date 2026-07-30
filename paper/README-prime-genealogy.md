# Prime-genealogy proposal: audit and reproduction

## Status

This is a research-development package for the proposed paper
“Prime genealogy in Chebyshev \(abc\)-orbits.” It is not peer reviewed,
priority certified, or approved for submission.

Commit `6bf6864` preserves the manuscript and CLI supplied by Magnus from a
ChatGPT Pro session. The Phase 5 branch adds a source-backed overlap
correction, an exact bounded local-mean theorem, and a separately recorded
all-degree Chebyshev/Lucas generalization. The latter is not folded into the
prime-degree paper.

## Files

- `prime-genealogy-draft.md`: audited working manuscript.
- `chebyshev_abc.py`: supplied research CLI with input-validation hardening.
- `test_chebyshev_abc.py`: independent regression tests.
- `verify_prime_genealogy.py`: deterministic reproduction harness.
- `verification-results-prime-genealogy.json`: recorded harness output.
- `chebyshev_research.py`: exact Phase 5 local-mean and all-degree helpers.
- `test_research_directions.py`: independent Phase 5 regression tests.
- `verify_research_directions.py`: deterministic Phase 5 harness.
- `verification-results-research-directions.json`: recorded Phase 5 output.
- `render_prime_genealogy.py`: deterministic review-PDF renderer.
- `prime-genealogy-draft.tex`: generated LaTeX review source.
- `../output/pdf/prime-genealogy-draft.pdf`: rendered review PDF.
- `../notes/codex/prime-genealogy-audit.md`: proof findings and remaining
  publication risks.
- `../notes/codex/phase5-overlap-map.md`: theorem-by-theorem prior-art map.
- `../notes/codex/phase5-average-local-theorem.md`: full local-mean proof
  and the unproved large-square tail.
- `../notes/codex/phase5-degree-unification.md`: companion all-degree
  theorem and normalization proof.
- `specialist-review-request.md`: unsent narrow review request for Magnus's
  approval.

## Commands

Run the supplied self-test:

```sh
python3 chebyshev_abc.py self-test
```

Run both independent regression suites:

```sh
python3 -m unittest -v \
  test_chebyshev_abc.py \
  test_research_directions.py
```

Reproduce the recorded finite verification:

```sh
python3 verify_prime_genealogy.py
python3 verify_research_directions.py
```

Recheck the independently implemented fibotomic bridge:

```sh
python3 ../notes/claude/fibotomic_bridge_check.py
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
primitive_density=1/56
composite_degrees=6,9,10,12,15,30
```

All programs use only the Python standard library. The combined regression
suite currently contains 28 tests.

## Interpretation

The computations test finite instances and guard the implementation. They do
not prove the universal theorems. Proposition 15 is now explicitly positioned
as a fibotomic reformulation rather than new local theory. The strongest
currently unlocated claim is Theorem 17's simultaneous orbit-level
realization. Theorem 20 proves only the iterated truncated/profinite mean;
equality with the full integer-box mean is blocked by an unproved
large-square tail. The prime paper and the all-degree companion theorem both
still require specialist human review, and all novelty language must remain
qualified.
