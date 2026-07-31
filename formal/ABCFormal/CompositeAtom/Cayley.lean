/-
The Cayley inversion fibers used by Lemma 9 of the companion note.

This file proves the universal algebraic part of the root classification:
away from 0 and -1 in characteristic not two, two Cayley seed ratios are
equal exactly when their parameters agree or are inverse. It then combines
that fact with Mathlib's `IsPrimitiveRoot` exact-order API to prove the
cross-index disjointness used in the paper.

It does not yet formalize the homogeneous coordinate atom, the norm-one
finite-field case, the exact root cardinality, or Hensel lifting.
-/
import Mathlib

namespace ABCFormal

variable {K : Type*} [Field K]

/-- The Cayley coordinate used to pass from a root of unity to a seed ratio. -/
def cayley (z : K) : K := (z - 1) / (z + 1)

/-- The projective seed ratio attached to a Cayley coordinate. -/
def cayleyRho (z : K) : K := -(cayley z) ^ 2

/-- The Cayley transform is injective away from its pole in characteristic
not two. -/
theorem cayley_injective_of_ne_neg_one [NeZero (2 : K)]
    {x y : K} (hx : x ≠ -1) (hy : y ≠ -1)
    (h : cayley x = cayley y) : x = y := by
  have hxden : x + 1 ≠ 0 := by
    intro hzero
    apply hx
    exact eq_neg_of_add_eq_zero_left hzero
  have hyden : y + 1 ≠ 0 := by
    intro hzero
    apply hy
    exact eq_neg_of_add_eq_zero_left hzero
  rw [cayley, cayley, div_eq_div_iff hxden hyden] at h
  have htwo : (2 : K) * (x - y) = 0 := by
    linear_combination h
  have hdiff : x - y = 0 := (mul_eq_zero.mp htwo).resolve_left NeZero.out
  exact sub_eq_zero.mp hdiff

/-- Inversion negates the Cayley coordinate. -/
theorem cayley_inv {z : K} (hz : z ≠ 0) (hneg : z ≠ -1) :
    cayley z⁻¹ = -cayley z := by
  have hinvneg : z⁻¹ + 1 ≠ 0 := by
    intro hzero
    apply hneg
    have hz' : z⁻¹ = -1 := eq_neg_of_add_eq_zero_left hzero
    calc
      z = (z⁻¹)⁻¹ := (inv_inv z).symm
      _ = (-1 : K)⁻¹ := congrArg Inv.inv hz'
      _ = -1 := inv_neg_one
  rw [cayley, cayley]
  field_simp [hz, hneg, hinvneg]
  ring

/-- The projective seed ratio is invariant under inversion. -/
theorem cayleyRho_inv {z : K} (hz : z ≠ 0) (hneg : z ≠ -1) :
    cayleyRho z⁻¹ = cayleyRho z := by
  simp only [cayleyRho, cayley_inv hz hneg, neg_sq]

/-- The fibers of the Cayley seed-ratio map are exactly the inversion pairs.
This is the algebraic two-to-one statement behind the `φ(k) / 2` root count
in Lemma 9. -/
theorem cayleyRho_eq_iff [NeZero (2 : K)]
    {x y : K} (hx0 : x ≠ 0) (hy0 : y ≠ 0)
    (hx : x ≠ -1) (hy : y ≠ -1) :
    cayleyRho x = cayleyRho y ↔ x = y ∨ x = y⁻¹ := by
  constructor
  · intro h
    have hsq : cayley x ^ 2 = cayley y ^ 2 := by
      simpa [cayleyRho] using h
    rcases eq_or_eq_neg_of_sq_eq_sq (cayley x) (cayley y) hsq with hsame | hinv
    · exact Or.inl (cayley_injective_of_ne_neg_one hx hy hsame)
    · right
      have hyinvneg : y⁻¹ ≠ -1 := by
        intro hbad
        apply hy
        calc
          y = (y⁻¹)⁻¹ := (inv_inv y).symm
          _ = (-1 : K)⁻¹ := congrArg Inv.inv hbad
          _ = -1 := inv_neg_one
      apply cayley_injective_of_ne_neg_one hx hyinvneg
      rw [cayley_inv hy0 hy]
      exact hinv
  · rintro (rfl | rfl)
    · rfl
    · exact cayleyRho_inv hy0 hy

/-- Primitive roots with the same Cayley seed ratio have the same exact
order. This is the cross-index disjointness assertion in Lemma 9. -/
theorem primitive_index_unique_of_cayleyRho_eq [NeZero (2 : K)]
    {x y : K} {k l : ℕ}
    (hx0 : x ≠ 0) (hy0 : y ≠ 0) (hx : x ≠ -1) (hy : y ≠ -1)
    (hk : IsPrimitiveRoot x k) (hl : IsPrimitiveRoot y l)
    (hrho : cayleyRho x = cayleyRho y) : k = l := by
  rcases (cayleyRho_eq_iff hx0 hy0 hx hy).mp hrho with hxy | hxy
  · subst y
    exact hk.unique hl
  · have hk' : IsPrimitiveRoot y⁻¹ k := by simpa [hxy] using hk
    exact hk'.unique hl.inv

/-- In a finite field, the exact order of a nonzero primitive root divides
the multiplicative-group order. Applied with `F = 𝔽_p`, this is the split
half of the paper's compatibility condition; it does not formalize the
norm-one subgroup argument. -/
theorem primitiveRoot_order_dvd_card_sub_one
    {F : Type*} [Field F] [Fintype F]
    {z : F} {k : ℕ} (hk0 : k ≠ 0) (hz : IsPrimitiveRoot z k) :
    k ∣ Fintype.card F - 1 := by
  rw [hz.eq_orderOf]
  exact orderOf_dvd_of_pow_eq_one
    (FiniteField.pow_card_sub_one_eq_one z (hz.ne_zero hk0))

end ABCFormal
