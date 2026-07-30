# Phase 5, direction 2: the exact local mean and the large-square obstruction

Status: theorem-level derivation checked independently by Codex and Kuhn;
the integer-box tail statement is deliberately left as an obstruction, not
promoted to a theorem.

## 1. The quantity being averaged

Fix an odd prime \(\ell\).  For \(H\geq1\), let

\[
\mathscr S_\ell(H)=
\left\{
 (a,b)\in[1,H]^2:
\begin{array}{l}
 \gcd(a,b)=1,\quad a\not\equiv b\pmod2,\\
 \ell\mid a,\quad \ell\nmid b,\quad
 v_\ell(S_\ell(a,b))=1
\end{array}
\right\}.
\]

The last condition is automatic for \(\ell\geq5\).  Standard local
counting and Möbius inversion give

\[
|\mathscr S_\ell(H)|\sim\kappa_\ell H^2,
\]

where

\[
\kappa_\ell=
\frac{2}{3(\ell+1)\zeta(2)}
\quad(\ell\geq5),
\qquad
\kappa_3=\frac1{9\zeta(2)}.
\]

The extra factor \(2/3\) at \(\ell=3\) is the condition
\(v_3(3b-a)=1\).

Let

\[
q_j=\ell^{j+1},
\qquad
d_j=\frac{\varphi(q_j)}2.
\]

Write \(F_{j,A}\) and \(F_{j,B}\) for the two normalized homogeneous
branch atoms.  All sums indexed by \(p\) below are over primes.  For
finite cutoffs \(P,K\), define the bounded local defect

\[
D_{n,P,K}(a,b)
=
\sum_{\substack{j<n,\ \varepsilon\in\{A,B\}\\
                 p\leq P,\ p\notin\{2,\ell\}\\
                 p\ {\rm prime}}}
\log p
\sum_{h=2}^{K+1}
\mathbf1_{p^h\mid F_{j,\varepsilon}(a,b)}.
\]

This truncates both the primes and the excess valuation.  It therefore
depends on finitely many congruence classes, so passage from boxes to the
corresponding local Haar measures is unconditional.

## 2. Exact primitive local density

Fix an odd prime \(p\ne\ell\), a level \(j\), a branch
\(\varepsilon\), and \(h\geq1\).  Proposition 15 gives \(d_j\) simple
projective roots precisely when

\[
q_j\mid p-1
\quad\hbox{or}\quad
q_j\mid p+1.
\]

All roots have \(b\) a unit.  Modulo \(p^h\), each simple root has one
Hensel lift and permits \(\varphi(p^h)\) unit choices for \(b\).  The
number of primitive pairs modulo \(p^h\) is

\[
p^{2h}-p^{2h-2}.
\]

Consequently, for either branch,

\[
\lim_{H\to\infty}
\Pr_{\mathscr S_\ell(H)}
\left(p^h\mid F_{j,\varepsilon}(a,b)\right)
=
\begin{cases}
\displaystyle
\frac{d_j}{p^{h-1}(p+1)},
&
q_j\mid p-1\ \hbox{or}\ q_j\mid p+1,\\[7pt]
0,&\text{otherwise.}
\end{cases}
\tag{1}
\]

The factor \(p+1\), rather than \(p\), is the correction from conditioning
on a primitive projective pair.  The restrictions at \(2\) and \(\ell\)
do not alter (1), by the Chinese remainder theorem.

Subtracting consecutive tails yields

\[
\Pr(v_p(F_{j,\varepsilon})=h)
=
\frac{d_j(p-1)}{p^h(p+1)}
\qquad(h\geq1)
\tag{2}
\]

for compatible \(p\).  In particular,

\[
\mathbb E\bigl[(v_p(F_{j,\varepsilon})-1)_+\bigr]
=
\frac{d_j}{p^2-1}.
\tag{3}
\]

No independence assertion is needed for this first moment.  In fact,
different levels and branches at a fixed \(p\) are mutually exclusive:
their exact cyclotomic orders differ.

## 3. The bounded local-mean theorem

From (1), for fixed \(n,P,K\),

\[
\lim_{H\to\infty}
\mathbb E_{\mathscr S_\ell(H)}D_{n,P,K}
=
\sum_{j<n}\varphi(q_j)
\sum_{\substack{p\leq P,\ p\notin\{2,\ell\}\\
                 q_j\mid p^2-1}}
\frac{(1-p^{-K})\log p}{p^2-1}.
\tag{4}
\]

Letting \(K\), then \(P\), tend to infinity gives the exact local main
term

\[
L_\ell(n)
=
\sum_{j<n}\varphi(q_j)
\sum_{\substack{p\notin\{2,\ell\}\\q_j\mid p^2-1}}
\frac{\log p}{p^2-1}.
\tag{5}
\]

It is uniformly bounded in \(n\).  Indeed, because \(p,q_j\) are odd,
every eligible prime has the form \(2rq_j+1\) or \(2rq_j-1\).  For
\(q\geq3\),

\[
\begin{aligned}
(2rq+1)^2-1&\geq4r^2q^2,\\
(2rq-1)^2-1&\geq\frac83r^2q^2,\\
\log(2rq\pm1)&\leq\log(3rq).
\end{aligned}
\]

Thus

\[
\sum_{\substack{p\ {\rm odd}\\q\mid p^2-1}}
\frac{\log p}{p^2-1}
\leq
\frac5{8q^2}
\left(
\zeta(2)\log(3q)
+
\sum_{r\geq1}\frac{\log r}{r^2}
\right).
\tag{6}
\]

Using \(\varphi(q_j)\leq q_j\) and summing the two geometric series gives
the explicit bound

\[
\boxed{
L_\ell(n)
\leq
C_\ell
:=
\frac58
\left[
\frac{\zeta(2)\log3+B}{\ell-1}
+
\frac{\zeta(2)\ell\log\ell}{(\ell-1)^2}
\right],
}
\tag{7}
\]

where \(B=\sum_{r\geq1}\log(r)/r^2=-\zeta'(2)\).  This proves

\[
L_\ell(n)=O_\ell(1),
\]

which is much stronger than the earlier \(O_\ell(n^2)\) heuristic.
The script `paper/chebyshev_research.py` evaluates (5) with a prime cutoff
and implements a slightly looser explicit upper bound for (7), replacing
\(B\) by an elementary integral-test majorant.

Equivalently, on the restricted product of primitive local seed spaces,
the nonnegative local defect has finite expectation \(L_\ell(n)\).
Markov's inequality then gives local-model tightness.  This is a statement
about the local model, not about any fixed integer orbit.

## 4. Why this is not yet the full box average

For an actual integer seed,

\[
\log W_n
=
\sum_{j<n}\sum_p
(v_p(E_j)-1)_+\log p.
\]

Equating its box mean with (5) requires the weighted large-square tail

\[
\lim_{P\to\infty}\limsup_{H\to\infty}
\mathbb E_{\mathscr S_\ell(H)}
\left[
\log W_n-D_{n,P,\infty}
\right]
=0.
\tag{8}
\]

Fixed-modulus CRT and Hensel densities do not prove (8): they say nothing
uniform about primes \(p\) growing with \(H\).  This is the familiar hard
range in squarefree-value problems for binary forms.  Poonen's general
multivariable theorem assumes \(abc\), so invoking it here would be
circular.  Unconditional binary-form theorems have degree and factor
restrictions that do not cover the exponentially growing branch degrees.

Accordingly:

- **Theorem:** the iterated truncated limit (4), the local mean (5), and
  the uniform bound (7).
- **Conjecture:** the full integer-box mean exists and equals
  \(L_\ell(n)\).
- **Weaker conjectural target:** its limsup is \(O_\ell(n^2)\).
- **Open obstruction:** the large-square tail (8).

The order of limits matters.  None of these average statements proves
Conjecture 22 for one fixed seed as \(n\to\infty\).

Finally, averaging \(W_n\) rather than \(\log W_n\) is the wrong
formulation.  From (2), the local expectation of
\(p^{(v_p-1)_+}\) diverges: after weighting by \(p^{h-1}\), every
valuation level contributes the same positive amount.  The logarithm is
essential.

## Primary sources

- G. Alecci, P. Miska, N. Murru, and G. Romeo, “On alternative
  definition of Lucas atoms and their \(p\)-adic valuations,”
  *Monatshefte für Mathematik* 207 (2025), 175–196,
  <https://arxiv.org/abs/2308.10216>.
- B. Poonen, “Squarefree values of multivariable polynomials,”
  *Duke Mathematical Journal* 118 (2003), 353–373,
  <https://arxiv.org/abs/math/0203292>.
- S. Y. Xiao, “Square-free values of decomposable forms,”
  <https://arxiv.org/abs/1612.08028>.
