# Cross-review record

## Phase 3 reference-integrity addendum

Current v3 candidate:

- Source SHA-256:
  `31afa5cba14edfbcd2b122244ff37c44e89400ca9c14085eb986d825ef939fd0`
- PDF SHA-256:
  `31225a993d29ec53adb22472408852a8f6ba5743569717fa90e96f5c07a4bb5a`

The later full reference audit suspended the Phase 2 signatures below.
Version 3 re-established Ohana--Spicer--Stein, Stewart Theorem 1, and
Ribenboim item 2.13 from primary sources; removed the unsupported Bajorska
content citation; repaired the van der Horst URL; and clarified Guninski's
live display name. The evidence is in
`notes/codex/reference-closure.md`.

Magnus explicitly canceled the planned Claude re-review and directed Codex
to perform the final review itself. The resulting exact-hash approval is
`mailbox/0062-codex.md`. It is deliberately labeled Codex-only and does not
claim a renewed dual signature. All 11 v3 pages were freshly rendered and
inspected, the exact source compiled without diagnostics, and the full
finite search reproduced 664,577 tested primes and zero square lifts.

## Phase 2 frozen candidate (historical)

- Source SHA-256:
  `a42b5458fa94dad482be1db199d9b0d9d81fa2a6e31e19e752c1c51f6a14b9e0`
- PDF SHA-256:
  `1a6c0b77f43a5a7e1a2e86c03ef5bd50413351231c2bd6c0e24db1d587eaa53f`

## Codex-side review

- A fresh mathematical referee checked the final diff and approved the exact
  hashes with no mathematical blocker.
- A separate editorial/novelty referee checked the closest prior art,
  bibliography, priority wording, extracted text, build log, and final
  rendered changes. It approved the exact hashes as a narrowly scoped short
  note with no manuscript blocker.
- Codex compiled the exact source, found no TeX diagnostics, rendered all 11
  pages at 144 dpi, and visually inspected every page.
- The source archive was extracted and built in a clean temporary directory.
- The full finite search was rerun with the reported result:
  664,577 primes tested and zero square lifts.

## Claude-side review

Claude performed a fresh end-to-end review in the existing interactive
collaboration session. It rechecked the final source changes, core
mathematics, citations and priority framing; verified both hashes on disk;
combined a fresh rendered-page inspection with its earlier full PDF passes;
and relied on its prior independent reproduction of the computation.

In `mailbox/0053-claude.md`, Claude states:

> PAPER APPROVED

and judges the exact candidate suitable for publication as-is as a narrowly
scoped short note. Its source and PDF hashes match those above.

Codex's corresponding exact-hash approval is
`mailbox/0054-codex.md`. Both collaborator signatures therefore refer to
identical immutable artifacts.

## Joint venue verdict

After independently checking the current primary policy pages, both agents
recommend Mathematika as the journal target and arXiv math.NT as the
preprint route after human validation. Claude's venue concurrence is
`mailbox/0055-claude.md`; Codex's evidence and proposal are
`mailbox/0058-codex.md`.

INTEGERS, the Journal of Integer Sequences, and Notes on Number Theory and
Discrete Mathematics are excluded for this manuscript as written by their
AI-use rules. The Fibonacci Quarterly is only a fallback after a transparent
presubmission policy inquiry.

## Human-author gate

Even after both AI systems approve the manuscript, their review does not
replace human authorship or journal peer review. The named author must
personally validate the proofs, sources, code, PDF, and AI-use statement
before submission.
