# The least degree for the two conjugate points of order two

On the elliptic curve
\[
 E' : y^2=x^3+16x^2+32x,
 \qquad T_\pm=(-8\pm4\sqrt2,0),
\]
the least degree of a Belyi map defined over \(\mathbb Q\) for which both \(T_+\) and \(T_-\) lie above \(0,1,\infty\) is **eight**. Marking them here means inclusion in the union of the three fibers, with any ramification indices allowed. The invariants of this model are \(c_4=2560\), \(\Delta=2^{21}\), and \(j=8000\).

## The upper bound

The map
\[
 \beta=\left(\frac{x^2+16x+32}{32}\right)^2
\]
has degree eight. The degree-two projection to \(x\) branches at \(0,-8\pm4\sqrt2,\infty\). The polynomial \(q(x)=(x^2+16x+32)/32\) sends these to \(1,0,0,\infty\), respectively, and its own branch values are \(-1,\infty\). Squaring takes all these values to \(0,1,\infty\) and has no further branch values. Both marked points lie above zero.

## The lower bound

Use the genus-one records in the Belyi database of Musty, Schiavone, Sijsling and Voight. The checker uses the model-to-dessin identifications supplied by that database. It independently enumerates the expected permutation classes and checks each recorded model's \(j\)-invariant. [Database at the checked revision](https://github.com/michaelmusty/BelyiDB/tree/aa663d2aded41c6844f3237ac26f687f7382bda3) · [Database paper](https://arxiv.org/abs/1805.07751)

| Degree | Permutation classes | Recorded model and embedding entries | Entries with \(j=8000\) |
|---:|---:|---:|---:|
| 3 | 1 | 1 | 0 |
| 4 | 2 | 2 | 0 |
| 5 | 9 | 9 | 0 |
| 6 | 70 | 70 | 0 |
| 7 | 443 | 411 | 0 |

For a degree-\(d\) Belyi map on a genus-one source, Riemann–Hurwitz says that the three fibers contain a total of \(d\) distinct geometric points. Each fiber is nonempty, giving \(d\ge3\). For larger \(d\) the permutation census uses transitive pairs \((a,b)\) of permutations of \(d\) letters up to simultaneous conjugation, with \(c=(ab)^{-1}\). It retains those with a combined total of \(d\) cycles in \(a,b,c\). One ordering of each multiset of three cycle partitions suffices, since a permutation of \(0,1,\infty\) is defined over \(\mathbb Q\) and preserves the marking condition. After fixing \(a\), its centralizer accounts for the remaining simultaneous conjugations. The resulting counts agree with the sums of the catalog's passport sizes separately for every multiset of partitions.

For every individual passport except one, the number of listed model/embedding entries equals its passport size. Several entries may use conjugate coefficients or even the same curve. For each entry the checker takes its five Weierstrass coefficients in the stated defining field and finds a finite-field evaluation with \(\Delta\ne0\) and \(c_4^3-8000\Delta\ne0\). It tests that the field generator satisfies its monic defining polynomial and that all required denominators are invertible at that evaluation. Thus the difference is nonzero in the defining field and at every characteristic-zero embedding. The largest prime needed for these certificates was 61.

The one passport without model entries contains 32 permutation classes of degree seven. Its three partitions are \((6,1),(6,1),(4,2,1)\). In each fiber every ramification index occurs exactly once. For any Belyi map defined over \(\mathbb Q\), Galois conjugation fixes each of the three target values and preserves local ramification indices. It must therefore fix every point in those three fibers for this passport. In particular, if \(T_+\) mapped to one of them then \(T_-\) would map to the *same* value with the same index. The two distinct conjugate points rule this out. This resolves the missing passport for the stated marking problem without computing its elliptic curves. [Passport record](https://github.com/michaelmusty/BelyiDB/blob/aa663d2aded41c6844f3237ac26f687f7382bda3/belyi_db/7/7T7-%5B6%2C6%2C4%5D-61-61-421-g1.m)

The portable checker uses Python's standard library. Give it the upstream git archive at the pinned revision. It checks the embedded commit identifier, reads the degree-three through degree-seven directories, and enumerates the permutations for those degrees. The local archive stream contained that entire range; the checker stops at the next degree. [Checker](abc_octic_marked_belyi_minimum.py) · [Pinned archive](https://codeload.github.com/michaelmusty/BelyiDB/tar.gz/aa663d2aded41c6844f3237ac26f687f7382bda3)
