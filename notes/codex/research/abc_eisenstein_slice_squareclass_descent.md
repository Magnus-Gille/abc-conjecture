# Two forced odd exponents and the least possible squarefree kernel

Take the [fixed elliptic orbit](abc_eisenstein_twelfth_elliptic_slice.md) at an odd index \(n\ge3\). Thus \(P=(-2,8)\) on \(Y^2=X^3+36X^2+36X\), \(X(nP)=-2(x/y)^2\), \(x,y\) are coprime positive odd integers, \(3\nmid x\), and \(x^4-18x^2y^2+9y^4=-2z^2\). Set
\[
 F_0=x^4-18x^2y^2+9y^4,\quad F_\pm=F_0\pm12xy(x^2-3y^2),
 \quad J_n=|F_+F_-|/512 .
\]
For a positive integer \(m\), write \(\operatorname{sf}(m)=\prod_{v_p(m)\ {\rm odd}}p\). This is the unique squarefree numerator in \(m=\operatorname{sf}(m)r^2\).

On this orbit the exact minimum of \(\operatorname{sf}(J_n)\) is \(2{,}671{,}321=1031\cdot2591\). Each quartic contributes a separate prime of odd exponent at every index. The proof below first establishes the assertion for each factor and then explains the finite sieve for the sharp minimum.

## Signed squarefree parts

The 2-adic valuations of \(F_+,F_-\) are 4 and 5, in either order. This follows by evaluating the two quartics at odd \(x/y\bmod64\); they are homogeneous of degree four and \(y\) is odd. Both are \(1\bmod3\). Denote the factor of valuation \(j\) by \(F_j\), and write
\[
 F_0=-8s^2,\qquad F_4=16k t^2,\qquad F_5=32l u^2,\qquad
 W=(x^2+3y^2)/4 .
\]
Here \(s=|z|/2\), and \(k,l\) are signed squarefree integers. All of \(s,t,u,W\) are odd. At \(p>3\) no two of \(F_0,F_+,F_-\) have a common zero at a primitive pair: a common zero would have \(p\mid xy(x^2-3y^2)\), and then the other factor is a unit (in the last case \(F_0=-36y^4\bmod p\)). No such prime divides both \(x^2+3y^2\) and \(F_0\), since \(F_0\equiv72y^4\) when \(x^2=-3y^2\). In particular \((s,W)=1\). The signs are fixed by reduction modulo 3: \(k\equiv1\bmod3,\ l\equiv-1\bmod3\). Write \(d_4=|k|,\ d_5=|l|\). Then \((d_4,d_5)=1\) and \(\operatorname{sf}(J_n)=d_4d_5\).

Writing out the norm of \((x+y\sqrt{-3})^4\), and using \(F_4+F_5=2F_0\), gives
\[
 s^2+kt^2+2lu^2=0,\qquad
 3W^4=s^4+ks^2t^2+k^2t^4=s^4+2ls^2u^2+4l^2u^4.       \tag{1}
\]
For example \(3(x^2+3y^2)^4=4F_0^2-2F_0F_4+F_4^2\), which gives the first quartic identity after division by \(256\).

## Why \(d_4>1\)

If \(d_4=1\), its sign forces \(k=1\). With \(r=s/t,\ w=W^2/t^2\), equation (1) gives \(3w^2=r^4+r^2+1\). Consequently \((3r^2,9rw)\) is a rational point with nonzero ordinate on
\[
             E_1:\quad Y^2=X^3+3X^2+9X.
\]
Its only such points are \((3,\pm9)\). Here is an elementary verification. In the rational 2-isogeny descent for \(Y^2=X^3+aX^2+cX\), the squareclass map takes an ordinary point to \([X]\) and \((0,0)\) to \([c]\). Its image is supported on the sign and primes of \(c\). A squarefree representative \(b\) requires a primitive solution \(V^2=bR^4+aR^2T^2+(c/b)T^4\), including the two torsion/identity cases by allowing zero coordinates. The product of the image sizes for the two isogenous curves is \(4\cdot2^{\operatorname{rank}}\).

For \(E_1\), positivity and the point \((3,9)\) give the image \(\{1,3\}\). The other curve has \(a=-6,\ c=-27\); its image contains \(\{1,-3\}\). To exclude the other coset it suffices to exclude \(-1\). The equation would be \(V^2=-R^4-6R^2T^2+27T^4\). Modulo 3 this forces \(3\mid R\). With \(R=3R'\) the right side has valuation exactly 3, since \(3\nmid T\) and \(T^4-2R'^2T^2-3R'^4\ne0\bmod3\). Thus the rank is zero. The group orders at the good primes 5 and 7 are respectively 4 and 8, bounding the rational torsion order by 4. The four displayed points, counting \(O,(0,0)\), exhaust it.

It follows that \(s=t\), hence \(W=s\). Since \((s,W)=1\), this requires \(W=1\). But \(x^2+3y^2=4\) gives \(x=y=1\) and \(nP=\pm P\), impossible for \(n\ge3\) since \(P\) is nontorsion. This proves \(d_4>1\).

## Why \(d_5>1\)

The substitutions \(M_\pm(x,y)=(-x\mp3y,\ \pm x-y)\) satisfy \(F_0(M_\pm)=-8F_\pm\). On the given orbit neither coordinate vanishes: \(x=y\) is excluded above and \(x=3y\) would contradict \(3\nmid x\). Rotating the factor \(F_5\) therefore gives a nonzero finite rational slope \(r\) with
\[
                 r^4-18r^2+9=bv^2,\qquad b=-l,\quad v\ne0.
\]
The point \((A,B)=(br^2,b^2rv)\) lies on \(B^2=A^3-18bA^2+9b^2A\). Its 2-isogenous image, after scaling, has coordinates
\[
        \left(\frac{(A-3b)^2}{4A},\,\frac{B(1-9b^2/A^2)}8\right)
        \quad\text{on}\quad Y^2=X^3-(3b)^2X .
\]
Its ordinate is nonzero, since \(r^2\ne\pm3\) for a finite nonzero rational \(r\). Thus \(3d_5\) is a congruent number (the area of a rational right triangle). The identical calculation with \(F_4\) gives the separate necessity that \(6d_4\) is a congruent number.

In particular \(d_5\ne1\): on \(Y^2=X^3-9X\) the only rational points are its four 2-torsion points including the identity. For completeness, its 2-descent image is all of \(\{1,-1,3,-3\}\) from torsion. The 2-isogenous curve is \(Y^2=X^3+36X\); its only possible classes are \(1,2,3,6\). For \(b=2\) the equation \(V^2=2R^4+18T^4\) forces \(3\mid R,V\), and then \(3\mid T\) after division by 9. For \(b=3,6\) the valuation at 3 of the right side is exactly one for any primitive pair, as the fourth powers are 0 or 1 modulo 3. Thus the rank is zero, and the group orders 4 and 8 at 5 and 7 again bound rational torsion by 4.

## Finite certificate for the minimum

For odd \(n\), the 2-isogenous image \(Q=(-8,-64)\) of \(P\) lies on \(v^2=w^3-576w\). Direct substitution gives
\[
            w(nQ)^2+336w(nQ)+576=4F_+F_-/(xy)^4 .
\]
At \(p>3\) dividing \(F_+F_-\), the denominator \(xy\) is a unit. Thus a necessary condition on \(p\) is that an odd multiple of \(Q\) hit one of these abscissas modulo \(p\). It can be checked over a complete period of the point in the finite group. The three least primes passing are \(167,191,263\). Their product is \(8{,}388{,}911\). Hence for \(d_4d_5\le2{,}671{,}321\) the two nontrivial coprime kernels must each be prime, and the larger is at most \(\lfloor2{,}671{,}321/167\rfloor=15{,}995\).

Exhausting the relevant primes up to \(15{,}995\) gives 218 candidate pairs and 436 ordered assignments. For each of these, reduce \(F_0,F_+,F_-\) on \(\mathbf P^1(\mathbf F_\ell)\) for auxiliary primes \(5\le\ell\le53\). Their respective values must be \(-8,16k,32l\) times squares, with zeros permitted. The assignment of the two signs \(+\) and \(-\) can be fixed in this projective test since changing the sign of \(x\) exchanges them. Projective rescaling multiplies quartic values by a fourth power. After the tests only \((d_4,d_5)=(2591,1031)\) remains. At \(n=3\) one has \((x,y)=(11,3)\), \(F_+=32\cdot1031,\ F_-=-16\cdot2591\). The individual minima are also \(d_4=2591\) and \(d_5=1031\), by checking each candidate prime below the corresponding bound against the odd point orbits at auxiliary primes. These results do not establish uniqueness of the attaining index. [Finite-field exclusions](abc_eisenstein_slice_squareclass_census.md) · [Individual minimum verifier](abc_eisenstein_slice_individual_minima.py) · [Independent indexed proof and verifier](abc_eisenstein_slice_squareclass_min.md)

Thus if \(D^2\mid J_n\), the complementary factor \(J_n/D^2\) is at least \(2{,}671{,}321\). The bound on that factor is constant. A prime with square dividing a quartic factor can still be a fixed power of the triple height.

## Quadratic reciprocity for the odd-exponent primes

Here is a separate obstruction which applies at arbitrarily large kernels. Order the distinct primes of \(d=d_4d_5\) as \(p_1,\ldots,p_h\). All are \(1\) or \(-1\bmod24\), since they divide the square root of the square entry in the twelfth-power triple. Equivalently, reduction of the ratio of the Eisenstein parameter to its conjugate at a prime in the real part gives an element of the norm-one group whose twelfth power is \(-1\). The order has exact 2-part 8 and the group order is \(p-(\frac{-3}{p})\).

Put \(u_i=1\) for \(p_i\equiv-1\bmod24\) and \(0\) otherwise. Form a matrix \(L\) over \(\mathbf F_2\) with off-diagonal entry \(L_{ij}=1\) when \((p_i/p_j)=-1\) (Legendre symbol), zero otherwise; set the diagonal entries so that the row sums vanish. There must be a vector \(v\notin\{0,\mathbf 1\}\) with
\[
                (L+\operatorname{diag}(u_1,\ldots,u_h))v=0.       \tag{2}
\]
Specifically \(v_i=1\) marks \(p_i\mid d_5\). To prove this let \(p_i^*=(-1)^{u_i}p_i\), so that \(k=\prod_{p_i\mid d_4}p_i^*\) and \(l=-\prod_{p_i\mid d_5}p_i^*\). The signs follow from reduction modulo 3. At \(p_i\mid d_4\), (1) gives \((-2l/p_i)=1\); at \(p_i\mid d_5\) it gives \((-k/p_i)=1\), since the other two terms in the equation are units there. Now \((2/p_i)=1\) and \((p_j^*/p_i)=(p_i/p_j)\). The crossing sum in row \(i\) of \(Lv\) is therefore \(0\) for \(v_i=0\), and \(u_i\) for \(v_i=1\). This proves (2).

In particular, if all \(p_i\equiv1\bmod24\), draw an undirected edge between quadratic nonresidues of each other. Every vertex must have an even number of edges crossing the nontrivial partition into \(d_4,d_5\). Any graph with an odd number of spanning trees is impossible, by the matrix-tree theorem applied to a reduced Laplacian modulo 2. For example, if \(d\) has just two such prime factors, they must be quadratic residues of each other.

There are arbitrarily large excluded configurations of every length \(h\ge2\) even if the prime factors also pass the individual test that 3 be a fourth power modulo each \(p_i\). For any previously chosen primes, the field \(K_0=\mathbf Q(\zeta_{24},3^{1/4})\) is unramified at each \(p_i\); by their distinct odd valuations the classes of the \(p_i\) are independent modulo squares in \(K_0\). Chebotarev therefore allows any prescribed edges from a new prime splitting in \(K_0\). In the iterated relative prime density where the primes are chosen successively subject to splitting in \(K_0\), every labeled graph has the same probability.

For such \(h\)-tuples, the proportion excluded by the graph test alone is
\[
        \prod_{j=1}^{\lceil(h-1)/2\rceil}(1-2^{1-2j}).
\]
Indeed the reduced Laplacian is uniformly distributed among symmetric \((h-1)\)-by-\((h-1)\) matrices over \(\mathbf F_2\): the edges to the deleted vertex determine its diagonal after fixing the other edges. The nonsingularity probabilities satisfy \(P_0=1,\ P_1=1/2,\ P_m=P_{m-1}/2+(1-2^{-(m-1)})P_{m-2}/2\). For first diagonal entry 1, pivot there. For first diagonal 0, a nonzero off-diagonal row allows a nonsingular two-by-two pivot after a change of basis in the remaining coordinates. In both cases the Schur complement is uniformly symmetric. This gives the product by induction. This density is for proposed prime tuples; no distribution of the actual orbit is assumed.

## Additional rational points forced by the kernels

The three congruent numbers forced by this orbit are \(6d_4,\ 3d_5,\ 3d_4d_5\). For the third, the full twelfth-power real coefficient has absolute value \(U=d_4d_5(stu)^2\), by its factorization and \(F_0=-8s^2\). Thus \(1-d^2a^4=3b^2\) with \(a=stu/W^3,\ b=V/W^6\). The point \((-3d^2a^2,9d^2ab)\) lies on \(Y^2=X^3-(3d)^2X\) and has nonzero ordinate.

There are three further positive-rank twist conditions on a curve with different \(j\)-invariant. In (1) the quantities \(A=s^2,\ B=kt^2,\ C=2lu^2\) satisfy \(A+B+C=0\), so \(A^2+AB+B^2=3W^4\) for any pair among the three. Write the chosen pair as \(d_a a^2,d_b b^2\) and set \(D=d_a d_b\). The point
\[
 \left(3d_a^2a^2/b^2,\,9d_a^2 a W^2/b^3\right)
 \quad\text{lies on}\quad
         Y^2=X^3+3DX^2+9D^2X .
\]
It is nontorsion in each of the cases \(D=k,2l,2kl\). At 5 and 7 the good reductions have orders 4 or 8 at 5 and 8 at 7, using the quadratic twists of \(E_1\). Rational torsion is thus a 2-group. There is only one rational nonidentity 2-torsion point, \((0,0)\). A point halving it must have abscissa \(\pm3D\) by duplication, requiring \(81D^3\) or \(-27D^3\) to be a square, respectively. The allowed \(D\) are squarefree, have absolute value greater than one, and are prime to 3. This excludes order four and proves the assertion.

There is also a rank-two requirement on the whole squarefree kernel \(d=d_4d_5\):
\[
             \operatorname{rank}\{Y^2=X^3-12d^2X\}(\mathbf Q)\ \ge 2 .
\]
To see it, put \(D=2kl\). The three numbers \(A,B,C\) above are the roots of \(Z^3-3W^4Z-D(stu)^2=0\). For each root \(Z\) this gives the point \((DZ/W^2,D^2stu/W^3)\) on \(Y^2=X^3-3D^2X\). Their abscissa squareclasses are \(2kl,2l,k\). The rational torsion consists of \(O,(0,0)\): the good reductions at 7 and 11 have sizes 8 and 12 by the quadratic character cancellation under \(X\mapsto-X\). There is only one rational nonidentity point of order two, and a half of it would require \(X^2=-3D^2\). Its class under the 2-descent map is \(-3\). The classes \(k,2l\) are independent modulo that class, since \(d_4,d_5>1\) are coprime odd squarefree integers prime to 3. Their two points are therefore independent modulo twice the group and rational torsion, proving the lower bound.

## Growth needed for abc

On this one orbit \(\log J_n=8\widehat h(P)n^2+o(n^2)\). If its squarefree kernel fell below \(\exp((8\widehat h(P)-\delta)n^2)\) infinitely often for some \(\delta>0\), the largest square dividing \(J_n\) would give a fixed positive exponent of radical gain in the associated primitive abc triples. This follows from \(J_n=dq^2\), \(J_n/\operatorname{rad}(J_n)\ge q\), and the [pointwise triple estimate](abc_eisenstein_twelfth_elliptic_slice.md). The sharp absolute minimum alone places no such restriction on the limiting exponential rate.
