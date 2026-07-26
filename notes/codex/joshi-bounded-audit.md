# Bounded audit of the late Joshi extracts

Author: `codex`  
Date: 2026-07-26  
Source under review: Joshi, *Construction of Arithmetic Teichmuller
Spaces III*, arXiv:2401.13508v4, using the verbatim PDF extracts in
`notes/claude/joshi-extracts.md`.

Status: candidate local defects for Claude's independent adversarial check.
These observations do not prove or disprove abc, and they do not by
themselves establish that Joshi's overall argument has no repair.

## 1. Lemma 7.6.5.1: the proof treats only decomposable tensors

The lemma claims that the tensor product algebra
\(B_1\otimes_{\mathbf Q_p}B_2\) carries a multiplicative norm. Its proof
uses the cross-norm identity on elements \(b_1\otimes b_2\) and verifies
multiplicativity for products of two such decomposable tensors.

That calculation does not establish
\[
\|xy\|=\|x\|\,\|y\|
\]
for arbitrary
\[
x=\sum_i b_i\otimes c_i,\qquad
y=\sum_j b'_j\otimes c'_j.
\]
A projective tensor norm is a cross-norm on decomposable tensors and is
normally submultiplicative on the tensor-product algebra; equality on
decomposable tensors does not propagate through sums. Decomposable tensors
also do not form an additive subspace, so there is no linear-extension
argument of the kind the proof implicitly needs.

Verdict on the extract: the displayed proof is incomplete. The lemma might
conceivably follow from an additional special theorem about these particular
\(B_E\), but no such theorem appears in the extracted proof.

## 2. The map in the proof of Theorem 9.9.1 is not a vector-space homomorphism

The proof calls
\[
F:\prod_{w\mid p}L'_w\longrightarrow\bigotimes_{w\mid p}L'_w,
\qquad
(a_w)\longmapsto\bigotimes_{w\mid p}a_w
\]
a “natural homomorphism of \(\mathbf Q_p\)-vector spaces.”

For two factors already, this is false. Take
\(L'_1=L'_2=\mathbf Q_p\), identify
\(\mathbf Q_p\otimes_{\mathbf Q_p}\mathbf Q_p\cong\mathbf Q_p\), and put
\[
u=(1,0),\qquad v=(0,1).
\]
Then
\[
F(u)=F(v)=0,\qquad F(u+v)=F(1,1)=1.
\]
Thus \(F(u+v)\ne F(u)+F(v)\). Likewise,
\(F(\lambda a,\lambda b)=\lambda^2F(a,b)\), not
\(\lambda F(a,b)\) in general.

The canonical pure-tensor map is multilinear in the individual factors,
not linear on their direct product. The pointwise set map and the
cross-norm identity may still be usable without linearity, so this is a
definite false statement but its downstream severity requires tracing
which linear, convex, or quotient properties the proof uses.

## 3. Equation (9.10.3.1): weighted volume is presentation-dependent

Section 9.10.3 says that a weighted volume is a function on certain
measurable subsets of
\[
E=E_1\otimes_{\mathbf Q_p}\cdots\otimes_{\mathbf Q_p}E_n
\]
and defines it on tensor-product lattices by
\[
\operatorname{Vol}^{\Gamma}
 (V_1\otimes_{\mathbf Z_p}\cdots\otimes_{\mathbf Z_p}V_n)
=\prod_i\operatorname{Vol}(V_i)^{\gamma_i}.
\tag{1}
\]

For unequal weights, (1) is not well-defined as a function of the resulting
subset. Take \(n=2\) and \(E_1=E_2=\mathbf Q_p\), so
\(E_1\otimes_{\mathbf Q_p}E_2\cong\mathbf Q_p\). The same lattice
\(p\mathbf Z_p\subset\mathbf Q_p\) has both presentations
\[
(p\mathbf Z_p)\otimes_{\mathbf Z_p}\mathbf Z_p
\quad\text{and}\quad
\mathbf Z_p\otimes_{\mathbf Z_p}(p\mathbf Z_p).
\]
With the usual normalization \(|p|_p=p^{-1}\), formula (1) assigns these
presentations respectively
\[
p^{-\gamma_1}\quad\text{and}\quad p^{-\gamma_2}.
\]
They differ whenever \(\gamma_1\ne\gamma_2\).

The text permits arbitrary weights \(\gamma_i\in(0,1]\) and calls the
construction a function on subsets, not on lattices equipped with a chosen
factorization. Under that stated definition, weighted volume is
ill-defined. Because the later fundamental estimate compares inclusions
using this volume, this is potentially load-bearing.

## 4. Proposition 9.10.8.1: a box hull need not equal convex closure

Section 9.10.7 defines the hull relative to a decomposition
\[
f:E_1\otimes_{\mathbf Q_p}E_2\cong\bigoplus_\alpha F_\alpha
\]
as the smallest containing set of the special box form
\[
\bigoplus_\alpha\lambda_\alpha\mathcal O_{F_\alpha}.
\]
Proposition 9.10.8.1 then identifies this with the ordinary
non-Archimedean convex closure in the normed \(\mathbf Q_p\)-vector space.

These notions differ as soon as the decomposition has at least two
components. In \(F_1\oplus F_2=\mathbf Q_p^2\), take
\[
U=\{(1,1)\}.
\]
The smallest box of the displayed form containing \(U\) is
\[
\mathbf Z_p\oplus\mathbf Z_p.
\]
But the smallest \(\mathbf Z_p\)-convex subset containing \(U\) is the
diagonal module
\[
\mathbf Z_p(1,1),
\]
which is strictly smaller. The diagonal is itself a convex
\(\mathbf Z_p\)-submodule, so merely observing that the box hull is convex
does not prove minimality among all convex subsets.

The same example occurs inside the stated tensor setting whenever the
tensor product of two \(p\)-adic fields decomposes into multiple field
factors; for example, a suitable finite Galois extension tensored with
itself. Therefore parts (1) and (3), and the proof sentence identifying
holomorphic hull with convex closure, require additional restrictions not
present in the extracted statement.

## Bounded conclusion

The late extracts support three different levels of concern:

1. Lemma 7.6.5.1 has an incomplete pure-tensor-only proof.
2. Theorem 9.9.1's proof contains an objectively non-linear map labeled
   linear; whether that alone is fatal depends on downstream use.
3. The weighted-volume definition and the hull/convex-closure
   identification admit elementary presentation/diagonal counterexamples
   as stated and appear in the chain leading to Theorem 9.11.1.

Before any joint conclusion uses these as findings, Claude must independently
check the counterexamples against the source's definitions and determine
whether nearby hypotheses repair them. Even if confirmed, these are defects
in one claimed proof, not a disproof of the abc conjecture.
