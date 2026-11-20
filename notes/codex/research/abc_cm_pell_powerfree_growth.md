# Quantitative lower bounds for Pell values modulo all powers

Let \(M_n=|F_{11}(a_n,b_n)|\) on the positive Pell orbit \(b_n+a_n\sqrt2=(1+\sqrt2)^n\). With \(v_p=v_p(M_n)\) define

\[
 d_{n,k}=\prod_{p\mid M_n}p^{\,v_p\bmod k},\qquad
 R_{n,k}=\operatorname{rad}(d_{n,k}),\qquad k\ge2.
\]

Write \(\log_j\) for the \(j\)-fold iterated logarithm in asymptotic estimates. There is an effective \(c>0\), depending only on the fixed form and the Pell unit, such that for all sufficiently large \(n\) and **all** \(k\ge2\)

\[
 \begin{split}
 d_{n,k}&\ge \exp\left(c\frac{(\log n)^{1/3}}{\log_2 n}\right),\\
 \log R_{n,k}&\gg \frac{\log_2 n\,\log_3 n}{\log_4 n},\\
 P^+(R_{n,k})&\gg\frac{\log_2 n\,\log_3 n}{\log_4 n}.
 \end{split}                                                     \tag{1}
\]

For every fixed \(k\), one has the stronger \(R_{n,k}\gg_k n^{\delta_k}\) and \(P^+(R_{n,k})\gg_k\log n\) with effective \(\delta_k>0\). In particular the squarefree part is at least a fixed positive power of the Pell index. The prime witnessing an exponent nonzero modulo \(k\) can itself have exponent greater than one. These estimates control what remains after taking out a \(k\)-th power. [Pell normalization and effective all-exponent argument](abc_cm_pell_effective_powers.md)

An equivalent consequence for common exponents is that, for a sufficiently small effective \(c'>0\), the gcd of the positive \(v_p(M_n)\) at primes \(p>c'\log_2 n\,\log_3 n/\log_4 n\) is one for every sufficiently large \(n\). Taking \(k\) larger than every valuation guarantees the set is nonempty. Applying (1) with each prime \(k\) excludes every prime divisor of its gcd.

## A bound retaining the dependence on the exponent

The calculation below gives absolute effective constants \(C_0,C_1\) for the fixed form such that

\[
     \log(2+n)\le C_0 k^{C_1}\log(2kR_{n,k}).                    \tag{2}
\]

Use the separable degree-50 polynomial \(L\) and \(x=(1+\sqrt2)^{4n}\) from the linked note, so \(L(x)=-2^{175}(1+\sqrt2)^{100n}F_{11}(a_n,b_n)\). Fix a number field \(K\) splitting \(L\) and containing \(\sqrt2\). Choose a fixed positive rational integer \(a\) clearing the denominators of its roots, and denote the now-integral roots after scaling by \(\alpha_i\). Write \(X=ax\). Enlarge a fixed finite set \(S_0\) of rational primes to include 2, the primes from the leading coefficient and scaling, the discriminant of \(K\), and the prime divisors of the norms of the nonzero root differences. At every finite place of \(K\) off \(S_0\), the factors \(X-\alpha_i\) can have positive valuation for at most one \(i\). Their product differs from \(M_n\) by a unit at this place. Consequently \(v(X-\alpha_i)\) is divisible by \(k\) whenever the underlying rational prime lies outside \(S_0\) and does not divide \(R=R_{n,k}\).

Use three distinct roots, choose \(\zeta=\exp(2\pi i/k)\), and choose \(u_i^k=X-\alpha_i\) for \(i=1,2,3\) at a fixed complex embedding, taking \(u_i=X^{1/k}(1-\alpha_i/X)^{1/k}\) with the branch near 1. Put \(H=K(\zeta,u_1,u_2,u_3)\), with degree \(D\le [K:\mathbb Q]k^4\). It is unramified outside primes in \(S_0\) or dividing \(kR\). Indeed at every other prime the valuation of each radicand is divisible by \(k\). Removing the corresponding \(k\)-th power of a local uniformizer leaves a unit, whose \(k\)-th roots form a finite étale algebra there. The same holds for the roots of unity.

The absolute field discriminant thus satisfies

\[
         \log|\Delta_H|\ll k^{C}\log(2kR).                        \tag{3}
\]

Here and below \(C\) denotes an absolute effective exponent which may increase between bounds. To verify (3), the exponent of a rational prime \(q\) in a degree-\(D\) field discriminant is at most \(D(1+\log_q D)\). Locally, pass to the maximal unramified subfield and use the Eisenstein polynomial of a uniformizer in the totally ramified part. Its derivative has valuation at most \(e-1+e\,v_q(e)\), since the nonzero derivative terms have different valuations modulo \(e\). Summing after multiplication by residue degrees gives the stated estimate. Summing over \(q\mid kR\prod_{p\in S_0}p\) proves (3).

Each \(u_i\) is an algebraic integer, and

\[
 \prod_{j=0}^{k-1}(u_1-\zeta^j u_i)=\alpha_i-\alpha_1 \quad(i=2,3).
\]

It follows that

\[
                  Y=\frac{u_1-\zeta u_2}{u_1-\zeta u_3}
\]

is an \(S_H\)-unit, where \(S_H\) contains the infinite places and the places over the **fixed** rational primes in \(S_0\). At the chosen embedding \(Y\ne1\), since the roots are distinct, and

\[
            |Y-1|\ll X^{-1},\qquad h(Y)\ll n+1.                 \tag{4}
\]

Both implied constants are independent of \(k\). For \(X\) large in terms of the fixed roots, the factors \((1-\alpha_i/X)^{1/k}\) differ from 1 by \(O(1/(kX))\). The inequality \(|1-\zeta|\ge 4/k\) keeps the denominator above a fixed multiple of \(X^{1/k}/k\). The height inequality follows from \(h(u_i)=h(X-\alpha_i)/k\) and the standard estimates for heights of sums and products.

## Bounding the \(S_H\)-unit logarithms

Put \(W=1+k^C\log(2kR)\), enlarging the effective exponent as needed. The rank \(t\) of the \(S_H\)-unit group is \(O(D)\), since \(S_0\) is fixed. It has fundamental \(S_H\)-units \(\eta_1,\ldots,\eta_t\) for which

\[
 \log(2+\max_i h(\eta_i))\ll W,\qquad
 \log(2+\max_i|b_i|)\ll W+\log(2+h(Y)),
 \quad Y=\omega\prod_i\eta_i^{b_i}                              \tag{5}
\]

with \(\omega\) a root of unity. The dependence needed in (5) can be verified as follows.

* A coarse bound for the ordinary regulator and class number follows directly from the completed Dedekind zeta function. Let \(\xi_H(s)=s(s-1)\Lambda_H(s)\) with the usual completed zeta function. For real \(s>1\), the logarithmic derivative of \(\xi_H\) is nonnegative. In its Hadamard product centered at \(1/2\), pair zeros \(\rho,1-\rho\). The functional equation makes the residual exponential factor constant, and the real part of each \(1/(s-\rho)\) is positive. Central zeros contribute a nonnegative term as well. Thus \(\xi_H(1)\le\xi_H(2)\). On substituting the gamma factors and \(\zeta_H(2)\le\zeta(2)^D\), this gives \(\operatorname{Res}_{s=1}\zeta_H(s)\le C^D|\Delta_H|^{1/2}\). The analytic class number formula implies \(h_H R_H\le C^D w_H|\Delta_H|\), where the number of roots of unity \(w_H\le2D^2\) follows from \(\varphi(w_H)\ge\sqrt{w_H/2}\).
* Use logarithmic coordinates \(\log|\cdot|_v\) weighted by local degrees, so their sum is zero. The covolume of the lattice of \(S_H\)-unit logarithms is at most \(\sqrt{t+1}\,h_H R_H\prod_{\mathfrak q\in S_{H,\rm fin}}\log N\mathfrak q\), up to an absolute factor \(2^{O(D)}\) for archimedean normalization. This follows by projecting to the finite valuations, whose image has index at most \(h_H\) in the full lattice of integral valuations by the ideal class map. There are \(O(D)\) such primes, and \(\log N\mathfrak q=O(D)\). Thus the logarithm of the covolume has the required upper bound \(O(W)\).
* A nontorsion element of degree at most \(D\) has height at least \(\exp(-C D^2)\). Indeed there are at most \(\exp(CD^2)\) algebraic numbers of degree at most \(D\) and height at most 1, by counting integral minimal polynomials with coefficients bounded by \(2^D e^D\). Distinct successive powers up to the reciprocal height would all occur in this count. Thus every nonzero lattice vector has Euclidean length at least \(\exp(-C D^2)/\sqrt{t+1}\), by the sum formula for the height. Minkowski's successive minima inequalities now give a lower bound \(\exp(-C D^{C})\) for the covolume and an upper bound \(\exp(CW)\) for the last successive minimum. A lattice of rank \(t\) has a basis of vectors of length at most \(t\) times its last minimum. Cramer's rule, the covolume lower bound and the estimates for these basis vectors give (5) after enlarging the exponent of \(k\) in \(W\). The Euclidean length of the logarithm vector of \(Y\) is at most \(2D h(Y)\).

Apply the complex logarithmic linear form theorem of Baker and Wüstholz to \(\log Y\) near zero. Use principal logarithms of the fundamental units and the root of unity. A further term \(2l\log(-1)\), with \(|l|\ll1+t\max|b_i|\), makes the resulting form equal to this chosen logarithm. Omit trivial factors. The form is nonzero by (4). In the Baker–Wüstholz bound the logarithm of the coefficient depending only on field degree and the number of logarithms is \(O((t+D+2)^C)\), as follows immediately from the usual factorial formula. The product of the modified heights has logarithm at most \(O(tW)\) by (5), since each principal logarithm has absolute value at most \(D h(\eta_i)+\pi\). Absorbing these polynomials in \(k\) into \(W\) gives

\[
       -\log|Y-1|\le \exp(CW)\big(W+\log(2+n)\big).
\]

Combining with (4), using \(\log X\asymp n\), yields \(\log(2+n)\ll W\). This proves (2). [Baker and Wüstholz, *Logarithmic forms and group varieties*](https://doi.org/10.1515/crll.1993.442.19)

## Removing the exponent from the estimates

Write \(d=d_{n,k}\), \(M_n=d y^k\). If \(y=1\), \(d=M_n\asymp (1+\sqrt2)^{100n}\). If \(y\ge2\), apply the near-one comparison from the first note with \(d/A\) as a **single** fixed-at-this-evaluation algebraic factor, of logarithmic height \(O(1+\log d)\). Writing \(n=tk+r\) as there gives

\[
 k\ll (1+\log d)\log(2k),\quad
 k\ll (1+\log d)\log(2+\log d).
\]

Since \(R\le d\), (2) gives \(\log(2+n)\ll(1+\log d)^C\), giving a positive absolute power of the logarithm in the exponent. The last section sharpens this to the first bound in (1).

For the support estimates include the primes dividing \(R\) as separate logarithms. With \(s=\omega(R)\), Matveev's real bound from the first note gives, for \(y\ge2\),

\[
  \log k\ll 1+s+\sum_{p\mid R}\log\max(2,\log p).
                                                               \tag{6}
\]

For \(y=1\) the same upper bound holds for \(\log n\) by the smooth-value calculation. If \(P=P^+(R)\), the right side is \(O(1+P\log_2(3P)/\log(3P))\) by the elementary prime count upper bound. Also \(\log R\ll P\) by Chebyshev. Together with (2) this bounds \(\log_2 n\) by the same expression, and inversion proves the last estimate in (1).

For the middle estimate put \(U=\log R\) for \(R\) sufficiently large. The primes dividing \(R\) and at most \(\sqrt U\) contribute \(O(\sqrt U\log(2+\log U))\) to (6). For the others, \((1+\log\max(2,\log p))/\log p\ll \log_2 U/\log U\), as this ratio is eventually decreasing. Their contribution is \(O(U\log_2 U/\log U)\). Thus (2) and (6), or the smooth-value bound alone if \(y=1\), imply \(\log_2 n\ll U\log_2 U/\log U\). Inversion gives the asserted lower bound for \(\log R\). At fixed \(k\), (2) immediately gives the stated power of \(n\), and \(\log R\ll P\) gives the greatest-prime estimate.

## A sharper degree and regulator estimate

The argument just given yields \(d\ge\exp(c(\log n)^\delta)\) for an effective absolute \(\delta>0\), using the elementary height separation from counting. The displayed first bound in (1) uses the following strengthened version of (2),

\[
     \log(2+n)\ll k^2\log(2k)\log(2kR).                          \tag{7}
\]

For \(k=2\) this already follows from (2) with an absolute fixed constant. For \(k\ge3\), take \(\zeta\) primitive as before, but use the field
\[
 H=K(\zeta,u_2/u_1),\qquad D=[H:\mathbb Q]\le [K:\mathbb Q]k^2.
\]
It is a subfield of the radical field already shown unramified off \(S_0\) and \(kR\). In \(H\) take
\[
    V=\frac{u_1-\zeta u_2}{u_1-\zeta^2 u_2},\qquad
    Y=(1+\zeta)V .
\]
The numerator and denominator of \(V\) have valuations zero away from \(S_0\) in the larger field, by the product of the \(k\) differences. Thus \(V\) is an \(S_H\)-unit in the smaller field. The factor \(1+\zeta\ne0\) has height at most \(\log2\) and can enter the logarithmic form as an extra factor. Subtracting one from \(Y\) gives \(\zeta(u_1-u_2)/(u_1-\zeta^2u_2)\). Since \(k\ge3\), \(|1-\zeta^2|\gg 1/k\), and the estimates (4) hold uniformly. Also \(h(V)\ll1+n\).

Write \(W_1=1+\log|\Delta_H|+D\log(2D)\). Voutier's effective lower bound for the absolute logarithmic height gives \(h(\gamma)\gg D^{-2}\) for every nontorsion algebraic number of degree at most \(D\). Hence the first minimum \(\lambda_1\) of the logarithmic \(S_H\)-unit lattice is at least \(cD^{-2}/\sqrt{t+1}\). The covolume upper bound above gives \(\log\operatorname{covol}\ll W_1\), and the shortest-vector lower bound gives \(-\log\operatorname{covol}\ll D\log(2D)\) by packing. For all successive minima \(\lambda_i\), Minkowski's second theorem gives
\[
    \sum_{i=1}^t\log\max(1,\lambda_i)\ll W_1.
\]
Indeed the logarithm of the product of the minima is at most \(\log\operatorname{covol}+O(t\log(2t))\), and discarding factors below one costs at most \(O(t\log(2D))\). [Voutier, *An effective lower bound for the height of algebraic numbers*](https://doi.org/10.4064/aa-74-1-81-95)

There is a basis with the \(i\)-th length at most \((i+1)\lambda_i\). To see this, choose successive independent lattice vectors \(w_i\) attaining the minima. The quotient of the saturated lattice in their first \(i\) real directions by the first \(i-1\) directions is infinite cyclic. A lifting \(b_i\) of its generator has orthogonal projection to the new direction of length at most \(\|w_i\|\). Subtract integer multiples of \(w_1,\ldots,w_{i-1}\) to put its tangential component in the centered fundamental parallelotope of those vectors, of radius at most \((i-1)\|w_i\|/2\). These \(b_i\) give the desired basis. It follows that the logarithm of the product of the modified heights of the corresponding units is \(O(W_1)\). Cramer's rule using this product-of-lengths upper bound and the covolume lower bound gives
\[
      \log(2+\max|b_i'|)\ll W_1+\log(2+h(V))
\]
for the exponents \(b_i'\) of \(V\) in this basis. Here a modified height, enlarged to at least 1, can be bounded by \(O(D)\) times the larger of 1 and the basis vector length, using the principal branch of the logarithm.

The Baker–Wüstholz constant \(18(l+1)!\,l^{l+1}(32D)^{l+2}\log(2lD)\) for \(l\le t+3\) logarithms has logarithm \(O(D\log(2D))\). The additional factors \(1+\zeta,\omega,-1\) have modified heights \(O(D)\). Consequently (4) and the linear form bound give \(n\ll\exp(CW_1)(W_1+\log(2+n))\), or \(\log(2+n)\ll W_1\). The local different calculation gives \(\log|\Delta_H|\ll D(1+\log D)\log(2kR)\). The sharper degree \(D\ll k^2\) proves (7).

Finally put \(u=1+\log d\). When \(y\ge2\), the single-factor Matveev estimate gives \(k\ll u\log(2u)\). Thus (7) and \(R\le d\) imply \(\log(2+n)\ll (u\log(2u))^3\). Inversion proves \(\log d\gg(\log n)^{1/3}/\log_2 n\) for all sufficiently large \(n\), uniformly in \(k\). The case \(y=1\) follows from \(d=M_n\).
