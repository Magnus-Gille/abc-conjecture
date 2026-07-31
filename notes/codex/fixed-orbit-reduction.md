# Fixed-orbit repeated-prime growth: exact reduction and obstruction map

Agent: `codex`

Phase: 6

Date: 2026-07-31

Status: exact reductions and a moving-window estimate proved; full target **OPEN**

## 1. Scope and notation

Fix one admissible Chebyshev orbit of degree \(d\).  In the odd-prime
paper, \(d=\ell\) and

\[
E_j=A_jB_j,\qquad
W_n=\prod_{j<n}\frac{E_j}{\operatorname{rad}(E_j)},\qquad
c_n=c_0^{d^n}.
\]

The quadratic orbit \((1,8,9)\) has the same form with \(E_j=|d_j|\).
In both cases the positive layer integers \(E_j\) are pairwise coprime.
Put

\[
\delta_j
 :=\log\frac{E_j}{\operatorname{rad}(E_j)}
 =\sum_p (v_p(E_j)-1)_+\log p.
\]

Then

\[
\log W_n=\sum_{j<n}\delta_j.
\]

The target under investigation is

\[
\log W_n=o(\log c_n)=o(d^n).
\tag{1}
\]

Nothing below proves (1).  The point is to identify its weakest exact
per-layer form and to show precisely where the known congruence and
support information stops.

## 2. Global growth is equivalent to one-layer growth

### Proposition 1

For any nonnegative sequence \((\delta_j)\) and fixed \(d>1\),

\[
\sum_{j<n}\delta_j=o(d^n)
\quad\Longleftrightarrow\quad
\delta_j=o(d^j).
\tag{2}
\]

#### Proof

For the forward implication,

\[
0\leq\delta_j\leq\sum_{k<j+1}\delta_k=o(d^{j+1})=o(d^j).
\]

Conversely, fix \(\varepsilon>0\).  Choose \(J\) so that
\(\delta_j\leq\varepsilon d^j\) for \(j\geq J\).  Then

\[
\sum_{j<n}\delta_j
\leq
\sum_{j<J}\delta_j
+
\varepsilon\sum_{J\leq j<n}d^j
\leq
O_J(1)+\frac{\varepsilon}{d-1}d^n.
\]

Divide by \(d^n\), take the limsup, and then let \(\varepsilon\) tend to
zero. \(\square\)

Thus the per-layer estimate proposed in mailbox 0092 is not only
sufficient: it is exactly equivalent to the fixed-orbit target.

## 3. The exact missing object is the largest square divisor

For an integer \(N>0\), define

\[
\operatorname{Pow}(N)
 =
\prod_{v_p(N)\geq2}p^{v_p(N)}
\]

and let

\[
\operatorname{Sq}(N)
 =
\prod_p p^{\lfloor v_p(N)/2\rfloor},
\]

so that \(\operatorname{Sq}(N)^2\) is the largest square dividing \(N\).

### Proposition 2

For every \(N>0\),

\[
\frac12\log\operatorname{Pow}(N)
\leq
\log\frac{N}{\operatorname{rad}(N)}
\leq
\log\operatorname{Pow}(N),
\tag{3}
\]

and

\[
\log\operatorname{Sq}(N)
\leq
\log\frac{N}{\operatorname{rad}(N)}
\leq
2\log\operatorname{Sq}(N).
\tag{4}
\]

Consequently, (1) is equivalent to either of the per-layer statements

\[
\log\operatorname{Pow}(E_j)=o(d^j)
\tag{5}
\]

or

\[
\boxed{\log\operatorname{Sq}(E_j)=o(d^j).}
\tag{6}
\]

#### Proof

For every integer \(v\geq2\),

\[
\frac v2\leq v-1\leq v
\]

and

\[
\left\lfloor\frac v2\right\rfloor
\leq v-1
\leq
2\left\lfloor\frac v2\right\rfloor.
\]

Multiply each inequality by \(\log p\), sum over the primes with
\(v=v_p(N)\geq2\), and obtain (3)--(4).  Applying those inequalities
with \(N=E_j\), then using Proposition 1, gives (5)--(6). \(\square\)

There is also the exact layer-cake identity

\[
\delta_j
=
\sum_{k\geq2}
\ \sum_{p^k\mid E_j}\log p.
\tag{7}
\]

The manuscript's proposed first target,

\[
\sum_{p^2\mid E_j}\log p=o(d^j),
\tag{8}
\]

controls only the \(k=2\) summand in (7).  It does not by itself control
higher valuations.  For example, for \(N=p^e\), (8)'s analogue is only
\(\log p\), whereas the defect is \((e-1)\log p\).  Estimate (8) becomes
sufficient if it is paired with a suitable uniform bound on the excess
valuations, but no such fixed-orbit bound is presently in hand.

### 3.1 Rank localization

For odd prime degree, Proposition 12 gives

\[
\ell E_j
=
\left|
\frac{\mathcal U_{\ell^{j+1}}}
{\mathcal U_{\ell^j}}
\right|
=
\left|\Phi_{\ell^{j+1}}(\alpha,\beta)\right|.
\]

Every prime \(p\mid E_j\) has rank of apparition exactly
\(q_j=\ell^{j+1}\) in this descended Lucas sequence.  The denominator is
a \(p\)-adic unit at the birth level, so

\[
v_p(E_j)=v_p(\mathcal U_{q_j}).
\]

The quadratic orbit has the analogous signed-rank description with
\(q_j=2^{j+2}\).  Thus every term in \(\delta_j\) is a Wieferich excess
at the prime's own rank.  The Lucas law of repetition creates extra
valuation only at indices divisible by \(p\); those indices are not in
the \(d\)-smooth tower because \(p\nmid d\).  This explains
simultaneously why the prime is born in one layer and why later
cyclotomic quotients do not accumulate its valuation.

## 4. What the genealogy and congruence floor actually prove

Write \(q_j\) for the forced order modulus:

\[
q_j=
\begin{cases}
2^{j+2},&\text{for the quadratic orbit }(1,8,9),\\
\ell^{j+1},&\text{for the odd-prime degree-\(\ell\) orbit.}
\end{cases}
\]

Thus \(q_j\asymp d^j\), and every prime \(p\mid E_j\) satisfies

\[
p\equiv\pm1\pmod {q_j},
\qquad
p\geq q_j-1.
\tag{9}
\]

The following consequences are genuine but insufficient.

### 4.1 Every fixed prime cutoff eventually disappears

For fixed \(Q\), (9) implies that no prime \(p\leq Q\) can divide \(E_j\)
once \(q_j>Q+1\).  Hence

\[
\sum_{\substack{p\leq Q\\p^2\mid E_j}}
(v_p(E_j)-1)\log p=0
\]

for all sufficiently large \(j\).  Pairwise support separation gives the
same conclusion prime by prime.  This does not permit a cutoff \(Q=Q_j\)
growing with \(j\).

### 4.2 The trivial size bound remains on the full exponential scale

For odd prime degree,

\[
E_j
=
\frac{c_j^{\ell-1}}{\ell}
\left|U_{\ell-1}(x_j)\right|
<
c_j^{\ell-1}.
\]

For the quadratic orbit, \(E_j=|d_j|<c_j\).  Therefore, in either case,

\[
\log E_j=O(d^j)=O(q_j).
\tag{10}
\]

Since every prime factor is at least \(q_j-1\), (10) yields only

\[
\omega(E_j)=O\!\left(\frac{q_j}{\log q_j}\right).
\tag{11}
\]

It is compatible with (10)--(11) that a positive proportion of
\(\log E_j\) comes from squares.  Thus the order congruence and the
pairwise genealogy alone cannot produce the little-\(o\) in (6).

### 4.3 One large square is already fatal

If along an infinite subsequence there is a prime \(p_j\) with

\[
p_j^2\mid E_j
\quad\text{and}\quad
\log p_j\geq\varepsilon d^j,
\]

then

\[
\delta_j\geq\log p_j\geq\varepsilon d^j,
\]

so (1) fails.  Neither (9) nor (10) rules this out: (10) allows a squared
prime as large as \(\exp(Cd^j/2)\).  At the other extreme, roughly
\(d^j/\log d^j\) distinct polynomial-sized squared primes could also
produce a full-scale defect.  A proof has to exclude both mechanisms in
aggregate.

## 5. Prime-size splits

### 5.1 An unconditional moving window from Stewart's valuation lemma

The abstract of Stewart's largest-prime-factor theorem is not enough for
this problem, but a valuation lemma inside its proof is useful.  For the
fixed Lucas pair \((\alpha,\beta)\), put \(u=\alpha/\beta\).  Stewart
proves that, outside an effective seed-dependent finite set of primes,

\[
\operatorname{ord}_{\mathfrak p}(u^m-1)
<
p\exp\left(
-\frac{\log p}{51.9\log\log p}
\right)
\log|\alpha|\log m
\tag{12}
\]

for every unramified prime ideal \(\mathfrak p\mid p\) and \(m>1\).
This is Lemma 8 of arXiv:1008.1274; it appears as Lemma 4.3 in the
published Acta Mathematica version and is reproduced in Yu's 2013
companion paper.

### Proposition 3: Unconditional near-floor saving

Let

\[
L_j=\frac{\log q_j}{\log\log q_j}.
\]

For every fixed

\[
0<\gamma<\frac{1}{103.8},
\]

put

\[
Y_j=q_j\exp(\gamma L_j).
\tag{13}
\]

Then

\[
\boxed{
\sum_{\substack{p\leq Y_j\\p^2\mid E_j}}
(v_p(E_j)-1)\log p=o(q_j).
}
\tag{14}
\]

#### Proof

For all large \(j\), Theorem 13 and Proposition 14 of the prime-degree
paper, and their quadratic counterpart, give

\[
v_p(E_j)
\leq
\operatorname{ord}_{\mathfrak p}(u^{q_j}-1).
\tag{15}
\]

All these primes are unramified and outside the fixed exceptional set.
Fix \(\gamma<a/2\), where \(a=1/51.9\), and choose \(a'\) with

\[
2\gamma<a'<a.
\]

Because \(p\geq q_j-1\), for all sufficiently large \(j\),

\[
\exp\left(
-a\frac{\log p}{\log\log p}
\right)
\leq
\exp(-a'L_j).
\]

Equations (12) and (15) therefore imply, uniformly for \(p\leq Y_j\),

\[
(v_p(E_j)-1)_+\log p
\ll
Y_j\exp(-a'L_j)\log q_j\log Y_j.
\]

There are at most \(2(Y_j/q_j+1)\) candidate integers in the two
classes \(p\equiv\pm1\pmod {q_j}\).  Summing the last display gives

\[
\begin{aligned}
\sum_{\substack{p\leq Y_j\\p^2\mid E_j}}
(v_p(E_j)-1)\log p
&\ll
\left(\frac{Y_j}{q_j}+1\right)
Y_j\exp(-a'L_j)\log q_j\log Y_j\\
&=
q_j\exp\bigl((2\gamma-a'+o(1))L_j\bigr)\\
&=o(q_j).
\end{aligned}
\]

This proves (14). \(\square\)

The window is genuinely growing:

\[
\frac{Y_j}{q_j}
=
\exp\left(
\gamma\frac{\log q_j}{\log\log q_j}
\right)
=
q_j^{o(1)}.
\]

It is nevertheless much smaller than \(q_j^{1+\varepsilon}\) for every
fixed \(\varepsilon>0\).  Thus Proposition 3 is a nontrivial
unconditional partial result, not a solution of (6).

### 5.2 A wider conditional split

Fix \(0<\eta<1\), put

\[
Z_j=q_j^{\,2-\eta},
\]

and define

\[
B_j(Z_j)
=
\max_{\substack{p\leq Z_j\\p\mid E_j}}
(v_p(E_j)-1)_+,
\]

with the maximum interpreted as zero if the set is empty.  Counting the
two residue classes in (9) gives

\[
\sum_{\substack{p\leq Z_j\\p^2\mid E_j}}
(v_p(E_j)-1)\log p
\leq
2B_j(Z_j)
\left(\frac{Z_j}{q_j}+1\right)\log Z_j.
\tag{16}
\]

Hence a uniform estimate

\[
B_j(q_j^{2-\eta})=q_j^{o(1)}
\tag{17}
\]

would make the block in (16) equal to \(o(q_j)\).  This is a
conditional reduction, not a claimed bound.  Stewart's estimate (12)
proves (14), but it does not imply (17) over this polynomially wider
window.

After (17), the remaining estimate would be the genuinely global
large-square tail

\[
\sum_{\substack{p>q_j^{2-\eta}\\p^2\mid E_j}}
(v_p(E_j)-1)\log p=o(q_j).
\tag{18}
\]

No argument currently available to this agent proves (17) or (18).
Equation (18), or equivalently (6) without a split, is the point at which
an unproved squarefreeness, a growing-range Chebotarev assertion, or an
\(abc\)-type input is liable to be smuggled in.

## 6. Conditional and literature placement

### 6.1 The full target follows from \(abc\), circularly

Assume the \(abc\) conjecture.  For every \(\varepsilon>0\), its
application to the \(n\)-th primitive orbit triple gives

\[
c_n\ll_\varepsilon R_n^{1+\varepsilon}.
\]

Writing \(\Delta_n=\log(c_n/R_n)\), this implies

\[
\frac{\Delta_n}{\log c_n}
\leq
\frac{\varepsilon}{1+\varepsilon}+o(1).
\]

Since \(\varepsilon\) is arbitrary,

\[
\Delta_n=o(\log c_n).
\]

The exact radical identity and the archimedean estimate give

\[
\Delta_n=\log W_n+o(\log c_n),
\]

so (1) follows.  Thus the \(abc\)-conditional powerful-part results of
Ribenboim--Walsh and Yabuta are consistent with the target, but any use
of them in an attempted proof of \(abc\) would be circular.

### 6.2 What the checked unconditional literature does and does not do

- Stewart's headline theorem
  \[
  P(\Phi_m(\alpha,\beta))
  >
  m\exp\left(
  \frac{\log m}{104\log\log m}
  \right)
  \]
  is a lower bound for one large prime factor.  By itself it does not
  control the powerful part.  The useful input is instead the internal
  valuation lemma (12), which yields Proposition 3.
- Primitive-divisor theorems are weaker than the genealogy already
  available here: every prime has a unique birth layer.  They do not
  bound its birth valuation.
- Known subspace-theorem gcd estimates compare multiplicatively
  independent sequences.  The powerful part of one cyclotomic value has
  no known reformulation of that shape.
- No named conjecture equivalent to (6), and no unconditional theorem
  covering a fixed polynomial window \(p\leq q_j^{1+\varepsilon}\), was
  located in the bounded joint source search.

Mersenne squarefreeness is a useful difficulty benchmark, not a
reduction.  For prime \(r\), a square divisor \(p^2\mid2^r-1\) forces a
Wieferich congruence at \(p\), just as a square divisor of \(E_j\) forces
the cyclotomic lift in Proposition 14.  Whether all prime-index
Mersenne numbers are squarefree remains open.  Our target is weaker
than eventual squarefreeness, and neither problem is known to imply the
other.

## 7. Bounded computation on the three canonical orbits

The diagnostic

`notes/codex/fixed_orbit_probe.py`

uses exact orbit arithmetic and bounded factorization.  Stored factors
are replayed as certificates: their primality and exact product are
checked afresh.  A composite residual is labeled unresolved, never
squarefree.

| orbit | certified complete levels | result | first unresolved layer |
|---|---:|---|---:|
| quadratic \((1,8,9)\) | \(0\) through \(6\) | all squarefree | \(7\), 122 digits |
| cubic \((3,2,5)\) | \(0\) through \(3\) | all squarefree | \(4\), 113 digits |
| quintic \((5,2,7)\) | \(0\) through \(1\) | all squarefree | \(2\), 85 digits |

All certified prime factors satisfy the forced congruence (9).  Separate
modular searches with `paper/chebyshev_abc.py` found no square lift for

- the cubic seed among 78,495 eligible primes \(p\leq10^6\), through
  level 12; and
- the quintic seed among 78,495 eligible primes \(p\leq10^6\), through
  level 8.

The earlier quadratic search found no square lift for \(p\leq10^7\)
through level 50.  These are finite diagnostics only.  In particular,
the unresolved cofactors in the table may conceal repeated prime factors,
and the absence of small-prime lifts says nothing about the tail in (18).

Reproduction:

```bash
cd notes/codex
python3 -m unittest -v test_fixed_orbit_probe.py
python3 fixed_orbit_probe.py --factor-limit 100000

cd ../..
python3 paper/chebyshev_abc.py square-search \
  --ell 3 --a 3 --b 2 --prime-limit 1000000 --max-level 12
python3 paper/chebyshev_abc.py square-search \
  --ell 5 --a 5 --b 2 --prime-limit 1000000 --max-level 8
```

## 8. Current narrow research questions for the joint pass

1. Can Stewart's unconditional window (14) be enlarged to
   \(p\leq q_j^{1+\varepsilon}\), or can any published \(p\)-adic bound
   imply (17) in the wider window \(p\leq q_j^{2-\eta}\)?
2. Is (6) for a fixed nondegenerate Lucas pair already a named or
   explicitly recorded open problem, and what is its exact
   \(abc\)-conditional status?
3. Is there any fixed-seed method that controls (18), rather than an
   average over seed residue classes?  The bounded local mean from Phase
   5 controls the latter model but cannot be transferred pointwise without
   a new uniform-integrability or large-square theorem.

Until one of these questions has a positive answer, the honest conclusion
is that the papers have isolated the fixed-orbit obstruction more sharply,
but have not crossed it.
