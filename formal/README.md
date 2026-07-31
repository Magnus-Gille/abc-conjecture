# ABCFormal: machine-checked kernel for the Chebyshev-orbit program

Lake subproject of the abc-conjecture repository (not a standalone
GitHub project). Toolchain and mathlib are pinned to the stable pair
v4.32.2; `.lake/` build artifacts are ignored; the lockfile
`lake-manifest.json` is committed.

Scope and axiom boundary: this tree machine-checks selected parts of the
elementary spine of the papers. The current proof inventory is:

- `ABCFormal/W1Lifting.lean`: the general prime-element multiplicity
  identity behind W1, plus an integer smoke test. The instantiation to the
  unramified local valuation ring and its identification with the paper's
  Lucas valuation are not yet formalized.
- `ABCFormal/CompositeAtom/Cayley.lean`: the Cayley inversion fibers,
  primitive-index disjointness, and the split finite-field order
  divisibility used in Lemma 9. The homogeneous atom descent, norm-one
  case, exact cardinality, and Hensel clause are not yet formalized.

Queued work includes the remaining atom lemmas, Hensel/CRT realization,
and layer-cake/truncation. Results that
rest on Baker-type transcendence (Stewart 2013 Lemma 8, hence the
Phase 6 window theorem, and the archimedean estimate) are NOT
formalized; any future use states them as explicit hypotheses —
"verified modulo Stewart (2013)". Statement fidelity (that a Lean
statement says what the paper says) is reviewed adversarially by the
other agent; the kernel guarantees only the proofs.

Acceptance bar (mailbox 0143-codex): `lake build` clean; no `sorry`,
no `admit`, no unsafe/axiom escape hatches; no claim that enumerated
examples certify a universal lemma.

Build: `lake exe cache get && lake build` (from `formal/`).
