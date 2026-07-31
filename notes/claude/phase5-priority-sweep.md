# Phase 5 priority sweep (claude, supporting step 1)

Date: 2026-07-31. Scope: independent bounded sweep to prepare review of
codex's theorem-by-theorem overlap table. Not exhaustive; conclusions
are "not located," never "does not exist."

## Sources verified at statement level this session

1. BDEHWW, arXiv:2009.03345 = Adv. Appl. Math. 138 (2022) 102344.
   §5 read in full (LaTeX). Main theorem: complete factorization type of
   fibotomic Ψ_n in Z_p[x] for ALL p, n (δ ∈ {u/2, u, 2u} casework),
   plus prime-power layer collapse Ψ_{p^k m} ≡ Ψ_m^{φ(p^k)} (mod p).
   Bridge to our Prop 15 established both directions
   (x² = −4/(X+1); notes/claude/fibotomic_bridge_check.py, and codex's
   polynomial identity in 0072). No Hensel lifting, no valuation
   prescription, no CRT realization, no additive triples, no radicals.
2. Sagan–Tirrell, arXiv:1909.02593 (Lucas atoms; the founding source;
   published Adv. Math.). Combinatorial/algebraic factorization
   {n} = ∏ P_d(s,t) and Φ_d-relationship via gamma expansions. MUST be
   cited; Props 9–12 should attribute the atom concept here and to AMMR
   (arXiv:2308.10216, confirmed as the AMMR arXiv record) for the
   complete p-adic valuation theory.
3. Bluher, arXiv:1707.06877. Chebyshev functional structure over F_q,
   stabilized subsets, factorization formula. Adjacent to our
   split/norm-one mechanics; no orbit, no realization.
4. Gassert, arXiv:1209.4396. Complete description of prime-degree
   Chebyshev functional graphs over F_q; prime decomposition
   applications. Adjacent to our T_ℓ-dynamics mod p; no valuation
   prescription.
5. Bhargava–Zieve, Finite Fields Appl. 5 (1999) 103–111 (free PDF on
   Zieve's page; also Chou's earlier description they simplify).
   Complete factorization of Dickson D_n(X,a), E_n(X,a) and bivariate
   D_n(X,a)−D_n(Y,a) over any finite field. This is the classical
   umbrella under which BDEHWW/our-Prop-15-type local statements sit;
   the overlap map should route Prop 15's attribution through
   Chou / Bhargava–Zieve → Bluher/Gassert (Chebyshev form) →
   BDEHWW (fibotomic form) → our Cayley/ρ-descent normalization.

## Sweep queries run (arXiv API, math.NT / math.DS)

- "fibotomic" OR ("Lucas atoms" AND "valuation") → exactly two hits:
  BDEHWW and AMMR. No third party works in this exact niche; in
  particular no realization-type statement.
- "Lucas sequence" + "prescribed" + valuation/prime-power → noise, no
  relevant hits.
- "Chebyshev" + "abc" + radical/triple → noise, no relevant hits.

## Conclusion for the overlap table review

The five adjacent sources jointly cover the LOCAL side (factorization
of the branch polynomials mod p, in three equivalent languages:
Dickson, Chebyshev graphs, fibotomic). None contains: exact-valuation
Hensel prescription tied to seeds (Cor 16 as used), simultaneous CRT
realization with primitivity (Thm 17), the additive-orbit genealogy
(Thm 3), the radical telescope (Thm 5), or any abc-quality coupling
(Prop 14 / Cor 8). The correct manuscript posture: fully attribute the
local classification (Prop 15 → corollary-of-known after the
substitution lemma), and claim the orbit-plus-realization package only,
with the priority claim still gated on specialist review.
