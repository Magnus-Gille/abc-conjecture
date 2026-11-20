# Odd initial valuations in the dyadic packets

Let \(n=2^k\ge8\), and use the packet \(w_n\) attached to \(R=(-8,16)\) on \(E':y^2=x^3+16x^2+32x\). Every prime of \(w_n\) first occurs there and has the form \(p=(1+2na)^2+8n^2b^2\) with integers \(a,b\) and \(b\ne0\). Write \(K_n=\prod_{v_p(w_n)\text{ odd}}p\). [Recursion, order and prime-shape proofs](abc_octic_dyadic_fermat_audit.md)

For every \(n\ge8\), the packet has a prime \(p\equiv17\pmod{24}\) of odd exponent. Thus
\[
K_n\ge 12n^2-4n+1.
\]
Indeed \(u_4=v_4=1,w_4=7\). The duplication formulas preserve \(3\nmid u_nv_nw_n\), since \(w_n^2=u_n^4+16u_n^2v_n^2+32v_n^4\equiv1\pmod3\) whenever \(u_n,v_n\) are units. The formula for \(w_{2n}\) then gives \(w_{2n}\equiv1+32+192+1024+1024\equiv-1\pmod3\). Some \(p\equiv2\pmod3\) has odd exponent. Every prime of the packet is 1 modulo 8. Modulo 3 its norm expression reads \((1+2na)^2-b^2=-1\), forcing \(3\mid1+2na\), \(3\nmid b\); in particular \(a\ne0\). The size bound follows.

For additional small exponents, put \(a=u_n^2,b=v_n^2\). Modulo an odd prime \(q\), the next pair is \(((a^2-32b^2)^2,4ab(a^2+16ab+32b^2))\), and the next packet is \(a^4+32a^3b+192a^2b^2+1024ab^3+1024b^4\). Iterating from \((1,1)\) gives these complete cycles. Parentheses show periodic tails.

| Exponent \(m\) | Test prime \(q\) | Residues of \(w_8,w_{16},\ldots\) modulo \(q\) |
|---:|---:|---|
| 3 | 7 | 5, (2) |
| 5 | 31 | (10, 18) |
| 7 | 113 | 13, (100) |
| 11 | 23 | 19, (8, 13, 2, 12, 4) |

Every listed residue \(r\) has \(r^{(q-1)/m}\ne1\pmod q\). For each of these exponents and every dyadic \(n\ge8\), some primitive prime of the packet has valuation indivisible by \(m\).

## A larger lower bound on a subsequence

Let \(Q\) run through the positive integers, \(k_Q=\operatorname{lcm}(1,\ldots,Q)\) and \(n_Q=2^{k_Q}\). For every odd prime \(q\le Q\), \(n_Q\equiv1\pmod q\). Write any prime of \(w_{n_Q}\) as \(|1+n_Qz|^2\), \(z=2(a+b\sqrt{-2})\). The odd integer \(|1+z|^2=(1+2a)^2+8b^2\) is at least 9. If it were at most \(Q\), any prime factor \(q\) would divide \(|1+n_Qz|^2\), whereas the latter is prime and exceeds \(Q\). Consequently \(|z|>\sqrt Q-1\). Every prime of the packet exceeds \((n_Q(\sqrt Q-1)-1)^2\). Since \(\log k_Q=\sum_{p^j\le Q}\log p\sim Q\),
\[
\limsup_{n=2^k\to\infty}\frac{P^-(w_n)}{n^2\log\log n}\ge1.
\]
The nonempty odd-exponent support obeys the same bound. For every fixed \(C\), the conclusion \(P^-(w_{2^k})>C 2^{2k}\) in fact holds along an entire arithmetic progression of exponents \(k\), after finitely many terms, by taking all multiples of \(k_Q\) for sufficiently large fixed \(Q\).

## Valuation one and source hypotheses

Rational abc implies \(\log\prod_{p\parallel w_n}p=(1-o(1))\log w_n\) along all dyadic indices. Indeed \(w_n\mid T_{n-1}\), \(T_{n-1}\ll c_{n-1}\), \(\operatorname{rad}(T_{n-1})=\operatorname{rad}(a_{n-1}b_{n-1}c_{n-1})\), and \(\log c_{n-1}\asymp\log w_n\). Rational abc makes \(\log(T/\operatorname{rad}(T))=o(\log c)\). The corresponding excess for \(w_n\) is at most this amount, and \(e\le2(e-1)\) at every exponent \(e\ge2\). The same implication needs only the family-specific limsup quality at most one along these neighbours. [Whole-triple identity](abc_octic_whole_radical_tail.md)

The usual quotient \(x:E'\to\mathbb P^1\) gives the doubling Lattès map \(f(x)=(x^2-32)^2/(4x(x^2+16x+32))\). In a pullback of an abscissa, the local degree is \(e(f^j,x(T))=e(x,[2^j]T)/e(x,T)\) since multiplication is étale in characteristic zero. Over either marked nonzero root \(e_\pm=-8\pm4\sqrt2\), every pullback under every positive iterate is ramified: all target points are two-torsion, whereas every source two-torsion point maps to the identity. Over infinity the only possible unramified inverse branches come from \(E'[2]\). On the abscissa line the local exponent at a marked contact is twice the valuation in \(w_n\). Thus the standard non-dynamical-ramification hypothesis in squarefree primitive-divisor estimates fails for this choice of map and mark. Gratton–Nguyen–Tucker treat rational functions assuming abc over number fields. Their unconditional function-field result assumes non-isotriviality. Ghioca–Nguyen–Tucker study exact valuation one in **differences of iterates** under Vojta over number fields, with admissible portraits. In the squarefree EDS results of Ulmer–Urzúa, places are geometric points on the base curve of an elliptic surface over a field. These different hypotheses do not give an unconditional initial valuation one for this arithmetic packet. [Gratton–Nguyen–Tucker](https://arxiv.org/abs/1208.2989) · [Ghioca–Nguyen–Tucker](https://arxiv.org/abs/1608.01361) · [Ulmer–Urzúa](https://arxiv.org/abs/1908.02208)

An alternative conditional use of the dynamics marks one iterate earlier. Fix a four-torsion point \(T\) satisfying \(2T=(e_+,0)\), and take a number field containing its coordinates. The mark \(x(T)\) is preperiodic and nonperiodic; all its iterated inverse branches are unramified by the local degree formula. Conjugating by \(x\mapsto x-x(T)\) puts the mark at zero, and the orbit of \(x(R)-x(T)\) is wandering with all iterates nonzero. A squarefree prime place in the difference \(x([2^j]R)-x(T)\) measures depth one at one of \(T,-T\), since the abscissa is étale there away from fixed bad primes. Doubling preserves the depth and sends either point to \((e_+,0)\), so the rational prime below it has exact valuation one in \(w_{2^{j+2}}\), after excluding the finite ramified set. This explains why a squarefree dynamical theorem assuming number-field abc can instead be used with this earlier mark. The rational-abc proof above gives the stronger logarithmic conclusion.

Kim–Walsh's eventual compositeness applies to entire magnified elliptic Fermat quotients. Reynolds proves finiteness of perfect powers in a full EDS under, among other hypotheses, divisibility of its first term by 2 or 3; here \(R\) is integral, with first denominator 1. A packet whose every prime valuation exceeds one may still have distinct exponents 2 and 3. The modular arguments above leave this possibility open, as does the presence of arbitrarily large primes. I found no unconditional theorem proving a valuation-one prime for infinitely many of these dyadic packets. The literature scope here comes from primary abstracts; direct download of the Gratton–Nguyen–Tucker manuscript was unavailable during the check. The ramification and conditional mass arguments given above are independent. [Kim–Walsh](https://arxiv.org/abs/1808.03846) · [Reynolds](https://arxiv.org/abs/1101.2949)
