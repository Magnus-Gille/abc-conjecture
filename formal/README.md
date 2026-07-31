# ABCFormal: machine-checked kernel for the Chebyshev-orbit program

Lake subproject of the abc-conjecture repository (not a standalone
GitHub project). Toolchain and mathlib are pinned to the stable pair
v4.32.2; `.lake/` build artifacts are ignored; the lockfile
`lake-manifest.json` is committed.

Scope and axiom boundary: this tree machine-checks the ELEMENTARY
spine of the papers (starting with the W1 lifting step; queue: atom
lemmas, Hensel/CRT realization, layer-cake/truncation). Results that
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
