# Excluding perfect powers at every squarefull index for integer bases

For every integer \(A\ge2\) and every squarefull \(m>1\),
\[
                              \Phi_m(A)\quad\text{is not a square}.
\]
In fact, put \(d=\operatorname{rad}(m)\) and \(D=\varphi(d)\). For **each prime \(\ell\mid D\)**, \(\Phi_m(A)\) is not an \(\ell\)-th power. Equivalently the gcd of the positive prime valuations of \(\Phi_m(A)\) is coprime to \(D\).

Squarefull means \(v_p(m)\ge2\) for every \(p\mid m\). Both \(A\) and the support of \(m\) vary freely. Put \(u=m/d\); then \(d\mid u\) and \(\Phi_m(A)=\Phi_d(A^u)\). When \(d=2\), the value is a square plus one strictly between consecutive squares. For every \(d>2\), \(D\) is even, so the general perfect-power assertion includes the nonsquare case. Below take \(X=A^u\ge2^d\), fix a prime \(\ell\mid D\), and put \(s=D/\ell\).

## A rational approximation with an exact denominator

On \(|t|<1\), take the analytic root \(G(t)=\Phi_d(t)^{1/\ell}\) satisfying \(G(0)=1\), and write its coefficients \(c_j\). For squarefree \(d>1\) the coefficient of \(t\) in \(\Phi_d(t)\) is \(-\mu(d)=\pm1\), by the product formula in \(1-t^h\). In the binomial expansion of \(G\), the contribution to \(c_j\) from \(\binom{1/\ell}{j}(\Phi_d(t)-1)^j\) is \(\pm\binom{1/\ell}{j}\). Its denominator in lowest terms is
\[
                            D_j=\ell^{j+v_\ell(j!)} .
\]
Indeed the product formula for the binomial coefficient gives this exact \(\ell\)-part, since every integer \(1-i\ell\) is prime to \(\ell\). At each other prime \(q\), approximate \(1/\ell\) by positive integral exponents \(N\) in \(\mathbf Z_q\); the integers \(\binom Nj\) tend to \(\binom{1/\ell}j\), which is therefore \(q\)-integral. The lower binomial powers have strictly smaller denominators and integral multipliers. Thus \(c_j\) also has denominator exactly \(D_j\).

For every integer \(X\ge2\), the truncation \(P_X=\sum_{j=0}^s c_jX^{s-j}\) has denominator exactly \(D_s\), since the last term has uniquely largest denominator. Its distance from every integer is at least \(1/D_s\). The factorial valuation bound \(v_\ell(s!)\le(s-1)/(\ell-1)\) and \(\ell\le2^{\ell-1}\) give \(D_s\le \ell^{(D-1)/(\ell-1)}\le 2^{D-1}\). By reciprocity \(X^sG(1/X)=\Phi_d(X)^{1/\ell}\), using the positive real root.

## Bounding the error for composite support

For a squarefree composite \(d\), define \(R_d(k)=\sum_{\zeta}\zeta^k\), summing over the primitive \(d\)-th roots. The Ramanujan sum is \(\mu(d/g)\varphi(g)\), \(g=\gcd(d,k)\), by the Chinese remainder theorem or Möbius inversion. In particular \(|R_d(k)|\le g\le k\). Factoring \(\Phi_d(t)=\prod_{\zeta}(1-\zeta t)\) gives
\[
       \log G(t)=-\ell^{-1}\sum_{k\ge1}R_d(k)t^k/k .
\]
Consequently on \(|t|=r<1\), \(|G(t)|\le\exp(r/[2(1-r)])\). Take \(r=\exp(-1/\sqrt d)\). Since \(e^z>1+z\) for \(z>0\), this last bound is less than \(\exp(\sqrt d/2)\). Cauchy's coefficient estimate and the geometric tail give
\[
 |\Phi_d(X)^{1/\ell}-P_X|
 <\frac{\exp(\sqrt d/2+(s+1)/\sqrt d)}
           {X(1-\exp(1/\sqrt d)/X)}
 \le \frac{\exp(\sqrt d+1/\sqrt d)}
           {X(1-\exp(1/\sqrt d)/X)} .
\]
Here \(s\le d/2\). This bound and \(D_s\) give a numerical criterion even when \(d\nmid u\).

Factor the composite squarefree \(d=vw\) with \((v,w)=1\) and \(v,w>1\). Since \(D\le(v-1)(w-1)\),
\[
                 d-D+1\ge v+w\ge2\sqrt d .
\]
We have \(d\ge6\), so \(X\ge2^d\ge64\) and \(1-\exp(1/\sqrt d)/X>31/32\). The displayed tail is less than \(2^{1-D}\le1/D_s\), since
\[
             (2\log2-1)\sqrt d
                    >1/\sqrt d+\log(32/31)\qquad(d\ge6).
\]
The last strict inequality holds at 6, and its two sides respectively increase and decrease with \(d\). The \(\ell\)-th root therefore cannot be an integer.

## Prime support

If \(d=p\) is an odd prime, then \(G(t)=(1-t^p)^{1/\ell}(1-t)^{-1/\ell}\). Since \(s=(p-1)/\ell<p\), the coefficients through \(s\) equal those of \((1-t)^{-1/\ell}\). Its coefficients are positive and at most one, by their binomial recurrence. At \(t=1/X\), dropping its tail and restoring the factor \((1-t^p)^{1/\ell}\) cost, after multiplication by \(X^s\), at most
\[
         \frac{1}{X-1}+\frac{X^{s-p}}{1-1/X}<\frac2X .
\]
This uses \(0\le 1-(1-t^p)^{1/\ell}\le t^p\), \(s-p\le-2\), and \(X\ge2^p\ge8\). The bound is less than \(1/D_s\), since \(D_s\le2^{p-2}\). This proves the assertion for all squarefull \(m>1\). [Related prime-power estimate with two varying inputs](abc_mersenne_prime_power_parity.md)

## What the nonsquare gives for multiplicative orders

At a squarefull \(m>1\), at least one prime occurs to odd exponent in \(\Phi_m(A)\). If \(P\) is the largest prime of \(m\) and \(m/P^{v_P(m)}>P-1\), every such prime is primitive, for every \(A\ge2\). Indeed an imprimitive prime \(p\mid\Phi_m(A)\) must divide \(m\). Setting \(h=m/p^{v_p(m)}\), one has \(\Phi_m(T)=\Phi_h(T)^{\varphi(p^{v_p(m)})}\bmod p\) for \(p\nmid h\). Thus \(\operatorname{ord}_p(A)=h\mid p-1\). A prime factor of \(m\) larger than \(p\) would divide \(h\), which is impossible. Only \(p=P\) can cause this obstruction, and the stated inequality excludes it. The nonsquare result by itself does not determine whether a witnessing prime has valuation one.

## A uniform squarefree-part bound with unrestricted index primes

Let \(Q>1\) be any squarefree integer, \(k=\omega(Q)\), and \(A\ge2\) any integer. With \(\operatorname{sf}(M)=\prod_{v_p(M)\ {\rm odd}}p\), one obtains
\[
 \boxed{\displaystyle
  \operatorname{sf}(A^{Q^2}-1)
       \ \ge\ \frac{Q^{\,2^k-2}}{\varphi(Q)}
       \ >\ Q^{\,2^k-3}.}
\]
At least \(2^k-1-k\) distinct odd primes in the full difference occur to odd exponent. This bound is uniform in the set of primes of \(Q\).

For every \(b\mid Q,\ b>1\), the index \(d=b^2\) is squarefull. Choose a prime of odd valuation in \(\Phi_d(A)\). If it is imprimitive, the classification above gives
\[
                        d=p^2\operatorname{ord}_p(A)
\]
with \(p\mid Q,\ p\nmid A\), since the exponent of \(p\) in \(d\) is exactly two. Each \(p\mid Q\) therefore accounts for at most one possible bad index, and its index is at most \(p^2(p-1)\). This includes \(p=2\) with order one for odd \(A\). Delete all indices admitting such an imprimitive divisor. The product of the deleted indices is at most \(\prod_{p\mid Q}p^2(p-1)=Q^2\varphi(Q)\).

Each remaining index \(d>1\) has an odd prime \(p_d\) of exact order \(d\) occurring to odd exponent. These primes are distinct, and \(p_d\ge d+1\). Even if \(p_d\mid Q\), its valuation in \(A^{Q^2}-1\) is still odd: lifting adds \(v_{p_d}(Q^2/d)=v_{p_d}(Q^2)\), an even number since \(p_d\nmid d\). Finally \(\prod_{b\mid Q}b^2=Q^{2^k}\). Multiplying the surviving \(d\)'s proves the bound and counting them gives the assertion about distinct primes.

For \(A=2\), a proof of abc on this sequence would need \(\log\operatorname{rad}(2^{Q^2}-1)\ge(1-o(1))Q^2\log2\). The bound above supplies a log squarefree part of order at least \((2^{\omega(Q)}-3)\log Q\).

For arbitrary \(N>1\) the same argument gives a product bound. Let \(\mathcal D(N)\) be the set containing \(1\) and all squarefull divisors of \(N\). If \(p^a\parallel N\), put \(b_a=\sum_{j=2}^a j=a(a+1)/2-1\). Then
\[
 \operatorname{sf}(A^N-1)\ \ge\
 \frac{\displaystyle\prod_{d\in\mathcal D(N)}d}
      {\displaystyle\prod_{p^a\parallel N}
                 p^{b_a}(p-1)^{a-1+(a\bmod2)}}.
\]
To see this, first discard any order with an imprimitive divisor \(p\). For fixed \(p\) these orders are among \(p^j\operatorname{ord}_p(A)\), \(2\le j\le a\), with total product at most \(p^{b_a}(p-1)^{a-1}\). Next discard the order \(\operatorname{ord}_p(A)\) for each \(p^a\parallel N,\ p\nmid A\) with \(a\) odd, at an additional cost of at most \(p-1\). At every surviving order \(d>1\), a primitive odd-valuation prime exists and retains odd valuation at \(N\). The numerator can be evaluated by allowing independently the exponents \(0,2,\ldots,a\) at each prime. For \(N=Q^t\), \(Q\) squarefree with \(k\) prime factors, \(t\ge2\), this gives
\[
 \operatorname{sf}(A^{Q^t}-1)\ \ge\
 \frac{Q^{(t^{k-1}-1)b_t}}{\varphi(Q)^{t-1+(t\bmod2)}} .
\]
