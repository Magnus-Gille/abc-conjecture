# Phase 7 polynomial-window map

Authors: Codex and Claude, under the repository collaboration protocol

Date: 2026-07-31

Status: **FINAL CANDIDATE — CHECKSUM SIGNATURES PENDING**

The requested polynomial-window estimate remains open.  This note
records a new unconditional truncation theorem, the independently
derived Lucas--Wieferich bridge, the exact deep-lift obstruction, and
the bounded diagnostics.  It is a research handoff, not a proof of the
fixed-orbit conjecture or of the \(abc\) conjecture, and not a priority
claim.

## 1. Target and notation

Fix either the quadratic orbit or one admissible prime-degree orbit.
At layer \(j\), write

\[
q=q_j,
\qquad E=E_j,
\]

where

\[
q_j=
\begin{cases}
2^{j+2},&\text{quadratic orbit},\\
\ell^{j+1},&\text{prime degree }\ell.
\end{cases}
\]

For \(Y\ge q\), let

\[
D_j(Y)=
\sum_{\substack{p\le Y\\p^2\mid E_j}}
(v_p(E_j)-1)\log p.
\tag{1}
\]

Every sufficiently large layer prime satisfies

\[
p\equiv\pm1\pmod q.
\tag{2}
\]

The Phase 7 target is, for at least one fixed
\(0<\varepsilon<1\),

\[
D_j(q^{1+\varepsilon})=o(q).
\tag{3}
\]

## 2. Unconditional truncation theorem

For \(k\ge2\), put

\[
A_{j,k}(Y)=
\sum_{\substack{p\le Y\\p^k\mid E_j}}\log p.
\tag{4}
\]

### Theorem C: Every fixed depth is harmless

Fix \(1\le\beta<2\) and set \(Y=q^\beta\).  For every integer
\(k\ge2\),

\[
A_{j,k}(Y)
\le
2\left(\frac{Y}{q}+1\right)\log Y
=O(q^{\beta-1}\log q)
=o(q).
\tag{5}
\]

The bound is independent of \(k\).  In particular, even if every
candidate prime below \(q^{1+\varepsilon}\) were squared, its first
unit of defect would total only

\[
O(q^\varepsilon\log q)=o(q).
\tag{6}
\]

#### Proof

There are at most \(2(Y/q+1)\) integers up to \(Y\) in the two residue
classes (2).  The primes in (4) form a subset, and each has logarithm at
most \(\log Y\).  Since \(\beta-1<1\), (5) follows. \(\square\)

The exact layer-cake identity is

\[
D_j(Y)=\sum_{k\ge2}A_{j,k}(Y).
\tag{7}
\]

The point is that (5) cannot simply be summed over an unbounded number
of valuation depths.  For an integer \(K\ge1\), define

\[
T_{j,K}(Y)=
\sum_{\substack{p\le Y\\p^2\mid E_j}}
\min\{v_p(E_j)-1,K\}\log p
\tag{8}
\]

and

\[
R_{j,K}(Y)=
\sum_{\substack{p\le Y\\p^2\mid E_j}}
(v_p(E_j)-1-K)_+\log p.
\tag{9}
\]

Then

\[
D_j(Y)=T_{j,K}(Y)+R_{j,K}(Y)
\tag{10}
\]

exactly.

### Theorem D: Polynomial window equals its deep tail

Let \(1\le\beta<2\), \(Y=q^\beta\), and suppose

\[
K_j=o\!\left(\frac{q^{2-\beta}}{\log q}\right).
\tag{11}
\]

Then

\[
T_{j,K_j}(Y)=o(q),
\tag{12}
\]

and therefore

\[
\boxed{
D_j(q^\beta)=o(q)
\iff
R_{j,K_j}(q^\beta)=o(q).
}
\tag{13}
\]

#### Proof

Candidate counting gives

\[
T_{j,K_j}(Y)
\le
2K_j\left(\frac{Y}{q}+1\right)\log Y
=O(K_jq^{\beta-1}\log q)=o(q).
\]

Equation (13) follows from the nonnegative decomposition (10).
\(\square\)

For \(\beta=1+\varepsilon\), the concrete choice

\[
K_j=\left\lfloor
\frac{q^{1-\varepsilon}}{(\log q)^2}
\right\rfloor
\tag{14}
\]

makes \(T_{j,K_j}=O(q/\log q)\).  Thus ordinary square lifts, cube
lifts, every fixed depth, and even depths growing almost as fast as
\(q^{1-\varepsilon}/\log q\) are harmless.  The target is precisely a
uniform-integrability statement for the remaining extraordinarily deep
lifts.

## 3. Lucas--Wieferich bridge

Let

\[
m_j=
\begin{cases}
q_j/2,&\text{quadratic descended }U\text{-rank},\\
q_j,&\text{prime degree}.
\end{cases}
\]

Let \((U_n)\) be the fixed descended Lucas sequence, let
\(u=\alpha/\beta\), and write

\[
\chi(p)=\left(\frac{\Delta}{p}\right).
\]

### Proposition E: A squared layer prime is Lucas--Wieferich

Outside the fixed ramified and seed primes, if \(p^2\mid E_j\), then

\[
m_j\mid p-\chi(p),
\]

and

\[
v_p(U_{p-\chi(p)})=v_p(E_j)\ge2.
\tag{15}
\]

#### Proof

Write \(p-\chi(p)=r m_j\).  Since \(p\nmid r\), local lifting at the
unramified odd prime gives

\[
v_{\mathfrak p}(u^{p-\chi(p)}-1)
=v_{\mathfrak p}(u^{m_j}-1).
\]

The exact-rank denominator is a \(p\)-adic unit.  Hence the right side
is \(v_p(E_j)\), and clearing the fixed Lucas denominator gives (15).
For the quadratic orbit, the equivalent \(q_j\)-exponent statement
uses

\[
u^{q_j}-1=(u^{q_j/2}-1)(u^{q_j/2}+1),
\]

with the second factor a unit at the layer prime. \(\square\)

Define the weighted fixed-pair counting function

\[
S_U(x)=
\sum_{\substack{p\le x\ \mathrm{unramified}\\
p^2\mid U_{p-\chi(p)}}}
(v_p(U_{p-\chi(p)})-1)\log p.
\tag{16}
\]

### Corollary F: Two sufficient inputs

1. If, for some \(\theta<1\),
   \[
   S_U(x)\ll x^\theta,
   \tag{17}
   \]
   then (3) holds for every
   \[
   0<\varepsilon<\frac{1-\theta}{\theta}.
   \tag{18}
   \]
2. If
   \[
   B_j(q^{1+\varepsilon})
   :=
   \max_{\substack{p\le q^{1+\varepsilon}\\p^2\mid E_j}}
   v_p(E_j)
   =o\!\left(\frac{q^{1-\varepsilon}}{\log q}\right),
   \tag{19}
   \]
   then (3) holds.

The first claim follows from

\[
D_j(q^{1+\varepsilon})
\le S_U(q^{1+\varepsilon})
\ll q^{(1+\varepsilon)\theta}.
\]

The second follows by multiplying the maximum by the at most
\(2(q^\varepsilon+1)\) candidates and by \((1+\varepsilon)\log q\).

A fixed-power local estimate

\[
v_p(E_j)\ll p^{1-\kappa}
\tag{20}
\]

would yield at least one polynomial window, but the exponents must
satisfy

\[
\varepsilon<\frac{\kappa}{2-\kappa}.
\tag{21}
\]

No estimate (17), (19), or (20) with fixed power saving is known here.
They are sufficient, but Theorem D's deep-tail condition is weaker than
all of them.

## 4. Conditional super-Wieferich bridge

For a prime ideal \(\mathfrak p\) outside the fixed denominator set,
call \(\mathfrak p\) super-Wieferich for \(u\) when

\[
u^{N(\mathfrak p)-1}\equiv1\pmod{\mathfrak p^3}.
\tag{22}
\]

If \(v_p(E_j)\ge3\), Proposition E and one more lifting step show that
a relevant \(\mathfrak p\mid p\) satisfies (22): in the split case
\(q\mid p-1\), and in the inert case \(q\mid p+1\mid p^2-1\); the
remaining multiplier is prime to \(p\).

### Corollary G: Finiteness of super-Wieferich primes suffices

If the fixed \(S\)-unit \(u\) has only finitely many super-Wieferich
prime ideals, then

\[
D_j(q^\beta)=o(q)
\tag{23}
\]

for every fixed \(1\le\beta<2\).

Indeed, genealogy places those finitely many rational primes in
finitely many birth layers.  Later layers have \(v_p(E_j)\le2\), so
(23) is just Theorem C with \(k=2\).

Fellini--Murty explicitly state that finiteness of super-Wieferich
prime ideals is expected and use it as a hypothesis, not a theorem.
Their formal statements concern integral admissible bases in
\(\mathcal O_K\); our ratio \(u\) is generally only an \(S\)-unit.
Thus their theorem is not being applied verbatim.  Corollary G is the
elementary local implication above, and the citation identifies the
integral-base analogue as a recognized open hypothesis.

## 5. Why the standard tools still stop

### Stewart's pointwise valuation lemma

Summing Stewart's bound at the candidate sizes, rather than replacing
every term by one maximum, still has worst-case scale

\[
\frac{Y^2}{q}
\exp\!\left(
-\frac{\log Y}{51.9\log\log Y}
\right)
(\log q)(\log Y).
\]

At \(Y=q^{1+\varepsilon}\), this is

\[
q^{1+2\varepsilon-o(1)},
\tag{24}
\]

not \(o(q)\).  Stewart is useful near the congruence floor, as in
Phase 6, but does not give a uniform bound across a fixed polynomial
window.

### GRH and Chebotarev

GRH for a fixed Dirichlet or Hecke family does not encode the
mod-\(\mathfrak p^2\) lift of a fixed base.  Even mere prime counting
in the two window classes has GRH main term of scale
\(q^\varepsilon/\log q\) and error of scale
\(q^{(1+\varepsilon)/2}\log^2 q\), which dominates when
\(\varepsilon<1\).

More fundamentally, the natural Kummer extension with exponent \(p\)
varies with the prime being tested, and that prime is ramified in the
extension, so there is no Chebotarev Frobenius at the diagonal prime.
This does not exclude every conceivable Galois reformulation; it shows
that ordinary effective Chebotarev in a fixed extension is not the
missing theorem.

### Large sieve and seed averages

Known Fermat-quotient large-sieve results vary the base for a fixed
prime, or average over primes while retaining a family of bases.  They
do not bound a single fixed base along the varying moduli \(p^2\).
The Phase 5 local-mean theorem similarly averages over seeds at fixed
layer.  Neither average transfers pointwise to this one fixed orbit
without a new uniform-integrability theorem.

### Rank-density results do not reach the diagonal

Sanna proves an asymptotic for primes \(p\le x\) for which a prescribed
admissible odd integer \(d\) divides the rank of appearance in a fixed Lucas
sequence.  The uniform range in that theorem requires

\[
x\ge \exp\!\bigl(B e^{8\omega(d)}d^8\bigr).
\]

Our diagonal choice \(d\asymp q\), \(x=q^{1+\varepsilon}\) lies far outside
that range.  The theorem also controls a mod-\(p\) rank condition, not the
mod-\(p^2\) lift or its depth.

### A contrary preprint claim does not survive proof audit

Carella's arXiv preprint `1712.08166v2` claims fixed-base Wieferich
asymptotics and finiteness of primes with \(p^3\mid v^{p-1}-1\).  Its
characteristic function uses denominator \(\varphi(p^k)\) to detect equality
modulo \(p^k\), so it is not well-defined on the residue ring.  The later
error estimate also factors a shared character sum as a product and uses a
false geometric-sum evaluation.  Thus its Theorems 1.1--1.3 do not follow
from the displayed proof and cannot supply the missing super-Wieferich
input.  The exact audit is recorded in
`notes/codex/wieferich-source-audit.md`.

## 6. Finite diagnostics

The programmed-square constructions from Phase 5 give exact test
vectors for Proposition E:

- the quadratic realization has \(v_7(E_1)=v_7(U_8)=2\); and
- the cubic realization has \(v_{17}(E_1)=v_{17}(U_{18})=2\).

Two independent implementations then enumerated the fixed-pair
Lucas--Wieferich condition.  Claude's companion-matrix implementation
checked through \(10^6\); Codex's independent binary quadratic-algebra
implementation checked through \(10^6\).

| orbit pair \((P,Q)\) | Lucas--Wieferich primes \(p\le10^6\) | rank | pure orbit-degree power? | depth \(\ge3\)? |
|---|---:|---:|---:|---:|
| quadratic \((14,81)\) | 65519 | 455 | no | no |
| cubic \((-2,25)\) | 47 | 24 | no | no |
| quintic \((-6,49)\) | 53 | 26 | no | no |

The two implementations agree on the complete range through \(10^6\).
None of the three hits can enter its orbit tower because its rank is not
a pure power of the orbit degree, and none is super-Wieferich.  These
are finite observations only.  Treating Lucas--Wieferich behavior and
the rank filter as independent is a heuristic, not a theorem.

## 7. Joint draft opinion and exact frontier

The polynomial-window route has produced a real unconditional
refinement:

\[
\text{all fixed or moderately growing lift depths are harmless};
\]

the target is equivalent to the far deep-valuation tail (13).  This is
qualitatively sharper than asking for “few Wieferich primes”: even if
every candidate prime had valuation two, the whole window would still
be \(o(q)\).

What remains open is

\[
R_{j,K_j}(q^{1+\varepsilon})=o(q)
\]

for one fixed \(\varepsilon>0\) and one

\[
K_j=o(q^{1-\varepsilon}/\log q).
\]

Equivalently, a proof must rule out an aggregate of exceptionally deep
rank-Wieferich lifts at one sparse sequence of ranks.  The checked
unconditional tools do not do this.  Hence Phase 7 has sharpened the
boundary and connected it to the recognized super-Wieferich frontier,
but has not proved the polynomial window, the fixed-orbit conjecture,
or any new case of \(abc\).

## 8. Reproduction and primary records

- Codex proof and obstruction analysis:
  `notes/codex/polynomial-window-reduction.md`
- Codex independent arithmetic checker and tests:
  `notes/codex/polynomial_window_check.py`,
  `notes/codex/test_polynomial_window_check.py`
- Claude independent reduction and checker:
  `notes/claude/window-reduction.md`,
  `notes/claude/window_wieferich_check.py`

Primary records used in this phase:

- C. L. Stewart, “On divisors of Lucas and Lehmer numbers,”
  *Acta Mathematica* 211 (2013), 291--314,
  DOI `10.1007/s11511-013-0105-y`.
- Nic Fellini and M. Ram Murty, “Wieferich primes in number fields and
  the conjectures of Ankeny--Artin--Chowla and Mordell,” *Journal of
  Number Theory* 285 (2026), 209--229,
  DOI `10.1016/j.jnt.2026.01.002`.
- J. Bourgain, K. Ford, S. V. Konyagin, and I. E. Shparlinski, “On the
  divisibility of Fermat quotients,” *Michigan Mathematical Journal*
  59 (2010), 313--328, DOI `10.1307/mmj/1281531459`.
- Carlo Sanna, “On the divisibility of the rank of appearance of a
  Lucas sequence,” arXiv:`2008.12506`.
- N. A. Carella, “Results for Wieferich Primes,”
  arXiv:`1712.08166v2` (rejected after the proof audit above).
