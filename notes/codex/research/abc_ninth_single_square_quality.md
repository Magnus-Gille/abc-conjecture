# How much a single large square can contribute in a ninth-power triple

Let \(A>B>0\) be coprime. Write \(G=AB(A^3-B^3)\), \(Q=A^6+A^3B^3+B^6\), \(R=\operatorname{rad}(GQ)\), and suppose \(p>A^2\) satisfies \(p^2\mid Q\). There can be only one such prime: the squares of two would have product exceeding \(A^8>Q\). The complete cube classification gives \(v_p(Q)=2\). The least-squarefree-kernel result also gives the pointwise ceiling \(p\le\sqrt{Q/73}<\sqrt{3/73}\,A^3\). For every fixed \(c>0\) there are only finitely many pairs with \(p\ge cA^3\), since their kernels are bounded and the fixed sextic twists have finitely many rational points. [Cube classification](abc_cyclotomic_ninth_cube_points.md) · [Least positive kernel](abc_cyclotomic_ninth_least_positive_kernel.md) · [Twist count](abc_cyclotomic_large_square_twists.md)

Put \(K=Q/p^2\), \(U(m)=m/\operatorname{rad}(m)\), and \(h=B/A\). Then
\[
 \frac{A^9}{R}=
 \frac{p}{A^2h(1-h^9)}\,
          U(G)U(K)\operatorname{rad}(\gcd(G,K)).
\]
Indeed \(GQ=A^{11}h(1-h^9)\), \(p\nmid GK\), and \(\gcd(G,K)\mid3\) since an overlap with \(A^3-B^3\) must divide \(3B^6\) in \(Q\), which is prime to \(AB\). Thus \(p\ge A^{2+t}\) suffices by itself to give \(A^9>R^{1+\varepsilon}\), where \(t=9\varepsilon/(1+\varepsilon)\). Infinitely many such large squares for one fixed \(t>0\) would yield a disproof (decrease the exponent increment slightly to absorb any constant). On an interior sector \(c\le h\le1-c\), if \(U(G)U(K)=A^{o(1)}\) this threshold is necessary up to \(A^{o(1)}\).

## Counting exceptions with controlled losses outside the square

Let \(\operatorname{sf}(K)=\prod_{v_q(K)\ {\rm odd}}q\), and put \(W(K)=\prod_{q\mid K}q^{\lfloor(v_q(K)-1)/2\rfloor}\). The equality
\[
       pU(K)=\sqrt{Q/\operatorname{sf}(Q)}\,W(K)
\]
follows prime by prime. Fix \(c>0,\ \beta\ge0,\ \varepsilon>0\). On \(c\le B/A\le1-c\), impose \(U(G)W(K)\le A^\beta\). At a fixed-exponent exception the preceding identities imply
\[
                       \operatorname{sf}(Q)\ll_c A^{2-2t+2\beta}.
\]
For \(\sigma=2-2t+2\beta>0\) the number of such pairs up to \(A\le H\) is therefore \(O_{c,\varepsilon,\beta}(H^\sigma(1+\log H)^C)\), by the all-heights sextic twist count. At \(\sigma=0\) there are finitely many, and at \(\sigma<0\) there are none above a bounded height. For example, at \(\varepsilon=1/20\) the exponent is \(8/7+2\beta\). When \(K\) is cubefree, \(W(K)=1\) even if it contains many prime squares; in that case the auxiliary condition only concerns the explicit factor \(AB(A^3-B^3)\). The unrestricted exceptional count remains \(O_\xi(H^{12/7+\xi})\) at this exponent. [Unrestricted counting proof](abc_sextic_power_exception_count.md)
