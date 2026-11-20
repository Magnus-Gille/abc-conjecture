# The least positive kernel of the ninth cyclotomic form

For coprime integers \(A>B>0\), the least possible squarefree kernel
of \(\Phi_9(A,B)=A^6+A^3B^3+B^6\) is **73**, attained at \((2,1)\).
Here kernel means the unique squarefree \(D\) with \(\Phi_9=Dz^2\).
The kernel \(57\) has exactly two rational projective slopes,
\([-2:1]\) and \([-1:2]\), both negative. A local two-descent obstruction
also rules out a relative density \(9/16\) of candidate prime kernels.
[Standard-library verifier for the local tests, rank and tangent](abc_cyclotomic_ninth_least_positive_kernel.py)

Every prime of \(\Phi_9\) other than \(3\) has order nine for \(A/B\)
modulo that prime, hence is \(1\bmod9\). The form is odd. Thus the only
squarefree candidates below \(73\) are \(1,3,19,37,57\).
The first two have no slope \(A>B>0\) by the previously determined
rational points of those twists. [Kernels one and three](abc_cyclotomic_sextic_square_points.md)

## A local obstruction over the real cubic field

Put \(a=2\cos(2\pi/9),\ b=a^2-2,\ c=-a-b\). These conjugates satisfy
\(g(X)=X^3-3X+1\). The cyclic field \(K=\mathbf Q(a)\) has ring of
integers \(\mathbf Z[a]\), discriminant \(81\), and class number one.
Its unit squareclasses are determined by the three signatures. These
facts follow from the Minkowski bound and the signatures of the unit
conjugates of \(a\). [Field calculations](abc_cyclotomic_sextic_square_points.md)

The three totally positive factors
\(F_i=A^2-iAB+B^2\), for \(i=a,b,c\), multiply to \(\Phi_9(A,B)\).
Common prime divisors of two factors lie above \(3\), by their
differences and primitivity. At \(3\), the unique prime is generated
by \(\pi=2-a\), of norm three. When \(3\mid\Phi_9\), \(A\equiv
B\not\equiv0\bmod3\); then \(F_i=(A-B)^2+(2-i)AB\) has valuation
one there. For a split prime \(p\equiv1\bmod9\) in the kernel, each
\(F_i\) has odd valuation at one of the three primes above \(p\):
its norm is \(\Phi_9\), and a prime of \(K\) cannot divide two of
the \(F_i\). Thus for \(D=p\) or \(3p\) the squareclass of \(F_a\)
is one of three conjugate totally positive generators \(\beta_j\).
Their norms are \(D\), and in the second case all contain the ramified
prime. Class number one and the unit signatures remove the remaining
unit ambiguity.

For each row below take the listed \(\beta_0\) and its two conjugates.
The entries count ordered pairs \((A,B)\bmod8\) not both even with
\[
         A^2-aAB+B^2\equiv\beta_j t^2\bmod8\mathbf Z[a].
\]
The generators have the indicated norms by substitution into \(g\).

| \(D\) | \(\beta_0\) | Counts for \(\beta_0,\beta_1,\beta_2\) |
|---:|---|---|
| 19 | \(1+a+a^2\) | \(0,0,0\) |
| 37 | \(1-a+2a^2\) | \(0,0,0\) |
| 57 | \(5+2a\) | \(16,0,0\) |
| 73 | \(5-2a\) | \(16,0,0\) |
| 111 | \((2-a)(1-a+2a^2)\) | \(0,0,0\) |

One can reproduce the entire table by looping through the \(64\)
coefficient triples of \(t\bmod4\), reducing products by \(a^3=3a-1\),
and testing the \(48\) primitive residue pairs. For \(57,73\) the
surviving pairs have \(AB\equiv2\) or \(6\bmod8\).

The reciprocal rational elliptic quotient gives an independent short
test at \(D=111=3\cdot37\). Its model has coefficients
\([0,27D,0,99D^2,9D^3]\), abscissa
\(3D((A+B)/(A-B))^2\), and at \(D=111\) PARI/GP returns rank interval
\([0,0]\) and torsion order one:

~~~gp
D=111; E=ellinit([0,27*D,0,99*D^2,9*D^3]); [ellrank(E),elltors(E)]
~~~

The special slopes \(A=\pm B\) and \(AB=0\) have kernels three or one.

The product of primes **other than three** with odd valuation in \(\Phi_9(A,B)\) also has minimum 73 on positive \(A>B\). If this product were smaller, it could only be \(1,19,37\); the corresponding kernels are \(1,3,19,57,37,111\), all excluded on that domain. For \(\Phi_{18}(A,B)\) the least full squarefree kernel is 57, attained at \((2,1)\), since the smaller candidates \(1,3,19,37\) are excluded at the corresponding negative slopes apart from projective slopes outside this domain.

## The unique cover at \(57\)

Use \(\beta=5+2a\) and \(e=57/\beta=4a^2-10a+13\). For \(t=A/B\ne0\)
write \(S=t+t^{-1}\). The factors \(F_b,F_c\) have squareclass product
\(e\); also \(S^2-4=(t-t^{-1})^2\). This gives a point over \(K\) on
\[
             V^2=e(S-2)(S+2)(S-b)(S-c).
\]
Put \(h=4(2-b)(2-c)\) and \(d=(h/4,h/(2-b),h/(2-c))\).
The change \(X=he/(S-2),\ Y=heV/(S-2)^2\) gives
\[
        E\colon Y^2=\prod_{i=1}^3(X+e d_i),\qquad S=2+he/X .
\]
The point \(P=(-2he/9,he^2/27)\) has \(S=-5/2\).

**Rank certificate.** The full two-descent uses the classes of
\(X+ed_1,X+ed_2\). Away from the primes of \(2,3\) and the two factors
of \(e\) above \(19\), these have even valuations: the roots are
distinct there, and the product is square. At a two-torsion point
replace the zero factor by the product of its two companions.
Writing triples in the basis \(1,a,a^2\), the seven generators for
each global coordinate are
\[
         -1,\ a,\ b,\ 2,\ 2-a,\ (1,-3,3),\ (19,-3,-6).
\]
The last two are \((5+2b)/(2-b)\) and \((5+2c)/(2-c)\), both totally
positive of norm \(19\). The possible real sign pairs, in the three
embeddings \(a,b,c\), are \((+,+)\) or, respectively, \((-,+),(-,-),
(-,+)\). Indeed \(d_1\) is always smallest, and \(d_2<d_3\) only in
the middle embedding.

The following local generators and counts give the complete filtration.
At the odd places the two displayed torsion abscissae already generate
the four-element image. At the inert dyadic place the five listed
abscissae generate \(32\) elements. These cardinalities exhaust
\(E(K_v)/2E(K_v)\) by the formal-group index formula.

| Constraint | Local generating abscissae | Global pairs left |
|---|---|---:|
| Prime support | | 16384 |
| Three real places | | 2048 |
| Above \(3\) | \(-ed_1,-ed_2\) | 512 |
| \(a\equiv3\bmod19\) | \(-ed_1,-ed_2\) | 128 |
| \(a\equiv9\bmod19\) | \(-ed_1,-ed_2\) | 32 |
| Above \(2\) | \(-ed_1,-ed_2,(-5,-1,-5),(-4,-3,1),(-4,1,-3)\) | 8 |

For reproduction, enumerate all products of subsets of the seven
generators separately in each coordinate. Filter the sign pairs, then
retain the pairs whose images lie in the subgroup generated by the
displayed points. At \(3\) divide off \(2-a\) using \(3/(2-a)=(1+a)^2\);
the remaining residue uses \(a=2\bmod3\). At \(19\) evaluate at the
Hensel lift of the indicated root of \(g\). In both cases record
valuation parity and the Legendre sign of the unit part. At \(2\)
record valuation parity and the unit part modulo unit squares in
\((\mathbf Z[a]/8)^\times\). These tests also check that the product
at every nontorsion local abscissa is a square. Since \(E[2](K)\)
has order four, the final count gives rank at most one.

**The inert prime \(5\).** Modulo five, the square test on
\(57z^2=\Phi_9(A,B)\) excludes \(t=0,\infty,-1\). The others,
\(t=1,2,-2\), give \(S=2,0,0\), respectively. Good reduction at \(5\)
now puts the global elliptic point in a residue disk centered at
\(O,P,-P\): \(X\) has a pole above \(S=2\), and \(P,-P\) reduce to
distinct points above \(S=0\).

In \(k=\mathbf F_5[\bar a]\), the reduced group has order \(124\),
and \(\bar P\) has order \(31\). With \(\tau=-X/Y\) the formal
parameter, exact multiplication gives
\[
       v_5(\tau(31P))=1,\qquad
       w=\tau(31P)/5\bmod5=4+3\bar a+\bar a^2.
\]
The formal logarithm has this same first residue and is injective on
the kernel of reduction, proving \(P\) nontorsion and rank one.
Every nonzero global point in that kernel has initial parameter residue
proportional to \(w\) over \(\mathbf F_5\), since its logarithm is a
rational multiple of \(\log_E(31P)\). This argument requires no
saturation of \(P\). At \(O\), the first term of \(S-2\) is \(he\tau^2\);
at \(\pm P\), translation by a formal point gives first term
\(\mp(3e/2)\tau\) for \(S+5/2\), by \(dX/(2Y)\). The relevant
coefficients evaluated on the formal direction are
\[
 hew^2=4+3\bar a+4\bar a^2,\qquad -(3e/2)w=\bar a+\bar a^2\quad\text{in }k.
\]
Neither is rational over \(\mathbf F_5\), so the only points in the
three disks with rational \(S\) are the centers. The value \(S=2\)
gives \(t=1\), for which the kernel is three. The value \(-5/2\)
gives \(t=-2,-1/2\), each attaining kernel \(57\). The endpoints
give kernel one. This proves the asserted minimum, since
\(\Phi_9(2,1)=73\).

The following PARI/GP commands independently reproduce the tangent
and finite-group calculations; the rank computation can also be
repeated with Denis Simon's full two-descent. After loading his
\(\texttt{ell.gp}\) and its dependencies,
\(\texttt{bnfellrank(K,E[1..5],[],1,0)}\) gives \([1,3,\ldots]\),
where the second entry includes the two dimensions of rational
two-torsion. [Simon two-descent](https://simon.perso.math.cnrs.fr/)

~~~gp
g=y^3-3*y+1; K=bnfinit(g,1); bnfcertify(K)
a=Mod(y,g); b=a^2-2; c=-a-b; h=4*(2-b)*(2-c); e=57/(5+2*a);
d=e*[h/4,h/(2-b),h/(2-c)];
E=ellinit([0,vecsum(d),0,d[1]*d[2]+d[2]*d[3]+d[1]*d[3],prod(j=1,3,d[j])],K);
P=[-2*h*e/9,h*e^2/27]; pr=idealprimedec(K,5)[1]; mpr=nfmodprinit(K,pr);
red(z)=nfmodpr(K,z,mpr);
F=ellinit(apply(red,E[1..5])); [ellcard(F),ellorder(F,apply(red,P))]
R=ellmul(E,P,31); u=-R[1]/R[2]; w=red(u/5);
[idealval(K,u,pr),w,red(h*e)*w^2,red(-3*e/2)*w]
~~~

## A positive density of excluded prime kernels

Let \(U=(\mathcal O_K/8)^\times/((\mathcal O_K/8)^\times)^2\).
It has order \(16\): the \(448\) units modulo eight have \(28\)
squares. Write \(T\subset U\) for the classes of
\(A^2-aAB+B^2\bmod8\) from the \(48\) primitive residue pairs.
All these factors are units at \(2\). Enumerating as in the table
gives \(\#T=5\) and
\(\#T'=\#\bigcup_{\sigma\in\mathrm{Gal}(K/\mathbf Q)}\sigma T=7\).
Thus nine classes have no conjugate compatible with the local test.

A prime ideal of \(K\) away from two has a totally positive generator
whose image in \(U\) is well-defined, because totally positive units
are squares. This defines a surjection of the narrow ray class group
of modulus \(8\) and all real places onto \(U\): every unit residue
has a totally positive lift by adding a sufficiently large multiple
of eight. The corresponding class field is unramified over \(K\) at
\(3\), whereas \(\mathbf Q(\zeta_9)/K\) is quadratic and ramified
there. The extensions are disjoint over \(K\). Chebotarev therefore
distributes prime ideals uniformly in \(U\) even after requiring
splitting in \(\mathbf Q(\zeta_9)\). Degree-one prime ideals have
density one among prime ideals of \(K\). Their underlying rational
primes under the splitting requirement are \(p\equiv1\bmod9\),
and each such prime gives three conjugate ideals. The excluded
condition is conjugation-invariant. Thus this test alone excludes a
relative density \(9/16\) of the rational primes \(p\equiv1\bmod9\)
as kernels \(D=p\). For \(D=3p\) multiply the class by \(2-a\);
its conjugates differ by totally positive units and hence by squares,
so the exclusion density is again \(9/16\). Among the sixteen classes
\(u\), six have both \(u,(2-a)u\) outside \(T'\), three have just the
first outside, three just the second, and four have both inside.
Consequently the same calculation rules out **both** kernels \(p,3p\)
for a relative density \(3/8\) of the candidate primes.

At \(D=73\), \(t=2,1/2\) attain the kernel with \(z=1\) in primitive
coordinates. These seeds have no prime \(p>A^2\) with
\(p^2\mid\Phi_9(A,B)\). The minimum calculation alone does not
classify every slope at \(73\) or decide that prime-square condition
there.
