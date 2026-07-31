/-
W1 lifting step — pilot theorem of the ABCFormal tree.

Paper statement (Proposition W1 of the Phase 7 map, LTE step): for the
fixed pair and an odd unramified place 𝔭 above p, with x = u^m ≡ 1
(mod 𝔭) and p ∤ r,  v_𝔭(x^r − 1) = v_𝔭(x − 1).

Statement fidelity (per mailbox 0146-codex): the theorem below is
stated over an ARBITRARY integral domain R with a prime element p —
instantiating R to the valuation ring of the unramified local field,
where p itself is a uniformizer and v_𝔭 = emultiplicity p, gives the
paper's statement; that instantiation (and the passage v_𝔭(u^n − 1) =
v_p(U_n)) is NOT formalized here and remains on the informal side of
the boundary. The ℤ-corollary is labeled a smoke test, not W1.

Notably the ring form needs neither `Odd p` nor `p ∤ x` — the latter
follows from `p ∣ x − 1` for a prime element.
-/
import Mathlib

namespace ABCFormal

/-- **W1 lifting step, ring form.** In an integral domain `R` with a
prime element `p`: if `p ∣ x - 1` and `p` does not divide the image of
the exponent `r`, then `x ^ r - 1` and `x - 1` have equal
`p`-multiplicity. Instantiates to the valuation ring of an unramified
local field (where `p` is a uniformizer), which is the form consumed
by Proposition W1. -/
theorem w1_lifting {R : Type*} [CommRing R] [IsDomain R]
    {p : R} (hp : Prime p) {x : R} (hx1 : p ∣ x - 1)
    {r : ℕ} (hr : ¬ p ∣ (r : R)) :
    emultiplicity p (x ^ r - 1) = emultiplicity p (x - 1) := by
  have hx : ¬ p ∣ x := by
    intro h
    exact hp.not_unit (isUnit_of_dvd_one (by simpa using dvd_sub h hx1))
  simpa using
    emultiplicity_pow_sub_pow_of_prime hp (y := 1) (by simpa using hx1) hx hr

/-- **Integer LTE smoke test** (toolchain check; an analogue of W1 over
`ℤ`, not the local statement itself — see the fidelity note above). -/
theorem integer_lte_smoke {p : ℕ} (hp : p.Prime) {x : ℤ}
    (hx1 : (p : ℤ) ∣ x - 1) {r : ℕ} (hr : ¬ p ∣ r) :
    emultiplicity (p : ℤ) (x ^ r - 1) = emultiplicity (p : ℤ) (x - 1) :=
  w1_lifting (Nat.prime_iff_prime_int.mp hp) hx1 (by exact_mod_cast hr)

end ABCFormal
