# Phase 6 fixed-orbit defect map

Authors: Codex and Claude, under the repository collaboration protocol

Date: 2026-07-31

Status: **JOINT DRAFT FOR FINAL LINE-CHECK**

The fixed-orbit asymptotic target remains open.  This note records one
new unconditional partial theorem, the exact remaining obstruction, and
the finite diagnostics.  It is a research handoff, not a proof of the
\(abc\) conjecture and not a priority claim.

## 1. Fixed-orbit target

For one admissible prime-degree Chebyshev orbit, or for the quadratic
orbit \((1,8,9)\), write

\[
W_n=\prod_{j<n}\frac{E_j}{\operatorname{rad}(E_j)},
\qquad
\delta_j=\log\frac{E_j}{\operatorname{rad}(E_j)}.
\]

The layer integers \(E_j\) are pairwise coprime and

\[
\log W_n=\sum_{j<n}\delta_j,
\qquad
\log c_n=d^n\log c_0.
\]

The exact radical identity and the archimedean estimate from the two
papers show that orbit quality tends to one exactly when

\[
\log W_n=o(d^n).
\tag{1}
\]

## 2. Exact reduction

### Theorem A: Three equivalent fixed-orbit formulations

Let

\[
\operatorname{Sq}(N)
=
\prod_p p^{\lfloor v_p(N)/2\rfloor},
\]

so that \(\operatorname{Sq}(N)^2\) is the largest square dividing
\(N\).  Then the following are equivalent:

\[
\log W_n=o(d^n),
\tag{2}
\]

\[
\delta_j=o(d^j),
\tag{3}
\]

and

\[
\log\operatorname{Sq}(E_j)=o(d^j).
\tag{4}
\]

#### Proof

Nonnegativity gives

\[
\delta_j
\leq
\sum_{k<j+1}\delta_k
=
o(d^{j+1})
=
o(d^j).
\]

This proves (2) \(\Rightarrow\) (3).  Conversely, the geometric-tail
estimate

\[
\sum_{j<n}\delta_j
\leq
O_J(1)+\varepsilon\sum_{J\leq j<n}d^j
\]

proves (3) \(\Rightarrow\) (2).

For every integer \(v\geq2\),

\[
\left\lfloor\frac v2\right\rfloor
\leq v-1
\leq
2\left\lfloor\frac v2\right\rfloor.
\]

Summing prime by prime gives

\[
\log\operatorname{Sq}(E_j)
\leq\delta_j
\leq2\log\operatorname{Sq}(E_j),
\]

which proves the remaining equivalence. \(\square\)

The exact layer-cake identity is

\[
\delta_j
=
\sum_{k\geq2}\sum_{p^k\mid E_j}\log p.
\tag{5}
\]

Therefore controlling only

\[
\sum_{p^2\mid E_j}\log p
\]

does not control higher valuations.  That previously proposed first
target needs a separate uniform valuation estimate.

## 3. Rank localization and the congruence floor

Put

\[
q_j=
\begin{cases}
2^{j+2},&\text{quadratic orbit},\\
\ell^{j+1},&\text{prime degree }d=\ell.
\end{cases}
\]

Thus \(q_j\asymp d^j\).  Every \(p\mid E_j\) satisfies

\[
p\equiv\pm1\pmod {q_j},
\tag{6}
\]

and contributes its entire rank-Wieferich excess at that one layer.  Its
rank in the descended Lucas \(U\)-sequence is exactly \(q_j\) for prime
degree and exactly \(q_j/2=2^{j+1}\) for the quadratic orbit.  In both
cases the rank divides \(q_j\), so

\[
v_p(E_j)
\leq
\operatorname{ord}_{\mathfrak p}(u^{q_j}-1).
\]

The law of repetition creates additional valuation only at indices
divisible by \(p\), which do not belong to the \(d\)-smooth tower.

Two immediate consequences are:

1. every fixed prime cutoff is eventually empty; and
2. since \(\log E_j=O(q_j)\),
   \[
   \omega(E_j)=O(q_j/\log q_j).
   \]

The second estimate is still compatible with a full-scale defect
\(\delta_j\asymp q_j\).

## 4. Unconditional moving-window theorem

Stewart's valuation lemma for the fixed Lucas pair
\((\alpha,\beta)\), with \(u=\alpha/\beta\), states that outside an
effective finite set,

\[
\operatorname{ord}_{\mathfrak p}(u^m-1)
<
p\exp\left(
-\frac{\log p}{51.9\log\log p}
\right)
\log|\alpha|\log m.
\tag{7}
\]

The hypotheses hold for both fixed-orbit settings: the relevant primes
are unramified, do not divide \(\alpha\beta\), and tend to infinity with
\(j\).

### Theorem B: First growing \(o(q_j)\) block

Let

\[
L_j=\frac{\log q_j}{\log\log q_j}
\]

and fix

\[
0<\gamma<\frac1{103.8}.
\]

Then

\[
\boxed{
\sum_{\substack{
 p\leq q_j\exp(\gamma L_j)\\
 p^2\mid E_j
}}
(v_p(E_j)-1)\log p
=o(q_j).
}
\tag{8}
\]

#### Proof

At a birth prime,

\[
v_p(E_j)
\leq
\operatorname{ord}_{\mathfrak p}(u^{q_j}-1).
\]

Choose \(a'\) with

\[
2\gamma<a'<1/51.9.
\]

Because \(p\geq q_j-1\), the exponential factor in (7) is at most
\(e^{-a'L_j}\) for all large \(j\).  Put

\[
Y_j=q_j e^{\gamma L_j}.
\]

There are at most \(2(Y_j/q_j+1)\) candidate integers in the residue
classes (6).  Hence the left side of (8) is at most

\[
\begin{aligned}
&O\left(
\left(\frac{Y_j}{q_j}+1\right)
Y_je^{-a'L_j}\log q_j\log Y_j
\right)\\
&\qquad
=
q_j\exp\bigl((2\gamma-a'+o(1))L_j\bigr)
=o(q_j).
\end{aligned}
\]

\(\square\)

This window is larger than every fixed multiple of \(q_j\), but smaller
than \(q_j^{1+\varepsilon}\) for every fixed \(\varepsilon>0\).

## 5. Exact open frontier

| Prime region | Joint status | Reason |
|---|---|---|
| \(p\leq Q\), fixed \(Q\) | eventually empty | rank congruence |
| \(p\leq q_j e^{\gamma L_j}\), \(\gamma<1/103.8\) | \(o(q_j)\) defect | Theorem B |
| \(q_j e^{\gamma L_j}<p\leq q_j^{1+\varepsilon}\) | open | Stewart's bound loses its saving after summation |
| \(p>q_j^{1+\varepsilon}\) | open | one large square or many medium squares can carry full-scale defect |
| higher valuations at any moving prime | included, not discarded | weighted by \(v_p(E_j)-1\) |

For a wider diagnostic split, fix \(0<\eta<1\), put

\[
Z_j=q_j^{2-\eta},
\]

and let

\[
B_j(Z_j)
=
\max_{\substack{p\leq Z_j\\p\mid E_j}}
(v_p(E_j)-1)_+.
\]

The residue classes give

\[
\delta_j^{\leq Z_j}
\leq
2B_j(Z_j)
\left(\frac{Z_j}{q_j}+1\right)\log Z_j.
\tag{9}
\]

Thus

\[
B_j(q_j^{2-\eta})=q_j^{o(1)}
\tag{10}
\]

would close this wider block.  No known theorem proves (10).
The remaining global estimate would be

\[
\sum_{\substack{p>q_j^{2-\eta}\\p^2\mid E_j}}
(v_p(E_j)-1)\log p=o(q_j),
\tag{11}
\]

which is also open.  Equivalently, the unsplit missing estimate is

\[
\log\operatorname{Sq}(E_j)=o(q_j).
\tag{12}
\]

## 6. Literature and conditional position

- Stewart's largest-prime-factor theorem alone does not control the
  radical.  Its internal valuation lemma (7) is the input that proves
  Theorem B.
- Primitive-divisor theory supplies less support information than the
  pairwise genealogy already gives and does not bound birth
  multiplicity.
- Known subspace-theorem gcd results concern independent sequences, not
  the powerful part of one cyclotomic value.
- No named conjecture equivalent to (12), and no unconditional theorem
  covering a fixed polynomial window, was located in the bounded joint
  search.
- The full target follows from \(abc\) directly, for every orbit.
  Ribenboim--Walsh's published recurrence result is stated for positive
  discriminant, whereas the present pair is complex-conjugate.  Yabuta
  extends the consequence “only finitely many powerful terms” to
  negative discriminant.  Neither result is needed for the direct
  implication, and every \(abc\)-conditional route is circular for the
  present program.

Prime-index Mersenne squarefreeness is an analogy, not a reduction:
a square divisor similarly forces a Wieferich lift, and the
squarefreeness question remains open.  Our subpower target is weaker,
and neither problem is known to imply the other.

## 7. Finite diagnostics

A replayable factorization probe certifies:

| orbit | completely factored levels | certified defect |
|---|---:|---:|
| quadratic \((1,8,9)\) | \(0\)–\(6\) | \(0\) |
| cubic \((3,2,5)\) | \(0\)–\(3\) | \(0\) |
| quintic \((5,2,7)\) | \(0\)–\(1\) | \(0\) |

The next layers, of 122, 113, and 85 digits, retain unresolved composite
cofactors and are not called squarefree.

Modular searches found no square lift:

- for the quadratic seed, \(p\leq10^7\) through level 50;
- for the cubic seed, 78,495 eligible \(p\leq10^6\) through level 12;
  and
- for the quintic seed, 78,495 eligible \(p\leq10^6\) through level 8.

These finite results are consistent with the local model but prove no
asymptotic statement.

## 8. United draft opinion

The fixed-orbit route has made one rigorous step:

\[
\text{fixed primes}
\quad\longrightarrow\quad
\text{a growing }q_j^{1+o(1)}\text{ window}.
\]

It has not reached any fixed polynomial window and has not controlled
the global squarefull tail.  Therefore it does not prove the
fixed-orbit conjecture and does not materially advance a proof of
\(abc\).  Its value is a sharper boundary theorem: it identifies exactly
which rank-Wieferich primes are now harmless and where a genuinely new
idea is required.

## 9. Reproduction and detailed audits

- Full Codex proof and obstruction analysis:
  `notes/codex/fixed-orbit-reduction.md`
- Codex factorization probe and tests:
  `notes/codex/fixed_orbit_probe.py`,
  `notes/codex/test_fixed_orbit_probe.py`
- Claude source and rank audit:
  `notes/claude/fixed-orbit-sources.md`,
  `notes/claude/fixed_orbit_check.py`

Primary sources used for the moving-window theorem:

- C. L. Stewart, “On divisors of Lucas and Lehmer numbers,”
  *Acta Mathematica* 211 (2013), 291–314; arXiv:1008.1274.
- K. Yu, “\(p\)-adic logarithmic forms and a problem of Erdős,”
  *Acta Mathematica* 211 (2013), 315–382.
- P. Ribenboim and G. Walsh, “The \(ABC\) conjecture and the powerful
  part of terms in binary recurring sequences,” *Journal of Number
  Theory* 74 (1999), 134–147.
- M. Yabuta, “The \(ABC\)-conjecture and the powerful numbers in Lucas
  sequences,” *The Fibonacci Quarterly* 45 (2007), 362–365.
