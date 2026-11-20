# Arbitrarily small radical exponents on images that retain the abc conjecture

For each fixed integer \(k\ge3\), there is an explicit rational polynomial \(f_k\) with the following two properties. For a reduced rational \(0<t<1\) with \(0<f_k(t)<1\), write \(f_k(t)=A'/C'\) in lowest terms and put \(B'=C'-A'\), \(R'=\operatorname{rad}(A'B'C')\).

1. Unconditionally, every such image satisfies
   \[
   \log C'\ll_k (R')^{1/k}(\log(2R'))^3.
   \]
2. The rational abc conjecture follows if, for this one fixed \(f_k\), all its images satisfy \(C'\ll_{k,\eta}(R')^{1+\eta}\) for each \(\eta>0\). Conversely, rational abc implies this image bound.

The maps can be different for different \(k\). In the first inequality the logarithm on the height is essential. Constants depend on the chosen map. A map of degree three gives a concrete example at \(k=5\).

## Height from three marked points

Let \(L_1,\dots,L_k\) be fixed, pairwise nonproportional primitive integral linear forms in two variables. Write \(H=\max(|x|,|z|)\) for coprime integral \(x,z\), assume that every \(L_i(x,z)\ne0\), and write \(D=\operatorname{rad}(|\prod_i L_i(x,z)|)\). Then
\[
 \log(2H)\ll_{L_1,\dots,L_k}D^{1/k}(\log(2D))^3.                    \tag{1}
\]
Indeed, any three forms satisfy a linear relation with three nonzero fixed integral coefficients. Evaluate, divide by the common gcd and move the term of opposite sign to the other side to obtain a primitive positive triple. Its largest term is comparable to \(H\). For the lower bound, any two of the original forms recover \((x,z)\) by an invertible fixed linear map; the common gcd of their values divides their determinant by primitivity of \((x,z)\). Including the fixed coefficients still leaves a bounded common gcd.

Exclude once and for all the primes dividing any coefficient in these relations or any pairwise determinant. Every other prime divides at most one form at \((x,z)\). Thus it divides the radicals of at most \(\binom{k-1}{2}\) of the \(\binom{k}{3}\) triples. The fixed exceptional primes contribute a bounded factor to the product, uniformly in \(x,z\). At least one triple has radical \(\ll D^{3/k}\). Stewart and Yu's bound \(\log C\ll R^{1/3}(\log(2R))^3\) for primitive positive triples gives (1). C. L. Stewart and K. Yu, *On the abc conjecture, II*, Duke Math. J. **108** (2001), 169–181, Theorem 1.

## Constructing the map

Mark \(0,1,\infty\) and any \(k-3\) other distinct rational points in \((0,1)\). For a definite choice use \(1/j\) for \(2\le j\le k-2\). Start with the identity polynomial. If a marked point still has image \(r\notin\{0,1,\infty\}\), it lies in \((0,1)\). Choose positive integers \(m,n\) with \(r=m/(m+n)\) and postcompose with
\[
 g_r(u)=\frac{u^m(1-u)^n}{r^m(1-r)^n}.
\]
On \([0,1]\) this polynomial has maximum 1 at \(r\) and maps both endpoints to zero. It fixes infinity. Its derivative has no other critical points except possibly the endpoints, so its branch values lie among \(0,1,\infty\). Postcomposition preserves this property and keeps previously treated points in these three fibers. Each step treats another marked point; choose them in the listed order to fix one map per \(k\). The resulting \(f=f_k\) is a Belyi polynomial over the rationals.

Write \(t=x/z\) with \(0<x<z\) and \((x,z)=1\). Outside a fixed finite set of primes of bad reduction for the map and marked points, a prime dividing a marked linear form sends the reduction of \(t\) to the corresponding marked point. Its image therefore reduces to \(0,1\) or \(\infty\); the prime divides \(A'B'C'\). This gives \(D\ll_f R'\). The naive heights satisfy \(C'\asymp_f z^d\) for \(d=\deg f\): in a fixed integral homogeneous presentation of \(f\), the two output coordinates have bounded common gcd by the resultant, and their real maximum on normalized input coordinates is bounded above and below. Since \(0<f(t)<1\), the output height equals \(C'\). Apply (1).

## Recovering the endpoint conjecture

The distinct points over \(0,1,\infty\) number \(d+2\) over the algebraic closure. The three fibers have total multiplicity \(3d\); all \(2d-2\) units of ramification from the Riemann–Hurwitz formula occur in those fibers. Consequently the primitive integral homogeneous polynomial cutting out the reduced boundary has degree \(d+2\). The three marked points \(0,1,\infty\) supply factors \(X,Z-X,Z\). The remaining homogeneous factor has degree \(d-1\). Outside fixed bad primes the prime divisors of \(A'B'C'\) divide this boundary polynomial evaluated at \((x,z)\), by the same reduction argument. Thus, putting \(R=\operatorname{rad}(x(z-x)z)\), we obtain
\[
             R'\ll_f R z^{d-1},\qquad C'\asymp_f z^d.                  \tag{2}
\]
For a desired \(\varepsilon>0\), apply the endpoint image bound with \(\eta=\varepsilon/(d+(d-1)\varepsilon)\). Equation (2) gives \(z^{1-(d-1)\eta}\ll R^{1+\eta}\), hence \(z\ll_{f,\varepsilon} R^{1+\varepsilon}\). The finitely many boundary inputs give bounded heights and are absorbed into the constant. The reverse implication follows by applying abc to each primitive image triple.

More generally, let \(D\) be the radical of the product of the \(k\) marked forms. Removing those \(k\) points from the reduced boundary gives \(R'\ll_f D z^{d+2-k}\). The same endpoint calculation would give \(D\gg_{f,\delta}z^{k-2-\delta}\) for every \(\delta>0\). Conversely, the \(k-3\) additional marked linear forms have product of size \(O_f(z^{k-3})\), so this last lower bound implies abc for \(x+(z-x)=z\). This describes the open estimate directly in the linear forms of (1).

## A cubic example

Take \(f(t)=27t^2(1-t)/4\). Its five rational boundary points are \(0,1,\infty,2/3,-1/3\). The unnormalized positive triple at \(t=x/z\), apart from the boundary inputs, is
\[
 27x^2(z-x)+(3x-2z)^2(3x+z)=4z^3.
\]
Divide by the common gcd. The five linear forms \(x,z-x,z,3x-2z,3x+z\) give ten three-term relations; outside 2 and 3, any prime in their values occurs in six of those relations. Formula (1) therefore gives the exponent \(1/5\) on the resulting primitive triples. For example, \(t=1/3\) gives \(1+1=2\) after reduction, and \(t=1/4\) gives \(81+175=256\). [Arithmetic check of the cubic and all ten relations](abc_marked_rational_cubic.py)

Inequality (2) also shows where an attempted proof for all triples stops. Substituting it into the **unconditional** estimate introduces a factor \(z^{(d-1)/k}\) on the right of a bound for \(\log z\). The endpoint transfer works because there the left side grows as \(z^d\). Increasing the number of marked points by itself does not close this gap.
