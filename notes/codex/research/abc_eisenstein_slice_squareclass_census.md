# Squarefree kernels of the paired quartic on the elliptic slice

For positive odd indices \(n\ge3\), set \(b_n=\operatorname{sf}(|F_+F_-|/512)\), where the squarefree part is the product of primes with odd valuation. Write \(d_4=\operatorname{sf}(|F_4|/16)\) and \(d_5=\operatorname{sf}(|F_5|/32)\) for the factors of 2-adic valuations four and five. Then \(b_n=d_4d_5\), with coprime \(d_4,d_5\) prime to six. The exact minimum is
\[
               \min_{n\ge3\text{ odd}} b_n=2671321=2591\cdot1031.
\]
Both individual inequalities are sharp, with \(d_4\ge2591\) and \(d_5\ge1031\) at every index. Equality holds in both at \(n=3\).

## Individual lower bounds from the original point orbit

The elementary obstructions \(d_i>1\) reduce the small-kernel check to visiting-prime support. [Two-isogeny descent](abc_eisenstein_slice_squareclass_descent.md) Enumerating the odd multiples of \(Q=(-8,-64)\) for all 375 primes \(5\le p\le2591\), as in the following section, gives exactly the ten visiting primes
\[
  167,191,263,311,983,1031,1321,1367,2087,2591.
\]
Their two smallest already have product exceeding 2591. Thus any smaller individual squarefree kernel is a single prime in this list.

For an auxiliary prime \(p>3\), enumerate the odd multiples of the original point \(P=(-2,8)\) on \(Y^2=X^3+36X^2+36X\). At a finite abscissa choose either square root \(t\) of \(-X/2\) and evaluate the two quartics at \((t,1)\). At the identity evaluate at \((1,0)\). These are the reductions of the projective slope parameters up to sign, since \(X(nP)=-2(x/y)^2\). Reversing the sign interchanges the two quartics. Set \(k=(d/3)d\) if \(i=4\), and \(k=-(d/3)d\) for \(i=5\). A candidate \(d_i=d\) requires that at least one quartic lie in \(2^i k\mathbf F_p^2\). The following odd residue classes of \(n\) allowed by this condition have empty intersection in each row.

| Candidate | First auxiliary prime and allowed indices | Second auxiliary prime and allowed indices |
| --- | --- | --- |
| \(d_4=191,311,983,1367\) or \(d_5=191,311,983\) | 11, no odd residue | |
| \(d_4=167,1321,2087\) or \(d_5=263\) | 13, \(5\nmid n\) | 73, \(n=5\bmod10\) |
| \(d_4=263\) | 17, \(n=1,5,9\bmod10\) | 19, \(n=3,7\bmod10\) |
| \(d_5=167\) | 17, \(n=3,7\bmod10\) | 19, \(n=1,5,9\bmod10\) |
| \(d_4=1031\) | 71, \(n=1,9,17\bmod18\) | 251, \(n=3,7,11,15\bmod18\) |

The finite-field scan proves both inequalities. At \(3P\), the identity \((F_0,F_+,F_-)=(-8\cdot23^2,32\cdot1031,-16\cdot2591)\) proves simultaneous attainment. [Individual verifier](abc_eisenstein_slice_individual_minima.py) · [Residues and complete list](abc_eisenstein_slice_individual_minima.json)

## An elementary finite exhaustion

Use \(d_4,d_5>1\) from the individual square obstruction. A prime \(p>3\) dividing the pair visits \(J(u)=u^2+336u+576=0\) at an odd multiple of \(Q=(-8,-64)\) on \(v^2=u^3-576u\). This follows from \(4F_+F_-=(xy)^4J(u(nQ))\) and the fact that neither quartic vanishes at a prime divisor of \(xy\). Iterate directly starting with \(Q\), adding \(2Q\), and stop on returning to \(Q\). The smallest three visiting primes are \(167,191,263\). If \(b_n\le2671321\), every prime factor of \(b_n\) is at most \(\lfloor2671321/167\rfloor=15995\), and the product of the three smallest visiting primes already exceeds the bound. The 1,860 primes from 5 through 15,995 give 69 visiting primes, hence 218 unordered pairs or 436 orientations below the bound. The orbit test was repeated independently of the archived large-prime scan. [Paired-quartic identity and earlier scan](abc_eisenstein_slice_paired_quartic.md)

Put \(F_0=x^4-18x^2y^2+9y^4\) and \(F_\pm=F_0\pm12xy(x^2-3y^2)\). The signs forced by reduction modulo three are \(k=(d_4/3)d_4\), \(l=-(d_5/3)d_5\), using Legendre symbols. Replacing \(x\) by \(-x\) if necessary, a rational point gives, for every odd prime \(p\), some \((x:y)\in\mathbf P^1(\mathbf F_p)\) satisfying
\[
         F_0\in-8\,\mathbf F_p^2,\qquad
         F_+\in16k\,\mathbf F_p^2,\qquad
         F_-\in32l\,\mathbf F_p^2 .
\]
Zero is allowed among the squares. Scaling the projective coordinates multiplies each form by a fourth power. Enumerating the \(p+1\) pairs \((x,1),(1,0)\) gives the following successive numbers of surviving orientations.

| Auxiliary prime | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 | 43 | 47 | 53 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Survivors | 212 | 102 | 24 | 21 | 11 | 7 | 5 | 5 | 3 | 3 | 3 | 3 | 2 | 1 |

The remaining orientation is \(d_4=2591,d_5=1031\). At \(3P\) one has \(x=11,y=3\) and \((F_0,F_+,F_-)=(-8\cdot23^2,32\cdot1031,-16\cdot2591)\). [Verifier](abc_eisenstein_slice_minimum_kernel.py) · [All oriented pairs and first failed prime](abc_eisenstein_slice_minimum_kernel.tsv) · [Summary](abc_eisenstein_slice_minimum_kernel.json)

## Three congruent numbers and a second finite check

Primitivity on \(U^2+3V^2=W^{12}\) gives \(U=bt^2\), \(U,V>0\). For \(u=t/W^3\) and \(v=V/W^6\), the equation \(1-b^2u^4=3v^2\) gives
\[
        (-3b^2u^2,9b^2uv)\in E_{3b}(\mathbf Q),\qquad
        E_N:\ Y^2=X^3-N^2X .
\]
The ordinate is nonzero, hence \(3b\) is congruent. Individual quartic maps give the other two congruent numbers \(6d_4,3d_5\). The integral relation \(s^2+kt_4^2+2lt_5^2=0\) requires \(k<0\) or \(l<0\). Coprimality and the fact that \(p\mid F_+F_-\) implies \(p\nmid F_0\) give \((-2l/p)=1\) at \(p\mid d_4\) and \((-k/p)=1\) at \(p\mid d_5\).

For odd squarefree \(d\) prime to 3, write \(R_c(m)=\#\{(y,x)\in\mathbf Z^2:y^2+cx^2=m\}\) and
\[
 D_c(d)=-R_c(3d)+2\sum_{z\ge1}(-1)^{z+1}R_c(3d-8z^2).
\]
Terms with negative argument vanish. Tunnell's necessary equality for \(3d\) is \(D_2(d)=0\) and the one for \(6d\) is \(D_4(d)=0\). These are the ternary form differences \(B-2A\), using the odd argument \(3d\) and the \(z^2\) coefficients 8 and 32. The even form is divided by 2. All equalities here are applied in the unconditional necessary direction. J. B. Tunnell, *A classical Diophantine problem and modular forms of weight 3/2*, Invent. Math. 72 (1983), 323–334.

The following counts cover every squarefree \(b\le10^6\) with \((b,6)=1\), including every prime greater than three within that bound. The last column counts \(b\) for which some nontrivial ordered split passes the three Tunnell tests, the sign test and all displayed Legendre tests. The torus support requires every prime to be \(\pm1\bmod24\). The quartic support also requires \(3^{(p-1)/4}\equiv1\bmod p\) when \(p\equiv1\bmod24\).

| Candidates | Count | \(D_2(b)=0\) | \(D_4(b)=0\) | Both | Oriented test |
| --- | ---: | ---: | ---: | ---: | ---: |
| Squarefree, prime to 6 | 303,963 | 165,892 | 167,347 | 91,914 | 22,183 |
| Squarefree, torus support | 24,354 | 13,525 | 13,887 | 3,058 | 333 |
| Squarefree, quartic support | 17,470 | 11,581 | 7,984 | 2,095 | 177 |
| All primes greater than 3 | 78,496 | 40,169 | 40,239 | 21,564 | 0 |
| Primes \(1\bmod24\) | 9,732 | 877 | 9,732 | 877 | 0 |
| Primes \(-1\bmod24\) | 9,845 | 9,845 | 1,064 | 1,064 | 0 |
| Primes \(1\bmod24\) on quartic support | 4,845 | 429 | 4,845 | 429 | 0 |

On quartic support 2,779 composite \(b\) give 5,762 nontrivial orientations. The three equalities leave 1,457 orientations, real signs leave 376, and the Legendre conditions leave 177. None of the remaining integers is supported on actual visiting primes. The complete compressed table contains two differences per kernel, the number passing each stage, and the least passing \(d_4\). Its uncompressed SHA-256 is `b91cf3fc2df15b8d1ccf2719db9efb55698309b893192edd36e40cf4c7553692`. The theta differences were independently checked by direct ternary enumeration for all odd targets through 549. [Program](abc_eisenstein_slice_tunnell.py) · [Compressed table](abc_eisenstein_slice_tunnell.tsv.gz) · [Counts](abc_eisenstein_slice_tunnell.json)

Intersecting with the full visiting-prime archive gives the following counts through one million. For prime-to-three indices, a class \(n=h\bmod T\) permits such an index if \(3\nmid T\) or \(3\nmid h\). It permits a multiple of three if \(3\nmid T\) or \(3\mid h\). The rows impose this condition on each prime separately. The squarefree counts include one, and the last two columns count kernels with some nontrivial three-way orientation before and after the real/Legendre tests. [Orbit-support calculation](abc_eisenstein_slice_tunnell_orbit_support.py) · [Counts](abc_eisenstein_slice_tunnell_orbit_support.json)

| Prime support | Primes | Primes passing \(3p\) | Primes passing \(6p\) | Both | Squarefree kernels | Three-way | With signs and symbols |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| All visits | 2,777 | 2,531 | 457 | 211 | 2,848 | 13 | 0 |
| Some index prime to three | 2,010 | 1,783 | 384 | 157 | 2,033 | 6 | 0 |
| Some index divisible by three | 1,202 | 1,021 | 296 | 115 | 1,222 | 6 | 0 |
| Reduction order of \(Q\) prime to three | 435 | 273 | 223 | 61 | 436 | 0 | 0 |

For the 218 visited-prime pairs in the minimum computation, write \(T_p\) for the order of the odd-index period and \(H_p\) for the set of visiting residues. A pair \((p,q)\) requires some \(h\in H_p,j\in H_q\) with \(h\equiv j\bmod\gcd(T_p,T_q)\). This leaves 120 unordered pairs. Independently, three Tunnell equalities leave 38 of the original 218 pairs. The real and Legendre tests plus Tunnell leave five. Imposing the index congruence as well leaves four oriented pairs,
\[
          (191,7703),\ (191,8783),\ (191,13127),\ (2591,1031).
\]
The first three all fail the displayed local quartic test at 5. The second verifier computes the binary representation counts from unique factorization for norms in \(\mathbf Z[\sqrt{-2}]\) and \(\mathbf Z[i]\), independently of the vectorized theta computation. For odd \(m\), both counts equal \(2\prod_{p\text{ split}}(1+v_p(m))\) when all inert valuations are even and zero otherwise. For the Gaussian norm the even coordinate is prescribed, which accounts for half the four units.

## An all-height count of nearly square kernels

For each \(i=4,5\), one has a uniform bound
\[
            \#\{n\ge3\text{ odd}:d_i(n)=d\}\le C^{1+\omega(d)}
\]
with \(C\) absolute for this slice. Indeed each such index lifts to a rational point on one of the finite choices of twists \(Y^2=c d F_0(X,1)F_\pm(X,1)\), where \(c\) ranges over fixed signed constants. This follows by multiplying \(F_0=-8s^2\) by the signed normalized square identity for \(F_i\), and dividing the degree-eight form by \(y^8\). The quartics are separable and have no common root. Their discriminants are \(2^{14}3^6\) for \(F_0\) and \(2^{20}3^6\) for each \(F_\pm\). A common root forces \(x y(x^2-3y^2)=0\), none of which is a zero of \(F_0\). Thus the smooth hyperelliptic curve has genus three. The rational parameter \(X=x/y\) determines at most one positive odd index, since the elliptic abscissa of \(nP\) is \(-2X^2\) and \(P\) has infinite order.

Fix a splitting field \(K\) for the finitely many branch polynomials. The Jacobian two-torsion is rational over \(K\), uniformly for all these quadratic twists, since the twisting involution acts as \(-1\). Let \(S\) include places above the finitely many bad primes for the untwisted curves, the archimedean and dyadic places and those above \(d\). Good reduction of the twist away from \(S\) forces the two-Kummer image to be unramified there. It embeds in \(H^1(G_{K,S},\mathbf F_2^6)\) and its dimension is bounded by six times the dimension of the squareclasses in \(K^\times\) with even valuations outside \(S\). Units outside \(S\) and the two-torsion in the fixed class group bound that dimension by \(O_K(1+\omega(d))\). Consequently the Jacobian rank over \(\mathbf Q\) has that bound as well. For a curve with a rational point the uniform Mordell–Lang theorem bounds its rational points by \(C_3^{1+\operatorname{rank}J(\mathbf Q)}\). This yields the stated count. [Dimitrov, Gao and Habegger](https://arxiv.org/abs/2001.10276)

In particular each \(d_i(n)\to\infty\) with \(n\). If \(b_n\le Y\), some \(d_i(n)\le\sqrt Y\). Summing the preceding bound and majorizing \(C^{\omega(d)}\) by a fixed integer-order divisor function gives
\[
     \#\{n\ge3\text{ odd}:b_n\le Y\}\ll \sqrt Y(\log(2Y))^A.
\]
It follows that \(b_n>n^2/(\log n)^B\) for a relative density-one set of odd indices when \(B>2A\). For these indices, the largest integer whose square divides \(J_n=|F_+F_-|/512\) is at most \(\sqrt{J_n}(\log n)^{B/2}/n\). This estimate permits complete squarefulness of \(J_n\), which would require \(b_n^3\mid J_n\), and supplies no fixed positive saving in the logarithm of the radical.
