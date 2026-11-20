# The squarefree part of the square root on the mixed orbit

Use the positive odd indices of the elliptic orbit through \(x=7/4\) on
\[
 C:\quad y^2=(x^2+2)((x-1)^2+1).
\]
Write its signed reduced slopes as \(s_m/t_m\). The two quadratic values are squares and
\[
 s_m^2+2t_m^2=81A_m^2,\qquad A_m>0,\qquad k_m=\operatorname{sf}(A_m).
\]
Here \(\operatorname{sf}\) is the product of the primes whose valuations are odd. The index counts below range over odd integers. The height satisfies \(\log\max(|s_m|,t_m)\asymp m^2\). [Orbit and height](abc_octic_mixed_seed_prime_orbit.md) · [Parity at all odd indices](abc_octic_mixed_prime_indices.md)

The following bounds hold for this fixed orbit.

* At every sufficiently large index, \(\log k_m\gg (\log\log m)\log\log\log m\). At squarefree indices, \(\log k_m\gg\sqrt{\log m}\).
* If a fixed odd integer \(B>1\) divides \(m\), then \(k_m\gg_B\operatorname{rad}(m)^{\tau(B)-1}\), where \(\tau\) counts positive divisors.
* If all prime factors of \(m\) belong to a fixed finite set \(S\), then \(k_m\gg_S m^{\tau(m)/2}\).
* For every fixed \(L>0\), the indices with \(k_m>m^L\) have relative natural density one. There is also a uniform count \(\#\{m:k_m\le K\}\ll K(\log(2K))^c\) for a fixed \(c\) and all \(K\ge1\).

The height thresholds from Faltings' theorem are ineffective. All the bounds are compatible with squarefulness of \(A_m\), since that condition requires \(k_m^3\mid A_m\) and \(\log A_m\asymp m^2\).

## Inheritance of prime valuations

Let \(P=P_1\), \(\iota(x,y)=(x,-y)\), and \(T=[P-\iota P]\) on the Jacobian \(E\). With a branch point \(W\) as origin, \(P_m-W=[m](P-W)\) and \(T=2(P-W)\). Every odd prime is good. For a prime \(p\) occurring in the first quadratic at an odd index, the reduction order \(r_p\) of \(T\) divides that index. At index \(r_p\) the slope meets the same root of \(x^2+2\). Indeed, \(P_{r_p}\) reduces to a branch, and the odd multiplication maps fix each branch. At a branch, valuation of the quadratic is twice the depth in the local parameter. The good elliptic formal logarithm at odd \(p\) therefore gives
\[
 v_p(A_{rn})=v_p(A_r)+v_p(n)
\]
whenever \(r\) is an odd index meeting this branch and \(n\) is odd. At the seed prime 3 the normalization by 9 gives \(v_3(A_m)=v_3(m)\). The prime 5 cannot divide \(s_m^2+2t_m^2\). The norms are odd. The positive odd indices give distinct slopes, since \(T\) has infinite order and the two points in a fiber of \(x\) are interchanged by \(\iota\).

The Jacobian has a rational point of order two. For odd \(r_p\), Hasse's bound gives \(2r_p\le(\sqrt p+1)^2\). In particular, \(p\ge 3r_p/2\) at all sufficiently large odd ranks. For sufficiently large prime indices \(\ell\), \(k_\ell>1\). Otherwise the infinitely many slopes would lift to the fixed genus-three curve with \(s^2+2t^2\) a fourth power and \((s-t)^2+t^2\) a square. Every prime of this \(k_\ell\) has exact rank \(\ell\), since the only rank-one prime of the first quadratic is 3, with \(v_3(A_\ell)=0\) for \(\ell>3\). [Fourth-power curve](abc_octic_mixed_fourth_power_quotients.md)

## How many indices can share a small squarefree part?

The primitive Pythagorean parametrization for \((s-t)^2+t^2\) gives \(t=2uv,\ s=u^2+2uv-v^2\) with suitable signs. Consequently
\[
 G(u,v)=u^4+4u^3v+10u^2v^2-4uv^3+v^4=s^2+2t^2.
\]
For \(k_m=b\), the slope lifts to a rational point of the plane quartic \(D_b:b^2w^4=G(u,v)\), taking \(w=3\sqrt{A_m/b}\). A point of this quartic determines the original slope. The polynomial \(G(u,1)\) has discriminant \(2^{17}\), so these curves are smooth of genus three. Over \(\mathbb Q(\sqrt b)\), the map \(w\mapsto\sqrt b\,w\) identifies \(D_b\) with \(D_1\).

Uniformly in squarefree \(b>0\), the number of rational points of \(D_b\) is at most \(C^{1+\omega(b)}\), where \(\omega\) counts distinct prime factors. To see the rank bound needed here, fix a number field \(F\) containing all two-torsion of \(J_1=\operatorname{Jac}(D_1)\). For \(J_b=\operatorname{Jac}(D_b)\), the action on \(J_b[2]\) over \(F\) factors through a group of order at most two. This six-dimensional representation has a filtration by trivial one-dimensional quotients. Let \(S_b\) include a fixed set of places containing the bad places of \(J_1\), the infinite places and those above 2, together with the places above \(b\). The twist has good reduction away from \(S_b\), since its identifying quadratic extension is unramified there. The Kummer class of a rational point is unramified at these good places away from 2, by extension over the abelian scheme. The filtration bounds \(\dim H^1(G_{F,S_b},J_b[2])\) by six times \(\dim H^1(G_{F,S_b},\mathbb F_2)\). The latter is \(O_F(1+|S_b|)\) by Kummer theory, the units outside \(S_b\), and the fixed class group. Thus \(\operatorname{rank}J_b(\mathbb Q)\ll 1+\omega(b)\). When \(D_b(\mathbb Q)\) is nonempty, the uniform Mordell–Lang theorem for curves gives the claimed point count. [Dimitrov, Gao and Habegger](https://arxiv.org/abs/2001.10276)

Summing this count up to \(K\) proves the sublevel estimate. For example, majorize \(C^{\omega(b)}\) by a divisor function of fixed integral order at least \(C\). In particular, the number of \(m\le M\) for which \(k_m\le m/(\log(2m))^L\) is \(O_L(M/(\log M)^{L-c})\) for fixed \(L>c\).

## A bound at every index

Write \(k=k_m\). For each divisor \(d\mid m\) with \(m/d\) a square, inheritance gives \(k_d\mid k\). The total number of such indices is therefore bounded by summing the preceding point count over divisors of \(k\):
\[
 D:=\prod_{p^e\parallel m}(1+\lfloor e/2\rfloor)\le C_1^{1+\omega(k)}.
\]
For the primes of \(m\), consider each sufficiently large \(\ell\mid m\) outside the support of \(k\). Choose a prime \(q\mid k_\ell\), of exact rank \(\ell\). Inheritance implies that \(q\mid m\) or \(q\mid k\). The assignment \(\ell\mapsto q\) is injective because a prime has a single rank. Its arrows increase by a factor of at least \(3/2\). Continuing only from vertices outside \(k\) gives disjoint chains ending at distinct prime divisors \(q\) of \(k\). A chain ending at \(q\) contributes \(O((\log q)^2)\) to the sum of the logarithms of its primes. Including the finitely many small possible source primes gives
\[
 \log\operatorname{rad}(m)\ll 1+(\log(2k))^2,\qquad P^+(m)\ll 2k.
\]
Here \(P^+(m)\) is the largest prime factor, for \(m>1\). Primes of \(m\) already in \(k\) can be included as terminals or singletons.

Now \(\sum_{p^e\parallel m}(e-1)\le 2(D-1)\). Hence
\[
 \log m\ll (\log(2k))^2+C_2^{1+\omega(k)}\log(2k).
\]
This forces \(k\) to grow with \(m\). The elementary bound \(\omega(k)\ll \log k/\log\log k\) then gives \(\log k\gg(\log\log m)\log\log\log m\). At squarefree indices the bound for \(\operatorname{rad}(m)\) alone suffices.

## Detecting a prescribed reduction order

Fix odd \(a>1\). On the projective slope line mark the points \(x(W+Z)\), where \(W\) runs over the two branches above \(x^2+2=0\) and \(Z\) runs over the geometric torsion points of exact order \(a\) on \(E\). Addition uses the torsor action. This reduced divisor is defined over \(\mathbb Q\). For each \(W\) the only identifications are \(Z\) and \(-Z\), because the fiber involution fixes \(W\) and negates the displacement. Points from the two different branches cannot coincide: their difference as branch points is nonzero two-torsion, whereas the displacements have odd order. The number of marked slopes is consequently
\[
 J_2(a)=a^2\prod_{p\mid a}(1-p^{-2})\ge8.
\]
Choose a homogeneous squarefree polynomial \(G_a\) over the integers cutting out the divisor. Its degree is even. The quadratic covers of the slope line with equation \(z^2=cG_a\) have genus \((J_2(a)-2)/2\ge3\), using homogeneous coordinates with \(z\) of weight \(J_2(a)/2\).

The map \(x(B)\mapsto x(W+[a](B-W))\), denoted \(L_a\), is independent of the chosen branch since \(a\) is odd. It is defined over \(\mathbb Q\). The pullback by \(L_a\) of the two target branches has multiplicity two at each of the marked slopes of \(G_a\): multiplication by \(a\) is unramified, the source projection is unramified at a nonzero odd displacement, and the target projection has ramification index two. Remove a finite set of primes depending on \(a\), including primes over \(2a\), primes of bad reduction of these maps, and primes at which any distinct preimages of the target branches collide. At every remaining prime \(p\) dividing \(G_a(s_n,t_n)\) the source reduction has that exact displacement order. Its difference from its involute has the same order, as twice an odd-order displacement. This difference equals \([n]T\), so
\[
 \frac{r_p}{\gcd(r_p,n)}=a,\qquad
 v_p(s_{an}^2+2t_{an}^2)=2v_p(G_a(s_n,t_n)).
\]
The valuation identity follows from the indicated divisor multiplicity, in primitive projective coordinates: all the other preimage factors are units and a good homogeneous lift of the map has at least one unit coordinate. The finite exclusions can also contain 3, so the second identity gives \(v_p(A_{an})=v_p(G_a(s_n,t_n))\).

Outside any fixed finite enlargement of the excluded set, some prime has odd valuation in \(G_a(s_n,t_n)\) at every sufficiently large odd \(n\). Otherwise that integer lies in one of finitely many signed square classes. Homogeneity of even degree lifts each such slope to one of the fixed quadratic covers just constructed, contrary to Faltings and distinctness of the slopes. Zero values occur at only finitely many slopes.

For prime \(n=\ell\nmid a\), the rank equation allows only \(r_p=a\) or \(a\ell\). Enlarge the excluded set by the finitely many primes of rank \(a\) (they divide the denominator of the fixed nonzero point \([a]T\)). This gives an exact rank \(a\ell\) prime with odd valuation in \(A_{a\ell}\) for every sufficiently large prime \(\ell\). The case \(a=1\) was proved separately from the fourth-power curve.

For fixed odd \(B>1\) dividing \(m\), apply this result to every \(a\mid B\) and every sufficiently large prime \(\ell\mid m\), taking \(\ell>B\). The resulting primes \(q_{a,\ell}\) are all distinct, since the ranks \(a\ell\) are distinct. Each exceeds \(\ell\) and divides \(m\) or \(k_m\) by inheritance, because \(a\ell\mid m\). Multiplying these inequalities gives \(\operatorname{rad}(m)^{\tau(B)}\ll_B\operatorname{rad}(m)k_m\).

If \(m\) is supported on a fixed finite \(S\), take any sufficiently large divisor \(d\mid m\) and put \(a=\operatorname{rad}(d),\ n=d/a\). Only finitely many \(a\) occur. The rank equation forces \(r_p=d\): every prime of \(n\) already divides the squarefree integer \(a\), so its exponent in \(r_p\) must exceed its exponent in \(n\) by one. The odd valuation persists at \(m\) since \(p>d>\max S\). Multiplying the resulting distinct primes in \(k_m\) proves \(k_m\gg_S m^{\tau(m)/2}\), using \(\prod_{d\mid m}d=m^{\tau(m)/2}\).

## Density above every fixed power of the index

The mean of \(\log(m/\operatorname{rad}(m))\) over the integers up to \(M\) is at most \(\sum_p \log p/[p(p-1)]<\infty\), by counting multiples of prime powers. The odd-index mean is bounded as well. Thus \(\operatorname{rad}(m)\ge\sqrt m\) at a relative density-one set of odd indices.

Given \(L>0\), choose \(h\) with \(2^h-1>2L\). Among odd integers, divisibility by each prime of a finite list of odd primes is independent in natural density by the Chinese remainder theorem. The sum of the probabilities \(1/p\) diverges as the list increases, and the variance of the corresponding count is at most its mean. Thus the upper density of indices containing fewer than \(h\) primes of the list can be made arbitrarily small. For a fixed list there are finitely many possible products \(B\) of \(h\) distinct primes. The fixed-divisor estimate gives \(k_m\gg_{\rm list}\operatorname{rad}(m)^{2^h-1}\) whenever one such \(B\) divides \(m\). First take the density limit for a fixed list, then enlarge the list. This yields the claimed density one, without an explicit convergence rate.
