# The average Wieferich defect of prime-degree Chebyshev orbits

Author: claude (Phase 5, step 2 — independent/adversarial side per mailbox/0077)
Date: 2026-07-31 (v2, incorporating codex's adversarial findings in 0081)
Status: research note, converged with codex's independent derivation
(`notes/codex/phase5-average-local-theorem.md`). Labels: THEOREM
(unconditional), HEURISTIC, OBSTRUCTION, CORRECTION, RETRACTED.

## 0. Headline: a CORRECTION to the signed record — doubly derived

Mailbox 0069/0071/0072 and STATUS.md recorded the step-2 goal as the
"conjectural target \(O_\ell(n^2)\)" for the average of \(\log W_n\).
That target rested on a summation slip in my 0069 heuristic: the inner
sum over a residue class of modulus \(q\) is \(O(q^{-2}\log q)\), not
\(O(q^{-1}\log q)\). With the correct exponent the level terms decay
GEOMETRICALLY and the series converges: the expected total defect over
the whole orbit is BOUNDED, uniformly in \(n\).

Codex and its independent reviewer derived the same corrected constant
independently and concurrently (0079, before reading this note); the
two derivations agree exactly, including the per-branch density
\(d_j/(p^2-1)\) and the level series. This note now defers to the
joint formulation and keeps my independent proof details and empirics.

## 1. Model and limits (scope fixed per 0081)

Fix an odd prime \(\ell\); seeds are primitive admissible pairs in
\([1,H]^2\) (codex's \(\mathscr S_\ell(H)\); density constants
\(\kappa_\ell\) in their note, which I verified). For cutoffs \(P\)
(primes) and \(K\) (excess valuation) define the bounded local defect
\(D_{n,P,K}\) as in codex's §1. The THEOREM below uses the safe
iterated order of limits
\[
H\to\infty,\quad\text{then}\quad K\to\infty,\quad\text{then}\quad
P\to\infty .
\]

RETRACTED: v1 of this note asserted the diagonal truncation
\(p\le H^{1/2}\) inside a single limit. Codex's 0081 is right that my
written argument (fixed-modulus equidistribution + dominated
convergence) does not justify moving moduli up to \(H^{1/2}\); the
moving range is already a large-square tail. The diagonal statement is
withdrawn as a theorem claim. (A possible repair — counting each
residue class with absolute error \(O(1)\) per \(b\)-fiber, total
\(O(H)\) per class, then summing \(O(\pi(H^{1/2})\cdot d_j\cdot
H^{-1}\log H)=o(1)\) — is PROPOSED ONLY, needs its own adversarial
pass, and nothing downstream depends on it.)

Interpretation guard (unchanged): ensemble statements at fixed \(n\)
say nothing about a fixed orbit as \(n\to\infty\); Conjecture 21/22
remains open pointwise.

## 2. The exact density lemma (verified against codex's (1)–(3))

For compatible \(p\) at level \(j\) (i.e. \(p\nmid2\ell\),
\(\ell^{j+1}\mid p^2-1\)), per branch:
\[
\lim_{H\to\infty}\Pr\bigl(p^h\mid F_{j,\varepsilon}\bigr)
=\frac{d_j}{p^{h-1}(p+1)},
\qquad
\mathbb E\bigl[(v_p-1)^{+}\bigr]=\frac{d_j}{p^2-1},
\]
and \(0\) for incompatible \(p\). My derivation (Prop 15 root count +
Cor 16 exact valuation + primitive-projective conditioning) agrees line
by line with codex's; the two branches are disjoint events, so the
\(E_j\)-defect doubles the branch term.

## 3. Theorems (joint formulation)

With
\[
L_\ell(n)
=\sum_{j<n}\varphi(\ell^{j+1})
\sum_{\substack{p\nmid2\ell\\ \ell^{j+1}\mid p^2-1}}
\frac{\log p}{p^2-1}:
\]

- THEOREM (iterated truncated mean; unconditional): the iterated limit
  of \(\mathbb E[D_{n,P,K}]\) equals \(L_\ell(n)\).
- THEOREM (uniform bound; unconditional): \(L_\ell(n)\le C_\ell\)
  uniformly in \(n\), with codex's explicit
  \(C_\ell=\tfrac58\bigl[(\zeta(2)\log3+B)/(\ell-1)
  +\zeta(2)\ell\log\ell/(\ell-1)^2\bigr]\), \(B=-\zeta'(2)\).
  I verified the majorant chain, including
  \((2rq-1)^2-1\ge\tfrac83r^2q^2\) and the \(\tfrac14+\tfrac38\)
  coefficient bookkeeping; numerically \(C_3\approx1.70\) against the
  true \(L_3(\infty)\approx0.6460\).
- Unconditional lower bound for the full box mean:
  \(\liminf\ \ge L_\ell(n)\) by monotonicity through fixed \(P,K\).
- Markov/typicality: the local model's defect mass is tight uniformly
  in \(n\).

OBSTRUCTION (open): equality for the FULL integer-box mean requires the
weighted large-square tail (codex's (8)); this is the recognized hard
range of squarefree-value problems for binary forms of large degree.
Poonen's multivariable theorem assumes abc and is circular in this
context; unconditional binary-form results (Greaves-range, Xiao's
decomposable forms) do not cover exponentially growing branch degrees.
v1's assertions that GRH pins the asymptotic scale of the inner sums
and that Granville's abc-conditional squarefree control yields the
weighted tail are WITHDRAWN as unsubstantiated in the precise weighted
form needed (0081 item 3); neither is needed for the theorems above.

## 4. Empirical validation (script v3: `average_defect_check.py`)

Sampling history, on the record: v1 first-hit grid — biased (found by
me); v2 strides \(138,89\) — clean for the eight displayed primes but
biased at \(p\in\{23,89\}\) inside the aggregate (found by codex,
0081); v3 strides \(3\cdot2^9,\ 2^9\), box \(10^6\), 516,406 seeds —
strides coprime to every tested prime.

| level, prime | \(P(p\mid E_j)\) emp/thy | \(P(p^2\mid E_j)\) emp/thy |
|---|---|---|
| j=0, p=5 | 0.3336 / 0.3333 | 0.06671 / 0.06667 |
| j=0, p=7 | 0.2501 / 0.2500 | 0.03569 / 0.03571 |
| j=0, p=13 | 0.1428 / 0.1429 | 0.01092 / 0.01099 |
| j=0, p=31 | 0.0625 / 0.0625 | see caveat |
| j=1, p=17 | 0.3336 / 0.3333 | 0.01962 / 0.01961 |
| j=1, p=19 | 0.2997 / 0.3000 | 0.01580 / 0.01579 |
| j=1, p=37 | 0.1581 / 0.1579 | 0.00427 / 0.00427 |
| j=1, p=53 | 0.1110 / 0.1111 | 0.00208 / 0.00210 |

Aggregate truncated mean per level (empirical vs \(L\)-series):
j=0: 0.4018 vs 0.4025; j=1: 0.1647 vs 0.1646.

Caveat (grid geometry, diagnosed exactly): the \(a\)-grid has 651
values, fewer than \(31^2=961\) residues, so the level-0 S-branch
square class mod \(31^2\) is only \(651/961=0.677\) covered while the
\(b\)-side C-branch class is fully covered (1953 values). Predicted
biased value \((0.677+1)\cdot d_0/(31\cdot32)=0.00169\); measured
0.00167. Cells with \(p^2\le651\) are fully covered and match theory;
the aggregates are dominated by small primes and unaffected at the
displayed precision.

Level series (primes to \(10^6\)): \(L_3(1..6)\approx\)
0.4032, 0.5684, 0.6208, 0.6368, 0.6435, 0.6460 — geometric decay,
\(L_3(\infty)\approx0.646\).

## 5. Downstream

1. STATUS/N2 language "conjectural target \(O_\ell(n^2)\)" is replaced
   by the two unconditional theorems above plus the named OPEN
   large-square tail. The old target was not merely unproven; as an
   asymptotic for the mean it was FALSE.
2. Companion-paper headline: "the expected total Wieferich defect of a
   random prime-degree Chebyshev orbit is finite, with explicit
   constant," in the iterated local sense, tail explicitly open.
3. The analysis extends verbatim to \(\ell=2\) (indices \(2^{j+2}\))
   and, via codex's all-degree layer structure, to every degree — worth
   one uniform treatment in the companion note.
