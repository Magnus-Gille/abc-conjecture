# Audit of `firsttryabc.md` + a decisive negative result on its "missing lemma"

Author: claude (Claude Fable 5). Date: 2026-07-25T20:41Z.

## 1. Verification of the document's claims

I re-derived every load-bearing claim. Notation as in the document:
for x = (x_p) ∈ Z^s indexed by the s = ω(abc) primes dividing abc,

- D_x(n) = n·L_n(x) with L_n(x) = Σ_{p|n} v_p(n)·x_p/p,
- W_x(a,b) = a·D_x(b) − b·D_x(a) = ab·(L_b − L_a),
- constraint (1): D_x(a) + D_x(b) = D_x(c),
- H(x) = max_p |x_p|, R = rad(abc).

Checked and CORRECT:

1. Leibniz rule D_x(mn) = m·D_x(n) + n·D_x(m) for coprime m,n (in fact for all m,n). ✓
2. Under a+b=c and (1): W_x(a,b) = W_x(a,c) = W_x(c,b). ✓ (direct expansion)
3. n/rad(n) | D_x(n), because n/rad(n) | n/p for every p | n. ✓
4. Pairwise coprimality ⇒ (abc/R) | W_x(a,b).  ✓
5. Size bound: |L_n| ≤ H·Σ_{p|n} v_p(n)/p ≤ (H/2)·log₂ n, hence
   |W| ≤ ab·H·log₂ c  (using log₂ a + log₂ b ≤ 2 log₂ c).  ✓
   (Document states |W| ≤ ab·H·log c/log 2 — same thing.)
6. Consequence (4): if W ≠ 0 then c ≤ R·H(x)·log₂ c. ✓
7. Reduction: if for every η>0 all but finitely many triples admit x with (1),
   W ≠ 0, H(x) ≤ C_η·c^η  — call this (*_η) —  then abc holds
   (with η = ε/(2(1+ε))). ✓ Their algebra checks out.
8. §6 numerics for the Reyssat triple (2, 3¹⁰·109, 23⁵), x = (x₂,x₃,x₁₀₉,x₂₃) =
   (−721, 20, 79, 310): I recomputed
   D(a) = −721; D(b) = 10·2 145 447·20 + 59 049·79 = 433 754 271;
   D(c) = 5·279 841·310 = 433 753 550 = D(a)+D(b) ✓;
   W = 2·433 754 271 + 721·6 436 341 = 5 508 110 403 = 3⁹·23⁴ = abc/R exactly. ✓
   R = 15 042, q = log c/log R ≈ 1.62991. ✓

The document is honest: no invalid step found; it correctly refrains from claiming
a proof and correctly isolates (*_η) as the missing piece, and §5's worry (short
lattice vectors may all be degenerate) is well-founded.

## 2. Proposition 1 — the missing lemma is self-referential (NEW)

**Proposition 1.** Let (a,b,c) be a primitive abc triple, and suppose x satisfies
constraint (1) with W_x(a,b) ≠ 0. Then

    H(x) ≥ (c/R) · log 2 / log c  =  (c/R) / log₂ c.

*Proof.* abc/R divides W ≠ 0, so abc/R ≤ |W| ≤ ab·H(x)·log₂ c by items 4–5 above.
Divide by ab. ∎

**Corollary (circularity).** For every triple, the minimal height H*(a,b,c) of a
*nondegenerate* certificate satisfies H* ≥ (c/R)/log₂ c. Hence:

- (*_η) can hold on a family of triples **only if** c ≤ R·c^η·log₂ c already holds
  on that family. A certificate for (*_η) carries the abc inequality on its face.
- If abc is false — infinitely many triples with c > R^{1+δ₀} — then along that
  family H* > c^{δ₀/(1+δ₀)}/log₂ c, so (*_η) fails for every η < δ₀/(1+δ₀).
- Inequality (4) is exactly the assertion H* ≥ (c/R)/log₂ c read backwards: for the
  optimal certificate the method's output equals its input hypothesis, up to log².
  Net information: zero.

So "(*_η) for all η" is not a lemma-sized gap: it is abc itself in a costume.
No Siegel-type, counting, or lattice-geometry argument can prove (*_η) without
first proving abc, because (*_η) is *false* precisely where abc is false, and its
truth for a given triple presupposes the abc-type bound for that triple. The §5
obstruction ("short vectors may be degenerate") is therefore not a technical
difficulty to be engineered around; Proposition 1 shows the degenerate subspace
MUST swallow every vector shorter than (c/R)/log₂ c whenever c/R is large.

**Remark (a = 1 mechanism, sharper view).** For triples (1, b, c), constraint (1)
reads b·L_b = c·L_c, and with M_b := rad(b)·L_b ∈ Z one gets (c/rad(c)) | M_b, and
nondegeneracy means M_b ≠ 0, so |M_b| ≥ c/rad(c) and directly
H ≥ 2(c/R)/log₂ b. The divisibility that powers the method is the same divisibility
that forces certificates to be large. Same phenomenon, one line.

**Conceptual reading.** In C[t] the Mason–Stothers proof uses the *canonical*
derivation d/dt, which does not grow heights. On Z there is no canonical
derivation; every D_x has free coefficients, and Proposition 1 says the freedom is
a mirage: any nondegenerate choice is at least as expensive as the inequality one
wants. This is a quantitative shadow of the standard "no derivation on Spec Z /
field-with-one-element" obstruction.

## 3. What remains genuinely open around this framework (agenda)

- **Q1 (upper bound / exact equivalence).** Is H* ≤ (c/R)·c^{o(1)} for all triples
  (subject to gcd solvability), i.e. is (*_η) *equivalent* to abc rather than
  merely ≥ it? Reyssat: c/R ≈ 427.9 and the exhibited certificate has H = 721 ≤
  2(c/R), consistent. Computable: for record triples s is tiny (4–8); exact H* by
  lattice enumeration. Worth doing to close the chapter cleanly.
- **Q2 (amplification).** Do higher-order constructions (k derivation vectors
  x⁽¹⁾,…,x⁽ᵏ⁾, k×k arithmetic Wronskian determinants) beat the c/R threshold?
  Prediction: no — divisibility and size both scale multiplicatively per row, the
  ratio is invariant. Needs a concrete k=2 computation to confirm or refute.
- **Q3 (small-ω regime).** For ω(abc) ≤ s₀ fixed, is quality bounded? (Not known;
  not implied by S-unit finiteness since the primes vary. Yu-type p-adic linear
  forms in logarithms give exponential-in-R bounds only — same wall as Stewart–Yu.)
