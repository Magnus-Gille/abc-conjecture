# Two small legs at the same hypotenuse

Fix \(K>0\). For all sufficiently large \(u\), at most two distinct primitive representations \(v^2+w^2=u^2\) have \(0<v<w\) and \(v\le K\sqrt u\). If two exist they are of opposite parity types. There are positive integers \(a,b\) bounded in terms of \(K\), with \(b\) odd, and positive \(X,Y\) such that
\[
 u=X^2+a^2=(Y^2+b^2)/2,\qquad
 Y^2-2X^2=2a^2-b^2.
\]
The two leg pairs are \((2aX,X^2-a^2)\) and \((bY,(Y^2-b^2)/2)\).

Indeed \(u\) is odd and \(u-w=v^2/(u+w)\le K^2\). If \(v\) is even, the coprime positive integers \((u-w)/2,(u+w)/2\) have square product, so they are \(a^2,X^2\). If \(v\) is odd, the coprime positive integers \(u-w,u+w\) themselves are squares \(b^2,Y^2\), with \(b,Y\) odd. In each parity case the larger square lies within a bounded distance of the fixed integer \(u\) or \(2u\). For large \(u\) there is room for at most one such square, hence for at most one pair of each type.

### When the larger legs have a small squarefree part

In any infinite sequence of these double representations, the squarefree part of \(X^2-a^2\) tends to infinity with \(u\). The same is true of \((Y^2-b^2)/2\) on the subfamily \(a\ne b\). Here squarefree part is the unique positive squarefree \(D\) such that the integer equals \(D\) times a square.

If the first assertion failed, the bounded parameters would give fixed \(a,b,D\) and infinitely many \(X\) with \(Y^2=2X^2+k,\ X^2-a^2=DZ^2,\ k=2a^2-b^2\). Hence
\[
 (DYZ)^2=D(2X^2+k)(X^2-a^2).
\]
The quartic has four simple roots: \(k\ne0\), \(a\ne0\), and at \(X^2=a^2\) the first factor equals \(4a^2-b^2\ne0\) since \(b\) is odd. This affine genus-one curve has only finitely many integral points by Siegel's theorem. For the other leg, use \((Y^2-b^2)/2=X^2+a^2-b^2\) as the second factor instead. It has simple roots when \(a\ne b\) and the first factor equals \(b^2\ne0\) at those roots. For \(a=b\) the larger leg is exactly \(X^2\).

### A family with an exact radical formula

Take \(a=b=1\), and write \(k_n+x_n\sqrt2=(3+2\sqrt2)^n\), \(u_n=x_n^2+1\). Then \(k_n^2=2x_n^2+1\). For \(n\ge2\) the two primitive leg pairs are
\[
 (2x_n,x_n^2-1),\qquad(k_n,x_n^2).
\]
Both smaller legs are \(O(\sqrt{u_n})\). At \(n=2\) this gives \(24^2+143^2=17^2+144^2=145^2\).

Let \(P_j=((1+\sqrt2)^j-(1-\sqrt2)^j)/(2\sqrt2)\) denote the Pell numbers and \(Q(m)=m/\operatorname{rad}(m)\). For the second pair put \(C_n=u_n^2,\ R_n=\operatorname{rad}(u_nx_nk_n)\). Then
\[
 \frac{C_n}{R_n}=
 \frac{u_n}{2x_n k_n}\,
 Q(P_{4n})\,Q(P_{2n-1})\,Q(P_{2n+1}).
\]
To verify this, \(x_n=P_{2n}\) and \(P_{4n}=2x_nk_n\). Multiplying the two odd-index Pell formulas gives \(P_{2n-1}P_{2n+1}=x_n^2+1=u_n\). Their indices and \(4n\) are pairwise coprime, so the three Pell numbers are pairwise coprime by strong divisibility. Since \(x_n\) is even, \(P_{4n}\) and \(P_{4n}/2\) have the same radical. These facts give the displayed identity.

The factor \(u_n/(2x_n k_n)\) tends to \(1/(2\sqrt2)\), and \(\log C_n=8n\log(1+\sqrt2)+O(1)\). Consequently there are infinitely many fixed-power abc violations in this particular family **if and only if**
\[
 \limsup_{m\to\infty}\frac{\log Q(P_m)}m>0 .
\]
In one direction a fixed-power violation forces one of the three terms in the identity to have logarithm \(\gg n\). In the other direction take \(n=m\) and use \(P_m\mid P_{4m}\), which implies \(Q(P_{4m})\ge Q(P_m)\). The sign of this limsup is unresolved here. In particular the small real legs, even at the optimal order \(\sqrt{u_n}\), do not establish a counterexample.

Allowing a denominator in the Pell equation gives a family to which every hypothetical rational abc failure transfers. The transfer forces the denominator to grow. A separate logarithmic-form argument gives an unconditional lower bound for the squarefree part of \(u_n\) on the integral slice. [Rational transfer](abc_rational_pell_transfer.md) · [Squarefree-part bounds](abc_small_legs_squarefree_height.md)

### Necessary prime multiplicities in this family

For an odd prime \(p\) let \(r_p\) be the first positive index with \(p\mid P_{r_p}\), and \(w_p=v_p(P_{r_p})\). Set \(\lambda=1+\sqrt2,\ \bar\lambda=1-\sqrt2\). Modulo \(p\), \(r_p\) is the order of \(\lambda/\bar\lambda\), and \(r_p\mid p-(2/p)\) by splitting or the norm-one condition in the residue field. The two split orders agree by conjugation. At \(r_p\mid m\), odd-prime binomial lifting gives \(v_p(P_m)=w_p+v_p(m)\). The elementary doubling relation and the parity of the Pell sequence give \(v_2(P_m)=v_2(m)\) for even \(m\). Consequently for \(m=4n,2n-1,2n+1\) all valuation increases *after* first occurrence supply at most \(4n(2n-1)(2n+1)\) in the product of the three \(Q\)-values. If only finitely many odd primes have \(w_p>1\), then \(C_n/R_n=O((\log C_n)^3)\) in this family.

There is a size restriction even if there are infinitely many such primes. For every fixed \(0<\epsilon<1\), the total \((w_p-1)\log p\) from primes with \(p w_p\le n^{2-\epsilon}\) or \(r_p\le n^{1-\epsilon/4}\), across those three indices, is \(o(n)\). For any one order \(r\), the primed factors \(p^{w_p}\) at this first occurrence divide the norm of the nonzero homogeneous cyclotomic value \(\Phi_r(\lambda,\bar\lambda)\) in aggregate. Its logarithmic absolute norm is \(O(\varphi(r))\) by its complex root product; the bases are fixed. Thus the orders \(r\mid m\) with \(r\le n^{1-\epsilon/4}\) contribute \(O(\tau(m)n^{1-\epsilon/4})=o(n)\). For each larger order, \(p\equiv\pm1\bmod r\), and the sum over \(p w_p\le n^{2-\epsilon}\) is at most
\[
 n^{2-\epsilon}\sum_{\substack{p\le n^{2-\epsilon}\\p\equiv\pm1\bmod r}}\frac{\log p}{p}
 \ll \frac{n^{2-\epsilon}(\log n)^2}{r}.
\]
The last bound follows by summing over integers \(jr\pm1\) for \(j\ge1\). Summing over at most \(\tau(m)=n^{o(1)}\) divisors proves the assertion. A fixed-power violation therefore needs a total \(\gg n\) from primes with both \(r_p>n^{1-\epsilon/4}\) and \(p w_p>n^{2-\epsilon}\), at their initial multiplicities. Their existence in that amount is unknown.

A finite check through \(2{,}000{,}000\) found the following initial excesses. The last column certifies the exact valuation.

| \(p\) | \(r_p\) | \(w_p\) | \(P_{r_p}/p^2\bmod p\) |
|---:|---:|---:|---:|
| 13 | 7 | 2 | 1 |
| 31 | 30 | 2 | 2 |
| 1,546,463 | 1,546,462 | 2 | 486,828 |

To reproduce the check, sieve all 148,932 odd primes up to the bound. For each, compute \(P_{p-(2/p)}\bmod p^2\) by binary doubling using \(P_{2j}=2P_j(P_{j+1}-P_j)\), \(P_{2j+1}=P_j^2+P_{j+1}^2\). Since \(p\) does not divide \(p-(2/p)\), a zero is equivalent to \(w_p>1\). For each zero, successively remove prime factors from the index while its Pell number still vanishes modulo \(p\), then evaluate modulo \(p^3\) at the resulting rank. The combined first-occurrence factor available from this entire prime range is at most \(623{,}224{,}589\) for every \(n\); a prime occurs in at most one of the three coprime Pell numbers. The finite check imposes no bound on primes beyond this range.
