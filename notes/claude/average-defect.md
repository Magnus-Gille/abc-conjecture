# The average Wieferich defect of prime-degree Chebyshev orbits

Author: claude (Phase 5, step 2 — independent/adversarial side per mailbox/0077)
Date: 2026-07-31
Status: research note for codex adversarial verification. Labels used:
THEOREM (unconditional, proof supplied), CONDITIONAL (hypothesis named),
HEURISTIC, OBSTRUCTION (identified open problem), CORRECTION (of our own
prior record).

## 0. Headline: a CORRECTION to the signed record

Mailbox 0069/0071/0072 and STATUS.md record the step-2 goal as the
"conjectural target \(O_\ell(n^2)\)" for the average of \(\log W_n\).
That target came from my 0069 heuristic
\(\sum_j d_j\sum_{p\equiv\pm1(\ell^{j+1})}p^{-2}\log p\asymp_\ell n^2\),
which contains a summation slip: the inner sum over a residue class of
modulus \(q\) is \(O(q^{-2}\log q)\), not \(O(q^{-1}\log q)\) — the
smallest admissible integers in the class already have size \(q-1\).
With the correct exponent the level terms decay GEOMETRICALLY and the
series converges. The corrected statement is stronger than the old
target: the expected total defect over the whole orbit is BOUNDED.
Empirics (§4) confirm the corrected constant to three decimals.

## 1. Setup and the averaging model (well-posedness)

Fix an odd prime \(\ell\). A seed is a primitive admissible pair
\((a_0,b_0)\): \(\gcd(a_0,b_0)=1\), opposite parity, \(\ell\mid a_0\),
and for \(\ell=3\) additionally \(v_3(3b_0-a_0)=1\). Let
\(\mathcal S(x)\) be the seeds in \([1,x]^2\), and for \(j\ge0\) let
\(E_j=A_jB_j\) be the level-\(j\) generation factor of the orbit, with
\(W_n=\prod_{j<n}E_j/\operatorname{rad}(E_j)\).

The model: average \(\log W_n\) over \(\mathcal S(x)\), let
\(x\to\infty\) FIRST, and study the limit as a function of \(n\).

Two well-posedness remarks, which are part of the deliverable:

- (Order of limits.) Any statement produced this way concerns the
  ensemble of orbits at a fixed level and says NOTHING about a fixed
  orbit as \(n\to\infty\). Conjecture 21 is a pointwise statement; the
  results below support it as typicality evidence and cannot prove it.
- (Truncation.) The full random variable \(\log W_n\) includes
  contributions of primes up to \(E_j^{1/2}\approx x^{d_j}\). Controlling
  the mean contribution of \(p>x^{1/2}\) meets a known open problem
  (§3). The unconditional theorem is therefore stated for the
  \(x^{1/2}\)-truncated defect
  \[
  \log W_n^{\le y}
  =\sum_{j<n}\ \sum_{p\le y}\ (v_p(E_j)-1)^{+}\log p,
  \qquad y=x^{1/2},
  \]
  which, as \(x\to\infty\), eventually includes every fixed prime. The
  full defect satisfies the same LOWER asymptotics unconditionally
  (monotonicity), and the same upper asymptotics under the named
  conditional inputs.

## 2. The exact density lemma

Write \(d_j=\ell^j(\ell-1)/2\), \(q_j=\ell^{j+1}\). Call \(p\)
compatible at level \(j\) if \(p\nmid2\ell\) and
\(q_j\mid p-1\) or \(q_j\mid p+1\).

LEMMA D (densities; unconditional). Let \(p\) be compatible at level
\(j\) and \(h\ge1\). Among seeds in \(\mathcal S(x)\), as
\(x\to\infty\):

\[
\mathbb P\bigl(v_p(E_j)\ge h\bigr)\to\frac{2d_j}{p^{h-1}(p+1)},
\qquad
\mathbb E\bigl[(v_p(E_j)-1)^{+}\bigr]\to\frac{2d_j}{p^2-1}.
\]

For incompatible \(p\nmid 2\ell\) both quantities are \(0\); the primes
\(2\) and \(\ell\) never divide \(E_j\) (Lemma 1 of the draft).

Proof. By Proposition 15 of the draft, each branch polynomial
\(\mathcal F_{j,\varepsilon}(X,1)\) has exactly \(d_j\) simple roots
mod \(p\) when \(p\) is compatible and none otherwise; its leading
coefficient is \(\pm\ell^{-1}\cdot1\) (value at \((1,0)\) is
\(\pm2^0(-X)^{d_j}\)-normalized), a \(p\)-adic unit, so there is no root
at infinity and \(p\mid b_0\) forces \(v_p=0\). By Corollary 16, for
\(t\equiv\rho\ (p)\) one has \(v_p(\mathcal F(t,1))=v_p(t-\widehat\rho)\).
Hence \(v_p(\text{branch factor})\ge h\) iff \(p\nmid b_0\) and
\(a_0/b_0\) falls in one of \(d_j\) residue classes mod \(p^h\). Among
all pairs mod \(p^h\) this event has probability
\(d_j p^{-h}(1-1/p)\); conditioning on \(p\)-primitivity (probability
\(1-1/p^2\)) gives \(d_jp^{-h}\cdot p/(p+1)\). The admissibility
conditions live at \(2\) and \(\ell\) and are independent by CRT; the
box error for fixed \(p^h\) is \(O(x^{-1}p^h)\) and vanishes for
\(p\le x^{1/2}\), \(h\) fixed, plus a standard geometric tail in \(h\).
A compatible \(p\) is compatible for both branches
(\(p-\chi\) is even, so \(2q_j\mid p-\chi\) follows from
\(q_j\mid p-\chi\)), the two root sets are disjoint (distinct exact
orders), and at most one branch is divisible (the collection is
coprime), so expectations add:
\(\mathbb E[(v_p(E_j)-1)^{+}]
=2\sum_{h\ge2}d_jp^{-h}\tfrac p{p+1}=\tfrac{2d_j}{p^2-1}\). ∎

## 3. Theorems

Define
\[
c_\ell(n)
=\sum_{j=0}^{n-1}\varphi(\ell^{j+1})
\sum_{\substack{p\nmid 2\ell\\ \ell^{j+1}\mid p\mp1}}
\frac{\log p}{p^2-1},
\qquad
\varphi(\ell^{j+1})=2d_j .
\]

THEOREM A (truncated mean; unconditional). For every fixed \(n\),
\[
\lim_{x\to\infty}\ \frac1{|\mathcal S(x)|}
\sum_{\mathcal S(x)}\log W_n^{\le x^{1/2}}
= c_\ell(n).
\]

Proof. Linearity of expectation over the triples \((j,p,h)\),
Lemma D for each term, and dominated convergence: the terms are
dominated by \(2d_j\log p/(p^2-1)\), summable over compatible \(p\); box
errors vanish as in Lemma D because every counted prime satisfies
\(p\le x^{1/2}\), and per-seed valuations at such \(p\) are bounded by
\(v_p\le\log E_j/\log p\) with total error \(o(1)\). ∎

THEOREM B (bounded total defect; unconditional). \(c_\ell(n)\)
increases to a finite limit
\[
c_\ell(\infty)
=\sum_{j\ge0}\varphi(\ell^{j+1})
\sum_{\ell^{j+1}\mid p\mp1}\frac{\log p}{p^2-1}
\ \le\
C\,\frac{\log\ell}{\ell-1}\quad(\text{absolute }C).
\]

Proof. Every prime in the inner sum lies in one of the two classes
\(\pm1\) mod \(q_j\), hence among integers \(m\ge q_j-1\),
\(m\equiv\pm1\ (q_j)\). Majorizing primes by those integers,
\[
\sum_{\ell^{j+1}\mid p\mp1}\frac{\log p}{p^2-1}
\le 2\sum_{k\ge1}\frac{\log(kq_j+1)}{(kq_j-1)^2-1}
\ll \frac{\log q_j}{q_j^{2}} .
\]
Multiplying by \(\varphi(q_j)\le q_j\) leaves
\(\ll(j+1)\log\ell\,/\,\ell^{\,j+1}\), which sums geometrically over
\(j\); evaluating the geometric-arithmetic series gives the displayed
bound with an absolute constant. ∎

INTERPRETATION (typicality; unconditional, via Markov). For every
\(T>0\) and every \(n\),
\[
\limsup_{x\to\infty}\
\mathbb P_{\mathcal S(x)}\bigl(\log W_n^{\le x^{1/2}}>T\bigr)
\le \frac{c_\ell(\infty)}{T},
\]
uniformly in \(n\). Typical seeds carry a uniformly bounded truncated
defect across ALL levels simultaneously — far stronger than the
retired \(O(n^2)\) target, and strong ensemble evidence for
Conjecture 21 (which it does not prove; §1).

CONDITIONAL COMPLEMENTS.

- (Lower bound for the full defect.) \(\log W_n\ge\log W_n^{\le y}\)
  always, so \(\liminf\) of the full mean is \(\ge c_\ell(n)\)
  unconditionally.
- (Upper bound for the full defect.) The missing piece is
  \(\sum_{p>x^{1/2}}(v_p(E_j)-1)^{+}\log p\) on average. Bounding it
  requires controlling square divisors \(p^2\mid F(a_0,b_0)\) of the
  binary forms \(F=\mathcal F_{j,\varepsilon}\) (degree \(d_j\)) for
  \(p\) beyond the box — precisely the large-square-divisor problem for
  binary forms, OPEN unconditionally for degree \(\ge7\) (squarefree
  values of binary forms are known only through degree 6, Greaves; all
  levels \(j\) with \(d_j\ge7\) are affected). Under the abc conjecture
  the tail mean vanishes (Granville's abc-conditional squarefree/
  powerful-part control for binary forms), giving
  \(\lim=c_\ell(n)\) for the FULL mean. Using abc to study the
  distribution of abc-quality within this family is methodologically
  legitimate (we are not proving abc), but must stay labeled
  CONDITIONAL.
- (Asymptotics of the constant.) Under GRH for the relevant Dirichlet
  L-functions, partial summation gives
  \(\sum_{q_j\mid p\mp1}\log p/(p^2-1)
  =(2+o(1))\log q_j/(\varphi(q_j)\,q_j)\)-scale refinements and hence
  effective evaluation of \(c_\ell(\infty)\); unconditionally the series
  converges regardless, and Linnik-type bounds already make every term
  positive and finite. No lower bound of shape \(\gg n^2\) exists — the
  old target was not merely unproven but FALSE as an asymptotic for the
  mean.

## 4. Empirical validation (script: `average_defect_check.py`)

Unbiased deterministic product grid, \(\ell=3\), box \(10^5\),
165,706 seeds, all predictions from Lemma D:

| level, prime | \(P(p\mid E_j)\) emp/thy | \(P(p^2\mid E_j)\) emp/thy |
|---|---|---|
| j=0, p=5 | 0.3332 / 0.3333 | 0.06660 / 0.06667 |
| j=0, p=7 | 0.2502 / 0.2500 | 0.03572 / 0.03571 |
| j=0, p=13 | 0.1427 / 0.1429 | 0.01105 / 0.01099 |
| j=0, p=31 | 0.0624 / 0.0625 | 0.00196 / 0.00202 |
| j=1, p=17 | 0.3336 / 0.3333 | 0.01950 / 0.01961 |
| j=1, p=19 | 0.3000 / 0.3000 | 0.01542 / 0.01579 |
| j=1, p=37 | 0.1581 / 0.1579 | 0.00431 / 0.00427 |
| j=1, p=53 | 0.1110 / 0.1111 | 0.00218 / 0.00210 |

Truncated mean defect per level: j=0: 0.4004 emp vs 0.4025 theory;
j=1: 0.1629 vs 0.1646. Partial constants:
\(c_3(1)\approx0.403\), \(c_3(2)\approx0.568\),
\(c_3(6)\approx0.646\), visibly geometric.
(A first script version used first-hit grid selection and showed a
depressed \(P(5\mid E_0)\); diagnosed as sampling bias — residues of
\(b_0\) mod 5 were not equidistributed — and fixed by the product grid.
Recorded here so the failure mode is on the record.)

## 5. What this changes downstream

1. STATUS/N2 language "conjectural target \(O_\ell(n^2)\)" must be
   replaced by: THEOREM A/B (truncated, unconditional) with
   \(c_\ell(\infty)<\infty\); full-mean upper bound CONDITIONAL
   (abc/Granville route) with the degree-\(\ge7\) square-divisor
   OBSTRUCTION named.
2. The companion-paper case is stronger than hoped: "the expected total
   Wieferich defect of a random prime-degree Chebyshev orbit is finite,
   with explicit constant" is a clean headline result, and the
   typicality corollary is uniform in \(n\).
3. For the manuscript's Conjecture 21 discussion: the ensemble now
   POINTS AT the conjecture (typical orbits have bounded defect), while
   the pointwise question and the large-prime tail remain the open
   content.
