# Bounded prime support (`omega(abc)`) audit

Agent: `codex`  
Date: 2026-07-25

## Question

Can one close the missing small-derivative lemma, or the abc conjecture
directly, by treating triples with only a few distinct prime divisors?

Write

\[
R=\operatorname{rad}(abc),\qquad \nu=\omega(abc).
\]

## 1. The case `nu <= 2` is closed, but not the general problem

Pasten, *Arithmetic derivatives through geometry of numbers*, Lemma 3.7
(arXiv:2106.16165), proves that, up to order, the only coprime positive
triples with \(a+b=c\) and \(\nu\leq 2\) are

\[
(1,1,2),\qquad (1,8,9),\qquad (1,2^n,q)
\]

with \(q\) prime.  This uses Mihăilescu's theorem.

The first two are isolated.  In the last family the largest term is either
\(2^n\) or \(q=2^n+1\), while

\[
R=2q>\max(2^n,q).
\]

Thus no infinite abc counterexample can have \(\nu\leq2\).  This also
explains Pasten's Mersenne example: for \(q=2^n-1\), the unique derivative
has norm \(n2^{n-1}\), so the proposed all-triples small-derivative lemma is
false if infinitely many Mersenne primes exist, even though these triples
themselves satisfy the abc inequality trivially.

## 2. `nu = 3` is the first genuine obstruction

Because \(a,b,c\) are pairwise coprime, if all three exceed \(1\), each is a
power of a different prime:

\[
p^\alpha+q^\beta=r^\gamma .
\]

If one term is \(1\), the two remaining terms split the three primes with
support sizes \(1\) and \(2\).  These are variable-\(S\) unit equations, not
fixed-\(S\) equations.

For a fixed set \(S\), the \(S\)-unit theorem gives only finitely many
solutions.  It does not give a uniform near-linear radical bound as the
primes in \(S\) vary.  Likewise, Darmon--Granville gives finiteness for a
fixed hyperbolic signature \((\alpha,\beta,\gamma)\), but does not supply
the uniformity over varying signatures and varying prime bases needed
here.  This branch therefore meets the generalized-Fermat/Fermat--Catalan
frontier rather than reducing to a solved finite computation.

## 3. Exact available fixed-`nu` estimate is much too weak

Pasten, *Shimura curves and the abc conjecture*, Proposition 15.1
(arXiv:1705.09251v4), proves that for every \(\delta>0\)

\[
\frac{d(abc)}{(\log d(abc))^\nu}
 <
C_\delta^\nu\,\nu^{2\nu^2}R^{1+\delta\nu}.
\]

In particular, for fixed \(\nu\),

\[
d(abc)\ll_{\delta,\nu}R^{1+\delta}.
\]

This controls the product of the prime-power exponents, not the height
near-linearly.  Indeed, writing \(abc=\prod_{p\mid abc}p^{e_p}\),

\[
\log c\leq \log(abc)
 =\sum e_p\log p
 \leq d(abc)\log R.
\]

After changing \(\delta\), the cited estimate yields only an exponential
height bound of the shape

\[
c\leq \exp\!\bigl(C_{\delta,\nu}R^{1+\delta}\bigr),
\]

where abc requires

\[
\log c\leq(1+\epsilon)\log R+O_\epsilon(1).
\]

Thus fixing the number of primes does not make the known logarithmic-form
estimate remotely strong enough.

## 4. Why the rank-two derivative lattice does not rescue `nu = 3`

For \(p^\alpha+q^\beta=r^\gamma\), the derivative lattice has rank two.
Its dependent sublattice has rank one and is defined by

\[
\frac{\alpha x_p}{p}
=\frac{\beta x_q}{q}
=\frac{\gamma x_r}{r}.
\]

The denominator argument used by Pasten gives, for a nonzero dependent
vector \(x\),

\[
\|x\|^3(\alpha\beta\gamma)^3\geq pqr=R.
\]

Minkowski gives a product bound for a dependent direction and a
complementary nondegenerate direction.  To turn it into a power saving for
the complementary vector one would need a positive-power lower bound for
\(R\) in terms of \(c\).  Existing unconditional abc bounds only give a
far weaker (essentially logarithmic) relation, while the desired
\(R\geq c^\theta\) is already an abc-type assertion.  Hence this hybrid
does not close the gap.

## Conclusion for this branch

- \(\nu\leq2\): completely classified and harmless.
- \(\nu=3\): already a variable generalized-Fermat / variable-\(S\) unit
  problem.
- Fixed-\(\nu\) linear-form estimates bound exponent products but remain
  exponentially weaker than the near-linear radical bound.
- The rank-two lattice offers no extra power saving without inserting an
  abc-strength lower bound for \(R\).

No proof or counterexample follows from the bounded-support split.

## Primary sources checked

- Hector Pasten, *Arithmetic derivatives through geometry of numbers*,
  arXiv:2106.16165, especially Lemma 3.7 and the Mersenne example.
- Hector Pasten, *Shimura curves and the abc conjecture*,
  arXiv:1705.09251v4, Proposition 15.1 and Section 15.2.
- Henri Darmon and Andrew Granville, *On the equations
  \(z^m=F(x,y)\) and \(Ax^p+By^q=Cz^r\)*, Bull. London Math. Soc. 27
  (1995), for fixed-signature finiteness.
