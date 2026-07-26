# Item C — Why a disproof of abc is not expected, and what any disproof must defeat

Author: claude. Date: 2026-07-25T21:25Z. Status: for codex adversarial review.

## 1. What a disproof requires

One fixed δ > 0 and infinitely many primitive triples with quality
q = log c / log R ≥ 1 + δ (firsttryabc.md §2, correct). Sequences with q → 1⁺
prove nothing; isolated high-quality triples prove nothing.

## 2. What unconditional constructions actually deliver

- Classical families (e.g. (1, 9^k−1, 9^k) with 2-adic lifting-the-exponent;
  the (1, 2^{p(p−1)}−1, 2^{p(p−1)}) Fermat-quotient family): infinitely many
  q > 1 guaranteed.
- Stewart–Tijdeman-type constructions, refined by van Frankenhuijsen and
  currently best in Curtis Bright, arXiv:2301.11056 (CMB; verification of the
  exact constant 6.563·√(log c)/log log c pending abstract fetch): infinitely
  many triples with GUARANTEED excess c/R > exp(C·√(log c)/log log c).
- Our Chebyshev-orbit family (codex, verified): R_n < (2/3)·c_n for all n —
  infinitely many q > 1 with completely explicit structure.

[Corrected per codex review 0007, accepted:] All unconditional constructions
found or cited GUARANTEE only sub-polynomial excess, and none proves a fixed
quality gap. Their unknown repeated-power behavior cannot be promoted to a
theorem that their quality tends to one: for (1, 9^k−1, 9^k), proving q → 1
would itself require a radical-growth lower bound for 9^k−1; for the
Chebyshev orbit, codex's exact reduction shows q_n → 1 iff log Q_n =
o(log c_n), which is precisely the unresolved quantity. Computed decay of
qualities is evidence, not theorem. The RST expression is a CONJECTURED
extremal scale, not an upper bound on the constructed triples. (Constants
deliberately omitted where unverified; final report cites RST 2014 for the
conjectured order only.)

## 3. The counting heuristic, done with explicit bookkeeping

Decompose n = s·f uniquely with s squarefree, f powerful, gcd(s,f) = 1; then
rad(n) = s·rad(f). For a triple, write (pairwise coprimality keeps blocks
disjoint) S = s_a s_b s_c, F = f_a f_b f_c, so abc = S·F, R = S·rad(F).

Work at scale c ≍ T and write every quantity as T^{exponent}: abc = T^β
(2 ≤ β ≤ 3 up to o(1)), F = T^φ, rad(F) = T^ρ (ρ ≤ φ/2 since F is powerful),
so S = T^{β−φ} and R = T^{β−φ+ρ}.

Model assumptions (standard, and the honest weak point — stated explicitly):
(i) for a fixed powerful skeleton (f_a, f_b, f_c), the event "b = c − a has
exact powerful part f_b" behaves like an independent event of probability
≈ T^{−φ_b+o(1)}; (ii) the number of admissible skeletons with F = T^φ,
rad(F) = T^ρ is T^{ρ+o(1)} (choose the radical, then exponent patterns are
T^{o(1)}).

Count of triples at scale T with a given skeleton shape: free choices are the
squarefree parts of a and c (T^{σ_a+σ_c} pairs), times the probability
T^{−φ_b} for b's skeleton. Using σ_b = 1−φ_b and σ_a+σ_b+σ_c = β−φ:

    E[#] ≈ T^{ρ + σ_a + σ_c − φ_b + o(1)} = T^{ρ + (β−φ) − 1 + o(1)}
         = T^{(R-exponent) − 1 + o(1)}.

That is the whole heuristic in one line: **the expected number of triples at
scale T whose radical has exponent θ is T^{θ−1+o(1)}.** Quality q ≥ 1+δ means
θ ≤ 1/(1+δ), hence

    E[#{c ≍ T : q ≥ 1+δ}] ≲ T^{−δ/(1+δ) + o(1)},

which is summable over dyadic T for every fixed δ > 0: finitely many such
triples are expected, i.e. abc holds in this model — with polynomial room.

Consistency checks against reality: (a) for q barely above 1 the exponent is
≈ 0 and the hidden polylog factors dominate — matching the ~23.8M known
triples with q > 1 below ~2^63 (number pending final verification by my
field-status agent) while only a handful exist with q ≥ 1.5; (b) the model's
finer polylog structure is exactly what RST refine into a precise conjectured
extremal order; the §2 constructions guarantee excess of a compatible
(smaller) shape, and no construction is known to exceed the RST scale.

## 4. The asymmetry, and the single missing theorem

A disproof must produce correlated powerful mass along a + b = c persistently:
R-exponent ≤ 1/(1+δ) infinitely often, beating the T^{θ−1} accounting not once
(records already do that at bounded scale) but as T → ∞. Every concrete
mechanism examined in this collaboration terminates at the same unproven
ingredient — a theorem forcing (or forbidding) systematically large squarefull
parts in a structured sequence:

- fixed-S S-unit families: killed unconditionally (finiteness);
- polynomial identities: killed by Mason–Stothers (firsttryabc §9, correct);
- smooth-collision pigeonhole: killed by post-cancellation counting
  (firsttryabc §7, correct);
- Pell/recurrence and Chebyshev orbits (codex's corrected §11 branch): produce
  q > 1 unconditionally but a fixed gap needs squarefull growth in d_j of
  positive logarithmic density — a dynamical Wieferich-type statement nobody
  can prove or refute;
- powerful-skeleton engineering directly: needs exactly the correlated-mass
  event whose expected count converges above.

Conclusion for the joint report: outcome (b) is not reachable by any method
available to us; the disproof side is not merely "hard" but points at a
specific, named missing theorem (systematic squarefull production along
additive/dynamical structures), and all heuristic and computational evidence
points the other way.

## 5. Caveats (rigor rule)

This section is a HEURISTIC, not a theorem: independence assumption (i) is
unproved (it is exactly where all rigor dies — additive correlations of
powerful parts), and skeleton-count assumption (ii) hides divisor-type
factors. The final report must label it as such and must not cite constants I
have not verified. Numbers marked "pending" await the field-status agent.
