# Prime genealogy in Chebyshev \(abc\)-orbits: interleaved Lucas atoms and exact radical telescopes

**Magnus Gille**

Independent researcher

Research draft, July 2026

> Import note (2026-07-28): this file preserves the complete Markdown
> manuscript supplied by Magnus in the Codex conversation. It is the source
> record for the prime-genealogy audit and is not yet an approved manuscript.

## Abstract

Let \(\ell\) be an odd prime. Splitting the real and imaginary parts of
\((\sqrt b+i\sqrt a)^\ell\) gives homogeneous integer polynomials
\(S_\ell,C_\ell\) satisfying

\[
aS_\ell(a,b)^2+bC_\ell(a,b)^2=(a+b)^\ell.
\]

We iterate the resulting degree-\(\ell\) transfer on primitive positive
triples \(a+b=c\). Under a natural \(\ell\)-adic normalization, every
non-seed prime has a unique birth time and a unique branch: the factors

\[
A_n=\frac{|S_\ell(a_n,b_n)|}{\ell},
\qquad
B_n=|C_\ell(a_n,b_n)|
\]

form one pairwise-coprime collection. They are two interleaved towers of
homogeneous Lucas atoms, of indices \(\ell^{n+1}\) and \(2\ell^{n+1}\),
respectively. Writing

\[
E_n=A_nB_n,
\qquad
W_n=\prod_{j<n}\frac{E_j}{\operatorname{rad}(E_j)},
\]

we obtain

\[
\frac{\operatorname{rad}(a_nb_nc_n)}{c_n}
=
\frac{\operatorname{rad}(a_0b_0c_0)}{c_0}
\frac{|\sin(\ell^n\theta)|}
{\ell^n\sin\theta\,W_n},
\qquad
\cos\theta=\frac{b_0-a_0}{c_0}.
\]

Thus every admissible orbit eventually consists of \(abc\)-hits, the
radical ratio decreases strictly at every step, and a persistent quality
gap is equivalent to positive-power accumulation in \(W_n\). The factors
\(\ell E_n\) are consecutive prime-power cyclotomic factors of a quadratic
Lucas sequence. Every prime \(p\mid E_n\) has exact order
\(\ell^{n+1}\) in the associated norm-one residue group and consequently
satisfies

\[
\ell^{n+1}\mid p-\left(\frac{D_K}{p}\right).
\]

Standard Lucas-atom valuation theory then identifies square divisors of
\(E_n\) with cyclotomic Wieferich lifts; the orbit identity couples their
aggregate multiplicity directly to \(abc\)-quality. Conversely, the order
congruence is locally sufficient: any finite compatible pattern of prime
birth levels, branches, split/inert signs, and exact positive
multiplicities can be realized by infinitely many primitive seeds. In
particular, the seeds \((\ell,2,\ell+2)\) give an explicit orbit for every
odd prime \(\ell\), and every member from index \(2\) onward is an
\(abc\)-hit.

**Status.** This is a research-development draft, not a peer-reviewed
manuscript. The polynomial transfer itself is a classical consequence of de
Moivre's formula. The proposed contribution is the orbit-wide package:
branchwise prime genealogy in two nested Lucas-atom towers, exact radical
identity, monotonicity, the coupling of cyclotomic valuations to
\(abc\)-quality, and an exact local-global realization theorem for finite
prime genealogies. A bounded literature search found no source containing
this package of statements; that search is not exhaustive.

*2020 Mathematics Subject Classification.* Primary 11B39; Secondary 11A05,
11D75, 11J86, 37P05.

*Keywords.* \(abc\) conjecture, Chebyshev polynomial, Lucas sequence,
homogeneous cyclotomic polynomial, radical, Wieferich prime, arithmetic
dynamics.

## Introduction

For a positive integer \(m\), write

\[
\operatorname{rad}(m)=\prod_{p\mid m}p.
\]

A primitive positive triple \((a,b,c)\) with \(a+b=c\) is an \(abc\)-hit
if \(\operatorname{rad}(abc)<c\), and its quality is

\[
q(a,b,c)=\frac{\log c}{\log\operatorname{rad}(abc)}.
\]

Polynomial transfers are a standard way to turn one additive triple into
another. Martin and Miao survey several such identities and a general
binomial-splitting construction; van der Horst gives a detailed treatment
of the transfer method and sharp polynomial triples. Homogeneous
cyclotomic factors of Lucas sequences ("Lucas atoms") and their
\(p\)-adic valuations are also established theory. Ross, Shen, and Cai
develop closely related cyclotomic congruences for Lucas sequences. Kym
recently obtained valuation separation for products of Lucas terms at
pairwise coprime indices.

The purpose here is different: instead of optimizing a single transfer, we
identify a prime-degree dynamical orbit whose two coordinate branches are
nested-index Lucas-atom towers but whose normalized integer values
nevertheless have exactly disjoint support.

Let \(\ell\) be an odd prime and put \(m=(\ell-1)/2\). Define

\[
\begin{aligned}
S_\ell(a,b)
&=
\sum_{r=0}^{m}
(-1)^r
\binom{\ell}{2r+1}
a^r b^{m-r},\\
C_\ell(a,b)
&=
\sum_{r=0}^{m}
(-1)^r
\binom{\ell}{2r}
a^r b^{m-r}.
\end{aligned}
\]

Then

\[
(\sqrt b+i\sqrt a)^\ell
=
\sqrt b\,C_\ell(a,b)
+i\sqrt a\,S_\ell(a,b),
\]

and taking norms gives

\[
aS_\ell(a,b)^2+bC_\ell(a,b)^2=(a+b)^\ell.
\]

The first cases are

\[
\begin{aligned}
S_3&=3b-a,
&
C_3&=b-3a,\\
S_5&=5b^2-10ab+a^2,
&
C_5&=b^2-10ab+5a^2.
\end{aligned}
\]

Thus the transfer identity includes, for example,

\[
a(3b-a)^2+b(b-3a)^2=(a+b)^3.
\]

The identity is elementary. The arithmetic rigidity appears only after
iteration and the normalization at the transfer prime \(\ell\).

## The prime-degree transfer

Let

\[
a_0+b_0=c_0,
\qquad
\gcd(a_0,b_0)=1,
\]

where \(a_0,b_0>0\) have opposite parity. Assume

\[
\ell\mid a_0,
\qquad
\ell\nmid b_0,
\qquad
v_\ell(S_\ell(a_0,b_0))=1.
\]

The final valuation condition is automatic when \(\ell\geq5\). For
\(\ell=3\), it is the explicit condition

\[
v_3(3b_0-a_0)=1.
\]

Define recursively

\[
\begin{aligned}
a_{n+1}&=a_nS_n^2,\\
b_{n+1}&=b_nC_n^2,\\
c_{n+1}&=c_n^\ell,
\end{aligned}
\qquad
S_n=S_\ell(a_n,b_n),
\quad
C_n=C_\ell(a_n,b_n).
\]

The transfer identity gives \(a_n+b_n=c_n\) for every \(n\), and

\[
c_n=c_0^{\ell^n}.
\]

### Lemma 1: Parity and \(\ell\)-adic normalization

For every \(n\geq0\), the integers \(a_n,b_n\) have opposite parity, and

\[
\ell\mid a_n,
\qquad
\ell\nmid b_nc_n,
\qquad
v_\ell(S_n)=1,
\qquad
\ell\nmid C_n.
\]

In particular, the integers

\[
A_n:=\frac{|S_n|}{\ell},
\qquad
B_n:=|C_n|,
\qquad
E_n:=A_nB_n=\frac{|S_nC_n|}{\ell}
\]

are positive and odd, and are coprime to \(\ell\).

#### Proof

If \(a,b\) have opposite parity, inspection of the definitions of
\(S_\ell\) and \(C_\ell\) shows that both \(S_\ell(a,b)\) and
\(C_\ell(a,b)\) are odd. Hence opposite parity is preserved by the orbit.

Suppose \(\ell\mid a\) and \(\ell\nmid b\). Modulo \(\ell\),

\[
C_\ell(a,b)\equiv b^m\not\equiv0.
\]

For \(\ell\geq5\), divide \(S_\ell(a,b)\) by \(\ell\). All interior
binomial coefficients are divisible by \(\ell\), and the terminal term
\((-1)^ma^m/\ell\) is divisible by \(\ell\) because \(m\geq2\). Thus

\[
\frac{S_\ell(a,b)}{\ell}\equiv b^m\pmod\ell,
\]

so \(v_\ell(S_\ell(a,b))=1\).

When \(\ell=3\), the asserted valuation is assumed at \(n=0\). It makes
\(v_3(a_1)\geq3\), after which

\[
\frac{3b-a}{3}\equiv b\pmod3,
\]

so the valuation remains one. The recurrence now proves all assertions by
induction. \(\square\)

### Lemma 2: Primitivity and local support exclusion

Every triple \((a_n,b_n,c_n)\) is primitive. Moreover,

\[
\gcd(E_n,a_nb_nc_n)=1
\qquad(n\geq0).
\]

#### Proof

Fix one stage and write \(a,b,c,S,C,E\) for the corresponding objects.
Let \(q\) be a prime.

If \(q\mid a\), then

\[
C\equiv b^m\pmod q,
\qquad
S\equiv \ell b^m\pmod q.
\]

These are nonzero unless \(q=\ell\); for \(q=\ell\), Lemma 1 shows that
the single factor \(\ell\) in \(S\) has been removed from \(E\).

If \(q\mid b\), then

\[
S\equiv(-1)^ma^m\pmod q,
\qquad
C\equiv(-1)^m\ell a^m\pmod q,
\]

and \(q\neq\ell\) by Lemma 1.

If \(q\mid c=a+b\), then \(b\equiv-a\pmod q\). Since \(c\) is odd,
\(q\) is odd, and direct summation of the even and odd binomial
coefficients gives

\[
S_\ell(a,-a)
=
C_\ell(a,-a)
=
(-1)^m2^{\ell-1}a^m.
\]

This is nonzero modulo \(q\). These congruences prove the local support
exclusion.

It remains to rule out a prime common to the two new summands \(aS^2\) and
\(bC^2\). A common prime cannot arise from an old factor by the
congruences above. If it divided both \(S\) and \(C\), then the transfer
identity would force it to divide \(c\), contradicting the boundary
evaluation; the prime \(2\) is excluded because \(S,C\) are odd.

Hence the transferred triple is primitive, and induction completes the
proof. \(\square\)

### Theorem 3: Branchwise prime genealogy

The full collection

\[
A_0,B_0,A_1,B_1,A_2,B_2,\ldots
\]

is pairwise coprime, and every member is coprime to \(a_0b_0c_0\). More
precisely,

\[
\begin{aligned}
a_n
&=
a_0\ell^{2n}
\prod_{j=0}^{n-1}A_j^2,\\
b_n
&=
b_0
\prod_{j=0}^{n-1}B_j^2,\\
c_n
&=
c_0^{\ell^n}.
\end{aligned}
\]

If

\[
R_n=\operatorname{rad}(a_nb_nc_n),
\]

then

\[
\boxed{
R_n
=
R_0
\prod_{j=0}^{n-1}
\operatorname{rad}(A_jB_j).
}
\]

Thus every non-seed prime has a unique birth generation and a unique
coordinate branch. Its valuation in that coordinate is fixed forever
after birth.

#### Proof

Every prime of \(A_j\) divides \(a_{j+1}\), and every prime of \(B_j\)
divides \(b_{j+1}\); hence either prime divides \(a_nb_n\) for every
\(n>j\). Lemma 2 then excludes it from both \(A_n\) and \(B_n\).

At a fixed generation, a prime common to \(A_n\) and \(B_n\) would divide
both \(S_n\) and \(C_n\), which was excluded in the proof of Lemma 2. The
same local equation at \(n=0\) gives coprimality with the seed. This proves
the pairwise claim.

Since

\[
S_j=\pm\ell A_j,
\qquad
C_j=\pm B_j,
\]

iterating the orbit gives the displayed coordinate factorizations. The
factors are support-disjoint, so taking radicals gives the radical
factorization. Because later multipliers are coprime to every earlier
factor, the valuation of a born prime never changes. \(\square\)

## Chebyshev dynamics and the radical telescope

Set

\[
x_n=\frac{b_n-a_n}{c_n},
\qquad
x_0=\cos\theta,
\qquad
0<\theta<\pi.
\]

The angle exists because \(-1<x_0<1\), and

\[
\sin\theta
=
\frac{2\sqrt{a_0b_0}}{c_0}.
\]

### Lemma 4: Chebyshev semiconjugacy

Let \(T_r,U_r\) be the Chebyshev polynomials of the first and second kind.
Then

\[
\begin{aligned}
x_{n+1}
&=
T_\ell(x_n),\\
x_n
&=
T_{\ell^n}(x_0)
=
\cos(\ell^n\theta),
\end{aligned}
\]

and

\[
\frac{S_nC_n}{c_n^{\ell-1}}
=
U_{\ell-1}(x_n)
=
\frac{\sin(\ell^{n+1}\theta)}
{\sin(\ell^n\theta)}.
\]

None of the sine values in the final expression vanishes.

#### Proof

Choose \(\phi_n\) with

\[
\sin^2\phi_n=\frac{a_n}{c_n},
\qquad
\cos^2\phi_n=\frac{b_n}{c_n},
\]

so that

\[
x_n=\cos(2\phi_n).
\]

The real and imaginary parts in the definition of \(S_\ell,C_\ell\) give

\[
\frac{S_n}{c_n^m}
=
\frac{\sin(\ell\phi_n)}{\sin\phi_n},
\qquad
\frac{C_n}{c_n^m}
=
\frac{\cos(\ell\phi_n)}{\cos\phi_n}.
\]

Therefore the normalized new coordinates are

\[
\frac{a_{n+1}}{c_{n+1}}
=
\sin^2(\ell\phi_n),
\qquad
\frac{b_{n+1}}{c_{n+1}}
=
\cos^2(\ell\phi_n),
\]

proving the Chebyshev dynamics. Multiplying the displayed formulas and
using the double-angle identity gives the \(U_{\ell-1}\) formula.

If a sine vanished, then \(z=e^{i\theta}\) would be a root of unity. But

\[
z+z^{-1}
=
2\frac{b_0-a_0}{c_0}
\]

would then be a rational algebraic integer. Since

\[
\gcd(c_0,b_0-a_0)=1,
\]

while \(c_0>1\) is odd, this is impossible. \(\square\)

Define

\[
W_n
=
\prod_{j=0}^{n-1}
\frac{E_j}{\operatorname{rad}(E_j)}.
\]

### Theorem 5: Exact prime-degree radical identity

For every \(n\geq0\),

\[
\boxed{
\frac{R_n}{c_n}
=
\frac{R_0}{c_0}
\frac{|\sin(\ell^n\theta)|}
{\ell^n\sin\theta\,W_n}.
}
\]

Consequently,

\[
\frac{c_n}{R_n}
\geq
\frac{2\sqrt{a_0b_0}}{R_0}\,\ell^n
=
\frac{2\sqrt{a_0b_0}}
{R_0\log c_0}
\log c_n.
\]

Every admissible orbit eventually consists of \(abc\)-hits.

#### Proof

Since

\[
\prod_{j<n}c_j^{\ell-1}
=
c_0^{\ell^n-1}
=
\frac{c_n}{c_0},
\]

Theorem 3 and the definitions of \(E_n,W_n\) give

\[
\frac{R_n}{c_n}
=
\frac{R_0}{c_0}
\frac{1}{\ell^nW_n}
\prod_{j<n}
\frac{|S_jC_j|}{c_j^{\ell-1}}.
\]

Lemma 4 telescopes the product to

\[
\frac{|\sin(\ell^n\theta)|}{\sin\theta},
\]

proving the identity. Now use

\[
W_n\geq1,
\qquad
|\sin(\ell^n\theta)|\leq1,
\qquad
\sin\theta=\frac{2\sqrt{a_0b_0}}{c_0}
\]

to obtain the lower bound. \(\square\)

### Proposition 6: Strict radical monotonicity

The normalized radical decreases at every transfer:

\[
\frac{R_{n+1}}{c_{n+1}}
<
\frac{R_n}{c_n}
\qquad(n\geq0).
\]

In particular, once an orbit member is an \(abc\)-hit, every later member
is a hit.

#### Proof

Theorem 3 and the growth of \(c_n\) give

\[
\frac{R_{n+1}/c_{n+1}}
{R_n/c_n}
=
\frac{\operatorname{rad}(E_n)}
{c_n^{\ell-1}}
\leq
\frac{|U_{\ell-1}(x_n)|}{\ell}.
\]

For \(-1<x<1\), writing \(x=\cos t\) gives

\[
|U_{\ell-1}(x)|
=
\frac{|\sin(\ell t)|}{\sin t}
<
\ell.
\]

The inequality is strict away from \(t=0,\pi\), which do not occur here.
\(\square\)

## Effective quality control

The exact identity isolates the only archimedean oscillation. It is much
smaller than \(\log c_n\).

### Theorem 7: Archimedean term

There is an effective constant

\[
A=A(a_0,b_0,\ell)>0
\]

such that

\[
|\sin(\ell^n\theta)|
>
\exp(-An)
\qquad(n\geq1).
\]

Consequently,

\[
\log\frac{c_n}{R_n}
=
\log W_n
+
\Theta_{a_0,b_0,\ell}(n).
\]

#### Proof

Let

\[
z=e^{i\theta}
=
\frac{b_0-a_0+2\sqrt{-a_0b_0}}{c_0}.
\]

Lemma 4 shows that \(z\) is not a root of unity. Put

\[
N=\ell^n,
\]

choose an integer \(k\) nearest to \(N\theta/\pi\), and use principal
logarithms to form

\[
\Lambda_N
=
N\log z-k\log(-1)
=
i(N\theta-k\pi)
\neq0.
\]

The explicit theorem on linear forms in logarithms of Baker and Wüstholz,
applied to \(z\) and \(-1\), gives

\[
\log|\Lambda_N|
>
-C\log N
\]

for an effective seed-dependent constant \(C\).

Since

\[
|N\theta-k\pi|
\leq
\frac{\pi}{2},
\]

the elementary inequality

\[
|\sin y|
\geq
\frac{2|y|}{\pi}
\]

on that interval gives

\[
|\sin(N\theta)|
\gg
N^{-C}
=
\exp(-Cn\log\ell).
\]

Taking logarithms in the exact radical identity now gives

\[
\log\frac{c_n}{R_n}
=
\log W_n
+n\log\ell
+\log\frac{c_0\sin\theta}{R_0}
-\log|\sin(\ell^n\theta)|.
\]

The lower estimate follows from \(|\sin|\leq1\), and the upper estimate
follows from the Baker-Wüstholz bound. \(\square\)

### Corollary 8: Exact quality criterion

Put

\[
q_n=\frac{\log c_n}{\log R_n}.
\]

Then

\[
q_n\longrightarrow1
\quad\Longleftrightarrow\quad
\log W_n=o(\log c_n),
\]

and

\[
\limsup_{n\to\infty}(q_n-1)>0
\quad\Longleftrightarrow\quad
\limsup_{n\to\infty}
\frac{\log W_n}{\log c_n}>0.
\]

For every fixed \(\delta>0\), if

\[
F_n
=
\log(c_n/R_n)-\log W_n,
\]

then

\[
q_n\geq1+\delta
\quad\Longleftrightarrow\quad
\log W_n+F_n
\geq
\frac{\delta}{1+\delta}\log c_n.
\]

#### Proof

By Theorem 5, one has \(R_n<c_n\) for all sufficiently large \(n\). Write

\[
\Delta_n
=
\log(c_n/R_n).
\]

Since

\[
\log c_n
=
\ell^n\log c_0,
\]

Theorem 7 gives

\[
\Delta_n
=
\log W_n
+
o(\log c_n).
\]

Now

\[
q_n-1
=
\frac{\Delta_n}{\log R_n}.
\]

This proves the two asymptotic equivalences, and direct rearrangement gives
the exact threshold. \(\square\)

## Cyclotomic Lucas factors and level primes

The support separation has a more refined interpretation than the product
\(E_n=A_nB_n\). Put

\[
\omega
=
\sqrt{b_0}+\sqrt{-a_0},
\qquad
\bar\omega
=
\sqrt{b_0}-\sqrt{-a_0}.
\]

### Proposition 9: Two interleaved Lucas-atom towers

For every \(n\geq0\),

\[
S_n
=
\Phi_{\ell^{n+1}}(\omega,\bar\omega),
\qquad
C_n
=
\Phi_{2\ell^{n+1}}(\omega,\bar\omega).
\]

Consequently, up to the systematic factor \(\ell\) in the first tower, the
\(a\)-branch and \(b\)-branch of the orbit are the nested-index Lucas atoms
\(\ell^{n+1}\) and \(2\ell^{n+1}\), respectively.

#### Proof

Let

\[
z_n
=
\omega^{\ell^n}
=
r_n+s_n\sqrt{-1},
\]

under the fixed complex embedding. De Moivre's formula and induction in the
orbit give

\[
r_n^2=b_n,
\qquad
s_n^2=a_n.
\]

Therefore

\[
S_n
=
\frac{z_n^\ell-\bar z_n^\ell}
{z_n-\bar z_n},
\qquad
C_n
=
\frac{z_n^\ell+\bar z_n^\ell}
{z_n+\bar z_n}.
\]

Substituting \(z_n=\omega^{\ell^n}\) and using the prime-power
factorizations

\[
\frac{
X^{\ell^{n+1}}-Y^{\ell^{n+1}}
}{
X^{\ell^n}-Y^{\ell^n}
}
=
\Phi_{\ell^{n+1}}(X,Y),
\]

and

\[
\frac{
X^{\ell^{n+1}}+Y^{\ell^{n+1}}
}{
X^{\ell^n}+Y^{\ell^n}
}
=
\Phi_{2\ell^{n+1}}(X,Y)
\]

proves the claim. \(\square\)

Let

\[
L
=
\mathbb{Q}(\sqrt{b_0},\sqrt{-a_0})
\]

and

\[
v=\frac{\omega}{\bar\omega}.
\]

The branch of a prime records a sharper order condition than the product
alone.

### Proposition 10: Branch order

Let \(p\) be a rational prime and \(\mathfrak P\mid p\) in \(L\). Then

\[
p\mid A_n
\quad\Longrightarrow\quad
\operatorname{ord}(\widetilde v)
=
\ell^{n+1},
\]

and

\[
p\mid B_n
\quad\Longrightarrow\quad
\operatorname{ord}(\widetilde v)
=
2\ell^{n+1}.
\]

Here \(\widetilde v\) is the reduction of \(v\) modulo \(\mathfrak P\).
Thus the unique coordinate branch in Theorem 3 is also a unique
cyclotomic order label.

#### Proof

Theorem 3 excludes

\[
p\mid2\ell a_0b_0c_0,
\]

so \(\omega\) and \(\bar\omega\) are units modulo \(\mathfrak P\). Divide
the atom formulas by the appropriate power of \(\bar\omega\). Since the
residue characteristic does not divide either cyclotomic index, a zero of
\(\Phi_{\ell^{n+1}}\), respectively
\(\Phi_{2\ell^{n+1}}\), has exactly the displayed order. \(\square\)

### Proposition 11: Signed branch Wieferich lifts

If \(p\mid A_n\), respectively \(p\mid B_n\), then

\[
p^2\mid A_n
\quad\Longleftrightarrow\quad
v^{\ell^{n+1}}
\equiv1
\pmod{\mathfrak P^2},
\]

and

\[
p^2\mid B_n
\quad\Longleftrightarrow\quad
v^{\ell^{n+1}}
\equiv-1
\pmod{\mathfrak P^2}.
\]

Thus a repeated prime records not only its level but also, through the sign
of the lift, the coordinate in which it was born.

#### Proof

For the first branch, the exact-order statement makes
\(v^{\ell^n}-1\) a \(\mathfrak P\)-adic unit, while

\[
\Phi_{\ell^{n+1}}(v)
=
\frac{v^{\ell^{n+1}}-1}
{v^{\ell^n}-1}.
\]

For the second branch, \(v^{\ell^n}\) has order \(2\ell\), so
\(v^{\ell^n}+1\) is also a unit, and

\[
\Phi_{2\ell^{n+1}}(v)
=
\frac{v^{\ell^{n+1}}+1}
{v^{\ell^n}+1}.
\]

The extension is unramified at \(p\), and \(A_n,B_n\) are rational
integers; hence divisibility by \(p^2\) is equivalent to valuation at least
two at every prime above \(p\). The two equivalences follow. \(\square\)

Squaring \(\omega\) descends the two branches to one quadratic Lucas atom.
Define

\[
\alpha
=
b_0-a_0+2\sqrt{-a_0b_0},
\qquad
\beta
=
b_0-a_0-2\sqrt{-a_0b_0}.
\]

Then

\[
\alpha\beta=c_0^2.
\]

Let

\[
\mathcal U_r
=
\frac{\alpha^r-\beta^r}
{\alpha-\beta}
\qquad(r\geq1)
\]

be the associated quadratic Lucas sequence, and let

\[
\Phi_r(X,Y)
=
Y^{\varphi(r)}
\Phi_r(X/Y)
\]

denote the homogeneous cyclotomic polynomial.

### Proposition 12: Prime-power cyclotomic factorization

For every \(n\geq0\),

\[
S_nC_n
=
\frac{\mathcal U_{\ell^{n+1}}}
{\mathcal U_{\ell^n}}
=
\Phi_{\ell^{n+1}}(\alpha,\beta).
\]

Thus \(\ell E_n\) is the absolute value of the
\(\ell^{n+1}\)-st homogeneous cyclotomic factor of the fixed Lucas pair
\((\alpha,\beta)\).

#### Proof

Write

\[
\alpha=c_0e^{i\theta},
\qquad
\beta=c_0e^{-i\theta}.
\]

Then

\[
\mathcal U_r
=
c_0^{r-1}
\frac{\sin(r\theta)}
{\sin\theta}.
\]

Taking the quotient at \(r=\ell^{n+1}\) and \(r=\ell^n\), and using
\(c_n=c_0^{\ell^n}\), gives the formula from Lemma 4. The second equality
is the standard identity

\[
\frac{
X^{\ell^{n+1}}-Y^{\ell^{n+1}}
}{
X^{\ell^n}-Y^{\ell^n}
}
=
\Phi_{\ell^{n+1}}(X,Y).
\]

\(\square\)

Let

\[
K
=
\mathbb{Q}(\sqrt{-a_0b_0}),
\]

let \(D_K\) be its field discriminant, and put

\[
u=\frac{\alpha}{\beta}\in K^\times.
\]

The norm of \(u\) is one.

### Theorem 13: Exact level and prime congruence

Let \(p\mid E_n\) be a rational prime, and let
\(\mathfrak p\mid p\) in \(K\). Then

\[
p\nmid2\ell a_0b_0c_0,
\]

and the image \(\widetilde u\) of \(u\) in
\((\mathcal O_K/\mathfrak p)^\times\) has exact order

\[
\operatorname{ord}(\widetilde u)
=
\ell^{n+1}.
\]

Consequently,

\[
\boxed{
\ell^{n+1}
\mid
p-\left(\frac{D_K}{p}\right).
}
\]

In particular, every new prime introduced at generation \(n\) lies in one
of the two residue classes

\[
\pm1\pmod{\ell^{n+1}},
\]

with the sign determined by splitting in \(K\).

#### Proof

The exclusion of \(2,\ell\), and the seed primes follows from Theorem 3.
Hence \(p\) is unramified in \(K\), and
\(\alpha,\beta,\alpha-\beta\) are units modulo \(\mathfrak p\).

By Proposition 12,

\[
\Phi_{\ell^{n+1}}(u)
\equiv0
\pmod{\mathfrak p}.
\]

Since \(p\neq\ell\), a root of this cyclotomic polynomial in the residue
field has exact order \(\ell^{n+1}\).

If \(p\) splits in \(K\), then

\[
\widetilde u\in\mathbb F_p^\times,
\]

so its order divides \(p-1\). If \(p\) is inert, Frobenius acts as
conjugation and therefore

\[
\widetilde u^{\,p}
=
\widetilde{\bar u}
=
\widetilde u^{-1};
\]

its order divides \(p+1\). These two cases give the displayed congruence.
\(\square\)

### Proposition 14: Cyclotomic Wieferich criterion

Let \(p\mid E_n\), and let \(\mathfrak p\mid p\) in \(K\). Then

\[
p^2\mid E_n
\quad\Longleftrightarrow\quad
u^{\ell^{n+1}}
\equiv1
\pmod{\mathfrak p^2}.
\]

The condition is independent of the choice of \(\mathfrak p\mid p\).
Moreover,

\[
W_n
=
\prod_{j=0}^{n-1}
\prod_{p\mid E_j}
p^{v_p(E_j)-1}.
\]

Thus the nonarchimedean term governing the asymptotic \(abc\)-quality is
exactly the aggregate multiplicity of cyclotomic Wieferich lifts at
\(\ell\)-power levels. The local valuation theory of Lucas atoms is known
in substantially greater generality; the point here is its exact
identification with the global defect term \(W_n\) of a single additive
orbit.

#### Proof

Modulo \(\mathfrak p\), the element \(u^{\ell^n}\) is not one by
Theorem 13. Hence the denominator in

\[
\Phi_{\ell^{n+1}}(u)
=
\frac{u^{\ell^{n+1}}-1}
{u^{\ell^n}-1}
\]

is a \(\mathfrak p\)-adic unit. Therefore the valuation of the cyclotomic
factor is at least two exactly when the numerator vanishes modulo
\(\mathfrak p^2\).

Since \(E_n\) is rational, conjugate prime ideals above a split prime occur
with equal valuations. The product formula for \(W_n\) is its definition
expanded prime by prime. \(\square\)

## Local classification and exact realization of prime genealogies

The congruence in Theorem 13 is not only necessary. When the seed is
allowed to vary, it is the complete local compatibility condition, and the
valuation can be prescribed exactly.

The recursion makes each level multiplier a homogeneous polynomial in the
seed variables. For a prime \(p\ne\ell\), write over
\(\mathbb Z_{(p)}\)

\[
\mathcal F_{n,A}(X,Y)
=
\frac{S_n(X,Y)}{\ell},
\qquad
\mathcal F_{n,B}(X,Y)
=
C_n(X,Y),
\]

where \(S_n(X,Y),C_n(X,Y)\) mean the multipliers at level \(n\) in the
orbit started from \((X,Y)\). Put

\[
m_{n,A}
=
\ell^{n+1},
\qquad
m_{n,B}
=
2\ell^{n+1},
\]

and

\[
d_n
=
\frac{\varphi(m_{n,A})}{2}
=
\frac{\ell^n(\ell-1)}{2}.
\]

### Proposition 15: Local root classification

Fix \(n\geq0\), a branch \(\varepsilon\in\{A,B\}\), and an odd prime
\(p\ne\ell\). Let

\[
m=m_{n,\varepsilon}.
\]

If

\[
m\mid p-\chi
\qquad
\text{for some }\chi\in\{1,-1\},
\]

then \(\mathcal F_{n,\varepsilon}(X,1)\) has exactly \(d_n\) distinct,
simple roots in \(\mathbb F_p\). They are

\[
\rho_\zeta
=
-\left(
\frac{\zeta-1}{\zeta+1}
\right)^2,
\]

where \(\zeta\) ranges, modulo \(\zeta\sim\zeta^{-1}\), over the
elements of exact order \(m\) in \(\mathbb F_p^\times\) when \(\chi=1\),
and over the norm-one subgroup of \(\mathbb F_{p^2}^\times\) when
\(\chi=-1\).

Every such root satisfies

\[
\rho_\zeta\ne0,-1,
\qquad
\left(\frac{-\rho_\zeta}{p}\right)
=
\chi.
\]

Conversely, every nondegenerate root arises in this way. Hence such roots
exist if and only if

\[
\ell^{n+1}\mid p-1
\quad\text{or}\quad
\ell^{n+1}\mid p+1.
\]

#### Proof

Under the compatibility condition, choose \(\zeta\) of exact order \(m\)
in the indicated cyclic group and put

\[
s
=
\frac{\zeta-1}{\zeta+1},
\qquad
\rho=-s^2.
\]

If \(\chi=1\), then \(s,\rho\in\mathbb F_p\).

If \(\chi=-1\), Frobenius on the norm-one group gives

\[
\zeta^p=\zeta^{-1},
\]

hence

\[
s^p=-s
\]

and again \(\rho\in\mathbb F_p\).

In either case, in the split or quadratic residue algebra containing
\(s\), the substitutions

\[
\sqrt{b_0}\longmapsto1,
\qquad
\sqrt{-a_0}\longmapsto s
\]

for \((a_0,b_0)=(\rho,1)\) give

\[
\frac{\omega}{\bar\omega}
\longmapsto
\frac{1+s}{1-s}
=
\zeta.
\]

Proposition 9 therefore makes the selected branch atom vanish. The
elements \(s\), \(1-s\), and \(1+s\) are nonzero, so

\[
\rho\ne0,-1.
\]

In the split case,

\[
-\rho=s^2
\]

is a square. In the inert case it is a nonsquare: otherwise \(s\) would
lie in \(\mathbb F_p\), forcing

\[
\zeta
=
\frac{1+s}{1-s}
\]

into \(\mathbb F_p\) although \(m\nmid p-1\). This proves the
Legendre-symbol assertion.

Moreover,

\[
\mathcal F_{n,\varepsilon}(0,1)=1,
\]

so its reduction is not the zero polynomial. The \(\varphi(m)\) elements
of exact order \(m\) yield exactly

\[
\frac{\varphi(m)}2=d_n
\]

values of \(\rho\), because

\[
\rho_\zeta=\rho_{\zeta^{-1}},
\]

and equality of two values forces the corresponding Cayley parameters to
differ by sign. The atom has degree \(d_n\) in \(X,Y\), so these roots
exhaust it and are simple.

Conversely, a nondegenerate root gives, after dividing the homogeneous atom
by the appropriate power of \(\bar\omega\), an element of exact order
\(m\) in the split group of order \(p-1\) or the norm-one group of order
\(p+1\). This proves the classification.

For the \(B\)-branch the factor \(2\) in \(m\) imposes no extra
congruence, because \(p-\chi\) is already even. \(\square\)

### Corollary 16: Exact local valuation

Every root in Proposition 15 has a unique lift

\[
\widehat\rho\in\mathbb Z_p
\]

satisfying

\[
\mathcal F_{n,\varepsilon}(\widehat\rho,1)=0.
\]

For every \(h\geq1\) and \(\lambda\in\mathbb Z_p^\times\),

\[
v_p\left(
\mathcal F_{n,\varepsilon}
(\widehat\rho+\lambda p^h,1)
\right)
=
h.
\]

#### Proof

The root is simple, so Hensel's lemma gives the unique lift and makes the
derivative a \(p\)-adic unit. Taylor expansion at \(\widehat\rho\) gives

\[
\mathcal F_{n,\varepsilon}
(\widehat\rho+\lambda p^h,1)
=
\lambda p^h
\mathcal F'_{n,\varepsilon}(\widehat\rho,1)
+
O(p^{2h}),
\]

which has valuation exactly \(h\). \(\square\)

### Theorem 17: Exact finite genealogy realization

Fix an odd prime \(\ell\). Let

\[
\mathcal D
=
\{
(p_i,n_i,\varepsilon_i,h_i,\chi_i):
1\leq i\leq r
\}
\]

be finite data in which:

- the \(p_i\) are distinct odd primes different from \(\ell\);
- \(n_i\geq0\);
- \(h_i\geq1\);
- \(\varepsilon_i\in\{A,B\}\);
- \(\chi_i\in\{1,-1\}\).

Suppose

\[
m_{n_i,\varepsilon_i}
\mid
p_i-\chi_i.
\]

Then there are infinitely many admissible primitive seeds for which

\[
\varepsilon_i=A
\quad\Longrightarrow\quad
v_{p_i}(A_{n_i})=h_i,
\]

\[
\varepsilon_i=B
\quad\Longrightarrow\quad
v_{p_i}(B_{n_i})=h_i,
\]

\[
\left(\frac{D_K}{p_i}\right)
=
\chi_i,
\]

and

\[
p_i\nmid A_jB_j
\qquad
(0\leq j<n_i),
\]

where

\[
K=\mathbb Q(\sqrt{-a_0b_0}).
\]

Hence every \(p_i\) is born at exactly the prescribed generation, in
exactly the prescribed branch, with exactly the prescribed multiplicity
and splitting sign. It never occurs in a later generation factor.

#### Proof

For each datum choose a simple root \(\rho_i\) from Proposition 15, and let
\(\widehat\rho_i\) be its \(p_i\)-adic lift. Impose

\[
b_0
\equiv
1
\pmod{p_i^{h_i+1}},
\]

and

\[
a_0
\equiv
\widehat\rho_i+p_i^{h_i}
\pmod{p_i^{h_i+1}}.
\]

Since \(b_0\) is a unit and the branch polynomial is homogeneous,
Corollary 16 gives the exact prescribed valuation.

Reduction modulo \(p_i\) leaves the exact order
\(m_{n_i,\varepsilon_i}\) unchanged, so every earlier atom and the
opposite atom at the target level are nonzero. Proposition 15 gives

\[
\left(\frac{-a_0b_0}{p_i}\right)
=
\chi_i,
\]

which equals the field-discriminant symbol because

\[
p_i\nmid2a_0b_0.
\]

This proves all local assertions.

It remains to realize them simultaneously by primitive positive integers.
Combine the local congruences by the Chinese remainder theorem and also
require \(a_0\) even and \(b_0\) odd.

For \(\ell\geq5\), impose

\[
a_0\equiv\ell\pmod{\ell^2},
\qquad
b_0\equiv1\pmod{\ell^2}.
\]

For \(\ell=3\), impose

\[
a_0\equiv3\pmod9,
\qquad
b_0\equiv2\pmod9.
\]

The latter gives

\[
v_3(3b_0-a_0)=1.
\]

Let \(M\) be the product of these coprime moduli. Choose infinitely many
positive \(b_0\) in its prescribed unit residue class. For each such
\(b_0\), the Chinese remainder theorem supplies a positive \(a_0\) in its
prescribed class modulo \(M\) and with

\[
a_0\equiv1\pmod{b_0},
\]

because

\[
\gcd(b_0,M)=1.
\]

Thus

\[
\gcd(a_0,b_0)=1,
\]

and the parity and \(\ell\)-adic conditions give admissibility. Theorem 3
excludes every prescribed prime from all later generation factors.
\(\square\)

### Remark 18: A programmed square

For \(\ell=3\), the admissible seed

\[
(a_0,b_0)
=
(304{,}260{,}006,39{,}305)
\]

satisfies

\[
17\nmid A_0B_0,
\qquad
v_{17}(A_1)=2,
\qquad
\left(\frac{D_K}{17}\right)=-1.
\]

Thus \(17\) is programmed to be born in the \(A\)-branch at level \(1\),
with multiplicity exactly two and inert sign. The accompanying verification
script constructs this seed from the local root and checks the assertions.

### Corollary 19: Unbounded fixed-level defect across seeds

Fix \(\ell\), a generation \(n\), and either branch. For every odd prime
\(p\ne\ell\) satisfying

\[
\ell^{n+1}\mid p-1
\quad\text{or}\quad
\ell^{n+1}\mid p+1,
\]

and every \(H\geq1\), there are infinitely many admissible seeds for which
the selected generation factor has \(p\)-adic valuation exactly \(H\).

In particular, \(W_{n+1}\) is unbounded as the seed varies, even with
\(\ell\) and \(n\) fixed.

This does not address Conjecture 21, which fixes one seed and lets \(n\)
tend to infinity. Rather, it shows that no uniform squarefreeness or
valuation bound can hold across all seeds. More sharply, the necessary
split/inert congruence and the signed branch conditions are locally
sufficient at every level, with arbitrary exact multiplicity.

## A canonical family for every odd prime

### Corollary 20: Uniform explicit hit orbits

For every odd prime \(\ell\), the seed

\[
(a_0,b_0,c_0)
=
(\ell,2,\ell+2)
\]

is admissible. Every member of its orbit with \(n\geq2\) is an
\(abc\)-hit.

#### Proof

The seed is primitive and has opposite parity. For \(\ell\geq5\),
admissibility follows from Lemma 1. For \(\ell=3\), one has

\[
S_3(3,2)=3.
\]

Since

\[
R_0
=
2\ell\,\operatorname{rad}(\ell+2)
\leq
2\ell(\ell+2),
\]

Theorem 5 gives

\[
\frac{c_n}{R_n}
\geq
\frac{\ell^{n-1}\sqrt{2\ell}}
{\ell+2}.
\]

At \(n=2\), the right side is greater than one for every odd prime
\(\ell\geq3\), and it increases with \(n\). \(\square\)

The first two nontrivial examples illustrate that the guaranteed hit need
not occur at the first transfer.

### The cubic orbit

For \(\ell=3\),

\[
(3,2,5)
\longmapsto
(27,98,125)
\longmapsto
(1{,}924{,}803,28{,}322,1{,}953{,}125).
\]

The second transferred triple factors as

\[
\begin{aligned}
1{,}924{,}803
&=
3^5\cdot89^2,\\
28{,}322
&=
2\cdot7^2\cdot17^2,\\
1{,}953{,}125
&=
5^9,
\end{aligned}
\]

so

\[
R_2
=
2\cdot3\cdot5\cdot7\cdot17\cdot89
=
317{,}730,
\]

and

\[
\frac{c_2}{R_2}
=
6.1471\ldots
\]

The first two generation factors are

\[
E_0=7,
\qquad
E_1=17\cdot89.
\]

Their prime divisors satisfy respectively

\[
p\equiv\pm1\pmod3
\]

and

\[
p\equiv\pm1\pmod9,
\]

as predicted by Theorem 13.

### The quintic orbit

For \(\ell=5\),

\[
(5,2,7)
\longmapsto
(15{,}125,1{,}682,16{,}807),
\]

where

\[
E_0=11\cdot29.
\]

The next member has

\[
\begin{aligned}
a_2
&=
1{,}997{,}240{,}239{,}809{,}753{,}125,\\
b_2
&=
1{,}339{,}071{,}379{,}424{,}155{,}147{,}682,\\
c_2
&=
1{,}341{,}068{,}619{,}663{,}964{,}900{,}807
=
7^{25},
\end{aligned}
\]

and

\[
\frac{c_2}{R_2}
=
29.2870\ldots
\]

Here

\[
E_1
=
199\cdot11{,}549\cdot892{,}254{,}749,
\]

and every displayed prime is congruent to

\[
\pm1\pmod{25}.
\]

## Open directions

The exact identity converts the asymptotic problem into one about repeated
prime factors in a sequence of pairwise coprime cyclotomic values.

### Conjecture 21: Subpower repeated-prime growth

For every admissible seed and odd prime \(\ell\),

\[
\log W_n=o(\ell^n).
\]

Equivalently, the quality of every prime-degree Chebyshev orbit tends to
one.

By Proposition 14, this is an averaged sparsity statement for cyclotomic
Wieferich lifts, not merely a primitive-divisor problem. Theorem 13
supplies a strong level restriction on every prime involved:

\[
p
\equiv
\left(\frac{D_K}{p}\right)
\pmod{\ell^{j+1}}
\qquad
(p\mid E_j).
\]

A plausible first target is the weaker estimate

\[
\sum_{j<n}
\sum_{p^2\mid E_j}
\log p
=
o(\ell^n),
\]

followed by control of higher valuations.

Another natural problem is to study Conjecture 21 on average over
admissible seeds, where large-sieve or Chebotarev methods may be more
accessible than for one fixed orbit.

The prime-degree restriction is arithmetically meaningful. It makes the
new Lucas factor a single homogeneous cyclotomic value

\[
\Phi_{\ell^{n+1}}(\alpha,\beta),
\]

and the only systematic overlap between generations is the transfer prime
\(\ell\), removed in the definition of \(E_n\). Composite degrees lead to
several cyclotomic layers at each step and require a different
normalization.

## Novelty boundary

The following distinctions are important.

The identity

\[
aS_\ell(a,b)^2+bC_\ell(a,b)^2=(a+b)^\ell
\]

is a direct form of de Moivre's formula and is not presented as a new
polynomial identity.

Polynomial \(abc\)-transfers and sharp polynomial triples are well
established; representative sources are Martin-Miao and van der Horst.

Prime-power cyclotomic factors and Lucas primitive-divisor phenomena are
classical. Bilu, Hanrot, and Voutier prove the general primitive-divisor
theorem for Lucas and Lehmer numbers. Alecci, Miska, Murru, and Romeo give
a general definition and complete \(p\)-adic valuation theory for Lucas
atoms; Ross, Shen, and Cai prove further cyclotomic congruences for Lucas
sequences. The local order, valuation, and congruence statements above are
specializations, not new local valuation theory.

Ratliff, Rush, and Shah construct pairwise radical-preserving families from
homogeneous cyclotomic polynomials in a commutative-algebra setting. That is
relevant support-separation prior art; the statement here identifies the
two particular towers as coordinate multipliers in one additive orbit and
derives its arithmetic dynamics.

Kym's valuation-separation theorem concerns products of Lucas terms at
pairwise coprime indices. Here the atom indices are nested powers,

\[
\ell^{n+1}
\quad\text{and}\quad
2\ell^{n+1};
\]

separation instead comes from the transfer normalization and the two
coordinate branches.

The proposed contribution is the orbit-level combination:

> A complete branchwise prime genealogy, the realization as two
> interleaved nested-index atom towers, the radical telescope, strict
> monotonicity, the if-and-only-if quality criterion, the coupling of
> known local valuations to one global \(abc\)-defect term, and the exact
> local-global realization of arbitrary finite compatible prime
> genealogies.

A bounded search through transfer catalogues, Chebyshev arithmetic,
Lucas-sequence literature, and arithmetic-dynamical primitive-divisor work
did not locate these statements as an existing theorem. Specialist review
is still required before making an unconditional priority claim.

## AI-use statement

OpenAI GPT-5.6 Pro was used for mathematical exploration, proof
development, symbolic and numerical checks, literature retrieval, and
drafting. The named author must independently verify every theorem, proof,
reference, and novelty statement before circulation or submission. The AI
system is not an author.

## References

G. Alecci, P. Miska, N. Murru, and G. Romeo, "On alternative definition
of Lucas atoms and their \(p\)-adic valuations," *Monatshefte fur
Mathematik* **207** (2025), 175-196.

<https://doi.org/10.1007/s00605-025-02087-w>

A. Baker and G. Wustholz, "Logarithmic forms and group varieties,"
*Journal fur die reine und angewandte Mathematik* **442** (1993), 19-62.

<https://doi.org/10.1515/crll.1993.442.19>

Y. Bilu, G. Hanrot, and P. M. Voutier, "Existence of primitive divisors of
Lucas and Lehmer numbers," *Journal fur die reine und angewandte
Mathematik* **539** (2001), 75-122.

<https://doi.org/10.1515/crll.2001.080>

T. Ross, Z. Shen, and T. Cai, "Cyclotomic congruences and Lucas sequences,"
arXiv:2512.03468 [math.NT], 2025.

<https://doi.org/10.48550/arXiv.2512.03468>

L. J. Ratliff, Jr., D. E. Rush, and K. Shah, "Note on cyclotomic
polynomials and prime ideals," *Communications in Algebra* **32** (2004),
333-343.

<https://doi.org/10.1081/AGB-120027870>

D. Kym, "Valuation separation for coprime Lucas products,"
arXiv:2605.24909 [math.NT], 2026.

<https://doi.org/10.48550/arXiv.2605.24909>

G. Martin and W. Miao, "\(abc\) triples," *Functional Approximation
Commentarii Mathematici* **55** (2016), 145-176.

<https://doi.org/10.7169/facm/2016.55.2.2>

J. P. van der Horst, *Finding \(ABC\)-triples using elliptic curves*,
M.Sc. thesis, Universiteit Leiden, 2010.

<https://math.leidenuniv.nl/scripties/vanderHorstMaster.pdf>
