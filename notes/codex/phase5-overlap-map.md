# Phase 5, direction 1: source-backed overlap map

Status: primary-source theorem check complete for the seven closest sources
below.  This is a positioning audit, not a priority certificate.

## Exact bridge to fibotomic polynomials

Let \(\Psi_m(x)\) be the fibotomic polynomial of
Byer–Dvorachek–Eckard–Harrington–Wise–Wong, characterized by

\[
\Psi_m(x)
=
\omega^{-\varphi(m)}
\Phi_m(-\omega^2),
\qquad
x=\omega-\omega^{-1}.
\tag{1}
\]

Because \(\Psi_m\) is even for every index \(m\geq3\) used here, write
\(\Psi_m(x)=G_m(x^2)\).  For the manuscript's Cayley parameter

\[
\rho
=
-\left(\frac{\zeta-1}{\zeta+1}\right)^2,
\qquad
\zeta=-\omega^2,
\]

one has

\[
\rho=-1-\frac4{x^2},
\qquad
x^2=-\frac4{\rho+1}.
\tag{2}
\]

Consequently, for either branch index \(m\), with
\(d=\varphi(m)/2\),

\[
\boxed{
\mathcal F_{n,\varepsilon}(X,1)
\doteq
(X+1)^d
G_m\!\left(-\frac4{X+1}\right),
}
\tag{3}
\]

where \(\doteq\) denotes equality up to a nonzero rational scalar (and
the \(A\)-branch includes its systematic \(\ell\)-normalization).

Equation (3) is the required explicit change of variables.  It transfers
the finite-field factorization theorem for fibotomic polynomials directly
to the root statement in Proposition 15.  Proposition 15 is therefore
not an independent new finite-field classification; it is a descended,
homogenized reformulation of known fibotomic factorization.

## Theorem-by-theorem map

| Manuscript item | Closest prior result | Position after audit |
|---|---|---|
| Transfer identity and prime-degree iteration | Classical de Moivre/Dickson-Chebyshev identities; Bhargava–Zieve treat factorization of Dickson polynomials of first and second kind | Identity classical; dynamical use may be new |
| Lemmas 1–2 (normalization, primitivity, support exclusion) | Elementary congruence consequences of the chosen transfer; Lucas valuation theory handles the systematic transfer prime abstractly | Self-contained orbit lemmas; no broad novelty claim |
| Theorem 3 (branchwise genealogy) | Lucas-atom divisibility/valuation results of Sagan–Tirrell and Alecci–Miska–Murru–Romeo; Ratliff–Rush–Shah for radical-preserving cyclotomic constructions | Particular coordinate-orbit support theorem not located |
| Lemma 4 (Chebyshev semiconjugacy) | Standard Chebyshev/Dickson dynamics; Gassert uses the same \(\alpha+\alpha^{-1}\) order parametrization | Classical semiconjugacy |
| Theorem 5 and Proposition 6 (radical telescope/monotonicity) | No matching orbit-wide radical identity located | Candidate contribution, subject to specialist review |
| Theorem 7 and Corollary 8 | Standard Baker–Wüstholz bound applied to the exact telescope | Application, not new transcendence theory |
| Proposition 9 (two atom towers) | Sagan–Tirrell define Lucas atoms \(P_n=\Phi_n(\alpha,\beta)\); Byer et al. give the fibotomic specialization | Specialization/identification, not new atom theory |
| Propositions 10–14 (orders and valuations) | Alecci–Miska–Murru–Romeo give rank congruences and complete \(p\)-adic atom valuations; Gassert gives Chebyshev order/preperiod structure | Specializations coupled to the orbit; local results known |
| Proposition 15 (local roots) | Byer et al., full finite-field factorization of fibotomic polynomials; also adjacent to Bhargava–Zieve and Bluher | Known after (2)–(3); must be cited and derived |
| Corollary 16 (exact Hensel valuation) | Standard simple-root Hensel theory | Routine corollary |
| Theorem 17 (simultaneous finite realization) | CRT/Hensel construction using the known local roots; no source found realizing arbitrary levels, branches, signs, and multiplicities in one additive orbit | Strongest currently unlocated contribution |
| Corollary 19 (unbounded fixed-level defect) | Immediate consequence of Theorem 17 | Corollary of candidate contribution |
| Canonical hit families | Direct specialization of the radical telescope | Explicit examples, not standalone novelty |
| Phase 5 local mean | Exact local root densities plus primitive projective measure | New deduction; only the truncated/profinite mean is proved |
| Phase 5 all-degree telescope | Classical, compositional Chebyshev transfers + standard Lucas layers/valuations | Useful degree-uniform synthesis; the transfer is not new, while the normalized support/radical package was not located and needs separate priority review |

## Source-level findings

### Byer et al. (2022)

The paper defines fibotomic \(\Psi_n\), proves (1), gives its homogeneous
extension, and determines its complete finite-field factorization.  Via
(2)–(3), this subsumes the substance of Proposition 15.  The manuscript
must cite it at the first appearance of the branch polynomials and again
at Proposition 15.

### Sagan–Tirrell (2020)

They define the Lucas atoms \(P_n(s,t)\), prove

\[
\{n\}=\prod_{d\mid n}P_d,
\]

and identify \(P_n\) with the cyclotomic descent.  This is the right
foundational citation for Propositions 9 and 12 and for composite layer
factorization.

### Alecci–Miska–Murru–Romeo (2025)

They give \(P_n(s,t)=\Phi_n(\alpha,\beta)\), the rank congruence

\[
\rho(p)\mid p-\left(\frac{\Delta}{p}\right),
\]

and a complete valuation theorem: away from the coefficient support, a
prime occurs in the rank atom and then only in the rank times powers of
that prime, with valuation one in the later atoms.  This is the correct
source for Propositions 10–14 and for the transfer-prime normalization in
the all-degree theorem.

The repetition laws used in that normalization are Sanna's Theorem 1.5
and Corollary 1.6, reproduced as Theorems 11–12 by
Alecci–Miska–Murru–Romeo.

### Bhargava–Zieve (1999)

Their Theorems 2 and 5 factor Dickson polynomials of the first and second
kind over finite fields, with roots parametrized by
\(\sqrt a(\zeta+\zeta^{-1})\).  This is adjacent finite-field prior art
for the Chebyshev/Dickson side, although the fibotomic paper is the closer
match to Proposition 15.

### Bluher (2021)

Bluher describes the finite-field images, fibers, and factorizations of
Dickson polynomials using trace/order subsets.  This should be cited as
nearby finite-field Chebyshev structure, not as the direct source of the
branch-root formula.

### Gassert (2014)

Gassert relates Chebyshev preperiods to the multiplicative order of the
parameter \(\alpha\) in \(x=\alpha+\alpha^{-1}\), and gives complete
prime-degree graph/splitting descriptions.  This is close prior art for
the order interpretation and semiconjugacy, but not for the additive
orbit's radical telescope or simultaneous seed realization.

## Revised novelty position

The defensible claim is not “new local classification.”  It is:

> Known Lucas-atom/fibotomic local structure is embedded into a primitive
> additive Chebyshev orbit.  In that orbit it yields a branchwise support
> genealogy, an exact radical telescope, and a simultaneous CRT
> realization theorem that prescribes finitely many birth levels,
> branches, splitting signs, and exact multiplicities.

The overlap search did not locate that whole orbit-level package.  That
negative search result is bounded and cannot certify priority.  Theorem 17
and the radical telescope are the correct questions for a human
specialist.

## Primary sources

- C. Byer, T. Dvorachek, E. Eckard, J. Harrington, L. Wise, and
  T. W. H. Wong,
  “On the properties of fibotomic polynomials,”
  *Advances in Applied Mathematics* 138 (2022), 102344,
  <https://arxiv.org/abs/2009.03345>.
- B. E. Sagan and J. P. Tirrell, “Lucas atoms,” *Advances in
  Mathematics* 374 (2020), 107387,
  <https://arxiv.org/abs/1909.02593>.
- G. Alecci, P. Miska, N. Murru, and G. Romeo, “On alternative
  definition of Lucas atoms and their \(p\)-adic valuations,”
  *Monatshefte für Mathematik* 207 (2025), 175–196,
  <https://arxiv.org/abs/2308.10216>.
- C. Sanna, “The \(p\)-adic valuation of Lucas sequences,”
  *Fibonacci Quarterly* 54(2) (2016), 118–124,
  <https://www.fq.math.ca/Papers1/54-2/Sanna02242016.pdf>.
- M. Bhargava and M. E. Zieve, “Factoring Dickson polynomials over finite
  fields,” *Finite Fields and Their Applications* 5 (1999), 103–111,
  <https://doi.org/10.1006/ffta.1998.0221>.
- A. W. Bluher, “Permutation properties of Dickson and Chebyshev
  polynomials with connections to number theory,” *Finite Fields and
  Their Applications* 76 (2021), 101899,
  <https://arxiv.org/abs/1707.06877>.
- T. A. Gassert, “Chebyshev action on finite fields,” *Discrete
  Mathematics* 315 (2014), 83–94,
  <https://arxiv.org/abs/1209.4396>.
