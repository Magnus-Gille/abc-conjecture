# abc-conjecture collaboration — joint status

Updated: 2026-07-30T21:40+02:00 by claude
## PHASE 4 JOINT REVIEW — united opinion signed 2026-07-30
Both agents independently reviewed the audited draft: claude full
line-check plus independent numerics (mailbox/0069: fresh 130-check
implementation, new Theorem 17 realization at (13,0,B,2,+1)); codex
audit, full harness re-verification, and priority pass (0070). The
united opinion (full text mailbox/0071 §3 with the 0072 scope guards;
signatures 0072-codex / 0073-claude):

1. Soundness: no counterexample or fatal error across three independent
   model reviews (Codex, GPT-5.5, Claude); the Prop 15 / Cor 16 /
   Thm 17 Hensel–homogeneity–CRT chain is sound.
2. Relative novelty vs paper 1: confirmed step up. The decisive advance
   is the constructive simultaneous-realization Theorem 17, not the
   degree generalization by itself.
3. Absolute novelty: NOT certified, and concretely narrowed. BDEHWW
   (Adv. Appl. Math. 138 (2022), arXiv:2009.03345) determines the mod-p
   factorization of the fibotomic atoms, which correspond to our branch
   polynomials under x^2 = -4/(X+1); confirmed from both directions
   (fiber-level: notes/claude/fibotomic_bridge_check.py; polynomial
   identity: 0072). Proposition 15 must be repositioned as
   equivalent-after-substitution. Sagan–Tirrell (arXiv:1909.02593,
   original Lucas atoms) and Bluher (arXiv:1707.06877) are missing
   citations. The orbit-level package — genealogy, telescope, Wieferich
   coupling, Theorem 17 — remains unlocated after bounded searches by
   both agents; that is not a priority certification.
4. Joint verdict: promising research draft; MAJOR REVISION required
   before publication-candidate status. Gates: (i) bibliography repair
   plus an explicit change-of-variables lemma; (ii) theorem-by-theorem
   overlap map; (iii) specialist human review in Lucas-atom /
   cyclotomic-valuation language; (iv) Magnus's validation and
   assumption of authorship.

Agreed next steps, in priority order:
1. Overlap map + bibliography repair + specialist reformulation +
   priority-search rerun from fibotomic/Dickson vocabulary. Close
   prior-art map: BDEHWW, Sagan–Tirrell, Bluher, Bhargava–Zieve
   (Finite Fields Appl. 5 (1999) 103–111), Gassert (arXiv:1209.4396).
   This gates everything else.
2. Average-form Conjecture 21: first moment of log W_n over admissible
   seed boxes via Prop 15's exact local densities; conjectural target
   O_ell(n^2) = o(log c_n) (typical orbit quality -> 1); large sieve /
   Chebotarev.
3. Degree unification: ell = 2 recovering paper 1's orbit and
   Lucas–Wieferich criterion as the 2-adic tower; composite degrees via
   multi-layer cyclotomic normalization.

(Previous Phase 4 audit state below.)

## PHASE 4 — prime-genealogy proposal audited; specialist review required
The prime-degree Chebyshev proposal and its supplied Python CLI were imported
on the isolated branch `codex/prime-genealogy-audit`. Commit `6bf6864`
preserves the proposal before audit. The audited working package adds an
explicit universal atom identity, closes four other proof gaps in
Proposition 11/Lemma 2/Theorem 17, hardens API validation, supplies independent
tests and a deterministic reproduction harness, and renders a review PDF.

No counterexample or fatal error was found in the central chain through
Proposition 15, Corollary 16, and Theorem 17. An independent GPT-5.5
adversarial review found five repairable omissions; a closure pass confirmed
all five repaired. This is not peer review or priority certification. The
principal next step is targeted human review by a specialist in Lucas atoms
and cyclotomic valuations, followed by a broader priority search.

Current audited artifacts:
- `paper/prime-genealogy-draft.md`
  ee0c4619b7b2785c58427bb998c0994da5d0c05d2f716534fbad73cbe489317d
- `paper/chebyshev_abc.py`
  b6fe57500db0b80670b8b74b7910155e219253e309c2e85847d9900849403554
- `paper/verification-results-prime-genealogy.json`
  29c54f4ce6fb51c725a7d503ef8435d0cf60eca75d8cb2cb6022e8cc3b89255e
- `output/pdf/prime-genealogy-draft.pdf`
  b4a541571b1372d2d8f1d7a563a59529024b8ceb431c704a88c8b04b44491257

Verification: 11 independent tests pass; the supplied self-test passes; the
deterministic harness checks 278 orbits with 11,398 exact assertions and 110
local roots/Hensel lifts; the PDF compiles without diagnostics and was
visually checked. M5 delegation was attempted twice for a bounded side task,
but the configured credential/service was unavailable, so no M5 output was
used.

(Previous Phase 3 state retained below for history.)

## PHASE 3 — v5 APPROVED: Opus 5 PR gate passed
The full audit in notes/claude/reference-audit.md suspended the historical
v2 signatures (0053/0054). The fresh Codex instance independently closed
the open items in notes/codex/reference-closure.md. The later headless Opus 5
review of exact PR head c0cda73 requested changes in
mailbox/0063-claude.md because the recovered Ohana–Spicer–Stein PDF lacked
the promised stable archive. Version 4 applies the pre-agreed fallback:
the citation is removed and the one-step formula is derived inline from
Lemma 1. It also displays Stewart's inequality before specialization,
governs every tracked PDF, narrows the mailbox-parity wording, clarifies the
historical v2 hash line, and names Opus 5 in the AI disclosure. The second
Opus 5 pass in mailbox/0065-claude.md found stale v3 submission guidance,
an obsolete human-checklist citation, an implicit primitivity hypothesis,
ambiguous `paper/main.tex` provenance, and over-broad model-role wording.
Version 5 resolves all of those items.

Current v5 candidate artifacts:
- paper/main-v5.tex
  a94309b910edb8791ec754fd2da1f013588527d8b50b7efb3080e05c89182c6c
- output/pdf/main-v5.pdf
  7f76868650d478a08d5633b5e37dd99042a75f0bc66d07a6435ca6460e014ec7

Magnus explicitly canceled the planned Claude re-review and directed Codex
to perform the v3 review itself. Approval 0062-codex is therefore Codex-only
and does not reinstate a dual signature. Magnus later authorized Opus 5 as
the PR reviewer. Its first two passes requested changes; its final read-only
pass approved the exact v5 source and PDF hashes in `mailbox/0067-claude.md`
with no required findings. The PDF is 11 pages, compiled without
diagnostics, and visually checked page-by-page. The public-repo rule remains:
never commit gitignored `uncommitted/`. For Phase 3 entries from 0057 onward,
existing odd numbers are Claude messages and even numbers are Codex messages;
0061 is intentionally absent.

(Previous close-state below for history.)
Outcome: **(c) CONCLUDED AND CO-SIGNED** — CONCLUSION.md at
md5 ea12446470cbc6c831a441c30d1d4370 (signatures: 0022-claude,
0023-codex; ratatoskr ping sent, 0024).

## PHASE 2 — COMPLETE 2026-07-26: manuscript approved by both agents
Final artifacts at the Phase 2 close (SHA-256, dual-signed in mailbox
0054-codex / 0053-claude):
- paper/main-v2.tex  a42b5458…b9e0
- output/pdf/main-v2.pdf and the then-current
  output/pdf/radicals-in-iterated-quadratic-abc-transfers.pdf were
  byte-identical at 1a6c0b77…a53f
- source tarball + SHA256SUMS in output/; reproducibility script
  paper/check_square_lifts.py (counts reproduced by both agents).
Title: "Radicals in iterated quadratic abc-transfers" (11 pp).
Venue verdict (final, co-signed 0058/0055 after dual primary-source
verification): journal target Mathematika (LMS AI policy, updated June
2026, expressly permits declared AI use in idea generation, calculation,
and proof construction/verification with full human responsibility —
our embedded disclosure already conforms); arXiv math.NT preprint after
human validation; INTEGERS/JIS/NNTDM excluded (AI bans); Fibonacci
Quarterly fallback only via presubmission inquiry (T&F "core
responsibilities" clause). Magnus owns validation (paper/
HUMAN_VALIDATION_CHECKLIST.md), authorship, and submission.

## PHASE 2 original brief (for the record)
Goal: a paper on the strongest result (the (1,8,9) quadratic orbit:
exact radical identity, Baker–Wüstholz elimination, Lucas–Wieferich
reduction, R < (2/3)c family), cross-reviewed to "suitable for
publication as-is", with novelty/priority checking and a venue
recommendation. Working title: "An iterated quadratic abc orbit and a
Lucas–Wieferich obstruction".
- Division: codex = LaTeX paper + re-derivations + reproducible
  computation + PDF; claude = abc-side priority search (agent running) +
  bibliography + venue recon + adversarial review + toolchain (tectonic
  installing). codex runs complementary Lucas/sequence-identifier search.
- Readiness bar: line-checked proofs; novelty claims surviving BOTH
  searches or explicitly weakened; independently reproduced computation;
  complete references; AI-disclosure + authorship placeholder (Magnus
  submits, not us); both post `PAPER APPROVED <date> <checksum>` against
  identical PDF + source.
- Mailbox convention from here: odd NNNN = claude, even NNNN = codex.

## Participants
- claude (Claude Fable 5 during development; Claude Opus 5 for PR review,
  Claude Code CLI)
- codex (OpenAI Codex, GPT-5-based)

## Branch ledger (all closed, co-signed)
1. A — Wronskian/derivative route: correct but literature-known (Pasten
   arXiv:2106.16165); missing lemma = Small Derivatives Conjecture,
   PROVEN equivalent to abc; certificate floor H ≥ c/(R log₂c). CLOSED.
2. B — Higher/alternating Wronskians: rank-one quotient kills k ≥ 2;
   iterated derivatives lose support/additivity. CLOSED.
3. Q1 — Reyssat exact minimum H* = 601 (dual independent computation). DONE.
4. C — Counting heuristic: T^{θ−1+o(1)}; abc expected true with polynomial
   room; labeled heuristic. CLOSED AS HEURISTIC.
5. Chebyshev/transformation: firsttryabc §11 refuted; exact reduction
   log(c_n/R_n) = log Q_n + O(n²) via Baker–Wüstholz; disproof ⟺
   positive-power Lucas–Wieferich accumulation (open); byproduct: infinite
   family with R_n < (2/3)c_n; no p²|d_j for p ≤ 10⁷, j ≤ 50. CLOSED.
6. E — small ω: ω ≤ 2 classified (Pasten/Mihăilescu); ω = 3 = variable
   generalized-Fermat/varying-S frontier; fixed-ν LFL exponentially weak
   (Pasten 1705.09251 Prop 15.1 CONFIRMED verbatim from PDF). CLOSED.
7. D — Field status: all five citations confirmed (incl. Project LANA
   2026-07-17 and Bright 6.563); IUT unaccepted (Cor 3.12 issue open);
   Joshi rejected by Mochizuki; unaccepted by the broader community, no
   peer review; no other credible claims found; Reyssat record stands;
   Stewart–Yu still general champion (Pasten Invent. 2024 restricted
   improvement; BBLT 2024 density bound). Joshi four-hypotheses audit:
   late extracts (Construction III v4 = arXiv:2401.13508,
   notes/claude/joshi-extracts.md) enabled a bounded JOINT validation —
   all four local defects CONFIRMED at extract level (codex
   notes/codex/joshi-bounded-audit.md; claude
   notes/claude/joshi-assessment-claude.md, with zero-divisor and
   discriminant-index sharpenings); calibrations recorded (items i/iv
   statement-level; ii/iii severity depends on unextracted context); not
   an adjudication of the route; no bearing on abc. CLOSED.

## No-new-line declarations (protocol §5)
- Round two: 0008-codex / 0010-claude.
- Final exchange (restarted after the Joshi-source audit):
  0020-claude / 0021-codex.

## Remaining steps
After PR merge, Magnus's external publication steps are:
1. Complete `paper/HUMAN_VALIDATION_CHECKLIST.md` and personally assume
   responsibility for the proofs, sources, computation, PDF, and AI-use
   disclosure.
2. Obtain independent human number-theorist review if possible.
3. After validation, optionally post to arXiv `math.NT` and submit the
   unchanged v5 manuscript to Mathematika.

Final session close-out and the Munin milestone/status update follow the PR
merge.
