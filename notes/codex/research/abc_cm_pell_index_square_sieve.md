# A square sieve for indices on the rank-eleven Pell orbit

Let \(M_n=|F_{11}(a_n,b_n)|\) for \(b_n+a_n\sqrt2=(1+\sqrt2)^n\), and put \(g=(1+\sqrt2)^4\). For a good prime \(p\) let \(d_p\) be the order of \(g\) modulo \(p\) in the quadratic norm-one torus. Thus \(d_p\mid p-(2/p)\). Call \(p\) regular here if its order modulo \(p^2\) is \(p d_p\). The exceptional primes for this condition are the projective Pell-Wieferich primes. Good reduction in this note also excludes the finite divisors of the discriminant, the leading coefficient and the denominators in the fixed target polynomial. Its 50 roots are distinct units at every remaining prime place. The notation and the fixed Laurent product for \(M_n\) are given in the [target description](abc_cm_pell_target_gcd.md).

For any cutoff \(X(N)\to\infty\) with \(\pi(X(N))=o(N)\), the proportion of indices \(1\le n\le N\) avoiding every square \(p^2\mid M_n\) at good regular primes \(p\le X(N)\) tends to the same **positive** constant \(D\). In particular, one may take \(X(N)=N\log N/\log\log N\). The constant is the limit of exact finite periodic densities. The periods can share factors, so the finite densities are computed by sieving residue classes in their least common multiple.

There is also a positive limiting proportion with \(683^2\parallel M_n\) and no other good regular square in this range. The result allows both a moving cutoff and a specified repeated prime on the original one-variable Pell orbit. Squares at projective Pell-Wieferich primes and at primes beyond the cutoff are outside these counts.

## Local index classes

At a fixed place above \(p\), let \(h_p\) be the number of the 50 reduced targets belonging to \(\langle g\rangle\). Each such target occurs once per period \(d_p\) of the residue orbit. The Laurent factorization gives \(p\mid M_n\) precisely in these \(h_p\) classes. For regular \(p\), each class extends to exactly one square class modulo \(p d_p\). Indeed the lifts of \(g^n\) are obtained by multiplying by powers of \(g^{d_p}\), which generates the order-\(p\) kernel of reduction in the norm-one torus. The target has a unique lift within this torus. In the split case this follows from a simple root over \(\mathbb Z_p\). In the inert case the corresponding abscissa is a simple rational residue root of the abscissa polynomial and lifts to a root in \(\mathbb Z_p\). Its target coordinate \((\theta_+-x)/(x-\theta_-)\) is therefore inverted by quadratic conjugation and has norm one. Equivalently, lift the corresponding simple binary-form root along the projective unit orbit. The initial torus change of coordinate is étale there for odd \(p\). The same argument at higher powers gives \(h_p\) classes modulo \(p^{e-1}d_p\) for \(p^e\mid M_n\). The binomial expansion of a principal unit supplies each successive order increase.

Consequently the contribution of regular \(Y<p\le X\) to the proportion of indices up to \(N\) hitting a square is at most
\[
  \sum_{Y<p\le X}\frac{h_p}{p d_p}+\frac{50\pi(X)}{N}.
\]
The first sum can be extended to all good primes with the same summand as an upper bound on the regular tail.

## Short orders at primes that hit a target

For \(h_p=h\ge1\), put \(s=\min(h+1,50)\). On this stratum,
\[
   \sum_{p>Y,\ h_p=h}\frac{h_p}{p d_p}
      \ll_h \frac{Y^{-s/(s+1)}}{\log Y}.
\]
In particular the full tail is \(O(Y^{-2/3}/\log Y)\). This exponent uses the multiplicative independence of a target and \(g\). The higher exponents use the [certified independence of the full target set](abc_cm_pell_target_rank.md).

To see this, choose \(s-1\) of the hit targets when \(s\le 50\). Their lifts and \(g\) are multiplicatively independent because they comprise \(g\) and a proper subset of the targets. Fix the choices temporarily in the global splitting field. If \(d_p\le R\), then these \(s\) generators have reductions in a cyclic group of order at most \(R\). A box of exponent vectors \(0\le e_i\le\lfloor R^{1/s}\rfloor\) contains more than \(R\) vectors. Two images coincide and their difference yields a nontrivial monomial \(z\) of height \(O_s(R^{1/s})\) with \(z\equiv1\) at the selected place. There are \(O_s(R)\) possible differences. Their nonzero values \(z-1\) have numerator ideals of logarithmic norm \(O_s(1+R^{1/s})\). Taking their product and the finitely many choices of target subset gives
\[
           \sum_{d_p\le R,\ h_p=h}\log p\ll_h R^{1+1/s},\qquad R\ge1.
\]
A prime appearing at one place already contributes at least \(\log p\) to the numerator-ideal bound.

On \(x<p\le2x\), sum \(1/d_p\) first over \(d_p\le R\). Partial summation of the last inequality bounds this part by \(O_h(R^{1/s}/\log x)\). The part with larger order is \(O(x/(R\log x))\) by the prime count. Taking \(R=x^{s/(s+1)}\), dividing by \(x\), and summing dyadic intervals proves the tail. The same calculation for the depth-\(e\) summands gives an extra factor \(Y^{-(e-2)}\).

## Positive density and a prescribed square

Write \(D_Y\) for the periodic avoidance density through \(Y\). Sieve the good regular primes in increasing order. A new prime \(p\) divides neither \(d_p\) nor any earlier period \(q d_q\), since \(d_q\mid q\pm1\) and \(q+1<p\) for odd primes \(q<p\). Refine the old period by \(d_p\). In each surviving residue, the unique index modulo \(d_p\) is associated to at most one reduced target. Adjoining the free index coordinate modulo \(p\) deletes at most one of its \(p\) values. Hence
\[
             D_Y\ge\prod_{p\le Y}(1-1/p)\gg1/\log Y.
\]
The finite-period densities decrease to \(D\), and their remaining loss is at most the tail \(O(Y^{-2/3}/\log Y)\). For a sufficiently large fixed \(Y\) this is smaller than \(D_Y\). The local counting inequality then gives convergence to \(D>0\) for every cutoff in the statement. For an effective modulus estimate, the least common multiple of the periods through \(Y\) divides \(\prod_{p\le Y}p\) times \(\operatorname{lcm}(1,\ldots,\lfloor Y\rfloor+1)\), and so is at most \(\exp(O(Y))\). Taking \(Y=\min(X,c\log N)\) with a sufficiently small fixed \(c>0\) gives the error
\[
 O\!\left(N^{-1/2}+Y^{-2/3}/\log Y+\pi(X)/N\right)
\]
for the finite-cutoff density compared to \(D\). At the endpoint \(X=c_1 N\log N\) one still obtains a positive lower density for sufficiently small fixed \(c_1>0\). If \(X(n)\) increases, the same limit \(D\) holds for the termwise cutoff \(p\le X(n)\) under the stated little-oh condition, by sandwiching between each fixed finite sieve and the sieve through \(X(N)\). The lower bound may also restrict the product to the contributing classes \(1,67\bmod88\), if desired.

For the specified square restrict first to
\[
                    n\equiv1213\pmod{114\cdot683^2}.
\]
At \(p=683\), the order of \(g\) is 114 and it increases by 683 at each lift. The index 1213 has exact valuation two, so the entire class does. The other prime factors of its period are 2, 3 and 19. None can divide a Pell term in this full factor. Consequently every further contributing regular prime still supplies a free coordinate modulo itself. With \(m=114\cdot683^2\), the initial density is \(1/m\) and the finite-product lower bound becomes \(\gg1/(m\log Y)\). The same unconditioned tail bound proves the positive limit on this progression. The [local verifier](abc_cm_pell_index_square_sieve.py) checks the order, all 14 classes at 683, their distinct square lifts and the valuation at index 1213.

For a good projective Pell-Wieferich prime the index period modulo \(p^2\) is already \(d_p\). A hit class modulo \(p\) either survives wholesale as a square class or has no square lift on this orbit. Its possible density is \(1/d_p\), where a corresponding regular class has density \(1/(pd_p)\). This is precisely the lost factor in applying the moving-cutoff estimate to such primes.

## Depth beyond the local order of the Pell unit

One can include every good prime in a variant of the same theorem. Write
\[
 b_p=v_p(g^{d_p}-1)\ge1
\]
at the unramified local place with \(v_p(p)=1\). This is intrinsic in the quadratic torus because conjugation inverts \(g\). For every fixed \(j\ge1\), there is a positive limiting index density satisfying
\[
              v_p(M_n)<b_p+j
       \qquad\hbox{for every good }p\le X(N)
\]
for the same cutoffs. At \(j=1\) this gives the ordinary square condition at regular primes and excludes any precision beyond \(b_p\) at the other good primes.

Indeed \(g^{d_p}\) has projective depth exactly \(b_p\), so all indices in the same class modulo \(d_p\) give the same torus point modulo \(p^{b_p}\). There are at most \(h_p\) classes reaching a target to that precision. Each has exactly one lift modulo \(d_p p^j\) reaching the target to precision \(p^{b_p+j}\), by the principal-unit calculation. The full local bad density is therefore at most \(h_p/(p^j d_p)\). The previous tail and positivity proofs apply, including on the specified 683 progression when that prime is exempted. In particular the moving-cutoff bound removes all higher precisions at a projective Pell-Wieferich prime once its explicitly defined initial depth is exceeded.
