# claude's FINAL sections for CONCLUSION.md (v2 — D2 integrated; Joshi block pending D1)

## SECTION: Preamble and verdict

Two AI agents — claude (Claude Fable 5, Claude Code CLI) and codex (OpenAI
Codex, GPT-5-based) — worked adversarially and cooperatively in this
repository on 2026-07-25 to prove or disprove the abc conjecture, starting
from the prior attempt in `firsttryabc.md`, under the protocol in
`COORDINATION.md`.

**Outcome: (c) — neither a proof nor a disproof.** Every examined line of
attack was refuted, shown to be a published reformulation of abc itself, or
reduced exactly to a recognized open problem. Both agents independently
declared that no viable route remains (mailbox 0008, 0010, 0014), completing
the protocol's two-round no-new-line criterion, and co-sign this report.

What is genuinely established here: a handful of small rigorous results —
the certificate-height floor H ≥ c/(R·log₂c); the exact minimal Reyssat
certificate H* = 601; a Baker–Wüstholz reduction of a quadratic-transform
orbit to an aggregate Lucas–Wieferich problem, with the byproduct of an
explicit unconditional infinite family satisfying R < (2/3)c; the refutation
of `firsttryabc.md` §11's monotonicity claim — plus a precise map of why
each path stops. Nothing here moves the conjecture itself.

## SECTION: Standard reformulations reviewed and not pursued

The classical reformulations were reviewed and deliberately not worked,
because each is known to re-encode abc rather than weaken it:

1. Szpiro-type conductor–discriminant bounds for Frey curves: modified
   Szpiro is equivalent to abc (Oesterlé–Szpiro–Frey dictionary).
2. The modular-degree/congruence-number conjecture deg φ_E ≪ N^{2+ε} is
   known to be tied to abc-type statements at the level of suitable
   formulations (Frey; Mai–Murty; with a gap in the older claimed
   equivalence noted and repaired in Pasten's later account). Modularity
   itself is a theorem, but the polynomial degree bound is exactly where
   abc's content reappears — which is why the FLT machinery does not yield
   abc.
3. Vojta's height conjecture SPECIALIZED to P¹∖{0,1,∞} is (equivalent to)
   the standard abc conjecture — not an equivalence with Vojta's full
   conjecture. The function-field and Nevanlinna analogues of that
   specialization are theorems (Mason–Stothers; Second Main Theorem), and
   the dictionary breaks precisely at the absence of an arithmetic
   derivative — the same obstruction quantified in the technical body via
   Pasten's equivalence.
4. Calibration of depth: abc implies effective Mordell (Elkies), and a
   uniform abc conjecture over number fields implies the absence of Siegel
   zeros for L-functions of the relevant odd real characters / negative
   discriminants (Granville–Stark). A short proof would effectivize large
   parts of diophantine geometry at once.
5. The unconditional frontier is exponential: Stewart–Yu (2001)
   log c ≪ R^{1/3}(log R)³ via linear forms in logarithms; the "one more
   log" barrier of LFL is a recognized wall, whose fixed-ω shadow is
   documented in the technical body.

## SECTION: Disproof-side heuristic summary

The powerful-skeleton counting model (notes/claude/disproof-side.md,
codex-audited) predicts T^{θ−1+o(1)} triples at height T whose radical is
T^θ, hence finitely many above any fixed quality 1+δ: abc is expected TRUE
with polynomial room. This is evidence, not proof — the model assumes
independence of additive structure from powerful-part structure, which is
exactly what nobody can prove. All unconditional constructions
(lifting-the-exponent families; Stewart–Tijdeman → van Frankenhuijsen →
Bright, CMB 67 (2024): infinitely many triples with c/R >
exp(6.563·√(log c)/log log c); our Chebyshev orbit with R_n < (2/3)c_n)
certify only sub-polynomial excess; they neither establish an infinite
fixed-quality-gap family nor prove that the selected sequences tend to
quality one. The Robert–Stewart–Tenenbaum
refinement (BLMS 46 (2014)) conjectures the extremal order
log(c/R) ~ 4√3·√(log R/log log R); the proven lower-bound constant 6.563
sits just below the conjectured extremal 4√3 ≈ 6.928. Computation agrees:
Reyssat's q ≈ 1.6299 (1987) is still the record; ABC@Home enumerated all
triples with c < 10¹⁸ exhaustively by 2011, and a later NON-exhaustive
extension brought the catalogue to ≈23.8 million q > 1 triples before the
project wound down by 2015.

## SECTION: Status of claimed proofs (verified 2026-07-25; sources in
notes/claude/field-status-2026.md)

- Mochizuki's IUT proof (published PRIMS 2021) remains unaccepted by the
  broad community. The Scholze–Stix 2018 objection to IUT-III Corollary 3.12
  stands unretracted and unresolved. The most concrete 2026 development is
  the 17 July 2026 interim report of ZEN University's Project LANA ("Lean
  for ANAbelian geometry" — a Lean formalization effort led by Fumiharu
  Kato, with Commelin, Kedlaya, Hoshi, Topaz among core members): judgment
  explicitly remains suspended, with the unresolved point being precisely
  the derivation of Corollary 3.12 from Theorem 3.11 (whether two q-pilot
  log-volume computations are "tautologically equivalent") — the same step
  Scholze–Stix attacked in 2018. The $1M IUGC Challenger Prize for a
  peer-reviewed disproof of IUT remains unclaimed.
- Kirti Joshi's independent claimed proof (series "Construction of
  Arithmetic Teichmuller Spaces" I–IV, IV = arXiv:2403.10430 "…Proof of the
  abc-conjecture", rev. Feb 2025; plus "Final Report on the
  Mochizuki–Scholze–Stix Controversy", arXiv:2505.10568) is rejected by
  Mochizuki (Mar 2024 report: "no meaningful mathematical content
  whatsoever") and viewed pessimistically by the wider community (experts
  polled by Woit, Sep 2025). No part has peer-reviewed acceptance.
- Our own bounded source-level audit of four specific alleged gaps in
  Joshi's construction: [PENDING D1 — to be filled]
- Our search found no other credible 2024–2026 proof/disproof claim
  (Letendre arXiv:2607.07641 proposes a different conjecture; remaining
  items found are non-serious self-published preprints).
- Unconditional progress since 2001 is real but structurally limited:
  Pasten (Invent. Math. 236, 2024) improves Stewart–Yu only in a restricted
  subexponential regime; Bernert–Browning–Lichtman–Teräväinen
  (arXiv:2410.12234) give a power-saving bound on the exceptional-set COUNT
  — a density statement, not a height bound.

We are not a referee committee; the Joshi/IUT observations above are audit
findings and community-status reporting, not mathematical adjudication.

## SECTION: Termination statement

Per COORDINATION.md §5: every proposed attack line is refuted, closed as
abc-equivalent, or reduced to a named open problem (see technical body and
branch table in STATUS.md); rounds two and three produced no new viable
line from either agent. Criteria for outcome (c) are met. Signatures follow
in mailbox (`SIGNED` messages from both agents).
