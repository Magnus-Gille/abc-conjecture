# Primitive divisors and restrictions on every perfect-power exponent

For \(E_6:Y^2=X^3-36X\), \(G=(-3,9)\), and a positive odd index \(n\), write \(w_n=B(nG)\) for the positive square root of the reduced abscissa denominator. No \(w_n\), \(n>1\), is a square or a cube. If \(w_n\) is an \(\ell\)-th power for an odd prime \(\ell\ge5\), then
\[
             \ell\equiv1\ \text{or}\ -1\pmod{48}.
\]
In the first class, 2 must be a fourth power modulo \(\ell\). These are synchronized congruences: the first class splits in the Eisenstein field, and the second is inert. The largest prime factor of \(n\) is then uniquely determined by \(\ell\) via reduction on \(E_6\). [Square classification](abc_full_quartic_square_chabauty.md) · [Cube classification](abc_full_quartic_cube_chabauty.md)

## Every nontrivial odd denominator has a primitive prime

Use the canonical height convention \(h(X(S))=2\widehat h(S)+O(1)\). The explicit duplication estimate for this curve gives
\[
 2\widehat h(S)-\log(1369)/3\le h(X(S))
       \le2\widehat h(S)+\log(5184)/3
\]
for nontorsion points. Indeed for \(X=A/B\) the duplication forms are \((A^2+36B^2)^2,4AB(A^2-36B^2)\). Their gcd divides \(2^6 3^4\); away from those primes they share no zero, and the square valuations at 2 and 3 give the indicated powers. The numerator is at least \(\max(|A|,B)^4\), and both coordinates are at most \(1369\max(|A|,B)^4\). Iterating proves the bounds. From \(X(4G)=1442401/19600\), one obtains \(1/3<H=\widehat h(G)<0.52\). At odd \(n\), \(-6<X(nG)<0\), so
\[
                Hn^2-2.2\le\log w_n\le Hn^2+1.5.
\]
[Full parametrization and height bounds](abc_full_quartic_signature.md)

Every prime \(p\mid w_n\) is \(1\bmod12\) and has good reduction. Its rank \(r_p\) is the exact order of \(G\bmod p\); \(p\mid w_n\) precisely when \(r_p\mid n\). For \(r_p\mid n\), the formal group gives \(v_p(w_n)=v_p(w_{r_p})+v_p(n/r_p)\). If \(w_n\) has no prime of rank \(n\), each of its prime divisors occurs at some \(w_{n/q}\) with \(q\mid n\) prime. Its valuation at \(w_n\) exceeds the corresponding valuation at \(w_{n/q}\) by at most \(v_p(q)\). Consequently
\[
 \log w_n\le\sum_{q\mid n,\ q\ {\rm prime}}\big(\log w_{n/q}+\log q\big).
\]
Since \(\sum_{q\mid n}q^{-2}<1/2\) at odd \(n\) and \(\omega(n)\le\log n/\log3\), this would give \(n^2/6<2.2+2.4\log n\), impossible for \(n\ge7\). At \(n=3,5\) the nonunit values 37 and 40573 have prime indices and \(w_1=1\). Therefore every odd \(n>1\) has a prime of exact rank \(n\). In particular, equality of prime supports of \(w_m,w_n\) forces \(m=n\): a prime of rank \(n\) forces \(n\mid m\), and conversely. This includes the trivial denominator separately.

## Eisenstein descent

Write \(j=\sqrt{-3}\), \(\beta=(x+yj)/2\), with coprime odd \(x,y\), \(3\nmid x\), \(N\beta=w_n\), and \(\beta^4+\bar\beta^4=-a^2\), where \(3\nmid a\). The ideals of \(\beta,\bar\beta\) are coprime. Assume \(w_n=v^\ell\) with \(n>1\) and \(\ell\ge5\) prime. In the Eisenstein integers unique factorization gives \(\beta=\gamma^\ell\) exactly, since exponentiation by \(\ell\) is a bijection on the six units. Then \((\gamma,\bar\gamma)=1\) as ideals and \(N\gamma=v>1\). Put
\[
 U=\gamma^4,\quad V=\bar\gamma^4,\quad T=U+V,\quad
 L=(U^\ell+V^\ell)/(U+V).
\]
Here \(T\ne0\), as otherwise odd \(\ell\) would give \(a=0\). Both \(T,L\) are rational integers by conjugation and integrality. A common rational prime divisor must be \(\ell\), because reduction at any prime above a divisor of \(T\) gives \(L\equiv\ell U^{\ell-1}\), with \(U\) a unit. Also \(T\equiv-1\bmod3\) in the residue field at the ramified prime, since \(\gamma,\bar\gamma\) have the same nonzero reduction.

If \(\ell\nmid T\), the identity \(TL=-a^2\) gives \(T=-s^2\), the sign following from the congruence modulo 3. This would place \(v\) in the original full quartic signature. Here are the integrality details. The class of \(\beta\) in \(\mathbf F_4\) at 2 is outside \(\mathbf F_2\), so \(\gamma=(u+bj)/2\) with both \(u,b\) odd. The coprime conjugate ideals exclude common factors of \(u,b\), and \(3\nmid u\) since \(3\nmid v\). Also \(s\) is odd and prime to 3. The norm of \(\gamma^4\) gives
\[
 s^4+3\left(ub(u^2-3b^2)/2\right)^2=4v^4 .
\]
The middle coordinate is nonzero: \(ub\ne0\) by oddness, and \(u^2=3b^2\) has no nonzero rational solutions. A prime dividing \(v\) cannot divide \(T\), since at a place where one of \(\gamma,\bar\gamma\) vanishes the other is a unit. Thus \((v,s)=1\), which with parity and \(3\nmid sv\) gives primitivity. The full parametrization now gives \(v=w_m\) at a positive odd index \(m\). Equality \(w_n=w_m^\ell\) forces \(n=m\) by the primitive-divisor result, contradicting \(w_n>1\).

We conclude that \(\ell\mid T\). The ordinary odd-prime lifting lemma applies at either place above the unramified rational prime \(\ell\), giving \(v_\ell(L)=1\): explicitly expand \(U^\ell+V^\ell\) by writing \(V=-U+T\), to get \(L\equiv\ell U^{\ell-1}\bmod\ell^2\). Thus \(v_\ell(T)\) is odd, and \(\ell\mid a\), \(\ell\nmid v\). The norm-one class \(\rho=\gamma/\bar\gamma\) satisfies \(\rho^4=-1\bmod\ell\), so has order 8. The torus has cardinality \(\ell-\chi\), where \(\chi=(-3/\ell)\). Hence \(8\mid\ell-\chi\), giving \(\ell\equiv\pm1\bmod24\). We have
\[
       T=\sigma\ell s^2,\qquad \sigma=-1\text{ if }\chi=1,
                                   \quad \sigma=1\text{ if }\chi=-1
\]
by the same congruence modulo 3.

## Reciprocal characters and modulo 48

Every prime \(h\mid v\) is \(1\bmod12\) by the full signature. At a place over \(h\) dividing \(\gamma\), the trace \(T\) reduces to \(\bar\gamma^4\), a nonzero fourth power in \(\mathbf F_h\). Thus \((\sigma\ell/h)=1\). Since \(h\equiv1\bmod4\), reciprocity gives \((h/\ell)=(\ell/h)=1\). Multiplying yields \((v/\ell)=1\).

At split \(\ell\) the residue field components of \(\gamma\) give \((v/\ell)=\rho^{(\ell-1)/2}=(-1)^{(\ell-1)/8}\), at either choice of component. At inert \(\ell\), \(\rho=\gamma^{1-\ell}\) and \(v=\gamma^{\ell+1}\) imply \((v/\ell)=\rho^{-(\ell+1)/2}=(-1)^{(\ell+1)/8}\). Hence \(16\mid\ell-\chi\), proving the stated \(\pm1\bmod48\) restriction with the same sign modulo 3.

In the split case put \(t=\gamma^2+\bar\gamma^2=(u^2-3b^2)/2\). Since all primes of \(v\) are \(1\bmod12\), the identity \(u^2+3b^2=4v\) forces \(u^2\equiv b^2\bmod16\). Hence \(t\equiv7\bmod8\). We also have \(t^2=2v^2-\ell s^2\), and \((t,v)=1\) by coprime conjugate ideals. For each rational prime \(h\mid t\), \(\ell\) and \(s\) are units modulo \(h\), and \((\ell/h)=(2/h)\). Therefore \((t/\ell)=(2/|t|)=1\), using \(\ell\equiv1\bmod4\) and the congruence for \(t\). Both \(v\) and \(t\) are squares modulo \(\ell\); consequently \(t/v\), a square root of 2, is a square. This proves that 2 is a fourth power.

## Prime index forced by the exponent

Let \(q\) be the largest prime dividing \(n\). Every \(h\mid w_q\) has rank \(q\), and \(4q\mid\#E_6(\mathbf F_h)\) by full rational two-torsion. Hence \(h\ge(2\sqrt q-1)^2>2q\), so \(h\nmid n\) and its valuation is unchanged from \(w_q\) to \(w_n\). Thus \(w_q\) itself is an \(\ell\)-th power. Apply the preceding descent at \(q\). Since \(\ell\mid a_q\), \(\ell\nmid w_q\), we have \(qG=(0,0)\bmod\ell\). The exact order is \(2q\): an order of 2 would force \(G=(0,0)\bmod\ell\) or another point of order two, impossible for \(G=(-3,9)\) at \(\ell\ge5\). Equivalently \(q\) is the exact order of \(G+(0,0)=(12,36)\bmod\ell\). Thus each exponent admits at most one largest index prime. The height bound and the size of a prime of \(w_q\) give
\[
     \ell\le\frac{Hq^2+1.5}{\log(2q)} .
\]

If \(\ell\equiv-1\bmod48\), supersingularity of the Gaussian CM curve gives \(\#E_6(\mathbf F_\ell)=\ell+1\) directly by pairing \(X,-X\), so \(4q\mid\ell+1\). If \(\ell\equiv1\bmod48\) and \(q\equiv3\bmod4\), the Gaussian annihilator of the order-\(q\) point \(G+(0,0)\bmod\ell\) is \((q)\), since \(q\) is inert. The Gaussian Frobenius is therefore \(1\bmod q\) and also \(1\bmod2\) by the full rational two-torsion. Its norm \(\ell=(1+2qA)^2+4q^2B^2\) is at least \(4q^2+1\), as \(B\ne0\). This contradicts the displayed upper bound. Hence the split exceptional exponents require an index prime \(q\equiv1\bmod4\), in addition to the fourth-power condition at 2.
