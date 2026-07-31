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

- Source candidate: `paper/chebyshev-companion.tex` at Codex commit
  `a36eac9`
- Change: arbitrary-index coordinate atoms and the bounded iterated local
  mean for every degree, including composite degrees
- Temporary build: 14 pages
- Tectonic build: clean; no warning, overfull/underfull box, undefined
  reference, missing resource, or error
- Paper tests: 28/28
- Codex tests: 24/24, including 7/7 independent composite-atom checks
- Claude independent atom checker: 251/251
- Prime-genealogy and research-directions verifiers: exit 0
- Final PDF hash and page-by-page visual inspection: pending the Phase 9
  Lean pilots and dual candidate review

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
