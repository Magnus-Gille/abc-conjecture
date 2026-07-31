# abc-conjecture collaboration — joint status

Updated: 2026-07-31T15:10+02:00 by claude
## PHASE 8 — companion note + deep computation (2026-07-31)
Magnus's two assignments executed; final candidate pending joint merge.

1. COMPANION NOTE: paper/chebyshev-companion.tex, final candidate at
   codex faab96b — tex SHA
   4a9b445d9eddd804ede6a6588d27fcbc2b89a9d2720494874c95422f12789906,
   pdf c3a51274…, 13 pages, clean Tectonic build, codex visual pass.
   Content: universal transfer for every degree d >= 2; d-admissible
   normalization + layer genealogy; all-degree radical telescope;
   quadratic realization theorem (b0 = 1 simplification); bounded
   iterated local mean for every prime degree with explicit constants
   (C_2 = (3/2)zeta(2)log2 - (3/8)zeta'(2), independently re-derived);
   fixed-orbit boundary section faithful to the signed Phase 6/7 maps;
   computation section. Claude line-check: 4 required + 3 minor
   findings, ALL applied and re-verified at faab96b (incl. the Stewart
   DOI fix 0105-y — the signed Phase 7 map was already correct).
   Narrowed-novelty and AI-use language per the signed verdicts.

2. LEVEL-7 FACTORIZATION (quadratic orbit, 122 digits): COMPLETE and
   SQUAREFREE — seven distinct primes, all = +-1 mod 512, found by
   codex GMP-ECM (p-1 + two ECM curves), counter-certified by claude
   (exact product, multiplicity, sympy primality), then upgraded to
   recursive Pocklington certificates (codex bundle; claude re-run +
   theorem-use audit). delta_7 = 0 certified.

3. CENSUS: dual-verified through 10^8 by two independent
   implementations (claude companion-matrix; codex quadratic-algebra):
   FOUR Lucas-Wieferich primes total — 65519 (quadratic, rank 455),
   47 and NEW 31220573 (cubic, ranks 24 and 7805143 = 19*547*751),
   53 (quintic, rank 26); none tower-compatible; zero super-Wieferich.
   The new prime was found by claude at 1e8 and reproduced exactly by
   codex. Records committed on both branches.

Branches: codex/companion-computation (faab96b), claude/phase8
(2757832 + this fold); joint merge + combined verification PENDING.

(Phase 7 record below.)

## PHASE 7 — polynomial-window map dual-signed (2026-07-31)
Target (Magnus): the first polynomial window
sum_{p <= q_j^{1+eps}, p^2 | E_j} (v_p-1) log p = o(q_j) for some fixed
eps > 0 — remains OPEN; the phase produced the exact reduction and a
new unconditional theorem. Deliverable:
paper/polynomial-window-phase7-map.md at codex head b1b68d8, map
SHA-256 04e4ffac7055b498617aebf8161fab1a077040166df37eb9128f2e0301aa9884,
dual-accepted 0118-claude / 0119-codex (content), signatures on the
final candidate in 0119/0120.

- Theorems C/D (NEW, unconditional): every fixed lift depth — indeed
  every depth up to o(q^{1-eps}/log q) — is harmless by candidate
  counting alone; the window is EQUIVALENT to its deep-valuation tail
  R_{j,K_j} = o(q_j). Qualitatively sharper than "few Wieferich
  primes": even all-candidates-squared costs only O(q^eps log q).
- Proposition E (dual-derived): every window-squared prime is a
  Lucas-Wieferich prime of the fixed pair (LTE at the unramified
  place; verified on programmed-square seeds). Corollary F: power-
  saving weighted LW bound gives eps < (1-theta)/theta; sharp max-form
  o(q^{1-eps}/log q); fixed-power valuation saving gives
  eps < kappa/(2-kappa). All sufficient; Theorem D's deep tail is
  weaker than each.
- Corollary G (conditional bridge): finiteness of super-Wieferich
  prime ideals for the fixed S-unit (Fellini-Murty JNT 285 (2026),
  scope-labeled: their theorems are for integral bases) implies the
  window for every beta < 2.
- Negative audit (corrected wording): GRH blocked for fixed families
  and window prime-counting; the tested prime is RAMIFIED in its own
  Kummer field (no Frobenius — structurally ill-posed diagonal);
  no large-sieve family; exact Stewart summation stops at
  q^{1+2eps-o(1)}. Source gate: Sanna 2008.12506 non-diagonal
  (threshold exp(B e^{8omega(d)} d^8), verified verbatim) and mod-p
  only; Carella 1712.08166's claimed super-Wieferich finiteness
  REJECTED at proof level — four defects dual-verified from the
  source (orthogonality modulus, false phase identity, invalid shared-
  sum factorization, false geometric-sum evaluation).
- Census (dual-verified to 10^6, two independent implementations):
  LW primes exactly {65519}, {47}, {53} for the three canonical
  pairs; none rank-compatible with its tower; none super-Wieferich.
- United opinion: real unconditional refinement; the exact open
  frontier is the deep-tail estimate, connected to the recognized
  super-Wieferich hypothesis; no proof of the window, the fixed-orbit
  conjecture, or abc.

Cross-review ledger this phase: codex caught four claude wording/
calibration defects (0113); claude required one typo fix and upgraded
the census range (0116); both implementations reproduced each other
exactly. Branches: codex/polynomial-window (b1b68d8), claude/phase7 (2f8f280);
joint/phase7-polynomial-window verified content head 4a7c904 —
combined suite green (28/28 legacy, self-test, prime-genealogy
278/11,398/110, research-directions verifier, square-lift search
664,577 primes zero lifts, codex phase-6/7 tests 12/12, codex census
to 10^6 exact, claude checkers 25/25 + 52/52; artifact hashes
unchanged).

(Phase 6 record below.)

## PHASE 6 — fixed-orbit defect map dual-signed (2026-07-31)
Target (Magnus, route 1): log W_n = o(log c_n) for a fixed admissible
orbit. Deliverable: paper/fixed-orbit-phase6-map.md at codex head
6123eb0, map SHA-256
210ce690b00a4ce5052b9bc442134ae6eb8c4e7f51d230aa989a4e25c474ae3d,
dual-accepted 0102-claude / 0103-codex.

- Theorem A: target <=> per-layer delta_j = o(d^j) <=> log Sq(E_j) =
  o(d^j); the layer-cake identity guards higher valuations.
- Rank localization: every prime contributes its rank-Wieferich excess
  at its birth layer; congruence floor p = +-1 mod q_j
  (q_j = 2^{j+2} quadratic, ell^{j+1} prime degree; descended U-rank
  q_j/2 resp. q_j); fixed-prime cutoffs eventually empty.
- Theorem B (NEW, unconditional, dual-verified from primary sources):
  the moving window p <= q_j exp(gamma log q_j / log log q_j),
  gamma < 1/103.8, contributes o(q_j) defect — Stewart's Lemma 8
  (Acta Math. 211 (2013) 291-314, arXiv:1008.1274; Yu's companion
  ibid. 315-382) — the first unconditional moving block. Window cap
  intrinsic: no polynomial window follows from this lemma.
- Open frontier (named): any window q_j^{1+eps}; the global squarefull
  tail; equivalently log Sq(E_j) = o(q_j). abc implies the target for
  every orbit (circular, labeled); Ribenboim-Walsh (Delta>0 as
  published) and Yabuta (finiteness at Delta<0) recorded with scope.
  Benchmark: Mersenne squarefreeness — analogy, not reduction.
- Certificates: quadratic levels 0-6 / cubic 0-3 / quintic 0-1
  squarefree; next layers unresolved (122/113/85-digit cofactors);
  modular searches clean (quadratic p<=10^7 level 50; cubic p<=10^6
  level 12; quintic p<=10^6 level 8). Finite evidence only.
- United opinion: a rigorous boundary advance identifying exactly
  which rank-Wieferich primes are harmless and where a new idea is
  required; NOT a proof of the fixed-orbit conjecture and not material
  progress on abc.

Cross-review ledger this phase: codex caught two claude defects (the
false (1/2)log E bound, 0095; the Q1 sublinearity under-claim, 0097);
claude required two map corrections (quadratic rank wording,
Ribenboim-Walsh discriminant caveat, 0100), both applied (0101).
Branches: codex/fixed-orbit (6123eb0), claude/phase6 (bce68a2);
joint/phase6-fixed-orbit verified content head aa570e1 — combined
suite green (28/28 legacy tests, self-test, prime-genealogy verifier
278/11,398/110, research-directions verifier, codex fixed-orbit 6/6,
claude fixed-orbit 25/25, map and proof SHA-256 unchanged).

(Phase 5 record below.)

## PHASE 5 — three directions executed and cross-verified (2026-07-31)
Branches: codex/phase5-three-directions (9496b9d; 1414f88 plus README
serializer convention), claude/phase5-three-directions (5232ecb plus
STATUS folds), joint/phase5-three-directions (merge 9ddfe12; signed
mailbox record a54888d). Cross-model verdicts ACCEPT x3, dual-signed in
0086-codex / 0087-claude; three-way convergence on every disputed
scope item.

1. Overlap map complete and dually verified. The manuscript now derives
   Prop 15 from fibotomic factorization via bridge (15.1), carries seven
   verified primary sources, and narrows novelty language accordingly.
   Claude's full line-read of the integrated manuscript at 1414f88 found
   no mathematical errors (0085).
2. CORRECTION to the Phase 4 record: the O(n^2) average target is
   replaced by the unconditional bounded iterated local mean
   L_ell(n) <= C_ell, derived independently by both agents (manuscript
   Theorem 20). The full integer-box mean and its large-square tail
   remain OPEN and so labeled. Averaging W_n itself diverges locally;
   log W_n is essential.
3. The all-degree transfer with corrected Lucas normalization is
   accepted mathematically; novelty is narrowed to the degree-uniform
   normalization / support separation / radical telescope synthesis
   (the transfer is classical and compositional). The quadratic
   programmed-square realization (Theorem Q17,
   notes/claude/quadratic-realization.md, 213-check verification):
   line-checked; corrections applied and accepted (0084-0086);
   destination is the companion unification note, not the prime-degree
   manuscript.

Phase 5 agent work FROZEN: final verification complete at joint
`ac37e7f` (joint/phase5-three-directions; full suite green — 28/28
regression, both harnesses, 130/130 + 6/6 + 80/80 + 213/213 claude
checks, 516,406-seed diagnostic, hashes match; 0090). No agent-side
Phase 5 work remains.

Remaining human/next-work gates: companion-note assembly; specialist
review approval (paper/specialist-review-request.md, UNSENT DRAFT) and
recipients; Magnus validation; any integration to main. Open
obstructions stay open: large-square tail; pointwise Conjecture 22.

(Phase 4 joint review below.)

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
