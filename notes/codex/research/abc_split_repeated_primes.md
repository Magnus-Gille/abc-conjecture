# Repeated prime divisors in the full CM denominator at split prime indices

Let \(R=(-8,16)\) on \(y^2=x^3+16x^2+32x\), and let \(B_q^2\) be the reduced denominator of \(x(qR)\). For primes \(q>3\) split in \(\mathbb Z[\sqrt{-2}]\), write \(C_q\) for the part of \(B_q\) supported on primes at which \(R\) has full CM annihilator \((q)\). All **1,749 pairs** \((q,p)\) with \(p\le10^{12}\) and \(p\mid C_q\) have \(v_p(B_q)=1\). They represent 1,616 distinct indices, the largest being 407633. For \(q=11,17,19\), the full packet is squarefree at primes of arbitrary size. Whether any \(C_q\) has a repeated prime divisor remains open in this calculation. [Pairs through one trillion](abc_split_repeated_pairs.tsv) · [Exhaustive search](abc_split_repeated_scan.cpp) · [Valuation, packet and density verifier](abc_split_repeated_verify.py)

At later scalar indices one can quantify how often these primes acquire a square divisor. The odd positive integers \(n\) for which some initially simple \(p\mid C_q\) satisfies \(p^2\mid B_n\) have a relative natural density between **0.00252219% and 0.0025455%**.

## Exhausting the pairs

Every prime \(p\mid C_q\) is split. Its Frobenius fixes \(R\), so its signed generator has the form \(1+q(a+b\sqrt{-2})\), with \(a\) even, \(b\ne0\), and \(p=(1+qa)^2+2q^2b^2\). Take \(b>0\) by conjugation. Thus \(p\ge2q^2+1\). For \(p\le10^{12}\) the search visits all 28,526 eligible split prime indices and all 9,726,154,172 odd norm values with these bounds. Trial divisibility by primes from 3 through 31 leaves 3,021,370,499 values. Every actual prime norm exceeds 31. At \(q\le251\) the test uses the exact normalized division polynomial \(T_q\), for which \(B_q=|T_q|\). At larger \(q\) it uses scalar multiplication on the \(x\)-coordinate. All prime outputs are certified by trial division. [Frobenius norm restriction](abc_odd_rank_quartic_cutoff.md) · [Normalized recurrence](abc_full_large_all_exponents.py)

On the scaled model \(y^2=x^3+4x^2+2x\), the base point has \(x=-2\). The ladder starts with \(R,2R\) and always maintains consecutive multiples. It uses
\[
 x(2P)=\frac{(x(P)^2-2)^2}{4x(P)(x(P)^2+4x(P)+2)},\qquad
 x(P+Q)x(P-Q)=\frac{(x(P)x(Q)-2)^2}{(x(P)-x(Q))^2}.
\]
At odd primes the duplication map on the projective line has no base point. In the differential formula the difference has \(x=-2\), a finite nonzero value. If its homogeneous numerator and denominator both vanish, the two input abscissas coincide, both finite and with square 2. Such a point has double of abscissa zero, so the difference would be either the origin or a point of abscissa zero. This excludes degeneration on the ladder. The point is killed exactly when the final projective denominator vanishes.

The independent verifier evaluates the unscaled \(\psi_q(R)\) modulo \(p\) and \(p^2\). At odd primes of good reduction \(v_p(\psi_q(R))=v_p(B_q)\), since \(R\) is integral and the multiplication formulas have no common zero. To identify the CM packet, write \(q=u^2+2v^2\) with \(u,v>0\), and put \(X=x(uR),Y=x(vR)\) modulo \(p\). Both are finite and \(Y\ne0\) since \(R\) has prime order \(q\). A proper annihilator occurs exactly when \(X=x([\sqrt{-2}]vR)\), equivalently \(2YX+Y^2+16Y+32=0\). Equality or opposition of the corresponding points gives one of the two conjugate factors. Every hit failed this equality and had nonzero \(\psi_q(R)\bmod p^2\). An independent enumeration by rational prime, using both possible CM group orders, gave exactly the same pairs through \(10^6\). The three complete small factors are
\[
 C_{11}=82633\cdot1781803,\quad C_{17}=281297284141331716203233329,\quad
 C_{19}=2243\cdot223902803\cdot22298211521\cdot519424618619.
\]
Exact rational multiplication and stored primality certificates verify these products. [CM map and packets](abc_odd_rank_primitive_cm_norm.md) · [Primality certificates](abc_octic_scalar_rank_certificates.json)

## How sparse the full packet primes are

Let \(\mathcal P=\bigcup_q\{p:p\mid C_q\}\) with the same split prime indices. A prime occurs at only one such \(q\), its exact scalar reduction order. For \(T\to\infty\),
\[
 \#(\mathcal P\cap[T,2T])\ll\frac{T^{3/4}}{(\log T)^{5/4}},
 \qquad \sum_{p\in\mathcal P} p^{-3/4}<\infty.
\]
Split the indices at \(Q=(T\log T)^{1/4}\). For \(q\le Q\), the height bound \(\log B_q\ll q^2\) gives \(O(Q^3/(\log Q\log T))\) distinct primes in the interval after summing over prime indices. For \(q>Q\), a nonempty packet in this interval requires \(q\le\sqrt T\). The norm representation has at most \(\sqrt T/q\) choices of \(b>0\) and at most \(1+\sqrt{2T}/q\) choices of even \(a\). This gives \(O(T\sum_{q>Q}q^{-2})=O(T/(Q\log Q))\) possibilities using the ordinary prime-counting bound. Dyadic summation proves convergence.

For an effective bound put \(H=10^{12}\). Then
\[
                         \sum_{p\in\mathcal P,\ p>H}\frac1p<0.00163.
\]
The normalized Ward terms satisfy \(|T_j|\le2^{j^2-3}\) for \(j\ge2\). The initial values from \(j=2\) through 7 are \(1,-9,-14,281,-765,-117041\). For \(j\ge8\), each summand of the odd recurrence has four factors, sum of squared subscripts \(j^2+3\), and the coefficients have total absolute value 33. Each summand for the even recurrence also has four factors, sum of squared subscripts \(j^2+6\), and coefficients of total absolute value 2. Induction gives the bound and hence \(\log B_q<q^2\log2\).

Write \(N(T)=\#(\mathcal P\cap[T,2T])\) and take \(Q=1.4(T\log T)^{1/4}\). Replacing the eligible primes by all positive integers in the two classes \(1,3\bmod8\), integration on intervals of length 8 gives \(\sum_{q\le Q}q^2\le(Q+8)^3/12\) and \(\sum_{q>Q}q^{-2}\le1/(4(Q-8))\) in these classes. The preceding counts yield
\[
 \frac{N(T)}T\le \frac{(\log 2)(Q+8)^3}{12T\log T}
             +\frac{\sqrt2+1}{4(Q-8)}
       \le 0.594(T\log T)^{-1/4}\qquad(T\ge H).
\]
After division by \((T\log T)^{-1/4}\), both correction factors \((1+8/Q)^3,(1-8/Q)^{-1}\) decrease, and the resulting coefficient at \(T=H\) is less than \(0.592\). Summing over \(T=2^jH\) gives the displayed \(0.00163\). The measured sum for \(p\le H\) is approximately \(0.00051639554118\).

One interpretation uses a random local lift of the same reduction \(R\bmod p\). Of the \(p\) lifts modulo \(p^2\), exactly one is killed by \(q\), since \(p\ne q\) and \([q]\) is bijective on the kernel of reduction. A model choosing a uniform lift at each prime therefore has probability below \(0.00163\) of any repeated full-packet prime beyond \(H\), by the union bound. The depths of the specified rational point \(R\) remain a deterministic question.

## Density of inherited square divisors

At \(p\mid C_q\), the exact scalar order is \(q\). For \(q\mid n\) the formal logarithm gives \(v_p(B_n)=v_p(B_q)+v_p(n/q)\). When \(v_p(B_q)=1\), the event \(p^2\mid B_n\) is exactly \(qp\mid n\). Its density among odd \(n\) is \(1/(qp)\). The sum of these densities converges by the bounds above. The union has a natural density, since finite unions are periodic and the upper density of the omitted multiples tends to zero by the convergent reciprocal sum. [Formal lifting at this point](abc_odd_rank_squareclass_support.md)

For the 1,749 verified pairs put \(d_i=q_ip_i\). Summing \(1/d_i\) gives an upper bound \(0.000025222000\). Subtracting the pairwise intersections \(1/\operatorname{lcm}(d_i,d_j)\) gives a lower bound \(0.00002522195568\). The verifier rounds every reciprocal outwards in units of \(10^{-28}\). For primes \(p>H\), indices \(q\le11000\) contribute at most
\[
 \frac{\log2}{H\log H}\sum_{\substack{11\le q\le11000\\q\text{ split prime}}}q
 =\frac{3351546\log2}{H\log H}.
\]
At a fixed \(q\) there are at most \(\log B_q/\log H\) such primes. The larger \(q\) contribute at most \(0.00163/11000\). The two terms together are below \(0.00000023226\). This gives the stated density interval after conversion to percentages.
