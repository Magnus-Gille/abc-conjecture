# The number of repeated primes and the square factor of a sum

Let \(a+b=c\) with \(a,b>0\) coprime, \(H=\log c\), and \(P=\operatorname{rad}(ab)\). Write \(c=d z^2\) with \(d\) squarefree. Thus \(d\) contains the primes occurring to an odd exponent in \(c\). All logarithms are natural.

## Counting only primes which repeat

Put \(M=\sum_{q^2\mid c}q^{f(q)}\), with the sum over primes, \(f(q)=1\) for \(q\equiv1\bmod4\), and \(f(q)=2\) otherwise. For fixed positive \(\alpha,\theta\), the conditions \(P\le H^\alpha,\ M\le H^\theta\) imply
\[
\log\big(c/\operatorname{rad}(c)\big)
\ \le\ H^{\max(\alpha,\theta)+o(1)}.
\tag{1}
\]
In particular, for \(P\le H^\alpha\) with \(\alpha<1\) and a bounded number of repeated primes, every such prime may be as large as \(H^{1/2-\delta}\) for any fixed \(0<\delta<1/2\), and \(c/\operatorname{rad}(abc)=c^{o(1)}\). Primes occurring exactly once have no size restriction here.

To see (1), sum the local valuation bound in the previous note just over \(q^2\mid c\). For \(q\le H^\gamma\) the sum of the full valuations times \(\log q\) is at most \(H^{\alpha+3\gamma+o(1)}\) by its small-prime argument. For \(q>H^\gamma\), the factor \([D(1+\log P/\log q)]^r\) in that bound is \(H^{o(1)}\) since \(r=O_\alpha(\log H/\log\log H)\). The factors polynomial in \(\log q,r,\log H\) are \(H^{o(1)}\) since every prime counted by \(M\) satisfies \(q\le H^\theta\). Summing \(q^{f(q)}\) now costs at most \(H^\theta\). Let \(\gamma\) tend to zero after taking the limit superior of logarithmic exponents. [Local bound and proof](abc_dyadic_moving_primes.md)

## A bound independent of the sizes of primes in the square factor

There is an absolute constant \(C>0\) such that
\[
d\ \gg\ \frac{H^2}{(2P)^C\log^4(3+H)}.
\tag{2}
\]
In particular \(d\ge H^{2-o(1)}\) along any sequence with \(c\to\infty\) and \(P=H^{o(1)}\). Equivalently, along such a sequence the largest integer \(z\) for which \(z^2\mid c\) satisfies \(z\le\sqrt c/H^{1-o(1)}\). This last bound applies to the product of all the square factors together. For each fixed \(P_0\), if \(P\le P_0\) and \(d\) is bounded, there are only finitely many triples.

### Reduction to a two-term unit equation

Set \(t=\sqrt{c/a}\), \(K=\mathbb Q(t)\), \(U=(1+t)/2\), and \(V=(1-t)/2\). Let \(S\) consist of the real places of \(K\) and the places above primes dividing \(2ab\). We have
\[
U+V=1,\qquad UV=-b/(4a).
\]
Outside \(S\), \(t,U,V\) are integral and \(UV\) is a unit, so \(U,V\) are both \(S\)-units. In particular primes dividing \(z\) need not be included in \(S\). Write \(h\) for absolute logarithmic height. Since \(\gcd(a,c)=1\) and \(a<c\), \(h(t)=H/2\). The relations \(t=2U-1=1-2V\) and the definitions give \(h(U),h(V)=H/2+O(1)\). The field is rational or real quadratic and its absolute discriminant satisfies
\[
|\Delta_K|\le4\operatorname{sf}(a)d\le4Pd ,
\]
where \(\operatorname{sf}(a)\) denotes its squarefree part. This uses \(\gcd(a,c)=1\).

For clarity, the requisite uniform height estimate is justified below with logarithmic forms and the regulator. It is a coarse version of standard effective estimates for the \(S\)-unit equation. [Győry, *Bounds for the solutions of S-unit equations and decomposable form equations II*](https://arxiv.org/abs/1901.11289)

### Small independent generators

At a finite place \(w\) use coordinates \(\ell_w(x)=-v_w(x)\log Nw\) and at real places use \(\ell_w(x)=\log|x|_w\). They sum to zero for \(S\)-units and their positive sum is \([K:\mathbb Q]h(x)\). Thus some \(w\in S\) satisfies \(-\ell_w(U)\gg H/|S|\) for large \(H\). If this place is finite, \(v_w(U)>0\) makes \(V=1-U\) a unit at \(w\); in this case put \(T=S\setminus\{w\}\). At a real place put \(T=S\). The omission in the finite case ensures that all the generators below are local units at the place where the logarithmic-form estimate is applied.

Write \(r=|T|-1\) and \(R_T\) for the \(T\)-regulator in these logarithmic coordinates with one real coordinate deleted. The torsion in \(K\) is \(\{\pm1\}\). If \(V\) is torsion, its bounded height bounds \(H\) already. Otherwise \(r\ge1\). Let \(\lambda_1,\ldots,\lambda_r\) be the successive minima of the projected unit lattice for the sup norm. Minkowski's second theorem gives \(\prod\lambda_i\le R_T\). Each non-torsion element of degree at most two has height bounded below by an absolute positive constant, by Northcott's finiteness theorem. The deleted coordinate is minus the sum of the others, so \(\lambda_i\gg1/r\).

Choose independent units \(g_i\) with sup norms at most \(2\lambda_i\). Their lattice has index \(I\le 2^r r!\) by the determinant expansion, and
\[
\prod (1+h(g_i))\le (C_1r)^r R_T
\]
for an absolute \(C_1\). Write \(V^I=\pm\prod g_i^{b_i}\). Cramer's rule expresses \(|b_i|\) as the absolute determinant with column \(i\) replaced by the vector for \(V\), divided by \(R_T\). Hence \(|b_i|\le (C_2 r)^{r+2}(H+1)\) by the product bound for the minima and the lower bound on \(\lambda_i\). Squaring removes the sign.

### Recovering the height and the squarefree part

At a real place, if \(|U|>1/(2I)\), the preceding small-place inequality bounds \(H\ll |S|\log(2I)\). Otherwise
\[
0<|1-V^{2I}|\le 2e I |U|.
\]
Matveev's real logarithmic-form estimate applied to \(\prod(g_i^2)^{b_i}-1\) bounds its negative log by \((C_3r)^{C_3r}\prod(1+h(g_i))\log(3+\max |b_i|)\) in degree at most two. All \(g_i^2\) are positive at this embedding. [Matveev](https://doi.org/10.1070/IM2000v064n06ABEH000314)

At a finite \(w\), \(v_w(1-V^{2I})\ge v_w(1-V)=v_w(U)\). Apply Yu's logarithmic-form estimate to \(V^{2I}\) with the \(w\)-unit generators just constructed. If necessary adjoin \(i\) for odd residue characteristic or \(\zeta_3\) for characteristic two. The field degree is at most four and the rational residue prime \(q\) divides \(2P\). Yu's explicit constants give
\[
v_w(1-V^{2I})\log Nw
\le q^4(C_4r)^{C_4r}(1+\log(2q))^{C_4(r+1)}
     \prod(1+h(g_i))\log(3+\max|2b_i|).
\]
Indeed the residue-degree factor is at most \(q^4\), the factorial and degree factors are \((C_4r)^{O(r)}\), and each modified height is at most a constant times \((1+\log(2q))(1+h(g_i))\). A torsion generator, if included, is absorbed by the displayed factors. Converting the valuation from the auxiliary extension to \(K\) costs at most a degree-dependent factor. The real and finite estimates apply to a nonzero difference since \(V\) is non-torsion. [Explicit Yu constants and heights](https://github.com/sagemath/sage/blob/develop/src/sage/rings/number_field/S_unit_solver.py#L462-L607) · [Alvarado et al.](https://arxiv.org/abs/1903.00977)

The number \(s\) of rational primes dividing \(2ab\) satisfies \(s!\le 2P\), and \(|S|\le 2s+2\). In particular all factors of the form \((C r)^{Cr}\) and \((1+\log(2q))^{C(r+1)}\) above are bounded by \((2P)^{O(1)}\); for the latter use \(s\log\log(3P)=O(\log(2P))\). Consequently both the real and finite cases give
\[
H\le (2P)^{C_5}(1+R_T)\log(3+H).
\]

The valuation image of the \(T\)-units in \(\mathbb Z^{|T_{\rm fin}|}\) has index at most the class number \(h_K\), since the cokernel maps isomorphically to the subgroup of the ideal class group generated by the indicated prime ideals. Taking determinants gives
\[
R_T\le h_K R_K\prod_{v\in T_{\rm fin}}\log Nv .
\]
Use \(R_{\mathbb Q}=1\). The product of finite-place logarithms is at most \((2P)^{O(1)}\). In a real quadratic field the class number formula gives \(h_KR_K\ll\sqrt{|\Delta_K|}\log(2|\Delta_K|)\), using the elementary bound \(L(1,\chi_{\Delta_K})\ll\log(2|\Delta_K|)\). Hence
\[
H\le (2P)^{C_6}\sqrt d\,\log(2Pd)\log(3+H).
\]
If \(P\) or \(d\) exceeds \(H^2\), (2) is immediate after increasing its constant exponent. Otherwise \(\log(2Pd)=O(\log(3+H))\), proving (2).

## An exact square case

If all primes in \(ab\) belong to \(\{2,3\}\) and \(c\) is a square, the unordered pairs of addends are exactly
\[
(1,3),\ (1,8),\ (1,24),\ (9,16),\ (1,48),\ (1,288).
\]
To prove completeness write \(c=y^2\). If neither addend is 1, they must be \(2^m,3^n\) with \(m,n>0\). Reduction modulo 3 forces \(m\) even. The coprime positive odd factors \(y-2^{m/2}\) and \(y+2^{m/2}\) multiply to \(3^n\), so the smaller is 1. Thus \(3^n-1=2^{m/2+1}\). Reduction modulo 4 makes \(n\) even, and \(3^{n/2}-1,3^{n/2}+1\) must be the powers of two 2 and 4. This gives \(9+16=25\).

If one addend is 1 then \(y-1,y+1\) are supported on \(\{2,3\}\). For even \(y\) these are coprime odd powers of three (including 1), giving \(y=2\). For odd \(y\), \((y-1)/2,(y+1)/2\) are consecutive coprime positive \(\{2,3\}\)-smooth numbers. The possible pairs are \((1,2),(2,3),(3,4),(8,9)\). Indeed a nontrivial pair consists of a power of 2 and a power of 3. For \(3^n-2^m=1\), either \(m=1\) or reduction modulo 4 permits factoring \(3^n-1\) as above. For \(2^m-3^n=1\), reduction modulo 3 makes \(m\) even and the coprime factors \(2^{m/2}\pm1\) force \(m=2,n=1\). This exhausts all cases.

The classification extends over infinitely many possible supports. Let \(p\) be any prime congruent to 3 or 5 modulo 8 and suppose every prime dividing \(ab\) belongs to \(\{2,p\}\). For \(p=3\) the list is as above. For \(p=5\) the full list is \((1,8),(4,5),(1,80)\). For every other such \(p\) the only pair is \((1,8)\).

Indeed \((2/p)=-1\) by the supplementary law of quadratic reciprocity. If \(2^m+p^n=y^2\) with \(m,n>0\), reduction modulo \(p\) forces \(m\) even. As before, \(y-2^{m/2}=1\), so \(p^n-1=2^{m/2+1}\). More generally, if \(p^n-1\) is a power of two then either \(n=1\), or \(n\) is even and \(p^{n/2}-1,p^{n/2}+1\) are 2 and 4. An odd \(n>1\) is impossible because \(1+p+\cdots+p^{n-1}\) is odd and exceeds 1. In the \(n=1\) case the residue condition and \(p=1+2^k\) force \(p=3\) or 5. For a gap of one in the opposite direction, \(2^m-p^n=1\) also forces \(m\) even by \((2/p)=-1\). Its two odd factors \(2^{m/2}-1,2^{m/2}+1\) then give \(2^m=4,\ p^n=3\). These facts exhaust the case where both addends exceed one and the consecutive smooth numbers needed when an addend equals one. In the latter case an even \(y\) forces \(y-1=1,\ y+1=3\). This proves all the lists without a height limit.

The squarefree-part estimate allows \(d\) to be a power of \(\log c\) even at arbitrarily large height. Rational abc would require \(\operatorname{rad}(abc)\ge c^{1-o(1)}\) uniformly over primitive triples. That gap remains here.
