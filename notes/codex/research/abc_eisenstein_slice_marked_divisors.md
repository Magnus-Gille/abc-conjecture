# All the marked divisors on the elliptic square slice

Use the slice \(x^4-18x^2y^2+9y^4=-2z^2\), where \(X(nP)=-2(x/y)^2\), \(P=(-2,8)\) on \(E:Y^2=X^3+36X^2+36X\), and \(n\ge3\) is odd. Write \(Q\) for the coefficient of \(\sqrt{-3}\) in \((x+y\sqrt{-3})^{12}\) and \(F_\pm=x^4-18x^2y^2+9y^4\pm12xy(x^2-3y^2)\). The support integer \(D_n=|zF_+F_-(Q/12)(x^2+3y^2)|\) has the same radical as the associated abc triple. All its factors except \(F_+F_-\) come from ordinary or complex-multiplication indices of the original rational point. The last two quartics form one denominator norm involving one independent algebraic point. [Slice, triple, and height criterion](abc_eisenstein_twelfth_elliptic_slice.md)

Let \(E':v^2=u^3-576u\) with \(P'=(-8,-64)\), the image of \(P\) under the 2-isogeny
\[
       u=X+12+36/X,\qquad v=Y(1-36/X^2).
\]
Write \(T_j=(j,0)\) for \(j=0,24,-24\). Over \(\mathbb Q(i)\), \([i](u,v)=(-u,iv)\). Put \(h=\sqrt[4]3>0\), \(L=\mathbb Q(h)\), and define
\[
           s=-168+96\sqrt3,\qquad S=(s,8h^3s)\in E'(L).
\]
For any of the fields \(K\) below, let \(\mathfrak B_K(A)\) be the denominator ideal of \(A\in E'(K)\), with exponent \(\max(0,-v_{\mathfrak p}(u(A))/2)\) at the good primes. Let \(B'_j\) denote the usual positive rational denominator of \(jP'\), whose abscissa denominator is \((B'_j)^2\). Write \(\doteq\) for equality of positive rational numbers in every valuation \(p\ge5\). Then
\[
\boxed{D_n\doteq B'_{2n}B'_{n-1}B'_{n+1}\,
       N_{\mathbb Q(i)/\mathbb Q}\mathfrak B_{\mathbb Q(i)}
                   ([n+i]P'+T_0)\,
       N_{L/\mathbb Q}\mathfrak B_L(nP'-S).}
                                                               \tag{1}
\]
The field norms here are absolute ideal norms. The point \(S\) is outside the divisible hull of \(E'(\mathbb Q(i))\), even after adding torsion. In particular its multiples cannot be CM multiples of \(P'\) up to torsion.

## Individual factors

Set \(t=x/y\), \(w=t-3/t\); thus \(u(nP')=-2w^2\). The identities
\[
\begin{aligned}
 u&=-2(x^2-3y^2)^2/(xy)^2, \quad
 u-24=-2(x^2+3y^2)^2/(xy)^2,\quad u+24=4z^2/(xy)^2,\\
 u+8&=-2(x^2-y^2)(x^2-9y^2)/(xy)^2,\\
 u+72&=-2(x^4-42x^2y^2+9y^4)/(xy)^2,\\
 u^2+336u+576&=4F_+F_-/(xy)^4
\end{aligned}
\]
give the following denominator assignments away from 2 and 3.

| Factors | Denominator |
|---|---|
| \(y,\ x\) | On \(E\), those of \(nP,\ nP-(0,0)\), respectively, since translation sends \(X\) to \(36/X\). Their product is \(B'_n\). |
| \(\lvert x^2-3y^2|,\ x^2+3y^2,\ |z\rvert\) | On \(E'\), those of \(nP'-T_0,\ nP'-T_{24},\ nP'-T_{-24}\), respectively. Together with \(B'_n\) they give \(B'_{2n}\). |
| \(\lvert x^2-y^2\rvert\) | On \(E\), the product of the denominators of \((n-1)P,\ (n+1)P\). |
| \(\lvert x^2-9y^2\rvert\) | On \(E\), the product for \((n-1)P-(0,0),\ (n+1)P-(0,0)\), since \(X(P+(0,0))=-18\). Together these last two rows give \(B'_{n-1}B'_{n+1}\). |
| \(\lvert (x^2-6xy-3y^2)(x^2+6xy-3y^2)\rvert\) | The \(\mathbb Q(i)\)-ideal norm in (1). |
| \(\lvert F_+F_-\rvert\) | The \(L\)-ideal norm in (1). |

At a good prime the formal depth of a point specializing to the identity equals its denominator exponent. At a nonidentity affine target with unit ordinate, its abscissa difference is an étale local parameter. At a nonzero two-torsion target the abscissa difference has valuation twice the depth: the derivative of the cubic at the root is a unit and the ordinate is an étale parameter. Multiplication by two preserves formal depth, accounting for the \(B'_{2n}\) grouping. The only denominator of \(u\) comes from \(xy\), and for \(p\mid xy\) the explicitly displayed numerators of \(u\), \(u+8\), \(u+72\) and \(u^2+336u+576\) after multiplying by their own denominators are units. This yields the finite-target formulas without extraneous factors at poles.

For the quadratic pair, the points over \(u=-72\) are \(\pm[i](P'+T_0)\): translation by \(T_0\) sends \(u(P')=-8\) to \(72\), and \(v(P'+T_0)=-576\). Both points have unit ordinate at every \(p\ge5\). Their two conjugates yield the indicated ideal norm since \([i]T_0=T_0\).

For the quartics the two abscissas are \(s\) and \(576/s=-168-96\sqrt3\). Since \(s-576/s=192\sqrt3\), the ordinate of \(S\) has the required square. Its four conjugates, under \(h\mapsto\pm h,\pm ih\), are \(\pm S,\ \pm[i](S+T_0)\). All are pairwise distinct after reduction at \(p\ge5\): the difference of the two abscissas is \(192\sqrt3\), and each ordinate is a unit. The number fields used here ramify only at 2 and 3. For a fixed place of a Galois closure over a good \(p\), sum the formal depths of \(nP'\) relative to all the conjugates of the target. This sum equals the exponent in the norm of \(\mathfrak B_K(nP'-\text{target})\), since each place of \(K\) occurs with its residue degree. At most one target can contribute. The corresponding étale parameter gives exactly the valuation of the displayed polynomial in \(u\). The quadratic and quartic denominators in (1) follow. The involution \((t,z/y^2)\mapsto(-t,-z/y^2)\) fixes the original point of \(E\) and exchanges the signs in each of those pairs of polynomials; their products descend to the abscissa.

## The last point is independent

Abscissa duplication on \(E'\) gives
\[
 u(2S)=\frac{(s^2+576)^2}{4s(s^2-576)}
       =\frac{28224}{s-576/s}=49\sqrt3 .
\]
The ordinate is \(-329h^3\), either by the doubling slope or by substituting this abscissa and checking the sign at the positive real embedding. Thus \(2S=\iota_h(Q_*)\) for the rational point
\[
 Q_*=(49,-329)\in E_*:\quad Y^2=X^3-192X,\qquad
 \iota_h(X,Y)=(h^2X,h^3Y)\in E'.
\]
Indeed \(49^3-192\cdot49=329^2\), and \(h^4=3\) makes the displayed map an isomorphism. Nagell–Lutz on \(E_*\) proves \(Q_*\), hence \(S\), nontorsion: the discriminant is supported on 2 and 3, while \(329=7\cdot47\) is nonzero.

There is an automorphism over \(\mathbb Q(i,\sqrt3)\) taking \(h\) to \(-h\): \(h\) is real and lies outside the real subfield \(\mathbb Q(\sqrt3)\) of this biquadratic field. It fixes \(s\) and sends \(S\) to \(-S\). Hence if a nonzero multiple of \(S\) were a point over \(\mathbb Q(i)\) plus torsion, applying this automorphism and subtracting would make \(S\) torsion. In particular \(P',S\) are independent over \(\mathbb Z[i]\): a nonzero Gaussian multiple can be converted to an integer multiple by multiplying by its conjugate. Every isogeny and torsion translate whose kernel condition puts a marked point in the divisible hull of the rational CM orbit is therefore excluded for this quartic pair.

## The bound on ordinary lifting

Let \(A_n\) be the part prime to 6 of \(D_n/|F_+F_-|\). For \(p\ge5\) use the original index of first occurrence \(r_p=\operatorname{ord}(P\bmod p)\), \(e_p=v_p(B_{r_p})\). The first depth for \(P'\) equals \(e_p\). Indeed its order \(r'_p\) divides \(r_p\) with quotient 1 or 2, and the 2-isogeny preserves depth on the good formal group. Also \(p\nmid r'_p\), since \(4\mid\#E'(\mathbb F_p)\) and Hasse's bound gives \(\#E'(\mathbb F_p)<4p\).

If \(p\) contributes to the Gaussian norm in (1), it splits in \(\mathbb Q(i)\) and exactly one place \(\mathfrak p\mid p\) has \(Z_n=[n+i]P'+T_0\) in the formal group. One has
\[
 [2(n-i)]Z_n=[2(n^2+1)]P',\qquad
 v_{\mathfrak p}\mathfrak B(Z_n)
     = e_p+v_p(n^2+1)-v_{\mathfrak p}(n-i)
     = e_p+v_{\mathfrak p}(n+i).
\]
The rational index gives \(e_p+v_p(2(n^2+1)/r'_p)\) by the formal logarithm, an isometry on \(p\mathbb Z_p\). The Gaussian endomorphism multiplies the logarithm by its indicated scalar, as \([i]\) acts by \(i\) on the parameter \(-u/v\). For the three rational denominator factors in (1) the valuation is \(e_p+v_p(j)\) at a contributing index \(j=2n,n-1,n+1\). Their good-prime supports and the Gaussian support are disjoint by the distinct target abscissas and the unit ordinates above: the rational targets on \(E'\) are the four two-torsion points and \(\pm P'\); the Gaussian ones have \(u=-72\). Consequently
\[
 0\le \log(A_n/\operatorname{rad}A_n)
      -\sum_{p\mid A_n}(e_p-1)\log p
 \le \log\big(2n(n^2-1)(n^2+1)\big).
\]
Thus an excess of order \(n^2\) from these good primes requires first-occurrence repetitions already present on the original rational orbit. All good-prime factors outside this computation are captured by the single independent point \(S\).

## A two-orbit local restriction on the residual quartics

Suppose \(p^j\mid F_+F_-\) with \(p\ge5\). There is a degree-one place above \(p\) in \(L\) where \(nP'\equiv S\bmod p^j\); this is the local denominator statement in (1). The corresponding embedding \(L\hookrightarrow\mathbb Q_p\) gives a \(p\)-adic unit fourth root of 3. Doubling and applying the twist isomorphism yields a relation between the two rational points
\[
  [2n]P'\equiv \iota_h(Q_*)\pmod{p^j},\qquad
  \operatorname{ord}_{p^j}(Q_*)=
     \frac{\operatorname{ord}_{p^j}(P')}
          {\gcd(2n,\operatorname{ord}_{p^j}(P'))}.
\]
Orders on the two sides are taken on the respective curves with good reduction. In particular the order of \(Q_*\bmod p\) divides \(r'_p\) and is prime to \(p\). Let \(a=e_p(P')=e_p\), and let \(b\) denote the first positive denominator depth for \(Q_*\). For either point, order modulo \(p^j\) is its first order times \(p^{\max(0,j-e)}\) by the elliptic formal group. Taking \(p\)-valuations above gives
\[
       \max(0,j-b)=\max(0,j-a-v_p(n)).
\]
If \(b\ne a+v_p(n)\), this forces \(j\le\min(b,a+v_p(n))\). In particular a prime dividing the index \(n\) cannot supply a square in this quartic layer when \(Q_*\) has ordinary first depth one there. At primes ordinary for both rational points and prime to the index the equality permits larger depths.

## Prime restrictions and an example

The quadratic pair requires \(p\equiv1\bmod12\): the ordinate at \(u=-72\) requires \(i\bmod p\), and the quadratic factors in \(t\) have discriminant 48. A good prime dividing the quartic pair must have a degree-one place in \(\mathbb Q(\sqrt[4]3)\), since a rational reduction can hit only one of the four distinct conjugates. Thus 3 is a fourth power modulo \(p\). The existing restriction \(p\equiv\pm1\bmod24\) applies as these quartics divide \(U\). Together these conditions permit a set of primes of density \(3/16\). For the class \(-1\bmod24\), 3 is a square and every square is a fourth power. For \(1\bmod24\), half qualify: the splitting field \(\mathbb Q(i,\sqrt[4]3)\) has group \(D_4\), whose maximal abelian subfield is \(\mathbb Q(i,\sqrt3)\), its intersection with \(\mathbb Q(\zeta_{24})\). Of the two possible Frobenius elements that are trivial on the cyclotomic field only the identity in \(D_4\) fixes a root. Chebotarev gives the asserted density of the necessary conditions.

At \(n=3\) the parameters are \(x=11,y=3,z=46\). The good-prime parts of the first row in the table have product 11. The three individual two-torsion translates give \(47,37,23\). The neighboring rational denominators have product \(5\cdot7\); the Gaussian norm layer gives \(13\cdot73\), and the quartic norm layer gives \(1031\cdot2591\).
