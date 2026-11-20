# Primitive primes of odd multiplicity at prescribed orders

Let \(A>B\ge1\) be coprime. Every order \(m=2^i3^j\) with \(i\ge0,\ j\ge2\), and every order \(m=2^i7^j\) with \(i\ge0,\ j\ge1\), has a prime \(p\) for which
\[
       \operatorname{ord}_p(A/B)=m,\qquad v_p(A^m-B^m)\ \text{is odd}.
\]
The multiplicity may exceed one. Write \(\operatorname{sf}(u)=\prod_{v_p(u)\ {\rm odd}}p\) for the squarefree part.

At \(m=9,18\), the two elliptic descents show that \(\Phi_m(A,B)\) is neither a square nor three times a square. The corresponding exclusions at \(m=7,14\) are a square and seven times a square. All four forms are odd by coprimality. Thus each has a prime of odd valuation outside the prime divisors of its index. For \(p\nmid mAB\) the cyclotomic factors of \(T^m-1\) have disjoint roots modulo \(p\), so such a prime gives order exactly \(m\). In all four cases the valuation in the cyclotomic factor equals its valuation in the full difference. [Ninth and eighteenth orders](abc_cyclotomic_sextic_square_points.md) · [Seventh and fourteenth orders](abc_cyclotomic_seventh_square_points.md) · [Independent descent for the cofactor seven](abc_cyclotomic_seventh_cofactor.md)

For the powers of three, take \(d=9\) when \(i=0\) and \(d=18\) otherwise. For the powers of seven, take \(d=7\) when \(i=0\) and \(d=14\) otherwise. In each case \(u=m/d\) is supported on primes dividing \(d\), and
\[
                    \Phi_m(A,B)=\Phi_d(A^u,B^u).
\]
This follows by iterating \(\Phi_d(T^\ell)=\Phi_{\ell d}(T)\) for prime \(\ell\mid d\), then homogenizing. The input powers are still coprime and unequal. The same exclusions now force a prime \(p\nmid m\) to odd valuation in \(\Phi_m(A,B)\). The disjoint-roots argument at index \(m\) proves its required order.

## Products in a full power difference

Let \(q=3\) or \(7\), \(j_0=2\) or \(1\), respectively, and \(N=2^h q^k\) with \(k\ge j_0\). The selected primes for the orders \(2^i q^j\mid N,\ j\ge j_0\), are distinct. They are odd and prime to \(q\), so the odd-prime lifting formula preserves their valuations in \(A^N-B^N\). Since \(p\equiv1\bmod m\),
\[
 \operatorname{sf}(A^N-B^N)\ \ge\
      \prod_{i=0}^h\prod_{j=j_0}^k
                              (\operatorname{lcm}(2,2^iq^j)+1).
\]
For \(N=(2q)^k\) the logarithm of the product is at least \((\tfrac12\log(2q)+o(1))k^3\), uniformly in the bases. This follows by summing \(i\log2+j\log q\) over the displayed rectangle. For fixed bases, abc would require \(\log\operatorname{rad}(A^N-B^N)\ge(1-o(1))N\log A\).

## All orders supported on two and three

The quartic descents supply the missing orders \(2^i\) for \(i\ge3\) and \(3\cdot2^i\) for \(i\ge2\). Thus the orders \(2^i3^j\) admitting such a prime for **every** coprime base pair are precisely those outside \(1,2,3,4,6\). At \(1\) take \(A-B=1\); at \(2\) take \((A,B)=(3,1)\). The three remaining failures are witnessed individually by \(\Phi_3(5,3)=7^2,\ \Phi_4(4,3)=5^2,\ \Phi_6(8,3)=7^2\). In particular, for every \(N=2^h3^k\) one has the numerical bound
\[
     \operatorname{sf}_{\{2,3\}^c}(A^N-B^N)
       \ \ge\ \prod_{\substack{d\mid N\\d\notin\{1,2,3,4,6\}}}(d+1)
       \ \ge\ N^{\tau(N)/2}/144.
\]
Here only primes outside \(2,3\) enter the squarefree part. Each displayed order exceeds six, so every exact-order prime lies outside \(2,3\). The factor \(144\) is \(1\cdot2\cdot3\cdot4\cdot6\). The same argument at \(N=2^h7^k\) gives \(N^{\tau(N)/2}/8\) after omitting \(1,2,4\): at the remaining dyadic orders, a prime of order at least eight also exceeds seven. [Quartic descents, including orders involving five](abc_cyclotomic_quartic_odd_primitive.md)

Even at the exceptional orders \(3,6\), **one of the two always works**. Indeed \(\Phi_3(A,B)\Phi_6(A,B)=A^4+A^2B^2+B^4\). The product is odd. If both orders failed, the product would equal \(D z^2\) with \(D=1\) or \(3\). Put \(t=A/B>1,\ v=z/B^2\). Then
\[
       (x,y)=(Dt^2,D^2tv)\ \in\
       E_D:\quad y^2=x^3+Dx^2+D^2x .
\]
We show that \(E_1(\mathbf Q)=\{O,(0,0)\}\) and \(E_3(\mathbf Q)=\{O,(0,0),(3,\pm9)\}\); none has \(x>D\).

Use the two-isogeny descent formula in the linked quartic proof. Its first squareclass image has positive classes supported on \(D\), since \(x^2+Dx+D^2>0\); it is trivial for \(D=1\) and has size at most two for \(D=3\). The companion has coefficients \((-2D,-3D^2)\) and squareclass image in \(\{1,-1,3,-3\}\). For \(D=3\) it contains \(-3\) and cannot contain \(-1\). Such a class would require
\[
                 n^2=-u^4-6u^2v^2+27v^4,\qquad (u,v)=1 .
\]
Modulo three this forces \(3\mid u,\ 3\nmid v\). Writing \(u=3k\), the right side is \(27(-3k^4-2k^2v^2+v^4)\), whose parenthesis is nonzero modulo three. This contradicts even valuation. The two class-image sizes therefore have product at most four for both curves, and both ranks are zero.

At \(D=1\) both good reductions at \(5,7\) have eight points. There is only one rational point of order two, and it has no rational half: the duplication formula \(x(2P)=(x(P)^2-1)^2/(4y(P)^2)\) would require \(x(P)=\pm1\), where the ordinates squared are \(3,-1\). This gives the asserted group. At \(D=3\) the same reductions have four and eight points, so the four displayed rational points exhaust the group. This proves the paired assertion. For \(6\mid N=2^h3^k\) the prime supplied at order 3 or 6 is at least seven and is distinct from those in the product above, so the first lower bound gains a further factor of seven.
