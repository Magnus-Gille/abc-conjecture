# Simultaneous finite genealogy realization for the quadratic orbit

Author: claude (Phase 5; formalization requested in mailbox/0083 §Scope)
Date: 2026-07-31
Status: full statement and proof for codex adversarial line-check.
Destination: companion unification note (NOT the integrated prime-degree
manuscript), per 0083. Verified in
`notes/claude/quadratic_realization_check.py`.

Throughout, the quadratic transfer is
\(t_2(a,b)=(4ab,\ (b-a)^2)\), \(c'=c^2\), on primitive positive
opposite-parity seeds; \(E_n=|b_n-a_n|\) is the level-\(n\) factor and
\(G_n(X,Y)=b_n-a_n\) as a form of degree \(2^n\) in the seed, so that
\(G_0=Y-X\) and, with \(\Omega=r+t\), \(r^2=Y\), \(t^2=-X\),
\[
G_n=\tfrac12\Phi_{2^{\,n+2}}(\Omega,\overline\Omega)
=\tfrac12\bigl(\Omega^{2^{\,n+1}}+\overline\Omega^{\,2^{\,n+1}}\bigr).
\]
This is a universal polynomial identity in
\(\mathbb Z[X,Y,r,t]/(r^2-Y,\ t^2+X)\): writing
\(\Omega^{2^{\,n}}=r_n+t_n\) with the involution \(t\mapsto-t\) fixing
\(r_n\) and negating \(t_n\), squaring gives
\(r_{n+1}=r_n^2+t_n^2\) and \(t_{n+1}=2r_nt_n\), so induction through
the squaring transfer yields \(r_n^2=b_n(X,Y)\),
\(t_n^2=-a_n(X,Y)\), and hence
\(\Omega^{2^{\,n+1}}+\overline\Omega^{\,2^{\,n+1}}
=2r_{n+1}=2(b_n-a_n)=2G_n\); the identity therefore survives every
specialization, including the finite residue algebras used below.

## Proposition Q15 (local roots, index \(2^{n+2}\))

Fix \(n\ge0\) and an odd prime \(p\). Put \(m=2^{\,n+2}\). If
\(m\mid p-\chi\) for some \(\chi\in\{1,-1\}\) — at most one \(\chi\)
qualifies, since \(m\mid\gcd(p-1,p+1)\) would force \(m\mid2\) — then
\(G_n(X,1)\) has exactly \(2^n\) distinct simple roots in
\(\mathbb F_p\), namely
\[
\rho_\zeta=-\Bigl(\frac{\zeta-1}{\zeta+1}\Bigr)^{2},
\]
\(\zeta\) ranging modulo \(\zeta\sim\zeta^{-1}\) over the elements of
exact order \(m\) in \(\mathbb F_p^\times\) (\(\chi=1\)) or in the
norm-one subgroup of \(\mathbb F_{p^2}^\times\) (\(\chi=-1\)). Every
root satisfies \(\rho\ne0,-1\) and
\(\bigl(\frac{-\rho}p\bigr)=\chi\). If \(m\nmid p-1\) and
\(m\nmid p+1\), there are no roots.

Proof. Specialize the displayed atom identity at \(Y=1\), \(s^2=-X\),
\(\Omega=1+s\), \(\zeta=(1+s)/(1-s)\). Since \(p\) is odd and
\(1\pm s\ne0\) for \(\rho\ne\mp1\)-type exceptional values checked
below, \(G_n(\rho,1)=0\) iff \(\zeta^{2^{\,n+1}}=-1\) iff \(\zeta\)
has exact order \(2^{\,n+2}=m\). Existence of such \(\zeta\) is
cyclicity of \(\mathbb F_p^\times\) (order \(p-1\)) or of the norm-one
group (order \(p+1\)); in the inert case Frobenius gives
\(\zeta^p=\zeta^{-1}\), hence \(s^p=-s\) and \(\rho=-s^2\in\mathbb F_p\).
Exceptional points: \(G_n(0,1)=\frac12\Phi_m(1,1)=1\) and
\(G_n(-1,1)=\frac12\Phi_m(2,0)=2^{\,2^{\,n+1}-1}\ne0\) in
\(\mathbb F_p\); the leading coefficient is
\(G_n(1,0)=\frac12\Phi_m(t,-t)=(-X)^{2^n}\!\mid_{\deg}\)-normalized
\(=\pm1\), a unit, so no projective root escapes to infinity and
\(\deg_p G_n(X,1)=2^n\). The map \(\zeta\mapsto\rho\) has fibers
\(\{\zeta,\zeta^{-1}\}\) exactly (as \(s(\zeta^{-1})=-s(\zeta)\), and
\(\rho\) determines \(s\) up to sign, \(s\) determines \(\zeta\)),
giving \(\varphi(m)/2=2^n\) distinct roots of a degree-\(2^n\)
polynomial: exhaustion and simplicity. Signs: split case
\(-\rho=s^2\) with \(s\in\mathbb F_p^\times\) is a square (\(s\ne0\)
since \(\zeta\ne1\)); inert case \(s\notin\mathbb F_p\), so \(s^2\) is
a nonsquare. Converse: a root \(\rho\ne0,-1\) yields \(s\), \(\zeta\)
with \(\zeta^{2^{n+1}}=-1\), so \(\zeta\) has exact order \(m\) and
lies in \(\mathbb F_p^\times\) or the norm-one group according to the
square class of \(-\rho\), forcing \(m\mid p-1\) or \(m\mid p+1\). ∎

Remark (level 0). \(m=4\), \(G_0(X,1)=1-X\), single root \(\rho=1\);
the criterion \(4\mid p-\chi\) is exactly \(\chi=(\tfrac{-1}p)\),
consistent with \(-\rho=-1\).

## Corollary Q16 (exact valuation)

Each root \(\rho\) has a unique Hensel lift
\(\widehat\rho\in\mathbb Z_p\) in its residue class with
\(G_n(\widehat\rho,1)=0\), and for \(h\ge1\),
\(\lambda\in\mathbb Z_p^\times\):
\(v_p(G_n(\widehat\rho+\lambda p^h,1))=h\). Proof: simple root, unit
derivative, Taylor congruence modulo \(p^{2h}\), \(2h\ge h+1\). ∎

## Theorem Q17 (simultaneous quadratic genealogy realization)

Let \(\mathcal D=\{(p_i,n_i,h_i,\chi_i):1\le i\le r\}\) with distinct
odd primes \(p_i\), \(n_i\ge0\), \(h_i\ge1\), \(\chi_i\in\{1,-1\}\),
and \(2^{\,n_i+2}\mid p_i-\chi_i\). Then there are infinitely many
primitive seeds \((a_0,b_0)\), \(a_0\) even, \(b_0\) odd, both
positive, such that for every \(i\):
\[
v_{p_i}(E_{n_i})=h_i,\qquad
\Bigl(\frac{D_K}{p_i}\Bigr)=\chi_i,\qquad
p_i\nmid a_0b_0c_0,\qquad
p_i\nmid E_j\ (j\ne n_i,\ j\ge0),
\]
with \(K=\mathbb Q(\sqrt{-a_0b_0})\). Distinct choices below give
distinct seeds.

Proof.
(1) Local step. For each \(i\), choose a root \(\rho_i\) of
\(G_{n_i}(X,1)\) mod \(p_i\) with sign \(\chi_i\) (Prop. Q15), let
\(\widehat\rho_i\) be its lift (Cor. Q16), and let \(r_i\) represent
\(\widehat\rho_i\) modulo \(p_i^{h_i+1}\). Impose
\[
b_0\equiv1\ (p_i^{h_i+1}),\qquad
a_0\equiv r_i+p_i^{h_i}\ (p_i^{h_i+1}).
\]
Homogeneity of degree \(2^{n_i}\) gives
\(G_{n_i}(a_0,b_0)=b_0^{2^{n_i}}G_{n_i}(a_0/b_0,1)\) with \(b_0\) a
\(p_i\)-adic unit, and \(a_0/b_0\equiv\widehat\rho_i+p_i^{h_i}\cdot
(\text{unit})\ (p_i^{h_i+1})\), so \(v_{p_i}(E_{n_i})
=v_{p_i}(G_{n_i}(a_0,b_0))=h_i\) exactly.

(2) Exclusion at every other level, uniformly. Modulo \(p_i\), the
seed reduces to \((\rho_i:1)\) and its Cayley parameter \(\zeta_i\) has
exact order \(2^{\,n_i+2}\). For any \(j\ne n_i\), a zero of
\(G_j(\rho_i,1)\) would force exact order \(2^{\,j+2}\ne2^{\,n_i+2}\)
(Prop. Q15 converse) — impossible. Hence
\(p_i\nmid G_j(a_0,b_0)=\pm E_j\) for every \(j\ne n_i\). (For
\(j>n_i\) this is consistent with, and independently implied by, the
support route: \(p_i\mid E_{n_i}\Rightarrow p_i\mid
b_{n_i+1}=E_{n_i}^2\), and since \(a_{j+1}=4a_jb_j\) at every step, the
prime then satisfies \(p_i\mid a_jb_j\) for all \(j>n_i\) — it
alternates into the \(a\)-coordinate rather than remaining in
\(b_j\), as codex corrected in 0084 — whence
\(\gcd(E_j,a_jb_jc_j)=1\) excludes it.)

(3) Seed-prime avoidance and sign. \(a_0\equiv\rho_i\ne0\),
\(b_0\equiv1\), \(c_0\equiv\rho_i+1\ne0\ (p_i)\) since
\(\rho_i\ne0,-1\); so \(p_i\nmid a_0b_0c_0\). Also
\((\tfrac{-a_0b_0}{p_i})=(\tfrac{-\rho_i}{p_i})=\chi_i\), and \(D_K\)
differs from the squarefree part of \(-a_0b_0\) by a square and
possibly a factor \(4\), both invisible to the Legendre symbol at the
odd prime \(p_i\nmid2a_0b_0\); hence
\((\tfrac{D_K}{p_i})=\chi_i\).

(4) Global 2-adic assembly. The moduli
\(p_1^{h_1+1},\dots,p_r^{h_r+1},2\) are pairwise coprime. Impose
additionally \(a_0\equiv0\ (2)\), \(b_0\equiv1\ (2)\); no further
\(2\)-power condition is required — the systematic prime \(2\) of the
quadratic orbit is governed by \(v_2(U_m)=v_2(m)\) for the fixed Lucas
pair and never enters \(E_n\), which is odd because opposite parity is
preserved by \(t_2\). CRT gives classes
\(\bar a,\bar b\ (\mathrm{mod}\ M)\), \(M=2\prod_ip_i^{h_i+1}\), and
\(\bar b\) is a unit modulo every factor of \(M\), hence modulo
\(M\).

(5) Primitivity, positivity, infinitude, distinctness. Choose any
positive \(b_0\equiv\bar b\ (M)\); then \(\gcd(b_0,M)=1\), so a second
CRT solves \(a_0\equiv\bar a\ (M)\) and \(a_0\equiv1\ (b_0)\)
simultaneously, and any positive representative works. Then
\(\gcd(a_0,b_0)=1\), \(a_0\) even, \(b_0\) odd, both positive:
admissible. Infinitely many \(b_0\) give infinitely many seeds, and
distinct \(b_0\) give distinct seeds. ∎

## Notes for the line-check (mapping to 0083's four items)

1. Root criterion/index \(2^{\,n+2}\): Prop. Q15, both directions,
   with the exceptional evaluations and leading-coefficient unit;
   level-0 degeneration stated.
2. Hensel exact-valuation separation for several prescriptions:
   Cor. Q16 + step (1); the check script realizes the three-prime
   prescription \(\{(17,0,3,+1),(7,1,2,-1),(31,2,1,-1)\}\) — three
   levels, mixed signs, one depth-3 valuation — on three distinct
   seeds, verifying exactness and cross-level avoidance through level
   3.
3. 2-adic CRT modulus and parity: step (4); modulus exactly
   \(2\prod p_i^{h_i+1}\); no higher 2-power needed, with the reason
   recorded.
4. Primitivity, positivity, seed-prime avoidance, distinctness:
   steps (3) and (5).

Differences from the odd-prime Theorem 17 worth a reviewer's eye:
single tower (no branch datum \(\varepsilon\)); compatibility
\(2^{\,n+2}\mid p-\chi\) determines \(\chi\) uniquely (no even/odd
index subtlety); no \(\ell\)-adic seed condition (no analogue of
\(v_3(3b_0-a_0)=1\)); the "later levels" exclusion follows from the
order argument alone, with the support route as an independent
consistency check.
