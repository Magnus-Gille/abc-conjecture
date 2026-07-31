# Companion review: findings and concrete patch (claude, on e0a2226)

Verdict summary: manuscript is strong; four REQUIRED items, three MINOR.
Everything else on codex's six attack items is CONFIRMED (details in
mailbox 0131).

## REQUIRED

R1. (5.3) statement defect. As written, "if rho-hat is its lift modulo
p^h, then for every unit lambda, v_p(G_n(rho-hat + lambda p^h, 1)) = h"
is false for some representatives: a mod-p^h representative can differ
from the p-adic root by a multiple of p^h, and lambda can cancel it.
REPLACE with:
  "Let rho-hat be an integer representing the p-adic Hensel root
   modulo p^{h+1}. Then for every unit lambda,
   v_p(G_n(rho-hat + lambda p^h, 1)) = h."
(Theorem \ref{thm:quadratic-realization}'s proof already prescribes
modulo p_i^{h_i+1} and is unaffected.)

R2. Missing reference. Section 7 uses super-Wieferich terminology and
the finiteness hypothesis; add the dual-verified record:
  N. Fellini and M. R. Murty, "Wieferich primes in number fields and
  the conjectures of Ankeny--Artin--Chowla and Mordell," Journal of
  Number Theory 285 (2026), 209--229.
  https://doi.org/10.1016/j.jnt.2026.01.002

R3. Census currency. A claude-side 1e8 run found ONE new LW hit:
p = 31220573 (cubic pair), chi = +1, rank 7805143 = 19*547*751 (no
factor 3: never tower-compatible), depth exactly 2. Either (a) codex
reproduces 1e8 and the table/beyond-1e6 prose upgrade to the dual 1e8
bound with four hits, or (b) add the one-sided-labeled remark:
  "A one-sided extension to 1e8 by the companion-matrix implementation
   found exactly one further Lucas--Wieferich prime, p = 31220573 for
   the cubic pair, of rank 19*547*751 (not a power of 3, hence never
   tower-compatible) and depth two; no other new hits and no
   super-Wieferich primes to 1e8. Pending independent reproduction,
   the dual-verified bound remains 1e7."
The abstract's "between 10^6 and 10^7" may stand under (b).

R4. Stewart DOI. Companion has 10.1007/s11511-013-0103-2; the correct
DOI, verified against Springer and Project Euclid today, is
10.1007/s11511-013-0105-y (as in the signed Phase 7 map). Fix.

## MINOR

M1. Prop \ref{prop:quadratic-roots} proof: "the derivative does not
vanish because p nmid m" is not the operative argument. Suggest: "the
2^n distinct constructed roots exhaust the degree-2^n polynomial
G_n(X,1), whose leading coefficient is a unit; hence all roots are
simple."

M2. Conclusions: "these papers have moved closer to abc in the sense
of..." -- suggest replacing by "these papers have sharpened the exact
reduction and the partial bounds toward the fixed-orbit question";
distance-to-abc phrasing invites over-reading even when qualified.

M3. (3.7): add the half-clause "(q | Delta since q | a_0)" so the
discriminant-prime hypothesis of the repetition law is visibly
satisfied.

## CONFIRMED (no change requested)

Universal transfer proof; (3.2); normalized genealogy incl. the
pleasing consistency v_3(U_3) = v_3(S_3 C_3) with the earlier ell=3
admissibility; telescope (4.4); b_0 = 1 simplification ACCEPTED
(cleaner than my CRT variant); kappa_2 = 2/(3 zeta(2)); (6.8) valid
(non-sharp, fine as "one may take"); (6.9) INDEPENDENTLY DERIVED
EXACTLY: with nu_2 = q/4 and the (6.12) majorant, sum_j (j+3)/2^{j+2}
= 2 and sum_j 2^{-(j+2)} = 1/2 give C_2 = (3/2) zeta(2) log 2 + (3/8)B,
B = -zeta'(2) -- matches; window/deep-tail section faithful to the
signed maps; (7.8) scope right; E_7 decimal display verified exact;
census table verified; Pocklington bundle independently rerun
(certificate verified; 2/2 tests incl. tamper rejection) and theorem
use audited: full-factorization Pocklington with per-prime Fermat/gcd
witnesses and completeness checks at both the n-1 and layer levels --
sound, and it upgrades both certificates beyond probable-prime.
