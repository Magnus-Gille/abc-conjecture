# Repeated prime factors in a family of quadratic twists

Let \(E:y^2=x^3+16x^2+32x\) and \(R=(-8,16)\). For an integer \(k\) put
\[
 S=2k^2+1,\qquad H=2k^2+2k+1,\qquad J=1-2k^2,\qquad D=SH.
\]
The quadratic twist and its rational point are
\[
 E_k:Y^2=X^3+16DX^2+32D^2X,\qquad
 R_k=(-8H^2,16H^2J).
\]
At \(k=0\) they specialize to \(E,R\). Take all split prime ranks \(q>3\) in \(\mathbb Q(\sqrt{-2})\), equivalently primes \(q>3\) congruent to 1 or 3 modulo 8. At a good odd prime \(p\) consider the elementary divisibility test consisting of the following two conditions.

* The point \(R_k\bmod p\), together with its image under multiplication by \(\sqrt{-2}\), generates the full geometric \(q\)-torsion. Equivalently its annihilator as a module for the CM ring is \((q)\).
* If the reduced denominator of \(X([q]R_k)\) is \(B_{k,q}^2\), then \(p^2\mid B_{k,q}\).

Ignore primes dividing \(2D\) in this integral model. For \(k\) uniform among \(1,\ldots,T\), the proportion for which **no** pair \(q,p\) passes the test with \(p\le T^{2/3}\) tends to a constant \(d\). Its numerical enclosure is
\[
              0.9993860\ \le d\le\ 0.9994041.
\]
The limit is a theorem for this family of rational points with growing prime cutoff. It provides no density assertion about the fixed point \(R\). Indeed if \(k\ne0\), then \(D=(S+k)^2-k^2\) lies strictly between \((S+k-1)^2\) and \((S+k)^2\), so these parameters give nontrivial quadratic twists.

## Local count

Write \(f(x)=x^3+16x^2+32x\) and \(h(x)=x^2+16x+32\). On setting
\[
 t=-8-\frac{16k}{1+2k^2}=-8H/S,\qquad
 u=\frac{4(1-2k^2)}{1+2k^2},
\]
one obtains \(h(t)=-2u^2\), \(f(t)/D=(16J/S^2)^2\), and \(X(R_k)=Dt\). These identities verify the model and the coordinates. Every \(R_k\) has infinite order. At 7, \(S,H\) are units since \(-2,-1\) are nonsquares there. The CM curve has trace zero at this inert prime, as do its quadratic twists, giving order eight on reduction. The formal kernel over \(\mathbb Q_7\) is torsion-free by the formal logarithm, so rational torsion injects. Only \((0,0)\) has order two since the quadratic factor has discriminant \(128D^2\). The duplication formula shows that a half of \((0,0)\) would satisfy \(X^2=32D^2\), which is impossible over \(\mathbb Q\). The displayed point has nonzero ordinate.

All good primes in the test split in \(K=\mathbb Q(\sqrt{-2})\). In fact \(R_k\bmod p\) has odd order and hence is a double in the same group. For a model \(Y^2=X^3+a_2X^2+a_4X\) the duplication formula gives \(X(2Q)=(X(Q)^2-a_4)^2/(4Y(Q)^2)\). The nonzero abscissa \(X(R_k)=-8H^2\) must be a square. There is no loss from points with \(p\mid J\), as they have order two in good reduction. An odd prime \(p\mid D\) divides exactly one of \(S,H\). Even if the twist admits a rescaling to good reduction there, the abscissa on the untwisted model specializes to infinity when \(p\mid S\), and to the two-torsion abscissa zero when \(p\mid H\). Neither gives a nonzero preimage of a prime-to-\(p\) torsion point of odd order.

At a good split prime, Frobenius on the geometric torsion of \(E\) is given by a multiplier \(\pi\) of norm \(p\) in \(\mathcal O=\mathbb Z[\sqrt{-2}]\). Its choices up to conjugation are immaterial. Twisting can change its sign. A geometric point \(Q\) of exact CM annihilator \((q)\) has a rational abscissa if and only if Frobenius sends it to \(Q\) or \(-Q\), equivalently \(\pi\equiv\pm1\bmod q\mathcal O\). There are \((q-1)^2\) such points when this holds, since the free rank-one module \(E[q]\) is cyclic over \(\mathcal O/(q)\simeq\mathbb F_q\times\mathbb F_q\) and both components must be nonzero. Rational abscissas thus number \((q-1)^2/2\). Here \(q=p\) cannot occur: even-order reduction and the Hasse bound exclude ordinary order \(p\) at \(p\ge11\).

The rational primes satisfying the sign congruence are exactly the prime norms
\[
     p=(1+qa)^2+2q^2b^2,\qquad a\in2\mathbb Z,\quad b\ge1.
\]
For the reverse implication one uses unique factorization in \(\mathcal O\) and its two units, so every generator of a prime of norm \(p\) is the indicated one up to sign or conjugation. For a given \(p,q\), choosing congruence \(+1\) and \(b>0\) gives a unique representation. In particular \(p\ge 2q^2+1\).

Every one of the abscissas \(x\) counted above has \(x f(x)\ne0\bmod p\). The point \((x,1)\) on \(f(x)y^2=f(X)\) has the prescribed odd order. Its abscissa on the standard integral twist is \(x f(x)=x^2h(x)\), so the duplication test gives \(h(x)\) square. As \(-2\) is square at this split prime, there are two solutions \(u\) of \(h(x)=-2u^2\), both nonzero. The parametrization \(k\mapsto(t,u)\) used above is the usual line parametrization of this smooth conic through \((-8,4)\), with inverse \(k=(u-4)/(t+8)\) when \(t\ne-8\). Both preimages are unramified for the abscissa map. At \(x=-8\) they are \(k=0,\infty\), only the first of which is an integer residue. Thus the number of admissible residues of \(k\bmod p\) is
\[
 n_{p,q}=(q-1)^2-\mathbf 1_{\{\,R\bmod p\ \mathrm{has\ exact\ CM\ annihilator}\ (q)\,\}}
\]
whenever the indicated Frobenius norm condition holds, and zero otherwise. At \(x=-8\) the twist by \(f(x)=256\) is the untwisted model. At distinct \(q\), the residues counted at a fixed \(p\) are disjoint by uniqueness of the order.

Let \(\psi_q\) be the odd division polynomial on \(E\). Its roots are the distinct abscissas of the nonzero \(q\)-torsion, simple in characteristic \(p\ne q\). Good reduction and coprimality with the abscissa numerator give \(v_p(B_{k,q})=v_p(\psi_q(t(k)))\) for each residue just counted. The factors from the twist and \(S\) are local units. Because \(k\mapsto t\) is unramified at these residues, Hensel's lemma gives exactly one lift modulo \(p^2\) at each of which \(p^2\mid B_{k,q}\). Put \(n_p=\sum_q n_{p,q}\). In particular \(n_p\le p\).

## The growing cutoff

The point count and the norm representation give
\[
   \sum_{p\le X}n_p \ll
   \sum_{\substack{q\le\sqrt X\\q\ \mathrm{prime}}}
       q^2\frac{X}{q^2}
   \ll \frac{X^{3/2}}{\log(2X)}.
\]
Indeed the disk \(N(a+b\sqrt{-2})\le(\sqrt X+1)^2/q^2\) has \(O(X/q^2)\) lattice points for \(q\le\sqrt X\). Hence \(\sum_p n_p/p^2<\infty\), with tail \(O(1/(\sqrt Y\log(2Y)))\) over \(p>Y\). For fixed \(Y\), the CRT gives avoidance probability tending to \(\prod_{p\le Y}(1-n_p/p^2)\). For \(Y<p\le X\) the union of all bad residues has relative size at most
\[
    \sum_{p>Y}\frac{n_p}{p^2}+\frac{1}{T}\sum_{p\le X} n_p.
\]
At \(X=T^{2/3}\) the second term tends to zero. Sending \(Y\to\infty\) proves \(d=\prod_p(1-n_p/p^2)\). This product converges to a positive number. The least contributing prime is 683, with \(q=11\) and \(n_{683}=100\). Indeed \([11]R\bmod683=(261,239)\).

## Numerical enclosure

The [verifier](abc_cm_twist_repeat_density.py) sums the local densities at all \(q\le12000,\ d'=a^2+2b^2\le3500\) using lower rounding to \(10^{-19}\). It checks each prime norm using a deterministic primality test in the range below \(2^{64}\), and the seed term via scalar division polynomials and the proper CM factor. Counts are 104135 pairs and 228 seed incidences. A possible norm has
\[
 \frac{n_{p,q}}{p^2}\le\frac{4}{3q^2(d')^2}
\]
since \(p\ge(q\sqrt{d'}-1)^2,\ q\ge11,\ d'\ge2\). Summing over \(a=2j\) and \(b\ge1\),
\[
 \sum_{j,b}(4j^2+2b^2)^{-2}
 \le \frac{\zeta(4)}4+\frac{\pi\zeta(3)}{8\sqrt2}<\frac23
\]
by separating \(j=0\) and bounding the positive \(j\) terms by an integral. The part at \(d'>D_0\) is at most \(2/D_0\) for \(D_0\ge8\), since the lattice counting function is at most \((\sqrt z+1)\sqrt{z/2}\), followed by integration of \(2z^{-3}\). The verifier uses these two bounds, the split-prime sum of \(1/q^2\) through \(10^6\) with upward rounding, and the remainder bound \(10^{-6}\). If \([L,U]\) encloses \(\sum_p n_p/p^2\), then \(1-U\le d\le1-L+U^2/2\) by the first two union bounds in the independent residue model. All endpoint calculations in the verifier are rational.
