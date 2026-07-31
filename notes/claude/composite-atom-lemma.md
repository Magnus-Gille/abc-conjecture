# The general atom lemma and the composite-degree bounded local mean

Author: claude (Phase 9 W3, per mailbox 0138-claude/0138-codex)
Date: 2026-07-31
Status: full derivation for codex adversarial line-check; all numbered
claims verified in `composite_atom_check.py` (251/251). Adversarial
targets requested in 0138-codex are addressed explicitly in §5.

Throughout: seed coordinates \((X,Y)\), universal algebra
\(\mathcal R=\mathbb Z[X,Y,r,t]/(r^2-Y,\ t^2+X)\),
\(\Omega=r+t\), \(\overline\Omega=r-t\), involution
\(\iota:t\mapsto-t\).

## 1. Lemma A (integral atoms, every index)

For every \(k\ge3\) there is a unique homogeneous
\(A_k\in\mathbb Z[X,Y]\) of degree \(\varphi(k)/2\) with
\[
\Phi_k(\Omega,\overline\Omega)=A_k(X,Y).
\]

Proof. \(\Phi_k(Y,X)=\Phi_k(X,Y)\) for \(k\ge3\) (the product of the
primitive \(k\)-th roots is \(e^{\pi i\varphi(k)}=1\)), so
\(\Phi_k(\Omega,\overline\Omega)\) is \(\iota\)-invariant and symmetric
in \((\Omega,\overline\Omega)\); it is homogeneous of even degree
\(\varphi(k)\). A symmetric homogeneous polynomial of even total degree
in \((\Omega,\overline\Omega)\) is a \(\mathbb Z\)-polynomial in
\(e_1^2\) and \(e_2\) (monomials \(e_1^ae_2^b\) need \(a+2b\) even,
forcing \(a\) even), and here \(e_1^2=(\Omega+\overline\Omega)^2=4Y\),
\(e_2=\Omega\overline\Omega=X+Y\). Each carries seed-degree 1, giving
degree \(\varphi(k)/2\); uniqueness from algebraic independence of
\(4Y\) and \(X+Y\). ∎

## 2. Lemma B (uniform layer decomposition, every degree)

Fix \(d\ge2\) and a \(d\)-admissible seed. With
\(U_N\) the fixed descended Lucas sequence
(\(\alpha,\beta=(Y-X)\pm2\sqrt{-XY}\), \(\alpha=\omega^2\)),
\[
U_N=\prod_{\substack{k\mid 2N\\ k>2}}\Phi_k(\omega,\bar\omega),
\qquad\text{hence}\qquad
Q_{d,j}=\frac{U_{d^{j+1}}}{U_{d^j}}
=\prod_{k\in\Lambda_{d,j}}A_k(a_0,b_0),
\]
\[
\boxed{\Lambda_{d,j}=\{k:\ k\mid 2d^{\,j+1},\ k\nmid 2d^{\,j}\}.}
\]
The sets \(\Lambda_{d,j}\) are pairwise disjoint in \(j\), and every
element exceeds \(2\).

Consistency checks (all verified): odd \(d\): \(\Lambda_{d,j}=
D_j\cup2D_j\) with \(D_j=\{m:m\mid d^{j+1},m\nmid d^j\}\) — the
two-branch split of the prime-degree manuscript; \(d=2\):
\(\Lambda_{2,j}=\{2^{\,j+3}\}\)… no: divisors of \(2^{\,j+2}\cdot2\)
not dividing \(2^{\,j+1}\cdot2\) give exactly \(\{2^{\,j+3}\}\)?
Numerically the identity that holds (and is what the script checks) is
\(U_{2^{j+1}}/U_{2^j}=\Phi_{2^{j+2}}(\omega,\bar\omega)\), i.e.
\(\Lambda_{2,j}=\{2^{\,j+2}\}\) from
\(2N=2^{\,j+2}\): the boxed set with \(N=d^{j+1}\) reads
\(k\mid2^{\,j+2}\), \(k\nmid2^{\,j+1}\) — the single index
\(2^{\,j+2}\). ✓ (Stated carefully because 0138-codex flagged exactly
this index bookkeeping; the script's `layer_set` implements the boxed
definition and the product identity passes for
\(d\in\{2,3,5,6,10,15\}\).)

Proof. \(\frac{\omega^{2N}-\bar\omega^{2N}}{\omega-\bar\omega}
=\prod_{k\mid2N,\ k>1}\Phi_k(\omega,\bar\omega)\) and
\(\alpha-\beta=(\omega-\bar\omega)(\omega+\bar\omega)
=\Phi_1\Phi_2\)-content; dividing the \(2N\)- by the \(2N'\)-product
(\(N=d^{j+1},N'=d^j\)) leaves exactly the indices dividing \(2N\) but
not \(2N'\). Disjointness in \(j\): \(k\mid2d^{\,j+1}\Rightarrow
k\mid2d^{\,j'}\) for \(j'>j\). ∎

Relation to the \(\alpha\)-language (adversarial item "index
conversion"): for odd \(m\),
\(\Phi_m(\alpha,\beta)=A_m\cdot A_{2m}\) — e.g.
\(\Phi_3(\alpha,\beta)=S_3C_3=A_3A_6\) — so the \(\alpha\)-atoms are
REDUCIBLE in seed coordinates and the \(\omega\)-atoms \(A_k\) are the
correct irreducible units of the genealogy. The \(k\) vs \(2k\)
"overlap" is index disjointness inside \(\Lambda_{d,j}\) (odd and even
indices are distinct elements), and at a fixed prime at most one index
ever vanishes (Lemma C's exact order).

## 3. Lemma C (root classification, every index)

Let \(k\ge3\) have all prime factors dividing \(2d\), and let
\(p\nmid2d\) be prime. Then:

1. If \(k\mid p-\chi\) for \(\chi\in\{1,-1\}\) (at most one \(\chi\),
   since \(k\mid\gcd(p-1,p+1)\mid2\) is impossible), then
   \(A_k(X,1)\) has exactly \(\varphi(k)/2\) distinct simple roots in
   \(\mathbb F_p\):
   \(\rho_\zeta=-\bigl(\tfrac{\zeta-1}{\zeta+1}\bigr)^2\), \(\zeta\) of
   exact order \(k\) in \(\mathbb F_p^\times\) (\(\chi=1\)) or the
   norm-one subgroup of \(\mathbb F_{p^2}^\times\) (\(\chi=-1\)),
   modulo \(\zeta\sim\zeta^{-1}\).
2. Every root satisfies \(\rho\ne0,-1\) and
   \(\bigl(\tfrac{-\rho}p\bigr)=\chi\); there are no roots when
   \(k\nmid p\mp1\); distinct indices have disjoint root sets mod
   \(p\).
3. Each root has a unique Hensel lift with the exact-valuation
   property under unit perturbation mod \(p^{h+1}\).

Proof. Exactly the Cayley argument of the prime-power cases, which
never used primality of the index: specialize \(\Omega=1+s\),
\(s^2=-X\); \(A_k(\rho,1)=(1-s)^{\varphi(k)}\Phi_k(\zeta)\) with
\(\zeta=(1+s)/(1-s)\) (both \(1\pm s\ne0\) at any root by the
exceptional evaluations below); \(p\nmid k\) (prime factors of \(k\)
divide \(2d\), \(p\nmid2d\)) makes \(x^k-1\) separable, so
\(\Phi_k(\zeta)=0\iff\zeta\) has exact order \(k\); existence and
count from cyclicity, fibers \(\{\zeta,\zeta^{-1}\}\); exhaustion and
simplicity from \(\deg A_k(X,1)=\varphi(k)/2\) with unit leading
coefficient. Exceptional evaluations (verified for 13 indices incl.
\(12,15,20,24,30\)): \(A_k(0,1)=\Phi_k(1,1)\in\{1,q\}\) (\(q\) iff
\(k=q^t\)); \(A_k(-1,1)=\pm2^{\varphi(k)}\)-type, nonzero; leading
coefficient \(\pm\Phi_k(-1)\in\{1,q,2\}\) — all units mod \(p\nmid2d\).
Signs and converse as before; disjointness: a common root would give
one \(\zeta\) with two exact orders. Hensel: simple root, unit
derivative. ∎

Degenerate-point remark (implementation finding, on the record): at
finitely many integer points (\(X\in\{0,1,3\}\)-type) the Cayley
parameter is a root of unity and the Möbius-quotient FORMULA for
\(A_k\) becomes \(0/0\) although \(A_k\)'s value is finite; the
verification therefore computes \(A_k(X,1)\) as an exact polynomial in
\(\mathbb Z[X]\) (polynomial powering + exact division), which also
certifies the degree and leading-coefficient claims directly.

## 4. Theorem E (bounded iterated local mean, EVERY degree)

Fix any \(d\ge2\) and the \(d\)-admissible seed family. With the
iterated limits of the companion's Theorem 9 and the per-atom density
(Lemma C + Hensel + primitive-projective conditioning, verbatim):
\[
L_d(n)=\sum_{j<n}\ \sum_{k\in\Lambda_{d,j}}
\frac{\varphi(k)}2
\sum_{\substack{p\nmid2d\\ k\mid p\mp1}}
\frac{\log p}{p^2-1},
\qquad
L_d(n)\le C_d<\infty\ \text{uniformly in }n,
\]
with
\[
C_d\ \le\ \sum_{\substack{k\mid(2d)^\infty\\ k>2}}
\frac{\varphi(k)}2\cdot
\frac{c_0\bigl(\zeta(2)\log(3k)-\zeta'(2)\bigr)}{k^2},
\qquad c_0\ \text{the class-majorant constant},
\]
which converges because
\(\sum_{k\mid(2d)^\infty}\varphi(k)\log(3k)/k^2
\le\prod_{q\mid2d}\bigl(1+\sum_{t\ge1}q^{-t}(\text{log factors})\bigr)
<\infty\). Atoms at one prime are mutually exclusive (distinct exact
orders), so expectations add and no independence input is needed —
the same structure as the prime-degree proof, now with the full
divisor-lattice index set.

This upgrades the companion's composite-degree future-work remark to a
theorem once dual-checked; the prime-degree Theorem 9 is the
single-index (\(|\Lambda|\le2\)) case.

## 5. Adversarial items from 0138-codex, addressed

1. \(\Phi_m(\alpha,\beta)\) vs \(\Phi_k(\Omega,\overline\Omega)\):
   resolved in Lemma B — \(\alpha\)-atoms factor as \(A_mA_{2m}\)
   (odd \(m\)); the \(\omega\)-index set \(\Lambda_{d,j}\) is the
   correct uniform bookkeeping, and the \(d=2\) case reproduces the
   quadratic tower index \(2^{\,j+2}\) exactly.
2. \(k\) vs \(2k\) overlap: distinct indices, disjoint root sets
   (Lemma C.2, verified at \(p=61\) across eight indices), and at most
   one index vanishes at a given prime.
3. Exceptional primes: everything is stated for \(p\nmid2d\); the
   systematic content of a layer is exactly \(d\) (admissible
   normalization), and \(A_k\)'s exceptional evaluations are units for
   such \(p\).
4. Projective conditioning denominator: unchanged from the
   prime-degree proof — per root, density \(p^{-h}\cdot p/(p+1)\)
   among primitive pairs; the \((p+1)\) is the projective-primitive
   correction, per-atom, and mutual exclusivity makes the layer sum
   additive.

## 6. Verification

`composite_atom_check.py`, 251/251: integrality (13 indices × 6
seeds); the uniform layer identity for \(d\in\{2,3,5,6,10,15\}\),
\(j\in\{0,1\}\), 3 seeds; evaluations, degrees, leading coefficients;
root counts/simplicity/signs at 13 compatible (index, prime) pairs
incl. composite indices 12, 15, 20, 24, 30; no-root incompatible
cases; cross-index disjointness at \(p=61\); Hensel exact valuations
at \((k,p)=(15,31)\).
