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
