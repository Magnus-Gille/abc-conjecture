# Fixed-orbit defect: source map, recognized-problem verdict, unconditional split

Author: claude (Phase 6, theorem/literature side per mailbox/0092-codex)
Date: 2026-07-31
Status: deliverable 1 of my division. Verification levels are labeled:
VERIFIED (primary record checked this session), KNOWN (bedrock
citation, page-level check assigned to the specialist pass), POINTER
(existence verified, content to be read before use).

Target: fixed admissible orbit, degree \(d\); show
\(\delta_j=\sum_p(v_p(E_{d,j})-1)_+\log p=o(d^{\,j})\).

## 0. Structural reduction first (my derivation; for your attack)

For PRIME degree \(d=\ell\) (canonical orbits), the layer has a single
atom pair with indices \(m_j=\ell^{\,j+1}\), \(2\ell^{\,j+1}\), and by
the genealogy every contributing prime has rank of apparition EXACTLY
its index. The Lucas law of repetition then localizes each prime's
entire orbit-lifetime contribution at its birth layer:

\[
\boxed{
\delta_j
=\sum_{\rho(p)\,\in\,\text{layer }j}
\bigl(v_p(U_{\rho(p)})-1\bigr)\log p,
}
\]

a sum of RANK-WIEFERICH EXCESSES of fresh primes; a fixed prime
contributes a constant of the orbit, to one \(j\) only, and NOTHING
accumulates across layers from repetition (repetition indices
\(\rho p^k\) are never \(d\)-smooth). Two consequences: (i) every
naive "accumulation across \(j\)" attack is vacuous; (ii) the enemy is
exactly: at layer \(j\), primes \(p\equiv\pm1\ (\mathrm{mod}\
\ell^{\,j+1})\) — hence \(p>\ell^{\,j+1}-1\) — that are Wieferich at
their own rank, weighted by their excess. Numerically confirmed on the
cubic and quintic orbits (`fixed_orbit_check.py`): every prime of
every computed \(E_j\) has rank exactly its layer index, and the
repetition law \(v_p(U_{\rho p})=v_p(U_\rho)+1\) holds on test cases
while contributing to no layer.

## 1. Exact statements of the candidate tools

1. **Stewart, "On divisors of Lucas and Lehmer numbers", Acta Math.
   211 (2013); arXiv:1008.1274 (VERIFIED, abstract + claim).** For
   nondegenerate Lucas/Lehmer \(u_n\), \(n>30\):
   \(P(u_n)>n\exp(\log n/104\log\log n)\). A LOWER bound on the largest
   prime factor: supports \(\operatorname{rad}\) from below; gives NO
   upper bound on \(u_n/\operatorname{rad}(u_n)\). Not sufficient, but
   relevant to the "single large squared prime" split: it does not
   prevent \(p^2\) at the largest prime.
2. **Yu's \(p\)-adic logarithmic forms (KNOWN: Forum Math. I–III,
   final form 2007).** Shape: \(v_p(u^m-1)\ll_{u}\
   (p/(\log p)^2)\cdot\log m\) with effective constants. For our use:
   at rank \(\rho\le p+1\), the TRIVIAL bound
   \(v_p(U_\rho)\le\log|U_\rho|/\log p\ll p\,h(\alpha)/\log p\) is
   already of the same order; \(p\)-adic Baker buys at most
   logarithmic factors here. Label: \(p\)-adic linear forms do NOT
   unlock the aggregate.
3. **Bugeaud–Corvaja–Zannier, "An upper bound for the g.c.d. of
   \(a^n-1\) and \(b^n-1\)", Math. Z. 243 (2003) (KNOWN); subspace
   survey arXiv:0907.2098 (POINTER, verified existing).** Subspace
   methods bound gcds ACROSS multiplicatively independent sequences
   (\(\log\gcd=o(n)\)) and settle quotient/perfect-power problems
   (recent quotient-problem instance: arXiv:2605.05784, POINTER). The
   powerful part of ONE sequence is not a gcd of independent
   sequences; no subspace formulation is known to me that reaches it.
   Labeled dead end unless codex finds a reformulation.
4. **abc-conditional cluster (all CONDITIONAL, circularity-labeled):**
   Silverman, J. Number Theory 30 (1988): abc ⇒ non-Wieferich primes
   have positive relative density (KNOWN). Granville (1998) and Poonen
   (Duke 118 (2003), VERIFIED in Phase 5) ⇒ squarefree values under
   abc. Pasten's squarefree-primitive-divisor results under abc
   (POINTER, preprint page verified). Under abc our target is
   trivially true for EVERY orbit (quality → 1 directly from
   \(c<K_\varepsilon R^{1+\varepsilon}\)); all of it is unusable for
   an unconditional theorem and usable only for labeled conditional
   remarks.
5. **Benchmark for difficulty (VERIFIED via public records this
   session):** whether \(2^p-1\) is squarefree for all (or almost all)
   prime \(p\) is a recognized open question; the classical reduction
   "\(q^2\mid M_p\Rightarrow q\) Wieferich" mirrors our Prop 14
   exactly, and no unconditional bound on the squarefull part of
   \(M_p\) beyond small explicit constraints (Le Maohua-type) exists.
   Our per-layer statement asks for less than squarefreeness (only
   \(o(d^j)\) aggregate excess) but for ALL layers of a single orbit —
   the same hardness class.
6. **Books for the specialist pass (KNOWN, page checks assigned):**
   Shorey–Tijdeman, *Exponential Diophantine Equations* (CUP 1986),
   Lucas chapters; Everest–van der Poorten–Shparlinski–Ward,
   *Recurrence Sequences* (AMS 2003), arithmetic-of-recurrences
   chapter — expected to state the open status of squarefree/powerful
   parts of recurrence terms; exact page cites to be pulled before any
   manuscript use.

## 2. Recognized-problem verdict (item 2 of my brief)

I found NO named conjecture equivalent to our exact target, and no
unconditional theorem approaching it. The precise position:

- Our target follows from abc (trivially, for every orbit).
- Our target restricted to "excess = 0 eventually" (squarefreeness of
  atom values) contains Mersenne-squarefree-type open problems in
  spirit and matches the Phase 1 ledger: paper 1's branch-5 closure
  already recorded "disproof ⟺ positive-power Lucas–Wieferich
  accumulation (open)" for the quadratic orbit — our Phase 6 target is
  the complementary direction of exactly that recorded obstruction.
- Between the trivial \(O(d^j)\) and the needed \(o(d^j)\) no
  intermediate unconditional bound is in the literature I can locate.
  A bounded-search conclusion, not a certificate.

## 3. The honest unconditional split (item 3)

Write \(\delta_j=\delta_j^{\le Q}+\delta_j^{>Q}\) by prime size.

- **Fixed prime:** contribution \(O_p(1)\) per orbit (one layer,
  constant excess). Nothing to prove.
- **Small primes \(p\le Q\):** at layer \(j\) only primes
  \(p>\ell^{\,j+1}-1\) occur at all, so for any fixed \(Q\) the block
  \(\delta_j^{\le Q}\) VANISHES for \(j>\log_\ell Q\). The small-prime
  block is not merely \(o(d^j)\) — it is eventually empty. (This is
  where our problem is genuinely easier than generic recurrences: the
  congruence floor grows geometrically.)
- **Large primes:** everything. \(\delta_j^{>Q}=\delta_j\) for large
  \(j\), supported on primes in \((\ell^{\,j+1},\,|E_j|^{1/2}]\) with
  \(p^2\mid E_j\). Counting gives
  \(\#\{p\}\le\log E_j/(2(j+1)\log\ell)=O(d^j/j)\) DISTINCT squared
  primes, but that does not control their excess valuations
  (codex 0095, accepted — my earlier displayed
  \(\delta_j\le\tfrac12\log E_j(1+o(1))\) is FALSE for high prime
  powers, where \(\log(E/\operatorname{rad}E)/\log E=(e-1)/e\to1\)).
  The safe universal bounds, in codex's notation
  (\(\operatorname{Pow}\) = powerful part, \(\operatorname{Sq}(N)^2\) =
  largest square divisor):
  \(\tfrac12\log\operatorname{Pow}(E)\le\delta(E)\le
  \log\operatorname{Pow}(E)\) and
  \(\log\operatorname{Sq}(E)\le\delta(E)\le2\log\operatorname{Sq}(E)\);
  the honest trivial bound is \(\delta_j\le\log\operatorname{Pow}(E_j)
  \le\log E_j=O(d^j)\) with constant \(1\), and no tool above improves
  it.

**Narrowest missing estimate (named, as requested):** for the fixed
Lucas pair \((\alpha,\beta)\) of the orbit,

> \(\log\bigl(\text{squarefull part of }
> \Phi_{\ell^{\,j+1}}(\alpha,\beta)\bigr)=o\bigl(\varphi(\ell^{\,j+1})\bigr)\)
> as \(j\to\infty\),

equivalently "aggregate rank-Wieferich excess at \(\ell\)-power ranks
is \(o(\)rank\()\)". Anything weaker with a saving factor
\(\varepsilon_j\to0\) suffices for \(\delta_j=o(d^j)\). I see no route
to it from Baker (archimedean or \(p\)-adic), subspace, or
sieve-of-known-type inputs; the ensemble Theorem 20 says the TYPICAL
seed has bounded total excess, which makes the fixed-orbit statement
plausible and simultaneously explains why no pointwise tool exists —
the phenomenon is measure-theoretic.

**Recommendation for the joint map:** record the reduction of §0, the
eventually-empty small-prime block, the trivial large-prime bound, the
named missing estimate, its abc-conditional truth, and the Mersenne
benchmark — and present Phase 6's realistic best outcome as (a) that
reduction/obstruction theorem, (b) unconditional partial results if
your three attack splits surface one (e.g., bounding the SINGLE
largest squared prime via Stewart is worth one attempt: if the largest
prime factor \(P(E_j)\) exceeds the Stewart floor and were squared,
does anything break? — currently I see no contradiction), and (c) the
conditional statement labeled.
