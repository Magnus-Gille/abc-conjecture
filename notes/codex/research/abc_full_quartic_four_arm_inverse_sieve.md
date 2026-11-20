# A power saving for small squarefree parts across all four coordinates

On the primitive quartic family \(a_n^4+3(c_nd_n)^2=4w_n^4\), write \(s(F)=\prod_{v_p(F)\ {\rm odd}}p\). There exists an absolute \(\delta>0\) such that
\[
 \#\{n\ge1:\ n\text{ odd},\ \min_{F\in\{a,c,d,w\}}s(F_n)\le Y\}
       \ll Y^{1/2-\delta}\quad(Y\ge2).
\]
There is no upper cutoff on the indices. In particular, amongst odd \(n\le N\), all but \(O(N^{1-\delta})\) have \(s(F_n)>n^{2+\delta}\) in each of the four coordinates (decrease \(\delta\) if necessary). The exponent improvement is existential. The proof uses Bombieri–Vinogradov, an upper-bound sieve for two linear forms, and Heath-Brown's quadratic large sieve. It transfers the [denominator sieve](abc_full_quartic_inverse_kernel_sieve.md) to all four coordinates by tracking the signs of three rational functions. Fixing those signs across primes is necessary here.

For the actual primitive triple let \(R_n=\operatorname{rad}(6a_nc_nd_nw_n)\), and put \(D_n=s(a_nc_nd_nw_n)\). Pairwise coprimality gives \(D_n=\prod_F s(F_n)\), so \(D_n\le Y\) forces one coordinate to have squarefree part at most \(Y^{1/4}\). Since \(D_n\mid R_n\), there is an absolute \(\eta=\delta/4>0\) with
\[
  \#\{n:R_n\le Y\}\ \le\ \#\{n:D_n\le Y\}\ \ll Y^{1/8-\eta}
\]
over all positive odd indices. The [exact census through \(10^{19}\)](abc_full_quartic_total_kernel.md) concerns this same \(D_n\).

## Local signs with a common short period

Take primes \(h\equiv7\pmod{24}\). Write \(E:y^2=x^3-36x\), \(G=(-3,9)\), and \(T\in E[2](\mathbf Q)\). The four points \(G+T\) have respective abscissas \(-3,12,18,-2\). None is a double in \(E(\mathbf F_h)\). In the full two-descent criterion the three quantities are \(x,x-6,x+6\). For these four abscissas, respectively, \(-9,12,12,-2\) is a nonsquare among the three, since \((-1/h)=(3/h)=-1\), \((2/h)=1\). A point of odd order would be a double. Thus **all four coordinates are units at \(h\) at every odd index**, by their four denominator identities. Also \(\#E(\mathbf F_h)=h+1\), by cancellation of the character sum under \(x\mapsto-x\). [Four denominators](abc_full_quartic_signature.md)

For \(w_n\) the Legendre symbol at \(h\) depends only on \(n\bmod h+1\). On the rational two-isogenous curve \(E_0:y^2=x^3+36x^2+36x\), put \(P=(-2,8)\). At odd indices \(x(nP)=-2u^2/v^2\) in coprime integers and \(w_n=(u^2+3v^2)/4\). If \(nP\) has finite reduction, its character is \((8(6-x(nP))/h)\). If it reduces to the identity, \(w_n\) is a nonzero square modulo \(h\). The potential zero \(x(nP)=6\bmod h\) cannot occur in the finite case since \(w_n\) is a unit. The isogeny gives \(\#E_0(\mathbf F_h)=h+1\). [Denominator symbol formula](abc_full_quartic_square_denominators.md)

To transfer to the other coordinates, for each \(e=0,-6,6\) there is a rational function \(g_e\in\mathbf Q(E)\) satisfying
\[
       g_e(Q)^2=\frac{x(G+2Q)-e}{x(G)-e}.
\]
Indeed write \(L_{U,V}\) for the chord of two generic points on the Weierstrass model. Substitution into the cubic gives \(L_{U,V}(e)^2=(x(U)-e)(x(V)-e)(x(U+V)-e)\). Divide the identity at \((G+Q,Q)\) by the identity at \((G,Q)\); the ratio of the chord values gives \(g_e\). The rational-function identity extends from generic \(Q\). At every good prime outside a fixed finite set, whenever the right side is a regular unit at a point of the reduced curve, the same holds for \(g_e\). One may use the normal local ring of the smooth model, in which both \(g_e\) and its inverse are integral over the ring. Thus its residue depends only on the reduced point, including where a particular chord formula has a removable indeterminacy.

For \(n=2m+1\), the displayed squares at \(Q=mG\) are \((a_n/w_n)^2,(c_n/w_n)^2,(d_n/w_n)^2\) in order. They are units at every chosen \(h\); the section \(nG\) is affine and avoids the corresponding two-torsion reductions. Each of \(a_n/w_n,c_n/w_n,d_n/w_n\) therefore equals its corresponding rational-function value up to **one rational sign**. This sign can change with \(n\) and the coordinate, but is shared by all primes for that coordinate. The two character values obtained by its two choices suffice, even though \(-1\) is a nonsquare at each \(h\).

If all \(h+1\) divide \(t\), it follows that, for each coordinate separately, the vectors \(((F_n/h))_h\) occupy at most \(4t\) words: \(n\bmod2t\) determines \(nP\) and \(mG\) at every place, and the rational sign has only two choices. Since the symbols are units they equal \((s(F_n)/h)\).

## A supply of primes with smooth shifted order

There exists a fixed \(e_0>0\), with \(\theta=1/2-e_0\), such that for all large \(Z\) there are \(\gg Z/\log Z\) primes \(Z/2<h\le Z\), \(h\equiv7\bmod24\), for which every prime power dividing \(h+1\) is at most \(Z^\theta\). In particular \(h+1\mid\mathrm{lcm}(1,\ldots,\lfloor Z^\theta\rfloor)\).

Here are details of the strict improvement past one half. For fixed small \(e\in(0,1/100)\) put \(a=1/2-3e, b=1/2-2e,\theta=1/2-e\), and let \(S_Z=\sum_{Z^a<r\le Z^b,\ r\ {\rm prime}}1/r\), tending to \(\log(b/a)>0\). Count pairs \((h,r)\) with in addition \(h\equiv-1\bmod r\). Bombieri–Vinogradov at moduli \(24r\) gives at least \(c S_Z Z/\log Z\) pairs, with an absolute \(c>0\) independent of small fixed \(e\). Indeed the main terms have denominator \(8(r-1)\), and the sum of errors is \(O(Z/(\log Z)^3)\) once \(Z\) is sufficiently large for the chosen \(e\).

If \(h+1\) has a prime divisor \(s>Z^\theta\), it is distinct from \(r\) and \(h+1=urs\) with \(u\le 2Z^{4e}\). For fixed \(u,r\), put \(T=(Z+1)/(ur)\); only \(T>Z^\theta\) contributes. The classical upper-bound sieve for the two linear forms \(s,urs-1\) gives
\[
 \#\{s\le T:s,urs-1\ {\rm prime}\}
 \ll \left(\frac{ur}{\varphi(ur)}\right)^2\frac{T}{(\log T)^2}.
\]
The constant is absolute in the nonempty range; if \(ur\) is odd there is no admissible odd \(s\) giving a large prime \(h\). For even \(ur\) the roots excluded modulo an odd prime are two except when the prime divides \(ur\), when there is just one. The resulting singular product is \(O((ur/\varphi(ur))^2)\); standard Selberg upper-bound sieve remainders for these linear forms are uniform since there are at most \(2^{\omega(v)}\) root classes modulo squarefree \(v\). Primes \(s>Z^\theta\) and \(h>Z/2\) both exceed the sieve cutoff (one may take \(T^{1/20}\)). Using \(\sum_{u\le V}(u/\varphi(u))^2/u\ll1+\log V\), the bad pairs thus cost at most \(C(e+1/\log Z)S_Z Z/\log Z\) with absolute \(C\). The last divisor-sum estimate follows by expanding the multiplicative weight in squarefree divisors: the local increment \((p/(p-1))^2-1\) is \(O(1/p)\), hence its divided-by-\(p\) Euler product converges. Choose a fixed \(e=e_0\) small enough that the bad pairs cost less than half the main term.

The number of remaining \(h\) for which some higher prime power \(p^j>Z^\theta\), \(j\ge2\), divides \(h+1\) is \(o(Z/\log Z)\). For \(p>Z^{\theta/2}\) count multiples of \(p^2\), at a cost \(O(Z^{1-\theta/2}+\sqrt Z)\). For each \(p\le Z^{\theta/2}\) count multiples of its first power exceeding \(Z^\theta\), at a cost in total \(O(Z^{1-\theta/2}+Z^{\theta/2})\). Each \(h\) belonged to only \(O(1)\) pairs, since each \(r>Z^a\) divides \(h+1\). This proves the supply assertion. Omitting any fixed finite set of bad reduction primes has no effect.

## The quadratic large sieve and the count of indices

Fix small \(\eta>0\). For growing \(Y\), choose \(Z=(\eta\log Y)^{1/\theta}\). The period \(2t\) above is at most \(\exp(O(Z^\theta))=Y^{O(\eta)}\) by Chebyshev's bound. Let \(M\gg Z/\log Z\) be the number of probes. Form a set \(\mathcal U\) of distinct odd squarefree integers by multiplying exactly \(j=\lfloor\log Y/\log Z\rfloor\) probes. All are at most \(Y\). The binomial lower bound gives
\[
 \log|\mathcal U|\ge j\log(M/j)\ge(1-\theta-o(1))\log Y.
\]
Each word prescribes one sign \(\sigma(u)\in\{1,-1\}\) for every \(u\in\mathcal U\). If \(D=s(F_n)\le Y\) has that word, then \(\sum_{u\in\mathcal U}\sigma(u)(D/u)=|\mathcal U|\). Heath-Brown's quadratic large sieve for odd squarefree indices and conductors gives
\[
 \sum_{D\le Y}^{*}\left|\sum_{u\in\mathcal U}\sigma(u)(D/u)\right|^2
          \ll_\epsilon Y^{1+\epsilon}|\mathcal U|.
\]
Here the star restricts to positive odd squarefree integers. Equivalently, apply the usual form with symbol \((u/D)\) by quadratic reciprocity: all products use the same number of primes \(3\bmod4\), so the reciprocal sign at fixed \(D\) is independent of \(u\). The allowed \(D\) per word number \(O_\epsilon(Y^{\theta+\epsilon+o(1)})\). Summing over words and using the uniform multiplicity \(A^{1+\omega(D)}=Y^{o(1)}\) for \(D\le Y\) costs only \(Y^{O(\eta)+o(1)}\). Fix \(\eta,\epsilon\) sufficiently small in terms of \(e_0\); there remains an absolute \(\delta>0\) as stated. Summing over the four coordinates completes the proof. [Uniform multiplicity and the pointwise bound](abc_full_quartic_four_squarefree_parts.md) · [D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995)](https://doi.org/10.4064/aa-72-3-235-275)

The conclusion compares cofactor size with the elliptic **index**. The height relevant for abc satisfies \(\log w_n\asymp n^2\), so this argument still allows cofactors exponentially smaller than their coordinates at every index it counts as typical. [Connection with the abc quality](abc_full_quartic_twin_and_mixed_valuations.md)
