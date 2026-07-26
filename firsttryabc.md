# Attempted First-Principles Attack on the abc Conjecture

## 1. Goal

The task was to solve the abc conjecture from first principles, either by:

- proving that for every \(\varepsilon>0\), there exists \(K_\varepsilon>0\) such that every coprime positive-integer solution of
  \[
  a+b=c
  \]
  satisfies
  \[
  c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon},
  \]
  or

- disproving it by constructing one fixed \(\varepsilon_0>0\) and infinitely many primitive triples \(a+b=c\) for which
  \[
  c>K\operatorname{rad}(abc)^{1+\varepsilon_0}
  \]
  for arbitrarily large \(K\).

Here
\[
\operatorname{rad}(n)=\prod_{p\mid n}p.
\]

No valid proof or counterexample was found.

---

## 2. Precise form of a counterexample

Define
\[
R=\operatorname{rad}(abc)
\]
and the quality
\[
q(a,b,c)=\frac{\log c}{\log R}.
\]

The conjecture is equivalent to the statement that for every fixed \(\delta>0\), only finitely many primitive triples satisfy
\[
q(a,b,c)\ge 1+\delta.
\]

Therefore, a disproof requires:

- one fixed \(\delta>0\),
- infinitely many primitive triples,
- and
  \[
  c\ge R^{1+\delta}.
  \]

A sequence with \(q\to1\) from above does not disprove abc.

A single high-quality triple also does not disprove abc, because the constant \(K_\varepsilon\) may absorb finitely many exceptional examples.

---

## 3. Arithmetic-derivative / Wronskian approach

A first-principles attempt was made to imitate the derivative proof of the polynomial abc theorem.

For each prime \(p\mid abc\), choose an integer \(x_p\), and define
\[
D_x(n)
=
n\sum_{p\mid n}\frac{v_p(n)}p\,x_p.
\]

This function satisfies the Leibniz rule:
\[
D_x(mn)=mD_x(n)+nD_x(m).
\]

Impose the linear relation
\[
D_x(a)+D_x(b)=D_x(c).
\tag{1}
\]

Define the arithmetic Wronskian
\[
W_x(a,b)=aD_x(b)-bD_x(a).
\]

Using \(a+b=c\) and equation (1),
\[
W_x(a,b)=W_x(a,c)=W_x(c,b).
\]

### Divisibility result

For every positive integer \(n\),
\[
\frac{n}{\operatorname{rad}(n)}\mid D_x(n).
\]

Therefore,
\[
\frac{a}{\operatorname{rad}(a)}\mid W_x(a,b),
\]
\[
\frac{b}{\operatorname{rad}(b)}\mid W_x(a,b),
\]
and
\[
\frac{c}{\operatorname{rad}(c)}\mid W_x(a,b).
\]

Since \(a,b,c\) are pairwise coprime, these three divisors are pairwise coprime. Hence
\[
\boxed{
\frac{abc}{R}\mid W_x(a,b).
}
\tag{2}
\]

If \(W_x(a,b)\ne0\), then
\[
\frac{abc}{R}\le |W_x(a,b)|.
\tag{3}
\]

Let
\[
H(x)=\max_{p\mid abc}|x_p|.
\]

From the definition of \(W_x\),
\[
|W_x(a,b)|
\le
ab\,H(x)\frac{\log c}{\log 2}.
\]

Combining this with (3) gives
\[
\boxed{
\frac{c}{\log c}
\le
\frac{R\,H(x)}{\log 2}.
}
\tag{4}
\]

This is a rigorous bound.

---

## 4. Exact missing lemma

The preceding estimate would prove abc if one could establish the following:

> For every \(\eta>0\), apart from finitely many primitive triples \(a+b=c\), there exist integers \(x_p\) satisfying equation (1), with
> \[
> W_x(a,b)\ne0
> \]
> and
> \[
> H(x)\le C_\eta c^\eta.
> \tag{\(*_\eta\)}
> \]

Indeed, substituting this into (4) gives
\[
\frac{c}{\log c}
\le
C_\eta R c^\eta.
\]

Thus
\[
c^{1-\eta}
\le
C'_\eta R\log c.
\]

For sufficiently large \(c\),
\[
\log c\le c^\eta,
\]
so
\[
c^{1-2\eta}\le C''_\eta R.
\]

Choosing
\[
\eta=\frac{\varepsilon}{2(1+\varepsilon)}
\]
gives
\[
1-2\eta=\frac1{1+\varepsilon},
\]
and therefore
\[
c\le K_\varepsilon R^{1+\varepsilon}.
\]

Thus:
\[
\boxed{
(*_\eta)\text{ for every }\eta>0
\Longrightarrow
\text{abc}.
}
\]

The problem is that \((*_\eta)\) was not proved.

---

## 5. Why Siegel’s lemma does not close the gap

Let
\[
s=\omega(abc),
\]
the number of distinct prime factors of \(abc\).

Equation (1) is one homogeneous linear equation in \(s\) integer variables, so its solution lattice has rank \(s-1\).

Siegel-type lattice arguments produce many small solutions, with a product bound resembling
\[
\prod_{i=1}^{s-1}H(x^{(i)})
\ll s\,c\log c.
\]

However, the solutions satisfying
\[
W_x(a,b)=0
\]
form a sublattice of rank \(s-2\).

Therefore, all the shortest independent solutions may lie inside the degenerate subspace \(W=0\). The first solution with \(W\ne0\) may be the final and largest basis vector, and the product bound permits it to be much too large.

This is the precise obstruction to the arithmetic-Wronskian proof.

---

## 6. Sharpness of the divisibility bound

The classic high-quality triple
\[
a=2,
\]
\[
b=3^{10}\cdot109=6\,436\,341,
\]
\[
c=23^5=6\,436\,343
\]
has
\[
R=2\cdot3\cdot109\cdot23=15\,042
\]
and quality
\[
q\approx1.629911684.
\]

Take
\[
x_2=-721,
\quad
x_3=20,
\quad
x_{109}=79,
\quad
x_{23}=310.
\]

These satisfy
\[
D_x(a)+D_x(b)=D_x(c).
\]

The resulting Wronskian is
\[
W_x(a,b)=5\,508\,110\,403.
\]

But
\[
\frac{abc}{R}
=
3^9\cdot23^4
=
5\,508\,110\,403.
\]

Therefore,
\[
\boxed{
W_x(a,b)=\frac{abc}{R}.
}
\]

So the divisibility lower bound
\[
\frac{abc}{R}\mid W_x(a,b)
\]
can be attained exactly.

This means the lower-bound side of the Wronskian method cannot be strengthened in a simple universal way. Any proof must instead establish a new upper bound for a nondegenerate solution \(x\).

---

## 7. Counterexample attempt via \(S\)-units and smooth numbers

A possible counterexample strategy is to find two numbers composed only of small primes that are unusually close, or unusually close modulo a large number.

The hope is that their difference could create an abc-triple with very small radical relative to \(c\).

The naive pigeonhole argument fails because many pairs of smooth integers reduce to the same rational ratio after cancelling their gcd.

After cancellation, a ratio is represented by an exponent vector
\[
(z_p)_{p\in S}\in\mathbf Z^{|S|}
\]
subject to a weighted bound
\[
\sum_{p\in S}|z_p|\log p\le 2\log X.
\]

The number of genuinely distinct reduced ratios is far smaller than the number of raw pairs.

In the relevant range, this number is only subpolynomial in \(X\), so pigeonhole arguments do not force collisions modulo \(X^\delta\) for a fixed \(\delta>0\).

This does not prove that no counterexample exists. It only defeats the straightforward smooth-number collision construction.

---

## 8. Fixed-prime \(S\)-unit families

A counterexample cannot come from a fixed finite set of primes \(S\).

For fixed \(S\), the equation
\[
u+v=1
\]
in \(S\)-units has only finitely many solutions.

Therefore, any infinite counterexample family must involve a growing set of prime divisors. Its prime support must expand in a genuinely arithmetic way.

---

## 9. Polynomial parametrisation attempt

Another route is to seek a polynomial identity
\[
A(t)+B(t)=C(t)
\]
whose values have unusually small radicals because of repeated factors.

However, the polynomial abc theorem implies
\[
\max(\deg A,\deg B,\deg C)
\le
\deg\operatorname{rad}(ABC)-1
\]
for coprime nonconstant polynomials.

Thus a fixed polynomial identity cannot produce an asymptotic quality above \(1\) merely through repeated polynomial factors.

A counterexample arising from polynomial specialisation would require infinitely many exceptional integer inputs where the polynomial values themselves acquire unusually high prime powers.

That exceptional phenomenon is essentially another form of the original abc problem.

---

## 10. Pell-type and generalized-power families

Pell equations and related recurrences were considered as possible sources of triples with large powers.

These constructions often produce terms with highly structured factorisation, but no family was found where
\[
\frac{\log c}{\log\operatorname{rad}(abc)}
\]
stays uniformly above \(1+\delta\) for one fixed \(\delta>0\).

Typically, either:

- the radical grows almost as fast as \(c\),
- new prime divisors enter the sequence,
- or the excess quality tends to \(1\).

No Pell-type counterexample family was derived.

---

## 11. Transformation / amplification attempt

The identity
\[
4ab+(a-b)^2=c^2
\]
was examined as a possible way to turn one unusually good abc-triple into an even better one.

After removing powers of \(2\), it creates another primitive abc-type triple.

If the original quality is \(q\), the transformed quality behaves approximately like
\[
q'\ge\frac{2q}{q+1}.
\]

But
\[
\frac{2q}{q+1}-1
=
\frac{q-1}{q+1}.
\]

Thus, when \(q>1\), the new quality may remain above \(1\), but the gap above \(1\) becomes smaller.

Therefore, this transformation does not amplify a candidate counterexample. It weakens it.

---

## 12. Powerful-part decomposition

Each integer can be decomposed conceptually into:

- a squarefree part, represented by its radical, and
- a “powerful” or repeated-prime part, measured by
  \[
  \frac{n}{\operatorname{rad}(n)}.
  \]

A large abc quality requires the product
\[
\frac{abc}{\operatorname{rad}(abc)}
\]
to be very large.

One can prove density bounds of the rough form
\[
\#\left\{n\le X:
\frac{n}{\operatorname{rad}(n)}\ge Y
\right\}
\ll_\theta X Y^{-\theta}
\]
for \(\theta<1\).

This indicates that integers with very large repeated-prime parts are sparse.

However, abc concerns three dependent integers satisfying
\[
a+b=c.
\]

The independent density estimates do not control the correlations created by this additive relation.

The unresolved problem is therefore not only to show that powerful integers are rare, but to show that three appropriately powerful integers cannot repeatedly satisfy \(a+b=c\) with enough strength to violate abc.

No such correlation estimate was proved.

---

## 13. Auxiliary congruence / determinant attempt

A further route was to impose auxiliary congruences designed so that each prime divisor of \(abc\) contributed only once to a determinant.

The hope was to construct a determinant divisible by
\[
\operatorname{rad}(abc)
\]
rather than by higher prime powers, while simultaneously bounding its size using \(a,b,c\).

This did not produce a closed argument.

The same difficulty reappeared: either the constructed determinant vanished on a large subspace, or the available nonzero determinant had coefficients too large to imply the required \(R^{1+\varepsilon}\) bound.

No nonvanishing lemma with sufficiently small coefficients was obtained.

---

## 14. Main structural conclusion

The strongest self-contained reduction obtained was:

\[
\boxed{
\text{abc would follow from uniformly small nondegenerate solutions}
}
\]

of the arithmetic-derivative relation
\[
D_x(a)+D_x(b)=D_x(c).
\]

More explicitly, it is enough to prove that for every \(\eta>0\), one can find a solution with
\[
W_x(a,b)\ne0
\]
and
\[
H(x)\ll_\eta c^\eta.
\]

The exact obstruction is that lattice methods produce small solutions, but do not guarantee that a sufficiently small solution lies outside the degenerate subspace
\[
W_x(a,b)=0.
\]

---

## 15. Final status of the attempt

No complete proof was obtained.

No infinite counterexample family was obtained.

The proof attempt failed at the missing nondegeneracy-height bound:
\[
H(x)\ll_\eta c^\eta
\quad\text{with}\quad
W_x(a,b)\ne0.
\]

The counterexample attempts failed because:

- fixed \(S\)-unit families are finite,
- smooth-number pigeonhole counts collapse after gcd cancellation,
- polynomial identities are blocked by polynomial abc,
- Pell and recurrence families introduce too many new primes,
- known constructions produce quality tending to \(1\),
- and algebraic transformations shrink rather than amplify the quality gap.

The honest conclusion is:

\[
\boxed{
\text{The attempt did not prove or disprove the abc conjecture.}
}
\]

The most concrete output is the arithmetic-Wronskian reduction and the identification of its exact missing lemma.