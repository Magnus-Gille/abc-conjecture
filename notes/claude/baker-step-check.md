# Referee-grade check of the archimedean (Baker) step — for the paper draft

Author: claude. Date: 2026-07-26. For codex to incorporate directly.

## Setup

z = (7+4i√2)/9 satisfies 9z² − 14z + 9 = 0: degree 2, |z| = 1, and the
Mahler measure of 9x² − 14x + 9 is 9 (both roots on the unit circle), so
the absolute logarithmic Weil height is h(z) = ½·log 9 = log 3. z is not
a root of unity (z + z⁻¹ = 14/9 is not an algebraic integer). Hence z and
−1 are multiplicatively independent: z^a(−1)^b = 1 forces z^{2a} = 1,
so a = 0, then b even.

With θ = arg z, t_j = |cos(Nθ)| for N = 2^j, and for the integer m
minimizing the distance,

    t_j = |cos(Nθ)| ≥ (2/π)·dist(Nθ, (π/2)+πZ) = |Λ_N|/π,
    Λ_N := 2N·log z − (2m+1)·log(−1),  log z = iθ, log(−1) = iπ,
    |2m+1| ≤ 2N+1,  Λ_N ≠ 0 (else z^{2N} = −1, a root of unity).

(The (2/π) chord inequality |cos x| ≥ (2/π)·dist(x, zeros) is elementary.)

## The citation subtlety (IMPORTANT for the as-is bar)

Two families of effective lower bounds, with DIFFERENT dependence on
B := max(|b₁|, |b₂|) = 2N+1:

1. Laurent–Mignotte–Nesterenko-type two-log bounds:
   log|Λ| ≥ −C·D⁴·A₁A₂·(log B + c₀)². The (log B)² gives
   −log t_j = O(j²), hence Σ_{j<n} −log t_j = O(n³).
2. Baker–Wüstholz (1993) / Matveev (2000): log|Λ| ≥ −C'·(∏ h'ᵢ)·log B,
   LINEAR in log B, giving −log t_j = O(j) and Σ = O(n²), i.e.
   |z^{2N}+1| ≥ C·N^{−A} with effective A.

Both suffice for the theorem, since O(n³) = o(2ⁿ) = o(log c_n) just as
well as O(n²). But the draft must NOT cite an LMN-type theorem while
claiming O(n²). Two acceptable resolutions — pick one:

- (Recommended) State the lemma as Σ_{j<n} −log t_j = O(n²) and cite
  Baker–Wüstholz (J. reine angew. Math. 442 (1993) 19–62) or Matveev
  (Izv. Math. 64 (2000)), applied to the two-term form Λ_N above with
  D = [Q(z, i):Q] ≤ 4-ish bookkeeping done explicitly (D = 2 suffices if
  one works with log z and iπ over Q(z); state whichever field you use
  and its degree honestly).
- (Alternative) Cite LMN (Laurent–Mignotte–Nesterenko, J. Number Theory
  55 (1995) 285–321) and state Σ = O(n³). Slightly cleaner constants,
  weaker exponent, identical corollaries.

Either way the paper's THEOREM should be stated with the safe form
"= log Q_n + O(n^κ) for an effectively computable κ (κ = 2 via [BW];
κ = 3 via [LMN]) — in particular o(log c_n)", or just fix one κ and cite
accordingly. Referees check exactly this.

## Also verify in draft

- The paper should note Λ_N is purely imaginary so |Λ_N| = |2Nθ−(2m+1)π|,
  making the chord inequality application transparent.
- h(−1) = 0; LMN/BW require the modified heights h'(αᵢ) ≥ max(h, |log αᵢ|/D, 1/D)-type
  floors — use the theorem's own h' definition, don't plug h(−1) = 0 raw.
- The degree/field bookkeeping: z ∈ Q(i√2)? z = (7+4i√2)/9 ∈ Q(√−2) ✓,
  so D = [Q(√−2):Q] = 2 for the pair (z, −1). Clean.
