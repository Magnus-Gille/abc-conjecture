# Polynomial-window defect: truncation, deep lifts, and the exact missing input

Author: Codex, Phase 7

Date: 2026-07-31

Status: working proof note for Claude cross-review

## 1. Setup

Fix either the quadratic orbit or one admissible prime-degree orbit from
the two papers.  At layer \(j\), put

\[
q=q_j,
\qquad E=E_j,
\qquad
D_j(Y)=
\sum_{\substack{p\leq Y\\p^2\mid E}}
(v_p(E)-1)\log p.
\]

For all sufficiently large \(j\), every rational prime in this sum is
outside the fixed exceptional set and satisfies

\[
p\equiv\pm1\pmod q.
\tag{1}
\]

The Phase 7 target is to prove, for at least one fixed
\(0<\varepsilon<1\),

\[
D_j(q^{1+\varepsilon})=o(q).
\tag{2}
\]

The restriction \(\varepsilon<1\) loses nothing for the first attack:
it is exactly the range in which congruence counting makes every fixed
valuation layer negligible.

## 2. Every fixed valuation layer is already harmless

For \(k\geq2\), define

\[
A_{j,k}(Y)=
\sum_{\substack{p\leq Y\\p^k\mid E}}\log p.
\tag{3}
\]

### Proposition 1 (fixed-layer polynomial window)

Fix \(1\leq\beta<2\) and put \(Y=q^\beta\).  For every integer
\(k\geq2\),

\[
A_{j,k}(Y)
\leq
2\left(\frac{Y}{q}+1\right)\log Y
=O(q^{\beta-1}\log q)
=o(q).
\tag{4}
\]

The implied constant is independent of \(k\).

#### Proof

There are at most \(2(Y/q+1)\) integers up to \(Y\) in the two residue
classes (1).  The primes counted by (3) are a subset of those integers,
and each has \(\log p\leq\log Y\).  Since \(\beta-1<1\), the final
quantity is \(o(q)\). \(\square\)

In particular, with \(\beta=1+\varepsilon\), even the adversarial
scenario in which **every** candidate prime is squared contributes only

\[
O(q^\varepsilon\log q)=o(q).
\tag{5}
\]

Thus the polynomial-window obstruction is not the number of ordinary
Lucas--Wieferich primes.  It is the failure to sum (4) uniformly over
unbounded valuation depth.

## 3. Exact truncation theorem

The layer-cake identity gives

\[
D_j(Y)=\sum_{k\geq2}A_{j,k}(Y).
\tag{6}
\]

For an integer \(K\geq1\), split it exactly as

\[
D_j(Y)=T_{j,K}(Y)+R_{j,K}(Y),
\tag{7}
\]

where

\[
T_{j,K}(Y)
=
\sum_{\substack{p\leq Y\\p^2\mid E}}
\min\{v_p(E)-1,K\}\log p
=\sum_{k=2}^{K+1}A_{j,k}(Y)
\tag{8}
\]

and

\[
R_{j,K}(Y)
=
\sum_{\substack{p\leq Y\\p^2\mid E}}
(v_p(E)-1-K)_+\log p.
\tag{9}
\]

### Theorem 2 (deep-lift equivalence)

Let \(1\leq\beta<2\), \(Y=q^\beta\), and let \(K_j\geq1\) satisfy

\[
K_j=o\!\left(\frac{q^{2-\beta}}{\log q}\right).
\tag{10}
\]

Then

\[
T_{j,K_j}(Y)=o(q),
\tag{11}
\]

and hence

\[
D_j(Y)=o(q)
\quad\Longleftrightarrow\quad
R_{j,K_j}(Y)=o(q).
\tag{12}
\]

#### Proof

Equations (4) and (8), or direct candidate counting, give

\[
T_{j,K_j}(Y)
\leq
2K_j\left(\frac{Y}{q}+1\right)\log Y
=O(K_jq^{\beta-1}\log q)=o(q).
\]

The equivalence follows from the exact nonnegative decomposition (7).
\(\square\)

For the target \(\beta=1+\varepsilon\), one convenient choice is

\[
K_j=\left\lfloor\frac{q^{1-\varepsilon}}{(\log q)^2}\right\rfloor,
\tag{13}
\]

for which \(T_{j,K_j}=O(q/\log q)\).  Therefore (2) is equivalent to
controlling only primes with birth valuation exceeding approximately
\(q^{1-\varepsilon}/(\log q)^2\).  Ordinary square lifts, cube lifts,
and indeed every fixed lift depth are all harmless.

This also corrects the non-sharp max-form sufficient condition in
mailbox 0110: if

\[
B_j(Y)=\max_{\substack{p\leq Y\\p\mid E}}(v_p(E)-1)_+,
\]

then candidate counting shows that the weakest direct max condition is

\[
B_j(q^{1+\varepsilon})
=o\!\left(\frac{q^{1-\varepsilon}}{\log q}\right),
\tag{14}
\]

not the stronger denominator \((\log q)^2\).  The latter is a useful
concrete sufficient hypothesis, but it is not sharp.

## 4. Weighted Lucas--Wieferich counting criterion

Let \(u=\alpha/\beta\) be the fixed norm-one algebraic number attached
to the orbit.  It is an \(S\)-unit for a fixed finite \(S\); all primes
below are outside \(S\).  Write \(\chi(p)=1\) in the split case and
\(\chi(p)=-1\) in the inert/norm-one case.  Define

\[
w_u(p)=
\max_{\mathfrak p\mid p}
\bigl(v_{\mathfrak p}(u^{p-\chi(p)}-1)-1\bigr)_+
\]

and the weighted count

\[
S_u(x)=
\sum_{p\leq x}w_u(p)\log p,
\tag{15}
\]

with the finitely many ramified and seed primes removed.

At a layer prime, \(q\mid p-\chi(p)\), while
\(p\nmid(p-\chi(p))/q\).  The local lifting law therefore gives

\[
v_{\mathfrak p}(u^{p-\chi(p)}-1)
=v_{\mathfrak p}(u^q-1),
\tag{16}
\]

and Phase 6 gives \(v_p(E)\leq v_{\mathfrak p}(u^q-1)\).  Consequently

\[
D_j(Y)\leq S_u(Y).
\tag{17}
\]

### Proposition 3 (power-saving criterion)

If, for some fixed \(\theta<1\),

\[
S_u(x)\ll x^\theta,
\tag{18}
\]

then (2) holds for every

\[
0<\varepsilon<\frac{1-\theta}{\theta}.
\tag{19}
\]

Indeed, (17)--(18) give

\[
D_j(q^{1+\varepsilon})
\ll q^{(1+\varepsilon)\theta}=o(q)
\]

exactly when \((1+\varepsilon)\theta<1\).

No bound of the form (18) is presently known for a fixed base.  This is
not a standard Chebotarev counting problem: (16)'s rank condition is a
residue-field/Frobenius condition, but the extra lift modulo
\(\mathfrak p^2\) is a Fermat-quotient condition whose modulus and local
field vary with \(p\).

## 5. Relation to super-Wieferich primes

Following Fellini--Murty's terminology, call \(\mathfrak p\)
super-Wieferich for the \(S\)-unit \(u\) when

\[
u^{N(\mathfrak p)-1}\equiv1\pmod{\mathfrak p^3}.
\tag{20}
\]

If \(v_p(E_j)\geq3\), Phase 6 supplies a relevant \(\mathfrak p\) with
\(v_{\mathfrak p}(u^q-1)\geq3\).  Since \(q\mid N(\mathfrak p)-1\)
and the quotient is prime to \(p\), the same lifting equality as (16)
shows that \(\mathfrak p\) satisfies (20).

### Corollary 4 (recognized conditional bridge)

If the fixed base \(u\) has only finitely many super-Wieferich prime
ideals, then for every fixed \(1\leq\beta<2\),

\[
D_j(q^\beta)=o(q).
\tag{21}
\]

#### Proof

The finitely many exceptional rational primes occur at finitely many
birth layers.  For all later layers, \(v_p(E_j)\leq2\).  Hence
\(D_j(q^\beta)=A_{j,2}(q^\beta)\), and Proposition 1 applies. \(\square\)

Fellini--Murty explicitly state that finiteness of super-Wieferich
primes is expected, and use it as a hypothesis rather than a theorem.
Their formal definition and theorems are stated for integral admissible
bases \(\alpha\in\mathcal O_K\); our ratio \(u\) is only a fixed
\(S\)-unit in general.  We use the same local terminology outside
\(S\), but do **not** claim that their theorem applies verbatim.  The
paper supports the open-status diagnosis even in the integral special
case; Corollary 4 itself is the elementary conditional implication
proved above.

Primary record checked:

- Nic Fellini and M. Ram Murty, “Wieferich primes in number fields and
  the conjectures of Ankeny--Artin--Chowla and Mordell,” *Journal of
  Number Theory* 285 (2026), 209--229,
  DOI `10.1016/j.jnt.2026.01.002`, especially Definition preceding
  Theorem 2.3 and Theorems 2.3--2.4.
- Publisher PDF retrieved from the author's Queens University page;
  SHA-256
  `104e9e6f3992e751a08f8af564857d9820e944ade1e178c3ba5ce07827faab4c`.

## 6. Why a more careful Stewart summation still stops

Stewart's Lemma 8 supplies, schematically,

\[
v_{\mathfrak p}(u^q-1)
\ll
p\exp\!\left(-a\frac{\log p}{\log\log p}\right)\log q,
\qquad a=1/51.9.
\tag{22}
\]

For \(Y=q^{1+\varepsilon}\), even summing (22) at the actual candidate
sizes instead of replacing every term by the maximum has worst-case
scale

\[
\frac{Y^2}{q}
\exp\!\left(-a\frac{\log Y}{\log\log Y}\right)
(\log q)(\log Y)
=q^{1+2\varepsilon-o(1)}.
\tag{23}
\]

The factor in (22) is only a subpower saving, whereas the candidate
population creates a fixed power \(q^{2\varepsilon}\) after the
pointwise bound is summed.  A prime-number sieve would save logarithms,
not that power.  Thus “average Stewart more carefully” does not prove
(2); a moment/counting theorem for the lift valuations themselves is
required.

## 7. Exact next lemma, and honest status

An unconditional proof of any one of the following would cross the
Phase 7 barrier:

1. a weighted power saving (18);
2. the sharp max estimate (14); or
3. more weakly, the deep-tail estimate
   \[
   R_{j,K_j}(q^{1+\varepsilon})=o(q)
   \]
   for one \(K_j\) satisfying (10).

Theorem 2 shows that item 3 is the weakest of these formulations.  It
also changes the qualitative diagnosis: the polynomial-window problem
does **not** require proving that Lucas--Wieferich primes are sparse.
It requires ruling out an aggregate of extraordinarily deep,
unbounded-order lifts.  Current fixed-base Wieferich theory does not
provide that input, and fixed-field Chebotarev or a large sieve over
primes does not automatically see it.
