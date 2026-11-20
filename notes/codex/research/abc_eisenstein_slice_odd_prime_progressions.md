# Persistent primes of odd valuation in both quartics

Fix an infinite progression of positive odd indices, a bound \(Y\), and \(k\ge1\). A subprogression and \(2k\) distinct primes above \(Y\) exist such that, at every index in that subprogression, \(k\) of the primes have prescribed exact odd valuations in \(F_4\) and the other \(k\) have prescribed exact odd valuations in \(F_5\). The primes and their odd valuations are chosen by the construction. The labels \(4,5\) refer to the respective two-adic valuations of the original paired quartics. The proof also permits any finite set of excluded primes and an arbitrarily large additional squarefree cofactor at each stage. On a separate explicitly computed progression, 533 distinct primes admit independent choices of **every** positive valuation.

## An all-height supply of new primes

Write \(d_i(n)=\operatorname{sf}(|F_i|/2^i)\), \(b_n=d_4(n)d_5(n)\), and \(J_n=|F_+F_-|/512\); here \(\operatorname{sf}\) denotes the product of primes of odd valuation. Let \(B\) be a finite set of \(s\) primes, \(V=\prod_{p\in B}p\), and split \(d_i=a_i u_i\) with \(a_i=\gcd(V,d_i)\). For either \(i\),
\[
 \#\{n\ge3\text{ odd}:u_i(n)\le Z\}
   \le C(1+C)^s\sum_{u\le Z} C^{\omega(u)}
   \ll (1+C)^s Z(\log(2Z))^A.                                       \tag{1}
\]
This follows by summing the [individual all-height fiber bound](abc_eisenstein_slice_squareclass_census.md) over \(a_i\mid V\) and \(u\le Z\). In particular, among any \(\lfloor2C(1+C)^s\rfloor+1\) distinct odd indices at least one has in each \(d_i\) an odd-valuation prime outside \(B\). These two primes are distinct by coprimality. With the larger search bound from (1) both outside parts may exceed any prescribed \(Z\). Thus these searches terminate on every input progression. The constants supplied by the uniform Mordell–Lang estimate have not been evaluated numerically here.

## Preserving the individual assignments

The original orbit uses \(P=(-2,8)\) on \(E:Y^2=X^3+36X^2+36X\). Its projective slope is determined up to sign by \(-X(nP)/2=(x_n/y_n)^2\). To transport a fixed sign along progressions, put \(n=2m+1\) and define a rational map \(\tau:E\to\mathbf P^1\) over \(\mathbf Q\). For a generic point \(R=(X,Y)\) put \(A=2R\) and \(c=(X^2-36)/(2Y)\), so \(X(A)=c^2\) by duplication. Let \(h\) be the intercept of the line through \(A\) and \(P\). Its three intersection abscissas multiply to \(h^2\), giving
\[
       X(2R+P)=-2\tau(R)^2,\qquad \tau(R)=h/(2c).
\]
A rational function on a smooth projective curve extends to a morphism to the projective line. The identity consequently holds as rational maps, including after specialization away from the displayed formulas' coordinate singularities. Thus at \(R=mP\), evaluating \(F_+,F_-\) in primitive projective coordinates of \(\tau(R)\) gives the original pair up to swapping. Sorting by two-adic valuation recovers the canonical \(F_4,F_5\).

Outside a fixed finite set \(B_0\) of primes, take the good integral models of the curve and map by spreading out the morphism. For \(p\notin B_0\), the residue of \(mP\bmod p^a\) determines the primitive projective value \(\tau(mP)\bmod p^a\) and hence all valuations of either quartic less than \(a\). Locally homogeneous evaluations in two primitive representatives differ by a fourth power of a unit. At 2, compactness of \(E(\mathbf Q_2)\) and continuity of \(\tau\) give an open finite-index subgroup on whose cosets \(\tau\bmod64\) is constant. Indeed the map to the finite projective reduction is locally constant, and a finite cover by small subgroup cosets gives a common subgroup by intersection. Choose \(D_2\) to annihilate \(P\) in the finite quotient. On the orbit, the fixed projective reduction distinguishes which signed quartic has valuation four and which has valuation five. Restrict the input progression in \(m\) to one residue class modulo \(D_2\). This costs a fixed factor and fixes the labeling for all subsequent stages.

Include \(B_0\), 2, 3 and all primes at most \(Y\) in the excluded set. Given a current progression, apply (1) with both the excluded and the previously marked primes. At a successful witness \(n_j=2m_j+1\), select one new prime from each \(d_i\). If \(v=v_p(J_{n_j})\) for any marked prime, impose \(m\equiv m_j\pmod{\operatorname{ord}(P\bmod p^{v+1})}\). The two-adic class and these congruences keep every marked prime in its assigned quartic at the attained exact odd valuation. All congruences have the common witness \(m_j\). Induction gives the stated nested progressions and the option of preserving all the primes in a selected outside cofactor.

For two new primes per stage, write \(D_0\) for the initial step in \(m\) after fixing the dyadic label. The step \(D_j\) can be taken as the lcm of \(D_0\) and the indicated orders of all marked primes. Hasse's bound and the formal kernel yield \(\operatorname{ord}(P\bmod p^{v+1})\le3p^{v+1}\). Every \(p^v\) in this product divides \(J_{n_j}\), with \(v\ge1\), whence
\[
        D_j\le D_0\,3^{2j}J_{n_j}^2,\qquad
        n_{j+1}\le n_j+2D_j\big(\lfloor2C(1+C)^{s_0+2j}\rfloor+1\big).
\]
Here \(s_0\) is the initial number of excluded primes. In particular \(\log n_{j+1}\ll n_j^2+s_0+j+\log(2D_0)\), using the quartic height upper bound. These witness bounds apply even if the starting progression avoids small indices.

## 533 independently adjustable valuations

For the explicit computation work with \(Q=(-8,-64)\) on \(E':v^2=u^3-576u\), and let \(A(n)=u(nQ)^2+336u(nQ)+576\). At a good prime where its residue vanishes, \(v_p(A(n))=v_p(J_n)\). The two roots of the quadratic are distinct, and the ordinates of their four points are units. [Orbit and local computation](abc_eisenstein_slice_paired_quartic.md)

Starting with \(n\equiv1\bmod 2\), the verifier visits primes between 10,000 and one million in increasing order. For a prime \(p\) in the archived list, set \(T_p=\operatorname{lcm}(2,\operatorname{ord}(Q\bmod p))\). Choose the first archived hitting residue \(h_p\bmod T_p\) compatible with the current progression \(a\bmod M\), provided \(p\nmid M\) and \(T_p\) is coprime to all previously selected primes. Replace the progression by its CRT intersection with \(h_p\bmod T_p\). For every selected prime, the verifier independently checks primality, the exact point order, \(A(h_p)\equiv A(h_p+T_p)\equiv0\bmod p\), and \(A(h_p)\not\equiv A(h_p+T_p)\bmod p^2\). The exact individual quantities are reproduced from the archive by the verifier. [Certificate verifier](abc_eisenstein_slice_odd_prime_progressions.py) · [Underlying finite data](abc_eisenstein_slice_paired_quartic_1m.csv)

The resulting prime set \(S\) has 533 members. The final step \(M\) has 6,690 bits, \(\prod_{p\in S}p\) has 9,670 bits, and \(\gcd(M,\prod_{p\in S}p)=1\). Within the base progression \(n=a+Mk\) the characterizations
\[
 \Pr(v_p(J_n)=j)=\frac{1-1/p}{p^{j-1}}\quad(j\ge1),\qquad
 \Pr(v_p(J_n)\text{ odd})=\frac{p}{p+1}
\]
hold independently across the 533 primes, with natural densities relative to the progression. Indeed translation by \(T_pQ\) has exact formal depth one by the checked nonzero derivative in the index direction. Because \(M/T_p\) is prime to \(p\), translation by \(MQ\) has that same depth. At each visited section \(A\) is an étale parameter. The formal logarithm therefore makes \(v_p(A(a+Mk))\ge j\) one residue class of \(k\bmod p^{j-1}\), with exactly one lift modulo \(p^j\). Distinct primes' digit choices are independent by CRT. Infinite parity unions follow by truncating the geometric tails. Thus all \(2^{533}\) parity patterns have positive density. On a relative fraction \(\prod(1-1/p)\ge1-\sum 1/p>0.99560\) all 533 exponents equal one. The least positive base representative itself has 6,690 bits. At this index the verifier additionally evaluates each contact modulo the prime square, reducing the index modulo its checked period times the prime, and confirms that all 533 valuations equal one. In particular the kernel at this explicit index exceeds its index to the power 1.44. The arbitrary-count proof leaves the valuations of its new primes unrestricted among positive odd integers.

For every fixed stage the marked prime product is constant along its infinite progression. Its certified logarithm is consequently \(o(n^2)\) along that progression. These constructions supply lower bounds for the squarefree kernel on explicit subfamilies. The exceptional sequences relevant to a fixed positive fractional radical deficit are unconstrained by those bounds. [Global block estimates](abc_eisenstein_slice_odd_prime_entropy.md) · [Radical criterion](abc_eisenstein_slice_squareclass_descent.md)
