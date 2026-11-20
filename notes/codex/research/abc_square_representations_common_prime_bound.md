# An upper bound for shared prime contributions at one hypotenuse

Let \(u>1\) have primitive representations \(v^2+w^2=u^2\) with \(0<v<w\). Its distinct prime factors are all \(1\bmod4\). Put \(k=\omega(u)\). Choose any set \(S\) of \(r\) primes, allowed to depend on \(u\) and on all its representations. For a triangle define
\[
 H_S(v,w)=\frac{u^2}{vw}\prod_{p\in S}p^{\max(v_p(vw)-1,0)}.
\]
This counts the contribution from a small leg and from repetitions at the specified primes, before charging for the primes dividing \(u\).

For \(0<\delta\le1,\ k\ge128/\delta,\ u^{\delta/10}\ge8\), the fraction of primitive representations with \(H_S(v,w)\ge u^\delta\) is at most
\[
 \frac{2\,[e(1+4/\delta)]^{r+1}}
 {\binom{k}{\lfloor\delta k/64\rfloor}} .
\]
In particular, if \(r+1\le\delta k/256\), the fraction is at most \(2(64/\delta)^{-\delta k/256}\). Even a number of prescribed primes growing linearly in \(k\) can explain power-scale savings on only an exponentially small fraction of the representations in this range. An exceptional sequence comprising just one or a few representations per height is still possible.

## A separation inequality

Write \(u=\prod_{j=1}^k p_j^{e_j}\), \(p_j=\pi_j\bar\pi_j\), \(\alpha_j=\pi_j/\bar\pi_j\) in \(\mathbb Z[i]\). The signs \(s\in\{-1,1\}^k\) give the normalized rotations \(\beta_s=\prod_j\alpha_j^{s_j e_j}\). Up to order and signs of the two coordinates, \(u\beta_s\) gives every primitive representation exactly twice, from \(s\) and \(-s\), by Gaussian factorization. Set \(A_s=u^2/(v_sw_s)\), so \(|\beta_s^4-1|=4/A_s\).

Consider distinct sign vectors \(s,t\) and an integer \(Q\mid\gcd(v_sw_s,v_tw_t)\). It is coprime to \(u\). Let \(I=\{j:s_j\ne t_j\}\), \(U_I=\prod_{j\in I}p_j^{e_j}\), and \(B=\prod_{j\in I}\alpha_j^{s_je_j}=(a+ib)/U_I\). One has \(\beta_s/\beta_t=B^2\). Both \(\beta_s^4\) and \(\beta_t^4\) are congruent to 1 modulo \(Q\) in the Gaussian rationals with denominators coprime to \(Q\); this follows from \(\beta_s^4-1=2i\beta_s^2\operatorname{Im}(\beta_s^2)\) and \(u^2\operatorname{Im}(\beta_s^2)=\pm2v_sw_s\). Hence \(Q\mid2\operatorname{Im}((a+ib)^4)\). This last integer is nonzero, since independent Gaussian prime factors make \(B^8\ne1\) whenever \(I\ne\varnothing\). Its absolute value is
\[
 U_I^4 |B^8-1|=U_I^4|\beta_s^4-\beta_t^4|
 \ \le\ 8U_I^4/\min(A_s,A_t).
\]
In particular \(Q\min(A_s,A_t)\le8U_I^4\). Thus the sign vectors of two points sharing both a divisor and a small-angle bound must disagree at primes of sufficiently large total logarithmic weight.

## Counting the possibilities

For a qualifying point record the \(r+1\) coordinates \(\log_u A_s\) and \(\log_u(p^{\max(v_p(v_sw_s)-1,0)})\) for \(p\in S\). These coordinates are nonnegative and have total at most 2 since \(H_S\le u^2\). Place each coordinate in a bin of width \(\delta/(2(r+1))\). The nonnegative integer bin indices sum to at most \(4(r+1)/\delta\). Stars and bars bounds the number of cells by \([e(1+4/\delta)]^{r+1}\).

Within a single nonempty cell take the coordinatewise minimum over its qualifying sign vectors. Its sum is at least \(\delta/2\). The last \(r\) minima specify an actual common integer divisor \(Q\) of all the leg products; the first coordinate gives their common lower bound for \(A_s\). The separation inequality shows that any two distinct vectors in that cell have weighted Hamming distance
\[
 \log U_I \ \ge\ \tfrac14\bigl((\delta/2)\log u-\log8\bigr)\ \ge\ (\delta/10)\log u=:D .
\]

Consider the open balls of radius \(D/2\) around these vectors in the sign cube, giving coordinate \(j\) weight \(e_j\log p_j\). They are disjoint. For \(a\le\lfloor\delta k/64\rfloor\), the mean weight of a uniformly chosen \(a\)-element set of coordinates is \(a\log u/k\le D/4\). At least half of these subsets have weight \(<D/2\), by Markov's inequality. Consequently one ball contains at least \(\tfrac12\binom{k}{\lfloor\delta k/64\rfloor}\) sign vectors. Counting cells and dividing by \(2^k\) proves the first estimate. For the simpler bound, \(a=\lfloor\delta k/64\rfloor\ge\delta k/128\) and \(\binom ka\ge(k/a)^a\ge(64/\delta)^{\delta k/128}\). Also \(e(1+4/\delta)<64/\delta\).

## Allowing a nonsquare complementary factor

Let \(d\) be positive and squarefree and \(u>1\) odd. Count positive pairs \((x,y)\) with \(x^2+dy^2=u^2,\ \gcd(u,x)=1\), assuming at least one exists. Define \(H_S\) using \(u^2/(\sqrt d\,xy)\) in place of \(u^2/(vw)\) and the repetitions in \(xy\). Let \(G\) be the ray class group of \(K=\mathbb Q(\sqrt{-d})\) modulo \(2\mathcal O_K\), of size \(h\). The same two fraction bounds hold multiplied by at most \(6\cdot2^h\). In particular the fraction still decays exponentially as \(k=\omega(u)\to\infty\) for fixed \(\delta>0,\ r+1\le\delta k/256\), even for varying \(d\) satisfying \(\sqrt d(1+\log d)=o(k)\).

To see the separation inequality, let \(\alpha=x+y\sqrt{-d},\ \beta=\alpha/u\). At any \(p\mid u\), the ideals of \(\alpha\) and \(\bar\alpha\) cannot have a common prime, since their sum of generators is \(2x\). All such primes \(p\) split, and the ideal \((\alpha)\) chooses one of the two prime ideals at \(p\), to exponent \(2v_p(u)\). For different signs \(s,t\), put \(\rho=\beta_s/\beta_t\). By its ideal factorization both \(U_I^2\rho\) and \(U_I^2\rho^{-1}\) are algebraic integers. Thus \(N=U_I^4(\rho^2-\rho^{-2})\) is a nonzero algebraic integer, since different signs give \(\rho\) a nontrivial fractional ideal. If \(Q\mid\gcd(x_sy_s,x_ty_t)\), then \(\gcd(Q,u)=1\), and \(\beta_s^4,\beta_t^4\equiv1\bmod Q\) away from \(u\) by the same identity as above, with \(\sqrt{-d}\) replacing \(i\). Hence \(N\in Q\mathcal O_K\). A nonzero imaginary quadratic algebraic integer has complex absolute value at least one by taking its norm. It follows that \(Q\le|N|\le8U_I^4/\min(A_s,A_t)\), now with \(A_s=u^2/(\sqrt d\, x_sy_s)\). The counting proof for sign patterns is unchanged. For a given pattern there are at most six generators, by the unit groups of imaginary quadratic fields.

For a lower bound on the number of actual pairs, anchor any one solution \(\alpha_0\). Flipping each prime's sign changes its ideal by a fixed fractional ideal of norm one. If the product of the selected flips is trivial in \(G\), it has a generator \(a\equiv1\bmod2\mathcal O_K\) locally at 2. Then \(\alpha'=\alpha_0a\) is integral, has norm \(u^2\), and is congruent to \(\alpha_0\) modulo \(2\mathcal O_K\). In particular \(\alpha'\in\mathbb Z[\sqrt{-d}]\). Its primitive ideal allocation gives \(\gcd(u,\operatorname{Re}\alpha')=1\): if \(p\mid u,\operatorname{Re}\alpha'\), then \(p\) splits and does not divide \(d\), so it would divide both coordinates. Neither coordinate vanishes, because \((\alpha')\ne(\bar\alpha')\).

In a finite group of size \(h\), the product of independent optional flips has probability at least \(2^{1-h}\) at every value it attains. At a step where the support grows, the least positive mass drops by at most a factor of two. At a step where the support is stable it cannot drop, since every new mass averages two old positive masses. There are at most \(h-1\) growth steps, and the identity is attained by the empty set. Thus at least \(2^{k+1-h}\) sign patterns give integral solutions, and taking positive coordinates identifies at most two patterns. This yields the stated factor in the fraction bound. Finally \(h\le4h_K\) by the ray class exact sequence, and \(h_K\ll\sqrt d(1+\log d)\): Minkowski's ideal class bound gives representatives of norm \(O(\sqrt d)\), and the number of ideals of norm \(a\) in a quadratic field is at most the divisor function \(\tau(a)\).
