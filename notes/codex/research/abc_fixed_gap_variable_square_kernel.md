# A power-saving count for variable squarefree kernels at a fixed additive gap

Fix a positive integer \(a\). Let \(N_a(X,Y)\) count \(X\le b\le 2X\), \((a,b)=1\), for which \(Y\le\operatorname{sf}(b(b+a))\le2Y\), where \(\operatorname{sf}\) is the product of primes of odd valuation. For each fixed \(\theta\ge1\), there is an absolute \(c>0\) such that
\[
       N_a(X,Y)\ll_{a,\theta}Y^{1-c/(1+\theta)^2}
                         \qquad (2\le X\le Y^\theta).                  \tag{1}
\]
The constants in this argument are not uniform as \(\theta\to\infty\). A sharper concrete consequence of the same argument is
\[
  \#\{X\le b\le 2X:(a,b)=1,\ \operatorname{sf}(b(b+a))\le X^{1/2}\}
                          \ll_{a,\varepsilon}X^{6/13+\varepsilon}.       \tag{2}
\]
The proof treats arbitrary fixed primitive gaps through rational approximations to a square root, the classical uniform Thue bound, and a descent when an auxiliary form is a pure power. Diao's October 2026 preprint treats the distribution of small integral fundamental solutions, with explicit uniformity over a growing range of \(\theta\). Its quadratic approximation, factorization, and square-sieve method are closely related. The estimates below use no unproved distribution assumption. [Diao's manuscript, especially §§2 and 4](https://github.com/s6yidiao-cloud/pell-lean/blob/c54387e7d4914e2e98ae5ec4c1f004d0b862e34a/paper/main.pdf) · [Determinant argument for two nearly powerful integers](abc_short_gap_powerful_determinant.md)

## Elementary counts and the norm-one obstruction

Write \(b=u x^2\), \(b+a=v y^2\) with \(u,v\) squarefree. The primitive gap gives \((u,v)=(x,y)=1\) and \((a,uvxy)=1\). Then \(D=uv\) and
\[
              (2b+a)^2-D(2xy)^2=a^2 .                                \tag{3}
\]
For fixed \(D>1\), the number of solutions in this dyadic height window is \(O_a(1)\), independent of \(D\). Indeed \(2b+a+2xy\sqrt D\) is a totally positive algebraic integer with norm \(a^2\). Its principal ideal divides \((a^2)\) in the maximal quadratic order, giving at most \(\tau(a^2)^2\) choices. Two generators of the same ideal differ by a totally positive unit of norm one. The smallest possible such unit greater than one is at least \((3+\sqrt5)/2\), by its integral trace. The real size \((\sqrt b+\sqrt{b+a})^2\) varies by at most a factor of two as \(b\) ranges from \(X\) to \(2X\), giving at most one solution per ideal. When \(D=1\), equation (3) factors over \(\mathbf Z\) and gives only \(O_a(1)\) positive solutions altogether. Thus the direct Pell count is \(N_a(X,Y)\ll_a Y\). For \(a=1\) the multiplicity per \(D>1\) is at most one.

The norm-one element \((2b+a+2xy\sqrt D)/a\) has trace \(2+4b/a\). Since \((a,b)=1\) and \(D>1\), it is an algebraic integer precisely for \(a\mid4\). Otherwise none of its positive powers is an algebraic integer, by transitivity of integrality. Thus the existence of (3) does not directly exhibit a small integral Pell unit for an arbitrary primitive fixed gap.

A second elementary estimate is
\[
            N_a(X,Y)\ll_{a,\varepsilon}X^\varepsilon
                            (\sqrt Y+X/\sqrt Y).                        \tag{4}
\]
The integer \(w=xy\asymp_a X/\sqrt Y\) has \((w,a)=1\) and \(w^2\mid b(b+a)\). Each prime-power factor of \(w^2\) must divide one of the two coprime factors. Thus there are at most \(2^{\omega(w)}\) allowable residue classes for \(b\bmod w^2\), each containing \(O(1+X/w^2)\) integers in the window. Summing over \(w\) proves (4); if the interval for \(w\) is empty the assertion is immediate. This supplies the base case of (1) whenever \(X\le Y\).

## The auxiliary rational functions

Divide \(u,v,x,y\) into dyadic boxes; a fixed gap affects only the implied constants in size comparisons. Normalize \(s=u/v\) and \(t=y/x\) by the respective ratios of denominator and numerator box sizes, so each lies in \([1/2,2]\). For these normalized variables, \(t=f(s)+O_a(X^{-1})\) with \(f(s)=\kappa\sqrt s\) and \(\kappa\) uniformly bounded above and below on nonempty boxes. The unnormalized rational coordinates are used below when writing the auxiliary equations. The products of the first and second pairs of box sizes are respectively \(\asymp Y\) and \(\asymp_a X/\sqrt Y\).

Fix \(r\ge1\), \(m=r+1\), and take the \(2m\) columns \(s^i,s^it\), \(0\le i\le r\). A nonzero \(2m\)-row determinant has absolute value
\[
                    \gg_{a,r}Y^{-r m}(X/\sqrt Y)^{-m}.
\]
For the original rational coordinates, clearing each row by its first denominator to the power \(r\) times its second denominator yields integers. Rescaling all the columns as above introduces the first scale to the total power \(r m\) and the second scale to the total power \(m\). This gives the displayed symmetric bound in the numerator and denominator scales.

In an interval of normalized length \(H\le1\) write each row as its evaluation at \(f(s)\) plus \((t-f(s))\) times the polynomial row with zero entries in the first \(m\) columns. Expanding by error rows gives
\[
            |\det|\ll_{a,r}\sum_{j=0}^m X^{-j}H^{B_j},\quad
            B_j=\binom{2m-j}{2}+\binom{j}{2}.
\]
Indeed the smooth and error minors factor after expanding in their corresponding column subsets. Each minor on \(k\) nodes is \(O_{a,r}(H^{k(k-1)/2})\) by divided differences; pull out the error factor from each error row beforehand. More than \(m\) errors give dependent rows.

Assume \(Y\le X\le Y^\theta\). With \(t_0=\log X/\log Y\), the margin in powers of \(Y\) at \(H=Y^{-1}\) in the \(j\)-th term is
\[
  B_j-rm+m/2-t_0(m-j)=(m-j)^2+m/2-t_0(m-j)\ge m/2-\theta^2/4.
\]
Use \(m=\lceil(1+\theta)^2\rceil+1\). Since \(B_j\le2m^2\), the determinants still vanish for \(H=Y^{-1+1/(16m)}\) and sufficiently large \(Y\) for fixed \(a,m\). There are \(O(Y^{1-1/(16m)})\) cells per dyadic box. Over each cell, all points satisfy one nonzero equation of bidegree at most \((r,1)\). It has integer coefficients \(X^{O_r(1)}\) in the original rational coordinates by clearing the rows and using minors of a maximal independent subset.

A vertical or horizontal component contains \(O_a(1)\) points of a cell: fixing a reduced slope fixes its pair of integers, while the other normalized slope lies in an interval of length \(O_a(1/X)\). Its Farey spacing is the reciprocal of its pair-size product up to constants; both products are \(O_a(X)\) here. Removing such components leaves a rational graph \(y/x=P(u,v)/Q(u,v)\) of actual degree \(e\), \(1\le e\le r\). The coprime homogeneous forms \(P,Q\) of degree \(e\) have coefficients \(X^{O_r(1)}\) by the fixed-degree integer polynomial factor bound. In particular they have no common projective root. For primitive \((u,v)\), the positive gcd \(g\) of their values divides the nonzero homogeneous resultant by the two Bézout identities at \(u,v\). Thus there are \(X^{o_r(1)}\) possibilities for \(g\), and substitution yields
\[
            F(u,v)=vP(u,v)^2-uQ(u,v)^2=a g^2.                         \tag{5}
\]
For each \(g\) there are \(X^{o_r(1)}\) points unless \(F\) is a rational constant times a linear form to the power \(2e+1\). In fact \(F\) has this odd degree and is nonzero. If it has two nonproportional irreducible rational factors, their integer values are divisors of the right side after clearing the content, hence have \(X^{o_r(1)}\) possibilities. The ratio of appropriate equal-degree powers of these factors is a nonconstant rational function of \(u/v\), giving a bounded number of primitive inputs for each pair of values. If \(F\) is a power of one irreducible factor of degree at least three, apply the uniform Thue bound \(O_j(C_j^{1+\omega(|h|)})\) for primitive solutions of an irreducible degree-\(j\) binary form with fixed nonzero right side \(h\). Here \(|h|\le X^{O_{a,r}(1)}\) and \(j\) is fixed. The odd degree excludes a pure power of an irreducible quadratic. E. Bombieri and W. M. Schmidt, *On Thue's equation*, Invent. Math. 88 (1987), 69–81.

## The pure powers give shorter solutions with the same squarefree kernel

If \(F=cL^{2e+1}\), its only projective zero cannot be zero or infinity. At zero a root would require \(P(0,1)=0\) and \(Q(0,1)\ne0\), giving a simple root of \(F\), whereas \(2e+1\ge3\). Infinity is symmetric. At the sole root \((u:v)=(w^2:1)\), the number \(w=P(u,v)/Q(u,v)\) is rational and nonzero. Write \(|w|=h/k\) in positive lowest terms and set \(d=2e+1\). In \(\mathbf Q[z]\) the two factors
\[
        P(z^2,1)+zQ(z^2,1),\qquad P(z^2,1)-zQ(z^2,1)
\]
are coprime: any common root would give a common projective root of \(P,Q\) or the excluded root zero of \(F\). Their product is a constant times \((z-w)^d(z+w)^d\). They are exchanged by \(z\mapsto-z\), so each is a constant times one of \((z-w)^d,(z+w)^d\). Taking their even and odd parts and homogenizing shows that the absolute values of the reduced ratio \(P/Q\) are furnished by the following two integer forms evaluated at \((u,v)\):
\[
   (h\sqrt v+k\sqrt u)^d=\sqrt v\,P_*+\sqrt u\,Q_*.
\]
Here \(P_*\) and \(Q_*\) are the positive even- and odd-index binomial sums, with factors \(\sqrt v,\sqrt u\) removed. More explicitly
\[
 P_*=h\sum_{j=0}^{e}\binom d{2j}A^{e-j}B^j,\qquad
 Q_*=k\sum_{j=0}^{e}\binom d{2j+1}A^{e-j}B^j,\qquad
 A=h^2v,\quad B=k^2u .
\]
Thus \(y=P_*/g_*\), \(x=Q_*/g_*\) where \(g_*=\gcd(P_*,Q_*)\), by primitivity. Multiplying by the conjugate binomial expression gives the exact identity
\[
                  a g_*^2=(A-B)^d.                                    \tag{6}
\]
In particular \(a'=A-B>0\). The integers \(A,B\) are coprime. Indeed \((h,k)=(u,v)=1\). If \(p\mid h,u\), then \(v_p(A-B)=1\) because \(u\) is squarefree while \(p^2\mid A\). The odd \(d\) in (6) forces \(p\mid a\), contrary to \((a,u)=1\). The same proof excludes \(p\mid k,v\). Consequently \(a'\) is prime to \(hkuv\). For an odd \(p\mid a'\), reducing the binomial sums at \(A=B\) gives \(P_*\equiv h 2^{d-1}A^e\not\equiv0\pmod p\) and the analogous formula for \(Q_*\). Every odd prime of \(g_*\) would divide \(a'\) by (6), so \(g_*\) is a power of two. If \(v_2(a')\ge d\), the same substitution modulo \(2^d\) gives \(v_2(g_*)=d-1\) since \(A,h,k\) are then odd. Otherwise (6) bounds \(2v_2(g_*)\le d(d-1)\). Thus \(g_*\ll_r1\) and \(a'\ll_{a,r}1\).

Taking the positive binomial sum yields
\[
      (\sqrt A+\sqrt B)^d=g_*(\sqrt{b+a}+\sqrt b)\asymp_{a,r}\sqrt X.
\]
Therefore \(A,B\) form a primitive pair of bounded positive gap at heights \(O_{a,r}(X^{1/d})\), with \(\operatorname{sf}(AB)=uv=D\). This statement holds over all auxiliary cells with no dependence on their coefficients. To count original triples admitting such a shorter pair, count all shorter pairs for the finite list of possible gaps and degrees, then use \(O_a(1)\) original triples per fixed \(D\) in the dyadic window by (3). In particular all pure-power cases combined contribute \(O_{a,r}(X^{1/3})\) by simply counting the possible shorter integers and bounded gaps.

## Completing the estimates

For (1), at every nonexceptional cell use (5), absorbing all subpower counts and logarithmic box factors to obtain \(O_{a,\theta}(Y^{1-1/(32m)})\) in total for large \(Y\). For exceptional points recurse on the shorter height with the same dyadic kernel and one of the bounded new gaps. Indeed \(X'\ll_{a,r} X^{1/3}\) is at most \(Y^{\theta/2}\) for all sufficiently large \(Y\) at any fixed current exponent \(\theta\ge1\). A finite number of dyadic shorter windows or \(O(\log X)\) windows both suffice. In fact (6) and bounded \(a',g_*\) give \(A,B\asymp_{a,r} X^{1/d}\) for large \(X\), so only boundedly many dyadic windows are needed per degree. Retain the original \(m\) and exponent \(1/(32m)\) at all steps (the width estimates improve as the height exponent falls). The recursion has bounded depth in terms of \(\theta\), with finitely many fixed possible gaps at each step. At \(X'\le Y\) use (4), with exponent margin. Constants or bounded small values of \(Y\) are harmless. This proves (1).

For (2), use \(r=3,m=4\). In any dyadic kernel box with \(Y\le X^{1/2}\) the reciprocal of the nonzero determinant bound is \(\ll_a X^9\): it equals \(Y^{12}(X/\sqrt Y)^4=X^4Y^{10}\). The exponents \(B_j\) are \(28,21,16,13,12\). For \(H\) a sufficiently small constant times \(X^{-6/13}\), each \(X^{-j}H^{B_j}\) is smaller than the determinant threshold with the required fixed constant; the limiting term is \(j=3\). The generic cells and dyadic subdivisions cost \(O_{a,\varepsilon}(X^{6/13+\varepsilon})\), and all pure powers cost \(O_a(X^{1/3})\) by the shorter-pair count. This proves (2). Directly for \(Y\le X^{1/2+\eta}\), the limiting exponents are \(\max_{0\le j\le4}(9+10\eta-j)/B_j\); this records the short extension past the square-root cutoff.

For comparison, bounded-gap high-quality triples of radical at most \(R\asymp X^{1-\delta}\) have elementary count \(\ll X^\varepsilon\sqrt R\) by choosing the less costly radical of the two large terms. Estimate (2) improves this for triples whose product of odd-valuation primes is at most \(X^{1/2}\) whenever \(\delta<1/13\). Estimate (1) strictly improves the corresponding count of the smaller-kernel subfamily \(D\le R^{1/2}\) for every fixed \(0<\delta<1\), by first counting smaller \(D\) with (3). The complementary regime with larger squarefree kernel and a small radical coming from primes repeated in the square parts remains open to this method.

## Which gaps can have a pure-power auxiliary component?

The descent identity (6) and the fact that \(g_*\) is a power of two show precisely that the odd part of \(a\) is the \(d\)-th power of the odd part of \(a'\). In particular a fixed gap with an odd prime to exponent one never has such a component at a contributing point. More generally if \(a\) has odd part greater than one, the product of the successive odd descent degrees divides the gcd of the valuations of the odd primes in \(a\). Thus the depth needed for these gaps can also be bounded solely in terms of \(a\).

## A square-root obstruction over varying kernels

For gap one, every fixed positive integer \(z\) gives arbitrarily large paired dyadic windows with \(X\asymp_z Y^{z/2}\) and at least \(\gg_z\sqrt Y\) distinct kernels at those heights. Choose integers \(t\) in \([T,(1+\rho)T]\), with fixed \(\rho>0\) small enough in terms of \(z\), for which \(t\) and \(t+1\) are squarefree. A positive proportion qualify: the union count for prime squares costs at most \(2\rho T\sum_p p^{-2}+O(\sqrt T)\), while \(\sum_p p^{-2}\le 1/4+\sum_{j\ge3,\ j\text{ odd}}j^{-2}=\pi^2/8-3/4<1/2\). Set \(D=t(t+1)\) and write
\[
       (2t+1+2\sqrt D)^z=T_z+W_z\sqrt D.
\]
The norm is one, \(T_z\) is odd and \(W_z\) even. Thus \(b=(T_z-1)/2\) gives \(b(b+1)=D(W_z/2)^2\). The distinct squarefree \(D\) have size \(\asymp T^2\), and \(b\sim 4^{z-1}t^z\), so taking small \(\rho\) and suitable dyadic windows gives the claim. In particular a universal upper bound with exponent strictly smaller than \(1/2\) in \(Y\) is impossible. These are lower bounds for the small-kernel counting problem; the construction by itself gives no fixed positive saving in the complete radical.
