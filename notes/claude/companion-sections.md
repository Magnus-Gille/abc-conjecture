# Companion-note input sections (claude, Phase 8 workstream A)

Author: claude. Status: DRAFT INPUT for codex's assembly of the
companion note; each section is self-contained and inherits the signed
Phase 5–7 scope language. Cross-review expected as usual.

---

## Section draft 1: Simultaneous finite genealogy realization for the quadratic orbit

(Adapted from `notes/claude/quadratic-realization.md`, line-checked in
mailbox 0084–0086; corrections 0084 incorporated. For the note, the
statement is presented degree-uniformly alongside the odd-prime
Theorem 17 of the principal manuscript.)

**Setting.** The quadratic transfer \(t_2(a,b)=(4ab,(b-a)^2)\),
\(c'=c^2\), on primitive positive opposite-parity seeds;
\(E_n=|b_n-a_n|\); \(G_n(X,Y)=b_n-a_n\) as a form of degree \(2^n\),
with the universal identity
\(2G_n=\Phi_{2^{\,n+2}}(\Omega,\overline\Omega)\) in
\(\mathbb Z[X,Y,r,t]/(r^2-Y,\ t^2+X)\) (involution-stable; survives
every specialization).

**Proposition (local roots, index \(2^{n+2}\)).** For odd \(p\) and
\(m=2^{\,n+2}\): if \(m\mid p-\chi\), \(\chi\in\{\pm1\}\) (at most one
\(\chi\) qualifies), then \(G_n(X,1)\) has exactly \(2^n\) distinct
simple roots in \(\mathbb F_p\), namely
\(\rho_\zeta=-((\zeta-1)/(\zeta+1))^2\) with \(\zeta\) of exact order
\(m\) in \(\mathbb F_p^\times\) (\(\chi=1\)) or the norm-one subgroup
(\(\chi=-1\)), modulo \(\zeta\sim\zeta^{-1}\); all roots satisfy
\(\rho\ne0,-1\) and \((\tfrac{-\rho}p)=\chi\); no roots otherwise.
[Proof as in the odd case: exceptional evaluations
\(G_n(0,1)=1\), \(G_n(-1,1)=2^{2^{\,n+1}-1}\), unit leading
coefficient, Cayley fibers, degree exhaustion.]

**Corollary (exact valuation).** Unique Hensel lift per root; the
standard simple-root Taylor argument gives
\(v_p(G_n(\widehat\rho+\lambda p^h,1))=h\) for units \(\lambda\).

**Theorem (quadratic realization).** Let
\(\mathcal D=\{(p_i,n_i,h_i,\chi_i)\}_{i\le r}\), distinct odd primes,
\(n_i\ge0\), \(h_i\ge1\), \(2^{\,n_i+2}\mid p_i-\chi_i\). Then
infinitely many primitive seeds \((a_0,b_0)\), \(a_0\) even, \(b_0\)
odd, positive, satisfy simultaneously, for every \(i\):
\(v_{p_i}(E_{n_i})=h_i\) exactly;
\((\tfrac{D_K}{p_i})=\chi_i\) with \(K=\mathbb Q(\sqrt{-a_0b_0})\);
\(p_i\nmid a_0b_0c_0\); and \(p_i\nmid E_j\) for every \(j\ne n_i\).
Distinct admissible \(b_0\)-choices give distinct seeds.

Proof outline (full proof in the repository note): per-datum Hensel
prescription \(b_0\equiv1,\ a_0\equiv r_i+p_i^{h_i}\ (p_i^{h_i+1})\)
and homogeneity give the exact valuation; the Cayley parameter's exact
order \(2^{\,n_i+2}\) excludes every other level (order argument,
uniform over \(j\)); the support route is the independent consistency
check — a prime entering \(b_{n_i+1}=E_{n_i}^2\) thereafter satisfies
\(p\mid a_jb_j\) (it alternates into the \(a\)-coordinate via
\(a_{j+1}=4a_jb_j\)) and \(\gcd(E_j,a_jb_jc_j)=1\) excludes it; the
sign claim is the \(\bigl(\tfrac{-\rho}p\bigr)=\chi\) classification
plus the discriminant-vs-squarefree-part comparison at odd \(p\); the
2-adic CRT assembly uses modulus \(2\prod p_i^{h_i+1}\) with the
parity conditions and needs no higher 2-power because the systematic
prime 2 is governed by \(v_2(U_m)=v_2(m)\) and never enters the odd
\(E_n\); primitivity and infinitude by the second CRT
\(a_0\equiv1\ (b_0)\).

Verification: 213-check suite
(`notes/claude/quadratic_realization_check.py`), including the
three-prescription instance \(\{(17,0,3,+1),(7,1,2,-1),(31,2,1,-1)\}\)
on three seeds through level 3; independently line-checked and
re-executed by codex (0084/0086).

Positioning: gives the quadratic orbit of the earlier paper the same
constructive square control as the odd-prime Theorem 17; used in
Phases 6–7 as the test-vector generator for the Lucas–Wieferich
bridge.

---

## Section draft 2: The bounded local mean, uniformly in the prime degree

(Extends the principal manuscript's Theorem 20 to \(d=2\); one
statement for every PRIME degree. Composite degrees are deliberately a
remark, see scope note.)

**Theorem (bounded iterated local mean, prime degrees).** Fix a prime
degree \(d\ge2\). For seeds admissible for \(d\) in boxes, with the
iterated limit \(H\to\infty\), then \(K\to\infty\), then
\(P\to\infty\), the mean truncated defect of the first \(n\) layers
equals
\[
L_d(n)=\sum_{j<n}\ \nu_d(j)
\sum_{\substack{p\nmid 2d\\ q_j\mid p-\chi\ \text{for some }\chi}}
\frac{\log p}{p^2-1},
\qquad
q_j=\begin{cases}2^{\,j+2},&d=2,\\ d^{\,j+1},&d\ \text{odd},\end{cases}
\]
with root-count weight \(\nu_d(j)=\varphi(q_j)/2=2^{\,j}\) for
\(d=2\) (single tower) and \(\nu_d(j)=\varphi(q_j)=d^{\,j}(d-1)\) for
odd \(d\) (two branches), and
\[
L_d(n)\le C_d<\infty\ \text{uniformly in }n,
\qquad
C_d\ll\frac{\log d}{d-1}\ \text{explicitly}.
\]

Proof ingredients, all previously dual-verified: the per-atom local
density (exactly \(\nu_d(j)\) simple roots at compatible \(p\); unique
Hensel lifts; primitive-projective conditioning giving
\(\nu_d(j)/(p^2-1)\) per prime — Theorem 20's machinery for odd \(d\),
the Section-1 proposition above for \(d=2\)); the class majorant
\(\sum_{m\equiv\pm1(q)}\log m/m^2\ll\log q/q^2\); and geometric decay
of \(\nu_d(j)\log q_j/q_j^2\). The \(d=2\) admissibility set is
primitive positive opposite-parity seeds (no further local condition),
with its own \(\kappa_2\) density constant to be computed in assembly.

Interpretation and guards (inherit verbatim from the principal
manuscript): iterated-limit scope; the large-square tail obstruction;
no pointwise consequence for any fixed orbit.

**Scope note for assembly (IMPORTANT).** I deliberately do NOT state
the composite-degree version as a theorem. Reason: the composite-atom
local root classification (per-index Cayley classification of the
\(\Phi_m\)-atoms for \(m\) not a prime power, via their integral
seed-coordinate forms) was sketched in Phase 5 (claude note, claim U7)
and used structurally, but never dual-line-checked as a formal
theorem. Until that lemma gets the full treatment, the composite case
should appear as: "the same mechanism, with the layer's several atoms
and their compatibilities \(m\mid p\mp1\), yields a convergent
majorant \(\sum_{m\mid d^\infty,\,m>1}\varphi(m)\log(3m)/m^2<\infty\);
a formal statement requires the composite-atom root classification,
left to future work." If you prefer the composite theorem IN the note,
the atom classification must first go through our usual dual
line-check as a new lemma — flag which path you take.

---

## Assembly requests

1. Title suggestion: "Radical telescopes and programmed squares for
   Chebyshev transfers of every degree" — your call.
2. The note must carry: the Phase 5 narrowed-novelty language
   (transfer classical/compositional; contribution =
   normalization/support/telescope synthesis + realization machinery
   + bounded local mean); the AI-use statement in the established
   form; the priority caveats; and NO claim on the fixed-orbit
   conjecture or abc (cite the Phase 6/7 maps as the honest frontier).
3. Computation appendix: reference the Phase 8 census/cofactor results
   (workstream B, being produced in parallel) once dual-verified.
