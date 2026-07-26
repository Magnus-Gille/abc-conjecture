# Proposed technical body for `CONCLUSION.md`

Author: `codex`  
Date: 2026-07-25  
Status: draft module for Claude's integration and adversarial review; not a
joint conclusion and not signed.

## Audit of the inherited arithmetic-derivative argument

Let \(a,b,c\) be positive, pairwise coprime integers with \(a+b=c\), let
\(S\) be the primes dividing \(abc\), and put
\[
R=\operatorname{rad}(abc).
\]
For \(x=(x_p)_{p\in S}\in\mathbf Z^S\), define
\[
D_x(n)=n\sum_{p\mid n}\frac{v_p(n)x_p}{p},
\qquad
H(x)=\max_{p\in S}|x_p|.
\]
The inherited argument imposes
\[
D_x(a)+D_x(b)=D_x(c)
\tag{A}
\]
and uses the arithmetic Wronskian
\[
W_x(a,b)=aD_x(b)-bD_x(a).
\]

Both agents independently checked the load-bearing calculation. Since
\(n/\operatorname{rad}(n)\mid D_x(n)\), pairwise coprimality and (A) imply
\[
\frac{abc}{R}\mid W_x(a,b).
\]
On the other hand,
\[
\begin{aligned}
|W_x(a,b)|
 &=ab\left|
 \sum_{p\mid b}\frac{v_p(b)x_p}{p}
 -\sum_{p\mid a}\frac{v_p(a)x_p}{p}
 \right|\\
 &\le ab\,H(x)\log_2 c.
\end{aligned}
\]
Consequently every nondegenerate certificate \(W_x(a,b)\ne0\) satisfies
\[
\boxed{\quad
  c\le R\,H(x)\log_2 c,
  \qquad
  H(x)\ge\frac{c}{R\log_2c}.
\quad}
\tag{B}
\]

Thus the divisibility calculation is correct, but the desired uniform
sub-power upper bound for a nondegenerate \(H(x)\) already carries the
missing abc-strength information. This is not a newly reduced lemma:
Hector Pasten's published arithmetic-derivative framework proves that the
appropriately formulated Small Derivatives Conjecture is equivalent to
abc, and that a power saving at the relevant geometry-of-numbers step
would imply abc. The inherited attempt reaches that same open step.

There is also a necessary qualification to the inherited all-triples
formulation. For a Mersenne-prime triple
\[
(1,2^n-1,2^n),
\]
nondegeneracy forces \(H(x)\ge n2^{n-1}\), even though
\(R=2(2^n-1)>c\). Therefore, conditional on infinitely many Mersenne
primes, the literal auxiliary lemma fails. This is not a conditional
counterexample to abc; it only explains why Pasten's precise formulation
excludes the exceptional \((1,N,q)\)-prime shapes.

As a finite check, both agents independently solved the exact
nondegenerate-height problem for the Reyssat triple
\[
(a,b,c)=(2,3^{10}\!\cdot109,23^5).
\]
The minimum is
\[
H^*=601,
\]
attained by the coefficient vector
\[
(x_2,x_3,x_{109},x_{23})=(601,-38,-79,-586),
\]
for which \(W_x=-abc/R\). This confirms sharpness of the divisibility
calculation in that example, not a uniform estimate.

## Why higher first-order Wronskians do not amplify the bound

Let \(T(a,b)\) be the lattice of solutions of (A), and let
\[
T^\circ(a,b)=\{x\in T(a,b):W_x(a,b)=0\}.
\]
The checked rank calculation is
\[
\operatorname{rank}T=\omega(abc)-1,\qquad
\operatorname{rank}T^\circ=\omega(abc)-2.
\]
All first-order Wronskian information therefore factors through the
rank-one quotient \(T/T^\circ\).

More explicitly, the logarithmic-differential row associated with \(x\) is
\[
\left(
\frac{D_x(a)}a-\frac{D_x(c)}c,\,
\frac{D_x(b)}b-\frac{D_x(c)}c
\right)
=
\left(-\frac{W_x}{ac},\,\frac{W_x}{bc}\right).
\]
Every such row is proportional to the same vector. Hence every alternating
determinant made from two or more first-order derivations vanishes. The
natural \(3\times3\) determinant with columns for \(a,b,c\) also vanishes
because its \(c\)-column is the sum of the other two.

Multiplying \(k\) ordinary nonzero Wronskians does not help: taking the
\(k\)-th root gives (B) again with \(H\) replaced by the geometric mean of
the \(k\) heights. Iterating \(D_x\) is not covered by the argument because
the first differentiation introduces new prime support and loses the
additivity and divisibility conditions. No controlled higher-order theory
was found. This closes amplification within the inherited first-order
framework.

## Bounded prime support

Write \(\nu=\omega(abc)\). Pasten's classification, using Mihăilescu's
theorem, shows that the primitive triples with \(\nu\le2\) are, up to
order,
\[
(1,1,2),\qquad(1,8,9),\qquad(1,2^n,q)
\]
with \(q\) prime and the displayed terms satisfying the additive relation.
They are harmless for abc; in the infinite-shaped case \(R=2q\) exceeds
the largest term.

The next case is already a genuine uniformity problem. If all three terms
are greater than one and \(\nu=3\), pairwise coprimality forces an equation
\[
p^\alpha+q^\beta=r^\gamma
\]
with distinct primes. If one term is \(1\), the other terms form a
variable-\(S\) unit equation on three varying primes. Fixed-\(S\) unit
finiteness and fixed-signature generalized-Fermat finiteness do not give a
uniform near-linear radical bound while the primes, signatures, or both
vary.

Known fixed-\(\nu\) logarithmic-form estimates control exponent products
but yield only height bounds of the shape
\[
c\le \exp\!\left(C_{\delta,\nu}R^{1+\delta}\right),
\]
far weaker than the abc target
\[
\log c\le(1+\epsilon)\log R+O_\epsilon(1).
\]
Likewise, in the rank-two derivative lattice for \(\nu=3\), converting a
lower bound on the dependent direction into a power saving for a
complementary nondegenerate vector would require a positive-power lower
bound for \(R\) in terms of \(c\). That is already abc-type input. The
bounded-support split therefore reaches the variable generalized-Fermat
and variable-\(S\) frontier rather than a solved finite problem.

## Exact obstruction in the quadratic transformation orbit

For a primitive triple of opposite parity, consider
\[
(a,b,c)\longmapsto\bigl(4ab,(a-b)^2,c^2\bigr).
\tag{C}
\]
Starting from \((a_0,b_0,c_0)=(1,8,9)\), put \(d_n=a_n-b_n\).
Then
\[
c_{n+1}=c_n^2,\qquad
d_{n+1}=c_n^2-2d_n^2,\qquad
c_n=9^{2^n},
\]
and
\[
-\frac{d_n}{c_n}=T_{2^n}(7/9).
\]
The \(d_j\) are pairwise coprime and coprime to \(6\), and a direct support
calculation gives
\[
R_n=\operatorname{rad}(a_nb_nc_n)
   =6\prod_{j<n}\operatorname{rad}(d_j).
\]

Separate real-size effects from repeated prime powers by defining
\[
t_j=\frac{|d_j|}{c_j},
\qquad
Q_n=\prod_{j<n}\frac{|d_j|}{\operatorname{rad}(d_j)}.
\]
Since \(\prod_{j<n}c_j=c_n/9\), there is an exact identity
\[
\boxed{\quad
\frac{R_n}{c_n}
=\frac23\,\frac{\prod_{j<n}t_j}{Q_n}.
\quad}
\tag{D}
\]
In particular, (C) gives an unconditional infinite family with
\(R_n<(2/3)c_n\), so finite quality amplification really occurs and the
contrary claim in `firsttryabc.md` was corrected.

Let
\[
z=\frac{7+4i\sqrt2}{9}.
\]
It is algebraic of modulus one and is not a root of unity. For
\(N=2^j\),
\[
t_j=\frac12|z^{2N}+1|.
\]
A standard Baker--Wüstholz lower bound for the corresponding nonzero
linear form in logarithms gives
\[
-\sum_{j<n}\log t_j=O(n^2)=o(\log c_n).
\]
Combining this with (D) yields the exact asymptotic reduction
\[
\boxed{\quad
\log\frac{c_n}{R_n}=\log Q_n+O(n^2).
\quad}
\tag{E}
\]
Both agents independently derived and checked (D)--(E).

If \(q_n=\log c_n/\log R_n\), then
\[
q_n\to1
\quad\Longleftrightarrow\quad
\log Q_n=o(\log c_n),
\]
while a fixed \(\delta>0\) can satisfy \(q_n\ge1+\delta\) infinitely often
only if, along that subsequence,
\[
\log Q_n\ge
\frac{\delta}{1+\delta}\log c_n-o(\log c_n).
\]
Thus this orbit disproves abc only if repeated prime powers accumulate at
positive-power scale.

The same sequence is a Lucas sequence at dyadic indices:
\[
|d_j|=\frac12\left|V_{2^{j+1}}(2,9)\right|.
\]
For
\(\alpha=1+2\sqrt{-2}\), \(\beta=1-2\sqrt{-2}\), and
\(u=\alpha/\beta\), a prime \(p\nmid6\) dividing \(d_j\) forces
\[
\operatorname{ord}_p(u)=2^{j+2}.
\]
The stronger condition \(p^2\mid d_j\) is a Lucas/number-field
Wieferich lift. Ordinary primitive-divisor theorems say that new primes
occur; they do not control these lifts or the aggregate squarefree part
strongly enough to decide (E). Even relevant squarefree primitive-divisor
results over number fields are conditional on Vojta-type conjectures and
remain too weak for the proportional bound needed here.

As a bounded check, the recurrence was tested modulo \(p^2\) for every
prime \(p\le10^7\) and \(0\le j\le50\). No square lift was found among the
664,577 primes tested after excluding \(2,3\). This is reproducible finite
evidence only and is not used as a theorem.

## Other inherited construction attempts

The remaining routes in `firsttryabc.md` were also accounted for:

- A fixed finite prime set cannot support an infinite counterexample
  family, by the \(S\)-unit theorem. Allowing the prime set to vary removes
  that finiteness.
- Naive smooth-number pigeonhole counts collapse after common factors are
  cancelled; the number of distinct reduced exponent vectors is too small
  to force the required fixed-power congruence.
- A fixed coprime polynomial identity is constrained by
  Mason--Stothers. Exceptional integer specializations with a
  positive-power repeated part ask for the same kind of unresolved radical
  control as abc.
- No Pell or elementary recurrence family examined retains a proven fixed
  quality gap. New prime divisors enter, and the available estimates do not
  control their repeated powers.
- The auxiliary-congruence/determinant proposal either vanishes on the
  rank-one quotient described above or incurs coefficient size matching
  its divisibility gain.

The powerful-part counting model is intentionally left to Claude's
separately assigned heuristic section. It is not a proof that
counterexamples are finite.

## Technical branch verdict

The inherited Wronskian argument is correct through (B), but its missing
height statement is a published abc-equivalent conjecture. Higher
first-order determinants vanish or reproduce the same bound. Bounded
support reaches variable generalized Fermat and variable-\(S\) problems.
The only promising transformation reduces exactly to an open aggregate
Lucas/Wieferich radical-growth problem. The remaining elementary
construction ideas supply no fixed-gap counterexample family.

Accordingly, this technical audit supplies neither a proof nor a
disproof. It records why each examined route cannot advance without a new
result at least as hard as a recognized open problem. The global verdict,
current literature seal, and termination statement remain for the joint
cross-audited `CONCLUSION.md`.
