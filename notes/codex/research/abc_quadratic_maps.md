# Transferring abc to squares with a prescribed power as their sum

Let \(a+b=c\) with \(0<a<b\) and \(\gcd(a,b)=1\). Write \(R=\operatorname{rad}(abc)\), the product of the distinct prime divisors. The only omitted equal-addend primitive triple is \(1+1=2\).

## A transfer for every input triple

For **each** \(m=2^k\), \(k\ge1\), one can construct positive coprime \(X,Y\) and an odd \(Z\) with \(X^2+Y^2=Z^m\). Put \(C=Z^m\) and \(R'=\operatorname{rad}(XYZ)\). Then

\[
\frac{C}{R'}\ \ge\ \frac{a^2+b^2}{(b-a)R}
   \ =\ \frac{c}{R}\frac{a^2+b^2}{b^2-a^2}
   \ >\ \frac{c}{R},\qquad
\frac{c^2}{4}\le Z\le c^2 .
\tag{1}
\]

In particular, for each fixed \(m=2^k\), rational abc is equivalent to its restriction to primitive triples \(X^2+Y^2=Z^m\).

To prove (1), set \(t=1\) when \(a,b\) have opposite parity and \(t=2\) when both are odd. Choose the Gaussian integer \(x+iy\) by

\[
(x,y)=
\begin{cases}
(b,a)&t=1,\\
(c/2,(b-a)/2)&t=2.
\end{cases}
\]

In the second case, any common divisor of \(x,y\) divides both \(b=x+y\) and \(a=x-y\), and \(x+y=b\) is odd. Thus in both cases \(x,y\) are positive, coprime, and of opposite parity. Their norm is \(Z=x^2+y^2=(a^2+b^2)/t\). The two bounds on \(Z\) follow from \(c^2/2\le a^2+b^2\le c^2\).

Put \(u_s+i v_s=(x+iy)^{2^s}\) for \(s\ge0\), and take \(X=|u_k|,\ Y=|v_k|\). Squaring gives \(u_{s+1}=u_s^2-v_s^2,\ v_{s+1}=2u_sv_s\). For \(s\ge1\), \(u_s\) is odd and \(v_s\) even. No odd prime can enter both coordinates, by the two formulas and induction. The odd coordinates are nonzero, and the formula for \(v_s\) preserves nonvanishing. Taking norms gives \(X^2+Y^2=Z^m\).

Iteration of the second coordinate formula gives
\[
u_kv_k=2^kxy\prod_{s=1}^k u_s.
\]
When \(t=1\), \(xyu_1=ab(b-a)c\). When \(t=2\), \(u_1=ab\), and \(x=c/2,\ y=(b-a)/2\). In both cases the primes from \(2^kxyu_1\) lie among those of \(abc\) and \((b-a)/t\); the prime 2 already divides \(abc\). Also \(|u_s|\le Z^{2^{s-1}}\). Hence
\[
 R'\le R\,\frac{b-a}{t}\,Z\prod_{s=2}^k |u_s|
     \le R\,\frac{b-a}{t}\,Z^{m-1}.
\]
Division proves (1), including \(k=1\) with the empty product.

For the equivalence, failure of abc would give a fixed \(\eta>0\) and infinitely many triples with \(c/R\ge c^\eta\). This formulation follows by shrinking the exponent if necessary. Equation (1) and \(C\le c^{2m}\) give \(C/R'\ge C^{\eta/(2m)}\). Also \(C\to\infty\) along the sequence by the lower bound on \(Z\). Thus some fixed exponent greater than 1 fails on this restricted class as well. The other implication follows because every restricted triple is a primitive abc triple. Keeping \(m\) fixed matters to this argument.

For example, take \(8+9=17\). Squaring \(9+8i\) gives \(17^2+144^2=145^2\). The original radical is \(102\), and the new radical is \(14790\). Equality holds in the first bound of (1) in this example. Taking the fourth Gaussian power gives \(20447^2+4896^2=145^4\).

### A concrete equivalent estimate using degree at most two

For \(m=4\) the real and imaginary parts of \((x+iy)^4\) factor over the integers. Define
\[
P(x,y)=xy(x-y)(x+y)(x^2+y^2)(x^2+2xy-y^2)(x^2-2xy-y^2).
\]
For coprime \(x>y>0\) of opposite parity, the two legs before squaring are \(\left|(x^2+2xy-y^2)(x^2-2xy-y^2)\right|\) and \(4xy(x-y)(x+y)\). The sum of their squares is \((x^2+y^2)^4\). Their triple's radical is exactly \(\operatorname{rad}(|P(x,y)|)\), since \(2\mid xy\).

The seven displayed factors are pairwise coprime in absolute value. A prime dividing \(xy\) divides no other factor. Of the remaining factors all are odd; an odd prime dividing \(x-y\) or \(x+y\) cannot divide another by substituting \(x=\pm y\) modulo that prime. The two last quadratics differ by \(4xy\). A common odd divisor of either one and \(x^2+y^2\) would force \(x=\pm y\) modulo that prime by subtracting the quadratics, which is incompatible with \(x^2+y^2=0\) there.

Consequently full rational abc is equivalent to this single statement: for every \(\delta>0\) there is a \(K_\delta>0\) such that
\[
\operatorname{rad}(|P(x,y)|)\ge K_\delta\,x^{8-\delta}
\]
for all such pairs. In one direction apply abc to the displayed triple, using \(x^8\le(x^2+y^2)^4\le16x^8\) and adjusting the exponent. In the other direction, the pairs produced from arbitrary input triples by (1) are in this range. The estimate would give abc on all their images, which suffices by the transfer. The product has degree ten; the desired exponent eight permits a loss of two degrees across the seven factors.

## All choices of quadratic map with three prescribed branch values

Encode a primitive triple as \(x=a/c\), with marked set \(B=\{0,1,\infty\}\). Consider rational maps of degree two which send \(B\) into \(B\) and have every critical value in \(B\). The first condition preserves existing prime support away from primes of bad reduction. The second minimizes the number of distinct preimages of \(B\).

Up to permutation of the output coordinates there are six such maps. For each row below, divide the two displayed addends by their gcd, and take their sum as the output height. Reorder the addends before the next step.

| Choice | Additional factor \(w\) | Addends before division |
|---|---|---|
| A | \(c+a\) | \(a^2,\ b(c+a)\) |
| A* | \(c+a\) | \(b^2,\ 4ac\) |
| B | \(c+b\) | \(b^2,\ a(c+b)\) |
| B* | \(c+b\) | \(a^2,\ 4bc\) |
| C | \(b-a\) | \(a^2,\ c(b-a)\) |
| C* | \(b-a\) | \((b-a)^2,\ 4ab\) |

Indeed there are two distinct critical values of a quadratic map in characteristic zero. After sending them to \(0,\infty\), the other marked value has two unramified preimages. All four preimages are rational since three are marked rational points and the full set is Galois invariant. A source coordinate taking the critical points to \(0,\infty\) identifies the map with a constant times a square. Rescaling at either of the unramified preimages makes the four points \(0,\infty,1,-1\). Marking any three as \(0,1,\infty\) makes the fourth one of \(-1,2,1/2\). For fourth point \(-1\), the only possible critical pairs are \(\{0,\infty\}\) and \(\{1,-1\}\): in a coordinate taking a proposed pair to \(0,\infty\), the other two must be negatives of each other. These two choices give \(x^2\) and \(((x-1)/(x+1))^2\). Permuting the input marks gives the table. The repository studied the single fixed choice C* on the seed \(1+8=9\). [Fixed-choice calculation](../../../CONCLUSION.md#L194)

For **all six** choices the radical and height satisfy the exact support rule and the bounds
\[
R_{\rm next}=R\,\frac{\operatorname{rad}(w)}{\gcd(2,w)},\qquad
c^2/4\le c_{\rm next}\le4c^2.
\tag{2}
\]
The gcd of the unnormalized addends is 1 or 4. Odd prime support in the output is exactly the union of the old support and the odd prime support of \(w\). No odd prime dividing \(w\) divides \(abc\). Every primitive positive triple includes 2 in its radical. These facts give the support rule. The possible heights can be read from the squares in the table.

## What varying the choice at each step can achieve

Start from any fixed primitive triple with \(c_0>4\). At each node of its tree allow any of the six choices. Write \(h_j=\log c_j\), and \(w_j\) for the additional factor chosen at depth \(j\). For every fixed \(P\ge2\),

\[
h_n-\log R_n
=\sum_{j<n}\ \sum_{p>P}\max(v_p(w_j)-1,0)\log p+o(h_n).
\tag{3}
\]

The error is uniform over all paths of length \(n\). In particular the tree gives a counterexample sequence precisely when some fixed \(\delta>0\) occurs at arbitrarily large depths in the single-step estimate \(\log(w_j/\operatorname{rad}(w_j))\ge\delta h_j\). Equation (3) permits discarding any fixed finite set of primes in this test.

For the approximation step, the three forms defining \(w_j\) have distinct rational roots among \(-1,2,1/2\), all outside \(B\). Every composition \(G\) of \(K\) maps from the table, including coordinate permutations, has its critical values in \(B\), since \(B\) is forward invariant. Therefore the \(2^K\) preimages of any one of those roots are simple. At the real place and each fixed prime \(p\le P\), if \(G(z)\) is close to the root then \(z\) is comparably close, in the local projective distance, to one of those preimages. This follows by factoring at the simple roots and bounding the other factors on a small neighborhood. Outside those neighborhoods the negative logarithm of the distance is bounded. There are only finitely many maps and preimages for fixed \(K\). Roth's theorem, with its \(p\)-adic version at a finite place, bounds the negative logarithm of such a distance from a rational \(z\) by \((2+\epsilon)h(z)+O_{K,P,\epsilon}(1)\). For rational preimages the elementary height bound suffices. Equality with a preimage cannot occur here because a target of height at most \(\log 2\) cannot occur at these nodes. [Related dynamical approximation theorem for semigroups](https://arxiv.org/abs/1903.06328)

By (2), \(h_j=2^Kh_{j-K}+O(2^K)\), and \(h_j\ge2^j\log(c_0/4)+\log4\). At the real place the relevant distance bounds \(\max(0,\log(c_j/w_j))\), up to a constant. At \(p\) its negative logarithm is \(v_p(w_j)\log p\) up to a constant, by primitivity of the homogeneous coordinates and the linear form. Apply the bound with \(z=x_{j-K}\), divide by \(h_j\), let \(j\to\infty\), and then let \(K\to\infty\). This makes both the real contribution and the sum over the fixed primes \(o(h_j)\) uniformly. The opposite real-size error is bounded by \(w_j\le2c_j\).

Finally (2) gives \(h_{j+1}-h_j=h_j+O(1)\). Subtract the logarithmic radical increments in (2) and sum; \(\sum_{j<n}h_j=h_n-h_0+O(n)\) makes the sum of the uniform \(o(h_j)\) errors \(o(h_n)\). This proves (3). Since the remaining terms are nonnegative, a single linear-size contribution suffices, and uniformly sublinear contributions cannot accumulate to a linear one.

## Finite verification

Starting with \(1+8=9\), all six choices were generated at every node through depth five. Identical sorted triples were deduplicated at each depth. The new factors were completely factored, each prime was checked, and integer powers certified the following intervals for the largest quality \(q=\log c/\log R\) at that depth.

| Depth | Distinct triples | Interval for the maximum \(q\) |
|---:|---:|---|
| 1 | 6 | \(1.292<q<1.293\) |
| 2 | 31 | \(1.337<q<1.338\) |
| 3 | 169 | \(1.356<q<1.357\) |
| 4 | 921 | \(1.193<q<1.194\) |
| 5 | 5019 | \(1.183<q<1.184\) |

For instance the depth-three path B*, A, B* gives \(1+27902695680=27902695681\), with radical \(50419110\). The transfer (1) and the primitive identities were independently checked for 732 choices of input and exponent with \(c\le40\) and \(m\in\{2,4,8\}\). The restricted-class equivalence supplies a different proof target. The search and (3) do not establish a counterexample sequence or prove abc on that class.
