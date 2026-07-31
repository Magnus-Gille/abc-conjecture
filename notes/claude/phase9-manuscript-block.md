# Manuscript-ready block: general atoms and the all-degree local mean

Author: claude (Phase 9; incorporates the five edits of mailbox
0141-codex and adopts codex's closed-form majorant (3.5) and
square-index identity (2.1) with cross-checks 30/30). For assembly
into the Phase 9 candidate; numbering placeholders (L1)–(T2).

**Setting.** \(\mathcal R=\mathbb Z[X,Y,r,t]/(r^2-Y,\ t^2+X)\),
\(\Omega=r+t\), \(\overline\Omega=r-t\). For \(k\ge3\) define the
coordinate atom \(\mathcal A_k(X,Y)=\Phi_k(\Omega,\overline\Omega)\).

**Lemma (L1) — integral atoms.** \(\mathcal A_k\in\mathbb Z[X,Y]\),
homogeneous of degree \(\varphi(k)/2\).
*Proof.* \(\Phi_k\) is symmetric of even degree \(\varphi(k)\) for
\(k\ge3\); by the fundamental theorem of symmetric polynomials it is
integral in \(\Omega+\overline\Omega=2r\) and
\(\Omega\overline\Omega=X+Y\), with only even powers of \(2r\)
occurring, and \((2r)^2=4Y\). \(\square\)

**Lemma (L2) — uniform layer decomposition.** Fix \(d\ge2\) and a
\(d\)-admissible seed. With \(U_N\) the fixed descended Lucas sequence
and \(Q_{d,j}=U_{d^{j+1}}/U_{d^j}\):
\[
Q_{d,j}=\prod_{k\in\Lambda_{d,j}}\mathcal A_k(a_0,b_0),
\qquad
\Lambda_{d,j}=\{k:\ k\mid 2d^{\,j+1},\ k\nmid 2d^{\,j}\},
\]
the sets \(\Lambda_{d,j}\) pairwise disjoint in \(j\). For \(d=2\)
this is the single index \(2^{\,j+2}\); for odd \(d\) it is
\(D_j\cup2D_j\) with \(D_j=\{m:m\mid d^{j+1},\ m\nmid d^j\}\); even
composite \(d\) is covered uniformly. Division by the systematic layer
content \(d\) (the \(d\)-admissible normalization
\(E_{d,j}=|Q_{d,j}|/d\)) changes no root and no valuation at any prime
\(p\nmid2d\), because \(d\) is a \(p\)-adic unit there.
*Proof.* \((\omega^{2N}-\bar\omega^{2N})/(\omega-\bar\omega)
=\prod_{k\mid2N,\ k>1}\Phi_k(\omega,\bar\omega)\); divide the
\(2d^{\,j+1}\)-product by the \(2d^{\,j}\)-product. Disjointness:
\(k\mid2d^{\,j+1}\Rightarrow k\mid2d^{\,j'}\) for \(j'>j\). \(\square\)

*Remark (index conversion).* For the \(\alpha\)-language atoms one has
the square-index identity
\(\Phi_m(\alpha,\beta)=\mathcal A_m\mathcal A_{2m}\) (\(m\) odd),
\(=\mathcal A_{2m}\) (\(m\) even); the \(\alpha\)-atoms are reducible
in seed coordinates and the \(\mathcal A_k\) are the irreducible units
of the genealogy.

**Lemma (L3) — root classification, arbitrary index.** Let \(k\ge3\),
\(p\nmid2k\) prime. Roots of \(\mathcal A_k(X,1)\) in \(\mathbb F_p\)
exist iff \(k\mid p-\chi\) for one \(\chi\in\{1,-1\}\) (unique, since
\(k\mid\gcd(p-1,p+1)\mid2\) is impossible). In that case there are
exactly \(\varphi(k)/2\) distinct simple roots
\(\rho_\zeta=-((\zeta-1)/(\zeta+1))^2\), \(\zeta\) of exact order
\(k\) in \(\mathbb F_p^\times\) (\(\chi=1\)) or the norm-one subgroup
of \(\mathbb F_{p^2}^\times\) (\(\chi=-1\)), modulo
\(\zeta\sim\zeta^{-1}\); every root satisfies \(\rho\ne0,-1\) and
\((\tfrac{-\rho}p)=\chi\); root sets of distinct indices are disjoint.
Hensel clause: each root has a unique \(p\)-adic lift; if
\(\widehat\rho_{h+1}\in\mathbb Z\) REPRESENTS THAT LIFT MODULO
\(p^{h+1}\), then for every \(h\ge1\) and every unit \(\lambda\),
\(v_p(\mathcal A_k(\widehat\rho_{h+1}+\lambda p^h,1))=h\).
*Proof.* Cayley specialization \(r=1\), \(t=s\), \(s^2=-X\),
\(\zeta=(1+s)/(1-s)\); separability of \(x^k-1\) from \(p\nmid k\);
counts by cyclicity and inversion fibers; exhaustion and simplicity
from degree \(\varphi(k)/2\) with unit leading coefficient (at
\(Y=0\) the quotient \(\Omega/\overline\Omega=-1\) has order
\(2\ne k\)); exceptional evaluations
\(\mathcal A_k(0,1)=\Phi_k(1,1)\) and \(\mathcal A_k(-1,1)\ne0\) are
units for \(p\nmid2k\); converse, sign, and disjointness by the exact
order of the recovered \(\zeta\); Hensel by the simple root and first
Taylor term. \(\square\)

**Theorem (T1) — bounded iterated local mean, every degree.** Fix any
\(d\ge2\). Over \(d\)-admissible seed boxes, with the iterated limits
\(H\to\infty\), then \(K\to\infty\), then \(P\to\infty\) (exactly as
in the prime-degree theorem), the mean truncated defect of the first
\(n\) layers equals
\[
L_d(n)=\sum_{j<n}\ \sum_{k\in\Lambda_{d,j}}
\frac{\varphi(k)}2
\sum_{\substack{p\nmid2d\\ k\mid p\mp1}}
\frac{\log p}{p^2-1},
\]
and, uniformly in \(n\), \(L_d(n)\le C_d<\infty\) with the EXPLICIT
constant
\[
C_d=2\bigl[\zeta(2)\log3-\zeta'(2)\bigr]S_1(d)
+2\zeta(2)\,S_2(d),
\]
\[
S_1(d)=\prod_{q\mid2d}\frac{q+1}q-\frac54,
\qquad
S_2(d)=\Bigl(\prod_{q\mid2d}\frac{q+1}q\Bigr)
\sum_{q\mid2d}\frac{q\log q}{q^2-1}-\frac{\log2}4 .
\]
*Proof.* Per-atom densities from (L3) with the projective-primitive
conditioning \(p^{-h}\cdot p/(p+1)\) per root (unchanged from the
prime-degree proof); atoms at one prime are mutually exclusive by the
exact order, so expectations add with no independence input. The class
majorant for \(k\ge3\),
\(\sum_{k\mid p\mp1}\log p/(p^2-1)
\le(4/k^2)(\zeta(2)\log(3k)-\zeta'(2))\)
(eligible integers \(rk\pm1\); \((rk+1)^2-1\ge r^2k^2\) and
\((rk-1)^2-1\ge r^2k^2/3\); the majorant may include the excluded
integer \(2\), which only enlarges it), and the closed-form Euler sums
over the \((2d)\)-smooth index lattice,
\[
\sum_{k\mid(2d)^\infty}\frac{\varphi(k)}{k^2}
=\prod_{q\mid2d}\frac{q+1}q,
\qquad
\sum_{k\mid(2d)^\infty}\frac{\varphi(k)\log k}{k^2}
=\Bigl(\prod_{q\mid2d}\frac{q+1}q\Bigr)
\sum_{q\mid2d}\frac{q\log q}{q^2-1}
\]
(differentiate the finite Euler product; per-prime factors
\(F_q=(q+1)/q\), \(G_q=1/(q-1)\), \(G_q/F_q=q/(q^2-1)\)), with the
\(k\in\{1,2\}\) terms removed (\(-1-\tfrac14\) and
\(-\tfrac{\log2}4\)), give the displayed \(C_d\). \(\square\)

**Scope (T2).** This completes the composite-degree ITERATED
TRUNCATED/PROFINITE mean, upgrading the companion's future-work remark
to a theorem. It does not pass to the untruncated integer-box mean and
gives no pointwise result for any fixed orbit; the large-square tail
and the fixed-orbit deep Lucas–Wieferich tail are unchanged.

**Verification.** `composite_atom_check.py` 251/251 (integrality;
layer identity for \(d\in\{2,3,5,6,10,15\}\); evaluations, degrees,
leading coefficients; roots/signs/disjointness at composite indices
12–30; Hensel), plus the (2.1)/Euler cross-checks 30/30; codex's
independent suite 7/7 and derivation reconciled (0141).
