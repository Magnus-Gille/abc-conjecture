# abc-conjecture collaboration — joint status

Updated: 2026-07-26T14:28+02:00 by codex
## PHASE 3 — COMPLETE: reference-integrity round
The full audit in notes/claude/reference-audit.md suspended the historical
v2 signatures (0053/0054). The fresh Codex instance independently closed
the open items in notes/codex/reference-closure.md: the exact
Ohana–Spicer–Stein PDF and Proposition 1 were recovered; Stewart's
author-hosted 1983 scan verifies Theorem 1 and the dyadic \(v_n\)
specialization; the journal-hosted Ribenboim PDF verifies item 2.13;
the unsupported Bajorska content citation was removed; van der Horst's URL
was repaired; and Guninski's `joro` handle was added.

Current frozen artifacts:
- paper/main-v3.tex
  31afa5cba14edfbcd2b122244ff37c44e89400ca9c14085eb986d825ef939fd0
- output/pdf/main-v3.pdf
  31225a993d29ec53adb22472408852a8f6ba5743569717fa90e96f5c07a4bb5a

Magnus explicitly canceled the planned Claude re-review and directed Codex
to perform the final review itself. Approval 0062-codex is therefore
Codex-only and does not reinstate a dual signature. The PDF is 11 pages,
compiled without diagnostics, visually checked page-by-page, and the full
664,577-prime search reproduced zero square lifts. The public-repo rule
remains: never commit gitignored `uncommitted/`. Mailbox parity remains odd
NNNN = claude, even NNNN = codex.

(Previous close-state below for history.)
Outcome: **(c) CONCLUDED AND CO-SIGNED** — CONCLUSION.md at
md5 ea12446470cbc6c831a441c30d1d4370 (signatures: 0022-claude,
0023-codex; ratatoskr ping sent, 0024).

## PHASE 2 — COMPLETE 2026-07-26: manuscript approved by both agents
Final artifacts (SHA-256, dual-signed in mailbox 0054-codex / 0053-claude):
- paper/main-v2.tex  a42b5458…b9e0
- output/pdf/main-v2.pdf = output/pdf/radicals-in-iterated-quadratic-abc-transfers.pdf  1a6c0b77…a53f
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
- claude (Claude Fable 5, Claude Code CLI)
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
No agent work remains. Magnus's external publication steps are:
1. Complete `paper/HUMAN_VALIDATION_CHECKLIST.md` and personally assume
   responsibility for the proofs, sources, computation, PDF, and AI-use
   disclosure.
2. Obtain independent human number-theorist review if possible.
3. After validation, optionally post to arXiv `math.NT` and submit the
   unchanged v3 manuscript to Mathematika.

Session close-out and the Munin milestone/status update are complete.
