# Companion validation report

Date: 2026-07-31

This report records agent-executed checks. It is not the named author's
validation and does not authorize circulation or submission.

## Frozen Phase 8 companion

- Source: `paper/chebyshev-companion.tex` at joint head `2893584`
- PDF: `output/pdf/chebyshev-companion.pdf`
- Pages: 13
- SHA-256:
  `c3a51274fc5e36b0d7c591ac7206ca403f15f2671dad1541829d4e4331267e3f`
- A clean temporary Tectonic rebuild was pixel-identical to the canonical
  PDF on all 13 pages at 120 dpi.
- The canonical PDF was visually inspected page by page; no clipping,
  overlap, broken glyph, or margin failure was found.
- The build log contained no TeX warnings, overfull/underfull boxes,
  undefined references, missing resources, or errors.

## Phase 9 all-degree candidate

- Joint content head before this validation-artifact update: `6d7bc01`
- Source: `paper/chebyshev-companion.tex`
- Source SHA-256:
  `327f149740d44f4551cbaf2dc2a8115b755da00be69a4a72cfc12ccf003d5372`
- PDF: `output/pdf/chebyshev-companion.pdf`
- Pages: 14
- PDF SHA-256:
  `38edec59d62ce9d901e0fd996d21be726e340123272fc2f5c68a247233586f04`
- Change: arbitrary-index coordinate atoms and the bounded iterated local
  mean for every degree, including composite degrees
- Tectonic build: clean; no warning, overfull/underfull box, undefined
  reference, missing resource, or error
- Paper tests: 28/28
- Codex tests: 24/24, including 7/7 independent composite-atom checks
- Claude independent atom checker: 251/251
- Prime-genealogy and research-directions verifiers: exit 0
- A separate clean temporary build and the canonical build rendered
  pixel-identically on all 14 pages at 130 dpi. All 14 pages were visually
  inspected; no clipping, overlap, broken glyph, or margin failure was found.
- Claude's independent manuscript line-review found no required issue; its
  one parity clarification was incorporated before the final build.

## Lean proof kernel

- Toolchain: Lean `v4.32.2`; mathlib `v4.32.2`, both exactly pinned in
  `formal/`
- Combined `lake build`: successful, 8,658 jobs
- `sorry` / `admit` / custom `axiom` / `unsafe` escape-hatch scan over all
  Lean sources: clean
- `#print axioms` for both W1 theorems and the three principal Cayley/index
  theorems reports only `propext`, `Classical.choice`, and `Quot.sound`
- Claude independently rebuilt and repeated the scan and axiom audit with
  matching output; its statement-fidelity verdict is `CONFIRMED` and
  `SIGNATURE-READY` in `mailbox/0149-claude.md`
- Scope boundary: Lean checks the generic prime-element multiplicity lemma,
  Cayley inversion fibers, primitive-index disjointness, and split
  finite-field order divisibility. It does not yet check the local-field
  valuation instantiation, homogeneous atom descent, norm-one case, exact
  root count, Hensel lifting, or the whole manuscript.

## Specialist packet

- Primary PDF: `output/pdf/prime-genealogy-draft.pdf`
- Pages: 32
- SHA-256:
  `7c429c31d49a3297a48291a6326ae6c321c0f22c8d7a6c3254c7862ff3ee9ec4`
- A clean temporary rebuild was pixel-identical to the canonical PDF on all
  32 pages at 120 dpi.
- All 32 canonical pages were visually inspected; no clipping, overlap,
  broken glyph, or margin failure was found.
- Its verifier passed 278 orbits, 11,398 assertions, 12 local cases, 110
  roots, and 110 Hensel lifts.
- Every source URL in the two drafts was checked. All resolved successfully
  except one publisher DOI endpoint that returned an anti-bot 403 after
  resolving to the correct publisher page; this was not a dead DOI.
- The recipient's current affiliation and address were rechecked against
  University of Trento institutional material on 2026-07-31.
- The message remains unsent. Its disclosure now says that preliminary
  technical feedback is being sought before wider circulation, instead of
  making the contradictory promise that validation precedes every form of
  circulation.

## Named-author actions still required

- Read and personally accept every theorem, proof, reference, novelty
  statement, and scope limitation in the final candidate.
- Inspect the final rendered PDF and reproduce the relevant commands.
- Confirm author, affiliation, date, contact details, AI disclosure, venue,
  originality, and submission declarations.
- Explicitly approve the exact specialist email, recipient, subject, and
  attachment before it is placed in a draft or sent.
