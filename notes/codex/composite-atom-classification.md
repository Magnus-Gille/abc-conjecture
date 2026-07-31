# Composite-atom classification and the all-degree local mean

Date: 2026-07-31

Status: Codex derivation for independent Claude line-check.  The finite
checks in `composite_atom.py` and `test_composite_atom.py` are regression
evidence, not inputs to the proofs.

## 1. Coordinate atoms of arbitrary index

Work in

\[
 \mathcal R=\mathbb Z[X,Y,r,t]/(r^2-Y,t^2+X)
\]

and put

\[
 \Omega=r+t,\qquad \overline\Omega=r-t.
\]

For every integer (m\ge3), define

\[
 \mathcal A_m(X,Y)=\Phi_m(\Omega,\overline\Omega).
 \tag{1.1}
\]

Here (\Phi_m(U,V)) is the homogeneous cyclotomic polynomial.

### Lemma 1 (general coordinate-atom classification)

The expression in (1.1) is an integral homogeneous polynomial in (X,Y)
of degree (\varphi(m)/2).  Let (p\nmid2m) be prime.  Then
(\mathcal A_m(X,1)) has roots in (\mathbb F_p) if and only if

\[
 m\mid p-\chi
 \qquad\text{for one }\chi\in\{1,-1\}.
 \tag{1.2}
\]

When (1.2) holds, it has exactly (\varphi(m)/2) distinct simple roots,
namely

\[
 \rho_\zeta=-\left(\frac{\zeta-1}{\zeta+1}\right)^2,
 \tag{1.3}
\]

where (\zeta), modulo (\zeta\sim\zeta^{-1}), ranges over the elements
of exact order (m) in (\mathbb F_p^\times) for (\chi=1), or in the
norm-one subgroup of (\mathbb F_{p^2}^\times) for (\chi=-1).  Every
root satisfies

\[
 \rho_\zeta\ne0,-1,
 \qquad
 \left(\frac{-\rho_\zeta}{p}\right)=\chi.
 \tag{1.4}
\]

Root sets belonging to two distinct indices (m,m'\ge3), with
(p\nmid mm'), are disjoint.

Every root is Hensel-simple.  More precisely, let
(\widehat\rho_{h+1}\in\mathbb Z) represent its (p)-adic lift modulo
(p^{h+1}).  For every (h\ge1) and every (p)-adic unit (\lambda),

\[
 v_p\!\left(\mathcal A_m
   (\widehat\rho_{h+1}+\lambda p^h,1)\right)=h.
 \tag{1.5}
\]

### Proof

For (m>2), the homogeneous cyclotomic polynomial is symmetric and has
even degree (\varphi(m)).  The fundamental theorem of symmetric
polynomials writes it integrally in

\[
 \Omega+\overline\Omega=2r,
 \qquad
 \Omega\overline\Omega=X+Y.
\]

Only even powers of the first generator occur, so (1.1) lies in
(\mathbb Z[X,Y]), homogeneously of degree (\varphi(m)/2).

Assume (1.2).  Choose (\zeta) of exact order (m) in the indicated
cyclic group and set

\[
 s=\frac{\zeta-1}{\zeta+1},\qquad \rho=-s^2.
\]

The denominator is nonzero because (m\ge3).  In the split case all
quantities lie in (\mathbb F_p).  In the norm-one case,
(\zeta^p=\zeta^{-1}), so (s^p=-s) and again (\rho\in\mathbb F_p).
At the specialization (r=1,t=s),

\[
 \frac{\Omega}{\overline\Omega}
 =\frac{1+s}{1-s}=\zeta,
\]

so the atom vanishes.  The same equations give (1.4): in the norm-one
case (s\notin\mathbb F_p), since otherwise (\zeta\in\mathbb F_p) and
(m\mid\gcd(p-1,p+1)=2).

The map (\zeta\mapsto\rho_\zeta) has precisely the inversion fibers.
Indeed equality of two values makes the corresponding Cayley parameters
(s) equal up to sign, hence makes the two (\zeta)'s equal or inverse.
Thus the construction gives (\varphi(m)/2) distinct roots.

The leading coefficient of (\mathcal A_m(X,1)) is a unit modulo (p):
at the projective point (Y=0), the quotient
(\Omega/\overline\Omega=-1) has order two, not (m), and reduction of
(\Phi_m) detects exact order because (p\nmid m).  The constructed
roots therefore exhaust a degree-(\varphi(m)/2) polynomial and are all
simple.

Conversely, a root is not (0): that specialization has quotient (1),
and (p\nmid m).  It is not (-1): one of (\Omega,\overline\Omega)
then vanishes and the homogeneous atom is nonzero.  Choose (s^2=-\rho)
and set (\zeta=(1+s)/(1-s)).  The atom equation makes (\zeta) have
exact order (m).  According as (s\in\mathbb F_p) or
(s^p=-s), this forces (m\mid p-1) or (m\mid p+1), and proves the
converse and sign assertion.

If one (\rho) belonged to the root sets for (m) and (m'), the two
choices of (s) would produce a Cayley parameter and its inverse.  Their
exact orders coincide, so (m=m').  This proves disjointness.  Simplicity,
Hensel's lemma, and the first nonzero Taylor term give (1.5).  \(\square\)

## 2. From coordinate atoms to the fixed Lucas atoms

For a seed ((X,Y)), put

\[
 \alpha=(r+t)^2,\qquad \beta=(r-t)^2.
\]

The homogeneous version of the standard identity for
(\Phi_m(Z^2)) is

\[
 \Phi_m(\alpha,\beta)=
 \begin{cases}
  \mathcal A_m(X,Y)\mathcal A_{2m}(X,Y),&m\text{ odd},\\
  \mathcal A_{2m}(X,Y),&m\text{ even}.
 \end{cases}
 \tag{2.1}
\]

Define

\[
 \lambda(m)=
 \begin{cases}
  m,&m\text{ odd},\\
  2m,&m\text{ even}.
 \end{cases}
 \tag{2.2}
\]

For odd (p\nmid m), the universal Lucas atom
(\Phi_m(\alpha,\beta)) therefore has exactly (\varphi(m)) distinct
simple projective roots if

\[
 \lambda(m)\mid p-1
 \quad\text{or}\quad
 \lambda(m)\mid p+1,
 \tag{2.3}
\]

and none otherwise.  For odd (m), the conditions for (m) and (2m)
are equivalent because (p\pm1) is even, and the two root sets are
disjoint.  For even (m),
(\varphi(2m)/2=\varphi(m)).  Distinct universal indices also have
disjoint root sets by Lemma 1.

For fixed degree (d\ge2), recall

\[
 \mathcal L_{d,j}
 =\{m:m\mid d^{j+1},\ m\nmid d^j\}.
\]

The coordinate indices contributed by (2.1) are pairwise distinct both
within one layer and across layers.  Consequently, for (p\nmid2d), the
normalized layer (E_{d,j}) has exactly

\[
 N_{d,j}(p)=
 \sum_{m\in\mathcal L_{d,j}}
 \varphi(m)\,
 \mathbf1_{\lambda(m)\mid p-1\ \text{or}\ \lambda(m)\mid p+1}
 \tag{2.4}
\]

distinct simple roots in the primitive projective line over
(\mathbb F_p).  No independence assertion is used: (2.4) is an exact
disjoint union.

## 3. Bounded local mean for every degree

Let (\mathcal S_d(H)) be the (d)-admissible positive primitive
opposite-parity seeds in ([1,H]^2), as in the companion note.  For fixed
(n,P,K), put

\[
 D_{d,n,P,K}(a,b)
 =\sum_{j<n}\sum_{\substack{p\le P\\p\nmid2d}}
 \log p\sum_{h=2}^{K+1}\mathbf1_{p^h\mid E_{d,j}(a,b)}.
 \tag{3.1}
\]

### Theorem 2 (all-degree bounded iterated local mean)

For every integer degree (d\ge2),

\[
 \lim_{P\to\infty}\lim_{K\to\infty}\lim_{H\to\infty}
 \frac1{|\mathcal S_d(H)|}
 \sum_{(a,b)\in\mathcal S_d(H)}D_{d,n,P,K}(a,b)
 =L_d(n),
 \tag{3.2}
\]

where

\[
 L_d(n)=
 \sum_{j<n}\sum_{m\in\mathcal L_{d,j}}\varphi(m)
 \sum_{\substack{p\nmid2d\\
  \lambda(m)\mid p-1\ \mathrm{or}\ \lambda(m)\mid p+1}}
 \frac{\log p}{p^2-1}.
 \tag{3.3}
\]

There is an explicit constant (C_d<\infty), independent of (n), for
which (L_d(n)\le C_d).  One may take

\[
 C_d=3\sum_{\substack{m\mid d^\infty\\m>1}}
 \frac{\varphi(m)}{m^2}
 \left(\zeta(2)\log(4m)-\zeta'(2)\right).
 \tag{3.4}
\]

If

\[
 A_d=\prod_{q\mid d}\left(1+\frac1q\right),
\]

then the same constant has the closed form

\[
 C_d=3\left[
  \bigl(\zeta(2)\log4-\zeta'(2)\bigr)(A_d-1)
  +\zeta(2)A_d\sum_{q\mid d}\frac{q\log q}{q^2-1}
 \right].
 \tag{3.5}
\]

### Proof

The fixed conditions at primes dividing (2d) define a positive set of
local classes; the (3)-adic valuation-one condition is nonempty, for
example on (a\equiv3,b\equiv2\pmod9).  Standard Möbius inversion and
the Chinese remainder theorem therefore give
(|\mathcal S_d(H)|\sim\kappa_dH^2) with (\kappa_d>0).

Fix (p\nmid2d).  The admissibility conditions are independent of the
primitive (p)-adic projective coordinate.  By (2.4), every root modulo
(p) lifts uniquely modulo (p^h).  Each root permits
(\varphi(p^h)) unit choices for the second coordinate, while the number
of primitive pairs modulo (p^h) is (p^{2h}-p^{2h-2}).  Hence

\[
 \lim_{H\to\infty}\Pr_{\mathcal S_d(H)}(p^h\mid E_{d,j})
 =\frac{N_{d,j}(p)}{p^{h-1}(p+1)}.
 \tag{3.6}
\]

Summing (3.6) for (2\le h\le K+1), and then taking the displayed
iterated limits, gives (3.3).

For every (q\ge3), enlarging the eligible primes to all integers
(aq\pm1) gives

\[
 \sum_{q\mid p-1\ \mathrm{or}\ q\mid p+1}
 \frac{\log p}{p^2-1}
 \le
 \frac3{q^2}\left(\zeta(2)\log(2q)-\zeta'(2)\right).
 \tag{3.7}
\]

Indeed, the plus denominator is at least (a^2q^2), the minus
denominator at least (a^2q^2/2), and
(\log(aq\pm1)\le\log(2aq)).  Since
(m\le\lambda(m)\le2m), (3.7) gives (3.4) after summing every index
supported on the prime divisors of (d).

Finally,

\[
 \sum_{m\mid d^\infty}\frac{\varphi(m)}{m^2}=A_d,
 \qquad
 \sum_{m\mid d^\infty}\frac{\varphi(m)\log m}{m^2}
 =A_d\sum_{q\mid d}\frac{q\log q}{q^2-1},
\]

by differentiating the finite Euler product over (q\mid d).  This
proves convergence and (3.5).  \(\square\)

## 4. Scope

Theorem 2 upgrades the companion's composite-degree future-work remark to
an unconditional theorem about the same iterated truncated/profinite
mean as its prime-degree result.  It does **not** pass to the untruncated
integer-box mean and gives no pointwise result for a fixed orbit.  The
large-square tail and the fixed-orbit deep Lucas--Wieferich tail remain
unchanged.
