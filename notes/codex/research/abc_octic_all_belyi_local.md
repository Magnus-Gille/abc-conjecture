# A two-prime proof of the least rational Belyi degree at \(j=8000\)

Every elliptic curve defined over \(\mathbb Q\) with \(j=8000\) has least degree **eight** among Belyi maps defined over \(\mathbb Q\). The three special fibers can be chosen freely. The proof uses good reduction at 11 and 19 and finite-field arithmetic. It gives an independent check of the earlier lower bound based on the Belyi database. [Standard-library checker](abc_octic_all_belyi_local.py)

## Upper bound

Write \(E:y^2=x^3+16x^2+32x\). Its discriminant is \(2^{21}\) and \(j(E)=8000\). Because \(j(E)\ne0,1728\), all elliptic curves over \(\mathbb Q\) with this invariant have models \(d y^2=x^3+16x^2+32x\). The same degree-eight map on every twist is
\[
 \beta=\left(\frac{x^2+16x+32}{32}\right)^2 .
\]
The projection to \(x\) branches at \(0,-8\pm4\sqrt2,\infty\). The quadratic polynomial inside the square takes these to \(1,0,0,\infty\) and contributes its own branch values \(-1,\infty\). Squaring sends all branch values to \(0,1,\infty\).

## Reduction of rational Belyi maps

For degree \(n\le7\), both 11 and 19 are prime to the order of the geometric Galois closure, whose group embeds in \(S_n\). Since the three branch values remain distinct, the prime-to-\(p\) good reduction theorem for covers of the three-pointed line gives good reduction of the cover after finite extension, with the same three fiber partitions. This follows by prime-to-characteristic specialization for tame covers and passage to a quotient of the Galois closure. [Grothendieck, *SGA 1*, Exposé XIII](https://arxiv.org/abs/math/0206203)

On a good elliptic curve the smooth proper model is unique, by uniqueness of the minimal regular model in positive genus. The model of the target with \(0,1,\infty\) distinct is fixed by those three sections. Therefore once the source has good reduction over a local field \(K\), the given Belyi map extends on these models over \(\mathcal O_K\). Indeed its extension after a further finite extension descends by faithful flatness and uniqueness on the dense generic fiber. The reduction is defined over the residue field of \(K\). For an unramified quadratic twist its reduction is one of the two elliptic curves with this invariant over \(\mathbb F_p\). For a ramified twist take \(K\) to be its totally ramified quadratic splitting field. Its residue field is still \(\mathbb F_p\), and over \(K\) the curve is already isomorphic to \(E\).

Consequently any characteristic-zero passport would occur among the two forms at **each** of the two primes. Here \(d\) labels the short model \(y^2=x^3+16d x^2+32d^2x\). The three partitions in a passport are unordered.

| \(p\) | \(d\) | \(\#E_d(\mathbb F_p)\) | All rational passports of degrees 3 through 7 |
|---:|---:|---:|---|
| 11 | 1 | 18 | \(32/32/5;\ 331/52/52;\ 42/42/51;\ 421/421/7;\ 421/43/52\) |
| 11 | 2 | 6 | None |
| 19 | 1 | 22 | \(33/42/42\) |
| 19 | 2 | 18 | \(2211/6/6\) |

An entry such as \(32/32/5\) means \((3,2),(3,2),(5)\). The two sets of passports have empty intersection.

## Why the finite enumeration is exhaustive

Let \(k=\mathbb F_p\). Riemann–Hurwitz gives \(a+b+c=n\), where \(a\le b\le c\) are the numbers of distinct geometric points in the three fibers. This gives \(n\ge3\). For \(n\le7\) with \(a=1\), the unique point with multiplicity \(n\) is rational. Translate it to the origin \(O\), so the first fiber is \(nO\) and the second has at most \(\lfloor(n-1)/2\rfloor\) points. A second fiber of size three can occur only for \(n=7\), when it has three rational points or one rational point and a conjugate pair. A Frobenius orbit of length three would require \(3\mid7\). For \(a\ge2\), the only possibilities are \(2,2,2\) and \(2,2,3\). It suffices in this case to enumerate pairs of disjoint two-point divisors. A rational two-point divisor consists of two rational points or a conjugate pair of equal multiplicity. All necessary points thus lie over \(k\) or its quadratic extension.

The sum \(S\) in the elliptic curve group of a rational degree-\(n\) fiber records its class minus \(nO\). Translating all points by \(T\in E(k)\) changes this sum by \(nT\). The checker considers one representative per coset in \(E(k)/nE(k)\). For \(S=O\) it uses the sections of \(nO\). For \(S\ne O\), adding the common fixed point \(B=-S\) to every candidate divisor embeds the desired linear system in \(|(n+1)O|\). In either case the Riemann–Roch basis consists of \(1,x,y,x^2,xy,x^3,x^2y,\ldots\) up to the required pole order. Imposing all zeros of a candidate divisor, including \(B\) when present, gives its unique projective section vector over \(k\). The checker imposes the conditions using truncated Taylor series and Gaussian elimination. For a point over the quadratic extension, each coefficient contributes its two coordinates over \(k\).

For two sections \(s,t\) having disjoint supports after removing \(B\), the remaining rational members of their pencil are exactly \(s+ut\), \(u\in k^\times\). A member giving \(c=n-a-b\) distinct geometric zeros completes a Belyi pencil by Riemann–Hurwitz in characteristic \(p>n\). To count the zeros write the section \(A(x)+yH(x)\), put \(C=x^3+16d x^2+32d^2 x\), \(N=A^2-CH^2\), and \(G=\gcd(A,H)\). The affine support has cardinality
\[
 \deg\operatorname{rad} N+\deg\operatorname{rad}G-
 \deg\operatorname{rad}\gcd(G,C).
\]
There is one point above each root of \(N\), with a second precisely when the root is common to \(A,H\) and is not a root of \(C\). The checker includes the order at \(O\) from the degree of \(N\) and subtracts the fixed zero \(B\) when present. It recovers all multiplicities by polynomial gcds. At an unramified abscissa the two positive or zero orders are \(\operatorname{ord}G\) and \(\operatorname{ord}N-\operatorname{ord}G\); at a ramified abscissa the sole order is \(\operatorname{ord}N\). These calculations need no factorization or external database.

## Genus-one sources without a specified rational point

The lower bound also holds for every genus-one curve over \(\mathbb Q\) with \(j=8000\). For a degree at most seven with no rational point, the fiber-size argument forces all three fibers to have type \((3,3)\). Indeed a single-point fiber is rational, and a two-point fiber of unequal multiplicities has two rational points. The remaining case is degree six with three equal two-point fibers.

This last passport implies that the source Jacobian is geometrically isogenous to the elliptic curve \(v^3=t(t-1)\) with \(j=0\). To see this, normalize their fiber product over the \(t\)-line over \(\overline{\mathbb Q}\). Both maps have local ramification index three precisely over \(0,1,\infty\), so the projections from each component are unramified. A component is therefore a genus-one curve with finite maps to both sources. Such an isogeny is impossible at 11. The curve with \(j=8000\) has ordinary reduction there, as its trace is \(11+1-18=-6\). The curve with \(j=0\) is supersingular there, since cubing is bijective in \(\mathbb F_{11}\) and the model \(y^2=x^3+1\) has trace zero. Isogenies between elliptic curves with good reduction specialize to isogenies. This proves the lower bound also in the absence of a rational origin.
