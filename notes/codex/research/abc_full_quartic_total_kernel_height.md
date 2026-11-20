# Effective height bounds from the squarefree part of the four-coordinate product

Write \(E:y^2=x^3-36x\), \(G=(-3,9)\), \(C_n=4w_n^4\), and \(\Delta_n=\operatorname{sf}(a_nw_nc_nd_n)\) at positive odd indices. Here \(\operatorname{sf}\) means the product of primes of odd valuation. The [parametrization](abc_full_quartic_signature.md) gives pairwise coprime positive odd coordinates, \(a_n^2+c_n^2=2w_n^2\), \(a_n^2+2w_n^2=3d_n^2\), and
\[
                x(nG)=-3a_n^2/w_n^2,\qquad |y(nG)|=9a_nc_nd_n/w_n^3.
\]
The following bounds use \(h=\max_{q\mid n}v_q(n)\) for \(n>1\).

* \(4^{\omega(n)}\operatorname{rad}(n)<\Delta_n\), with no exceptional indices. In particular \(\log C_n\le 2.08(\Delta_n/4^{\omega(n)})^{2h}+O(1)\), effectively. The exponent is two on squarefree indices.
* \(\operatorname{rad}(n)^3\ll\Delta_n\) with a fixed, unevaluated constant. Thus \(\log C_n\ll_h\Delta_n^{2h/3}\) at bounded multiplicity, in particular \(\log C_n\ll\Delta_n^{2/3}\) on squarefree indices.
* At unrestricted positive odd indices, \(\log C_n\le\exp(O(\Delta_n^L\log(2\Delta_n)))\) effectively, where \(L\) is an admissible effective absolute exponent in Linnik's least-prime theorem. Using just \(D_n=\operatorname{sf}(w_n)\) gives \(\log C_n\le\exp(O(D_n^{2L+1}))\).

## A single plane quartic for the total squareclass

Write \(a_nw_nc_nd_n=\Delta_n b^2\). Then
\[
                    |y(nG)|=\Delta_n(3b/w_n^2)^2.
\]
Use the sign of the multiple giving positive ordinate. Its abscissa and the positive rational square root of its ordinate divided by \(\Delta_n\) give a point on the plane quartic
\[
           \mathscr C_\Delta:\quad
              \Delta^2 Z^4=UV(U-6V)(U+6V).
\]
Explicit projective coordinates are \((U:V:Z)=(-3a_n^2:w_n^2:3b)\). It is a smooth genus-three curve. Over \(\mathbf Q(\sqrt\Delta)\), scaling \(Z\) identifies it with the fixed curve \(\mathscr C_1\). Over \(\mathbf Q(i)\) the equality becomes
\[
                (U+6iV)^4-(U-6iV)^4=48i\Delta^2 Z^4.
\]
These formulas exhibit a diagonal quartic with an explicit quadratic twisting field and good reduction outside \(6\Delta\). A rational point need not give an integral point on the affine chart \(V=1\) outside those primes: the denominators there include the full \(w_n^2\), whose even valuations do not enter \(\Delta\). Knowing the bad reduction of this fixed twist bounds the arithmetic height of its coefficients. An effective height for its varying rational point requires additional information.

## Two effective witnesses at every prime index

For each odd prime \(q\), \(w_q\) is nonsquare by the [square classification](abc_full_quartic_square_classification.md). Also \(a_q,c_q\) cannot both be squares. Indeed a simultaneous square gives \(u^4+v^4=2w_q^2\). The smooth curve \(S^2=2t^4+2\) has rational points \((t,S)=(\pm1,\pm2)\); its Jacobian is \(y^2=x^3-16x\), from the binary-even-quartic Jacobian formula. This is isomorphic over \(\mathbf Q\) to \(y^2=x^3-x\). Its rank is zero by Fermat's theorem that 1 is not a congruent number. The torsion order is four, as shown by good reduction at 3 and 7 with group orders 4 and 8 and the full rational two-torsion. Therefore the four displayed points exhaust the genus-one curve. Taking \(t=u/v\), \(S=2w_q/v^2\) gives \(u=v\) and by primitivity \(a_q=c_q=w_q=1\), excluded for \(q>1\).

Choose one prime of odd depth from \(w_q\) and one from the nonsquare coordinate among \(a_q,c_q\). Both are good, since these three coordinates are prime to 6, and they are distinct by pairwise coprimality. For each chosen \(p\) the corresponding integral translate \(G+T\) has exact order \(q\) modulo \(p\). Full rational two-torsion and Hasse give \(p\ge(2\sqrt q-1)^2>2q\). The scalar order of \(G\) is either \(q\) or \(2q\), so \(p\) determines its unique parent \(q\). An edge from an index prime \(q\mid n\) to a child \(p\nmid n\) gives a prime of \(\Delta_n\), as the odd formal depth is unchanged under multiplication by \(n/q\). Multiply the two child inequalities over all \(q\mid n\). The internal children contribute at most \(\operatorname{rad}(n)\), and the external children contribute at most \(\Delta_n\), since no child occurs twice. This gives \(4^{\omega(n)}\operatorname{rad}(n)^2<\operatorname{rad}(n)\Delta_n\) as claimed. The height bound follows from \(n\le\operatorname{rad}(n)^h\), \(H=\widehat h(G)<0.52\), and \(\log C_n=4Hn^2+O(1)\) with an effective bounded error on the compact real component.

At all sufficiently large prime indices, each of the four coordinates has a prime \(p>3\) of odd depth. Indeed for each coordinate the cases of squarefree part 1 and 3 give points on finitely many fixed smooth genus-three curves, hence occur at finitely many indices. [Four individual curves and point recovery](abc_full_quartic_four_squarefree_parts.md) The four choices now give four distinct children of \(q\). Restrict the preceding product argument to the primes above the fixed exceptional cutoff. Their children are all above that cutoff as well. Dividing out the internal children proves \(\prod_{q\mid n,q>q_0}q^3\le\Delta_n\). The omitted prime product is an absolute constant. This last argument does not compute it.

## A prime-power projection and an effective bound for unrestricted indices

Fix \(q^j\mid n\). Then
\[
          \operatorname{sf}(w_{q^j})\le D_n,\qquad
          \Delta_{q^j}/\gcd(3,\Delta_{q^j})\le\Delta_n.                 \tag{1}
\]
For each prime \(p\) in the product on the left, start at \(p\). It is good and its scalar order is \(q^i\) or \(2q^i\) for some \(1\le i\le j\), since every translate \(G+T\) is integral and its reduction has nontrivial odd order dividing \(q^j\). In particular \(p>2q\). For the first inequality use only the \(w\) coordinate. If the initial odd depth disappears at \(n\), the formal group forces \(p\mid n\). Fix for every odd prime \(u\) a witness \(f(u)\) of odd depth in \(w_u\), with scalar rank \(u\) and \(f(u)>2u\). From any lost initial prime go to \(f(p)\); if that odd depth also fails to survive, then \(f(p)\mid n\), and continue. Each path strictly increases and terminates at a prime in the final kernel. Distinct starting primes have disjoint paths. The map \(f\) is injective by exact scalar rank. If one start were downstream of another, its immediately preceding vertex would have to be the scalar order of the downstream start, which is prime only when that order is \(q\). Every vertex is already larger than \(2q\). This proves (1) by multiplying the distinct terminal inequalities. These inequalities compare numerical sizes even when the sets of prime divisors change.

Apply (1) at \(j=1\) and write \(D_q=\operatorname{sf}(w_q)\). For every \(q\mid n\), \(1<D_q\le D_n\), and the largest prime factor of \(n\) is smaller than \(D_n/2\) by its surviving first-level witness. All primes in \(D_q\) are \(1\bmod 12\) and exceed \(2q\). Choose a reduced class modulo \(4qD_q\) that is \(3\bmod4\), \(1\bmod q\), and a quadratic nonresidue at exactly one prime dividing \(D_q\). Linnik gives a prime \(s\ll(4qD_q)^L\ll D_n^{2L}\) in that class. The [periodic prime-power character construction](abc_full_quartic_effective_prime_support.md) then detects a new odd-depth prime at exact rank \(q^k\) whenever \(k\equiv1\bmod t_q\), where one may take \(t_q=\operatorname{ord}_{s+1}(q)\le s+1\). Indeed the curves have group order \(s+1\) and the denominator characters at 1 and \(q\) differ. The Hasse bound puts that witness above \(2q^k\). Choose the first such \(k\) with \(2q^k>D_n\); (1) would fail if \(q^k\mid n\). Thus
\[
     v_q(n)< t_q+1+\log(2D_n)/\log q\ll D_n^{2L}.
\]
Since \(\log\operatorname{rad}(n)\le\sum_{q\le D_n}\log q\ll D_n\), this proves the effective unrestricted estimate. In the [exact inverse census](abc_full_quartic_inverse_kernel_sieve.md) the test at prime indices can now discard \(q\) whenever \(D_q>Y\), immediately after stripping primes through \(Y\) and square-testing the remainder. Its deterministic running time improves to \(\exp(O(Y^{2L+1}))\) bit operations. The full total-kernel census can enumerate the same candidate indices using \(D_n\le\Delta_n\), compute all four coordinates, strip their product through \(Y\), and test its remaining square and resulting small-prime kernel.

### An effective improvement using two of the four squareclasses

In the total product one can improve the unconditional estimate to
\[
                 \log C_n\le\exp\!\big(O(\Delta_n^{L}\log(2\Delta_n))\big).
\]
For a fixed \(q\mid n\), choose the smaller kernel \(d\) of the two nonsquare coordinates guaranteed above at \(q\): \(w_q\) and a nonsquare among \(a_q,c_q\). The two underlying squarefree integers are coprime and their product is at most \(\Delta_n\) by the disjoint-path argument for (1). Each contains a good prime above \(2q\), so \(qd<d^2/2\le\Delta_n/2\). Write \(F\) for the coordinate chosen.

Fix \(h_0=7\); none of the four odd-index coordinates is divisible by 7. Choose an auxiliary prime \(h\equiv7\bmod24\), \(h\equiv1\bmod q\), with \((d/h)=-(d/7)\). The first congruence already gives \(1\bmod3\) when \(q=3\), and every prime divisor of \(d\) is above \(2q\) and prime to 6. At any such prime the Legendre value of \(h\) can be freely chosen by CRT; quadratic reciprocity has a fixed sign because \(h\equiv3\bmod4\). Linnik gives \(h\ll (24qd)^L\ll\Delta_n^L\).

At positive odd \(j\) the paired character
\[
                     J_F(j)=(F_j/7)(F_j/h)
\]
depends only on \(j\bmod U\), \(U=2\operatorname{lcm}(8,h+1)\). For \(w\) use the isogenous-curve character at both places. For \(a,c\) the [four-coordinate sign formula](abc_full_quartic_four_arm_inverse_sieve.md) writes \(F_j/w_j\) up to one rational sign as a fixed rational function of \([(j-1)/2]G\); its reduction then depends on that point. The rational sign cancels between the two primes because both are \(3\bmod4\). All the rational functions are units on the encountered residues at these primes, including 7. For precision, the squared function is \((x(G+2Q)-e)/(x(G)-e)\), with \(e=0,-6,6\) and \(x(G)-e\) a unit at every \(p\ge5\). At an encountered reduced point the numerator is finite and nonzero, since all four coordinates there are units. In the normal local ring of the good integral model, a rational square root of this unit and its inverse are integral, hence units themselves. Both primes are supersingular, giving the asserted periods for \(G\) and the isogenous seed.

Now \((q,U)=1\), \(J_F(1)=1\), and \(J_F(q)=-1\). Set \(t_q=\operatorname{ord}_{U}(q)\le U\le16(h+1)\). At every \(k\equiv1\bmod t_q\) the paired character therefore changes from \(q^{k-1}\) to \(q^k\). Denominator divisibility for the integral seed \(G+T_F\) makes \(F_{q^k}/F_{q^{k-1}}\) integral for this selection \(F=w,a,c\), all of whose primes are good. No old prime changes its depth, since its reduction rank for this seed is a positive power of \(q\) and the prime is bigger than \(2q\). A new prime of odd depth must therefore have exact rank \(q^k\) for the seed and exceeds \(2q^k\). If \(q^k\mid n\), (1) bounds it by \(\Delta_n\). Taking the first such \(k\) with \(2q^k>\Delta_n\) proves \(v_q(n)\ll\Delta_n^L\). The effective two-child bound gives \(\log\operatorname{rad}(n)\le\log\Delta_n\), completing the proof. In particular a direct sequential scan of indices through the resulting cutoff, stripping primes through \(Y\) and testing the residual square, takes \(\exp(O(Y^L\log(2Y)))\) bit operations for the total-kernel census through \(Y\).
