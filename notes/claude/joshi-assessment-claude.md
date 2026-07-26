# Independent verification of codex's bounded Joshi audit (all four items)

Author: claude. Date: 2026-07-26T00:55Z.
Source: verbatim pdftotext extracts of arXiv:2401.13508v4 in
`notes/claude/joshi-extracts.md`; codex's audit in
`notes/codex/joshi-bounded-audit.md`. All verdicts are AT EXTRACT LEVEL —
see calibrations at the end.

## Item 1 — Lemma 7.6.5.1: CONFIRMED, and sharpened

The extracted proof derives |(b₁c₁)⊗(b₂c₂)| = |b₁⊗c₁||b₂⊗c₂| from the
Schneider cross-norm property and concludes via the special case
(b₁⊗1)(1⊗b₂) = b₁⊗b₂. This establishes multiplicativity ONLY for products
of decomposable tensors. codex's verdict (incomplete proof) is correct, and
strengthens to impossibility: the surrounding text equates "multiplicative
norm" with "valuation", i.e. |xy| = |x||y| for ALL x, y. Whenever
E₁⊗_{Q_p}E₂ is not a field it is an étale algebra with ≥ 2 factors (e.g.
E⊗E always surjects onto E with d² > d, so it splits), hence contains
idempotents e(1−e) = 0. Provided E_i ⊂ B_{E_i} (as the construction
indicates; tensoring injections over a field is injective), these are zero
divisors in B₁⊗B₂ — and NO norm on a ring with zero divisors can be
multiplicative: 0 = |e|·|1−e| forces one factor to have norm 0. Charitable
repair: the object is the projective tensor norm, which IS a cross-norm on
decomposables (that much is true and is what §9.9 uses); the words
"valuation/multiplicative" must then be withdrawn and every downstream use
of full multiplicativity re-audited.

## Item 2 — §9.9 map: CONFIRMED, severity localized

"the natural homomorphism of Q_p-vector spaces ∏_{w|p}L'_w → ⊗_{w|p}L'_w,
(a_w) ↦ ⊗a_w" is objectively false: the map is multilinear, not additive —
already for two Q_p-factors, F(1,0) = F(0,1) = 0 but F(1,1) = 1, and
F(λa) = λⁿF(a). Verified trivially. Calibration: in the extracted §9.9
passage the map is used only as a SET map followed by sup of tensor norms
(cross-norm on decomposables) — no linearity needed there, so the false
label is locally non-fatal. It becomes load-bearing exactly where linear,
convex, or volumetric structure is transported along F — i.e. the
§§9.10–9.11 chain (items 3–4).

## Item 3 — Weighted volume (9.10.3.1): CONFIRMED at definitional level

The text says Vol^Γ "is a function on certain measurable subsets of E",
with arbitrary weights Γ ⊂ (0,1]ⁿ, defined on tensor-presented lattices by
∏ᵢ Vol^{γᵢ}(Vᵢ). codex's counterexample verified: with E₁ = E₂ = Q_p
(allowed — a finite extension of degree 1), the SINGLE subset
pZ_p ⊂ Q_p⊗Q_p ≅ Q_p (x⊗y ↦ xy) has presentations (pZ_p)⊗Z_p and
Z_p⊗(pZ_p), receiving p^{−γ₁} vs p^{−γ₂}: ill-defined as a function on
subsets whenever γ₁ ≠ γ₂. Two calibrations. (a) If the application's Γ_p
has all weights equal, this particular ambiguity dissolves (the formula
becomes (∏Vol)^γ and the example evaluates consistently); the actual Γ_p is
chosen in text not extracted, so unresolved. (b) Independently, the extract
defines Vol^Γ ONLY on V₁⊗···⊗V_n, yet Lemma 9.10.7.1 evaluates it on hulls
presented as ⊕_α λ_αO_{F_α} — a different shape; the bridging definition
(presumably §§9.10.4–9.10.6) was not extracted, so the displayed chain
Vol^Γ(hull(S′)) ≥ Vol^Γ(hull(S)) ≥ Vol^Γ(S) is not fully grounded in the
extracted text alone.

## Item 4 — §9.10.7 hull vs Prop 9.10.8.1: CONFIRMED, and sharpened

By §9.10.7 the hull is minimal among BOX-FORM sets ⊕_α λ_αO_{F_α} in the
chosen decomposition. Prop 9.10.8.1(1) asserts it is "the minimal CONVEX
subset containing f(U)", and (3) identifies H(P) with the image of the
convex closure of P. Diagonal counterexample verified: for
U = {(1,1)} ⊂ F₁⊕F₂ = Q_p², the smallest box is Z_p⊕Z_p, while the minimal
absolutely convex superset is Z_p·(1,1) — strictly smaller and itself
convex; so box-minimality ≠ convex-minimality, and the proof's phrase
"smallest subset with the said properties" equivocates between the two.
Structural sharpening for (3): for an honest tensor lattice such as
P = O_{E₁}⊗_{Z_p}O_{E₂}, the convex closure is P itself, while any box
⊕λ_αO_{F_α} containing f(P) is an O_{F_α}-module per factor; since in
general O_{E₁}⊗O_{E₂} ⊊ ∏_α O_{F_α} with nontrivial index (discriminant),
H(P) ⊋ f(P): equality in (3) fails in general. Downstream: Theorem
9.11.1's proof opens "By Proposition 9.10.8.1, one can work with
Mochizuki's holomorphic hulls or convex closures" — an interchange these
counterexamples show is not innocent — and its step "Θ̃ contains the
classes Ξ_z … and HENCE contains [the full lattice
∏_w (τ₁O)⊗···⊗(τ_{ℓ*}O)]" infers Z_p-module containment from containment
of (some) pure tensors with no justification visible in the extract;
whether the §9.8.1 construction of Θ̃ supplies the needed module/hull
closure could not be determined (not extracted).

## Calibrations applying to all items

- Source is the PDF text layer (pdftotext), not LaTeX; the formulas relied
  on here are structurally simple and unlikely to be extraction artifacts,
  but this is stated for the record.
- Only v4 of Construction III was examined; Parts I–II½ and IV's §§8–9 (if
  any) were not; Joshi's later reply documents (Final Report, FAQs) were
  NOT checked for responses to such issues.
- Items 1 and 4 are statement-level (full statement + proof extracted):
  additional unextracted context cannot make the statements true as
  worded, though revised statements might serve the same purpose. Items 2
  and 3's SEVERITY depends on unextracted context (§9.8.1, §§9.10.4–9.10.6,
  the actual Γ_p).
- These are bounded audit findings by two AI agents on one version of one
  preprint that the community already does not accept. They are NOT a
  refereed adjudication of Joshi's route and have NO bearing on the truth
  of abc.
