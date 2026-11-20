# A strict improvement over a squared logarithm from simultaneous marked primes

Let \(F=F_{11}\) be the degree-100 binary form in the degree-968 family. Fix a nonempty finite set \(S\) of good odd primes where \(F\) has a simple projective root with unit quadratic norm, and let \(D=\prod_{p\in S}p\). There is an effective \(\delta_S>0\) and infinitely many primitive specializations of this one family for which
\[
      C/\operatorname{rad}(ABC)\gg_S (\log C)^{2+\delta_S}.
\]
At each selected specialization every prime in \(S\) has the same exact valuation in \(F\), and these common valuations tend to infinity. Only the marked primes and a bounded norm radical enter the lower bound. The exponent improvement follows by comparing the two *largest* successive minima in a lattice of rank at least three. [Family and whole-radical bound](abc_cm_pell_whole_triple.md)

## The exponent lattice

Use coordinates \(\alpha=b+a\sqrt2\) in \(K=\mathbb Q(\sqrt2)\), with conjugation denoted by a bar. Choose a fixed integral \(\alpha_0\) representing a selected root modulo each \(p\in S\) by the Chinese remainder theorem. Its norm is a unit at these primes. For any fixed \(d\ge3\), take
\[
      \eta_i=1+D m_i\sqrt2,\qquad u_i=\eta_i/\bar\eta_i .
\]
Choose \(m_1=1\) and take each later positive \(m_i\) to be a multiple of all the preceding absolute norms. The norms \(2D^2m_i^2-1\) are greater than one, odd, pairwise coprime, and prime to \(D\). Each \(\eta_i\) is coprime to its conjugate because their sum is 2. Thus each has a split prime ideal in its support which is absent from all the other generators and from its own conjugate. Its valuation establishes multiplicative independence of the \(u_i\).

Let \(\Lambda_k\subseteq\mathbb Z^d\) be the kernel of the map sending \(z\) to the projective class of \(\prod_i\eta_i^{z_i}\) modulo \(p^k\) simultaneously for all \(p\in S\). Negative exponents are taken in the unit groups there. Equivalently, the product \(\prod_i u_i^{z_i}\) is 1 modulo these prime powers in the quadratic algebra. Indeed the difference between a unit and its conjugate is twice its \(\sqrt2\)-coefficient times \(\sqrt2\), both factors being units at the marked odd primes. The local projective principal group at \(p\) has order \(p^{k-1}\), by counting scalar classes with representatives \(1+pt\sqrt2\). The first generator spans it since \(v_p(u_1-1)=1\), and raising to the power \(p\) increases the depth by exactly one. The local orders are coprime across \(S\), so
\[
      [\mathbb Z^d:\Lambda_k]=D^{k-1},\qquad
      D\Lambda_k\subseteq\Lambda_{k+1}\subseteq\Lambda_k .
\]
Normalize each valuation by \(v_p(p)=1\), using either place over a split marked prime.

## The two largest successive minima

Let \(\lambda_i(k)\) be the successive minima for the sup norm. Infinitely many \(k\) satisfy
\[
                    \lambda_d(k)\le D\lambda_{d-1}(k).
                    \tag{1}
\]
Otherwise, for every large \(k\) the vectors in \(\Lambda_k\) of length strictly smaller than \(\lambda_d(k)\) span a rational hyperplane \(W_k\). In \(\Lambda_{k+1}\) one can find \(d-1\) independent vectors of length at most \(D\lambda_{d-1}(k)<\lambda_d(k)\). They can be chosen to realize \(\lambda_{d-1}(k+1)\) and span \(W_{k+1}\), so \(W_{k+1}=W_k\). Denote this fixed hyperplane by \(W\), and put \(L=W\cap\mathbb Z^d\).

For any fixed nonzero \(w\in L\) the algebraic number \(u(w)=\prod_i u_i^{w_i}\) differs from one, and its depth \(e_p=v_p(u(w)-1)\) is positive and finite at every marked prime. The local projective order of \(w\) at level \(k\) is \(p^{\max(0,k-e_p)}\). Its combined order is therefore \(\gg_w D^k\). This gives \([L:L\cap\Lambda_k]\gg_w D^k\). The first \(d-1\) ambient minima are also the minima in \(W\) with its induced norm. Minkowski's second theorem in \(W\) gives \(\prod_{i<d}\lambda_i(k)\gg_W D^k\), taking one fixed \(w\). Its ambient version gives \(\prod_{i\le d}\lambda_i(k)\asymp_d D^{k-1}\). Consequently \(\lambda_d(k)\) would be bounded. Every fixed nonzero integer vector eventually leaves \(\Lambda_k\) by multiplicative independence, so even \(\lambda_1(k)\) tends to infinity. This proves (1).

For a fixed number field, finite place \(v\), and fixed algebraic \(v\)-units \(t_1,\ldots,t_m\), the fixed-data consequence of Yu's Theorem 1 is
\[
  v(t_1^{b_1}\cdots t_m^{b_m}-1)
     \le K_{v,t_1,\ldots,t_m}\log\max(3,|b_1|,\ldots,|b_m|)
     \quad(t_1^{b_1}\cdots t_m^{b_m}\ne1).
                    \tag{2}
\]
The constant is effective. Any auxiliary field enlargement used in the theorem stays fixed, and valuation normalization changes the constant only. See Kunrui Yu, *p-adic logarithmic forms and group varieties III*, Forum Math. **19** (2007), 187–280, Theorem 1. [Fixed-place specialization and explicit formulas](https://arxiv.org/abs/1903.00977)

Apply (2) to the \(u_i\) at one fixed \(p\in S\). Every nonzero vector in \(\Lambda_k\) then has length \(\gg D^{\kappa k}\), where one may take any sufficiently small effective \(0<\kappa<1/d\) depending on the fixed data. Along (1) the product of all the minima gives
\[
       \lambda_d(k)\ll_{S,d}D^{\theta k},\qquad
       \theta=\frac{1-(d-2)\kappa}{2}<\frac12 .
                    \tag{3}
\]
There is also an elementary version. Clearing the fixed algebraic denominators in \(u(z)-1\), all of them units at \(p\), gives a nonzero algebraic integer whose absolute norm is at most \(\exp(O(1+\|z\|))\). If \(z\in\Lambda_k\) its norm is divisible by \(p^k\). Thus \(\lambda_1(k)\gg k\) and (1) yields \(\lambda_d(k)\ll D^{k/2} k^{-(d-2)/2}\). This proves a lower bound \(\gg (\log C)^2(\log\log C)^{d-2}\) in the construction below independently of (2).

## Exact depths, the complete radical, and the fixed-prime limit

For each \(k\ge3\) choose at each marked prime a lift of the seed with exact \(F\)-valuation \(k-1\). Hensel lifting yields a unique root at each precision, and exactly one of the \(p\) lifts from precision \(k-1\) remains a root at precision \(k\). The unit norm makes projective multiplication simply transitive on principal lifts of the seed. Hence the chosen tuple is one coset of \(\Lambda_k\). Any coset has some exponent vector of length at most \(d\lambda_d(k)/2\), by subtracting a nearest integral combination of \(d\) independent vectors realizing the last minimum. Put \(\alpha=\alpha_0\prod_i\eta_i^{z_i}\) and take its primitive integral projective coordinates \((a,b)\). The primes of \(b^2-2a^2\) belong to the finite support of the seed and generator norms. Clearing denominators and rational common factors preserves the local classes since these norms are units at the marked primes. The family gives
\[
  \log C\ll 1+\|z\|,\qquad
  \frac C{\operatorname{rad}(ABC)}\gg D^{k-2}.
\]
The second inequality is the whole-radical estimate using the excess in \(F\). The heights tend to infinity since \(F\) has no real projective zero and the marked valuations grow. Formula (3) gives exponent \(1/\theta>2\), as asserted, with \(d=3\) sufficient.

For fixed generators, the contribution of the selected primes to the excess of \(F\) also admits a polynomial upper bound in \(\log C\). Write \(t=\alpha/\bar\alpha=(\alpha_0/\bar\alpha_0)\prod_i u_i^{z_i}\). At the split prime over a unique divisor of the norm of \(\eta_i\), its valuation is a fixed integer plus a nonzero integer times \(z_i\). The conjugate place has the opposite valuation. These valuations give \(h(t)\gg\|z\|-O(1)\) for absolute logarithmic height. Since \(t\) is a fixed fractional linear transformation of the rational projective slope, \(h(t)=\log\max(|a|,|b|)+O(1)\). The fixed degree-968 height formula now gives
\[
                 1+\|z\|\asymp 1+\log C .
\]
At a marked prime a slope of unit norm gives integral-unit coordinates \(b\pm a\sqrt2\) locally. In the coordinate \(t\), the transformed \(F\) has finitely many distinct roots \(\beta\), with no root at zero or infinity since \(F\) and the quadratic norm have disjoint zeros. Factorization in a fixed splitting field shows that, up to a bounded additive constant, its valuation is bounded above by the largest \(v(t-\beta)\). Indeed the distance to every root except a closest one has valuation bounded above by the largest valuation of a difference of two distinct roots. Roots of nonzero valuation have bounded proximity since \(t\) is a unit. For a unit root apply (2) to \(t/\beta\) by adjoining the fixed factor \(\alpha_0/(\bar\alpha_0\beta)\) with exponent one. Exact equality would give a rational projective zero of \(F\). This proves for some effective \(A=A(S,d,\alpha_0,\eta_1,\ldots,\eta_d)\)
\[
     \prod_{p\in S}p^{\max(v_p(F(a,b))-1,0)}
         \ll (1+\log C)^A .
\]
Primes outside this set can contribute further to the true whole-triple ratio. The available constants in (2) depend on the generators and their number. Formula (3) supplies a strict improvement over two, while an unbounded sequence of exponents as the rank grows remains unproved by this argument.
