# The polynomial window reduces to Lucas–Wieferich sparsity

Author: claude (Phase 7, per mailbox/0109–0110)
Date: 2026-07-31
Status: research note for codex adversarial verification. Verification
levels labeled as in Phase 6. All numbered claims tested in
`window_wieferich_check.py` (46/46).

Target: fixed admissible orbit, fixed \(\varepsilon>0\),
\[
\sum_{\substack{p\le q_j^{1+\varepsilon}\\ p^2\mid E_j}}
(v_p(E_j)-1)\log p=o(q_j).
\tag{W}
\]

## 1. Proposition W1: window-squared primes are Lucas–Wieferich

Let \(p\) be a layer-\(j\) prime of the orbit with \(p^2\mid E_j\),
\(p\nmid2\,\alpha\beta\,\Delta\), \(\mathfrak p\) above \(p\) in
\(K=\mathbb Q(\sqrt\Delta)\), \(\chi=\bigl(\tfrac\Delta p\bigr)\), and
write \(p-\chi=rm\) where \(m\) is the descended rank of apparition
(\(m=q_j\) for prime degree, both branches; \(m=q_j/2\) for the
quadratic orbit). Then \(p\nmid r\), and
\[
v_{\mathfrak p}\bigl(u^{\,p-\chi}-1\bigr)
=v_{\mathfrak p}\bigl(u^{\,m}-1\bigr)
=v_p(E_j)\ \ge2 .
\]
In particular \(p\) is a Lucas–Wieferich prime of the fixed pair:
\(p^2\mid U_{p-\chi}\).

Proof. Rank \(m\mid p-\chi\) (Theorem 13 and the quadratic
counterpart); \(r=(p-\chi)/m<p\) since \(m\ge q_j/2>\!\!\sqrt p\)-scale
in every window \(p\le q_j^{1+\varepsilon}\) with \(\varepsilon<1\)
(indeed \(r\le(p+1)/m\le2q_j^{\varepsilon}+O(1)\)), so \(p\nmid r\).
Put \(x=u^{m}\); then \(x\equiv1\ (\mathfrak p)\), and lifting the
exponent in the unramified local field at odd \(p\) gives
\(v_{\mathfrak p}(x^{\,r}-1)=v_{\mathfrak p}(x-1)+v_{\mathfrak p}(r)
=v_{\mathfrak p}(x-1)\).
Finally \(v_{\mathfrak p}(u^{m}-1)=v_p(E_j)\): for prime degree this
is Proposition 14 (denominator a unit at exact rank); for the
quadratic orbit \(v_{\mathfrak p}(u^{q_j}-1)
=v_{\mathfrak p}(u^{q_j/2}-1)\) since \(u^{q_j/2}+1\equiv2\) is a
unit. Since \(\beta\) and \(\alpha-\beta\) are \(\mathfrak p\)-units,
\(v_{\mathfrak p}(u^{n}-1)=v_p(U_n)\) for all \(n\), so the condition
is the integer statement \(p^2\mid U_{p-\chi}\). ∎

Verified (script part A) on primes we PROGRAMMED to be squared:
the Q17 quadratic seeds (\(v_7(U_8)=2=v_7(E_1)\), three seeds) and the
Remark 18 cubic seed (\(v_{17}(U_{18})=2=v_{17}(E_1)\)); LTE stability
(part B) on six pair/prime combinations.

## 2. Corollary W2: sparsity reduction (the "distribution ingredient")

Define the weighted Lucas–Wieferich counting function of the fixed
pair,
\[
S_u(x)=\sum_{\substack{p\le x\ \text{unramified},\ p\nmid2\alpha\beta\\
p^2\mid U_{p-\chi(p)}}}
\bigl(v_p(U_{p-\chi})-1\bigr)\log p .
\]
If \(S_u(x)\ll x^{\theta}\) for SOME \(\theta<1\) (any power saving),
then (W) holds for every
\(\varepsilon<(1-\theta)/\theta\).

Proof. By W1 the window sum is at most \(S_u(q_j^{1+\varepsilon})\ll
q_j^{\theta(1+\varepsilon)}=o(q_j)\) when \(\theta(1+\varepsilon)<1\). ∎

This formalizes Magnus's hypothesized ingredient exactly. HEURISTIC
calibration (labeled, not evidence): Wieferich-type events have
expected density \(\asymp1/p\), giving
\(S_u(x)\asymp(\log x)(\log\log x)\), i.e. \(\theta\) arbitrarily
small and (W) for EVERY \(\varepsilon\) — the hypothesis has enormous
heuristic room; it is simply unproved for any pair and any
\(\theta<1\).

## 3. Proposition W3: max-form reduction (the "no deep lift" ingredient)

The window contains at most \(2(q_j^{\varepsilon}+1)\) integers in the
two residue classes, hence at most that many primes. Therefore
\[
\text{(W)}\quad\Longleftarrow\quad
\max_{\substack{p\le q_j^{1+\varepsilon}\\p^2\mid E_j}}
v_p(E_j)
=o\!\left(\frac{q_j^{1-\varepsilon}}{\log^2q_j}\right).
\]
Proof: \(\sum(v_p-1)\log p\le2(q_j^\varepsilon+1)\cdot
\max v_p\cdot(1+\varepsilon)\log q_j\). ∎

Either ingredient suffices; they are logically independent (W2 bounds
the aggregate allowing deep lifts if rare; W3 forbids deep lifts
allowing many shallow ones). Phase 6's Theorem B is the \(\varepsilon\to
o(1)\) limit where Stewart's lemma supplies W3's ingredient; for fixed
\(\varepsilon>0\) Stewart is weaker than the trivial bound
(\(p^{1-o(1)}>q_j/\log q_j\) in the window), so a FIXED-POWER-saving
valuation bound \(v_{\mathfrak p}(u^n-1)\ll p^{1-\kappa}\)
(\(\kappa>0\) fixed, \(p\) polynomial in \(n\)) would equally suffice.
No such bound exists in the literature we have checked.

## 4. Negative audit: why the standard tools do not apply (my lane 2)

1. **GRH.** Two independent blocks. (i) The LW event
   \(p^2\mid U_{p-\chi}\) is a congruence mod \(\mathfrak p^2\) on a
   fixed unit, not an L-function event; no Dirichlet/Hecke L-zero
   statement encodes it. (ii) Even mere prime COUNTING in the window
   classes is beyond GRH: \(\pi(q^{1+\varepsilon};q,\pm1)\) has GRH
   main term \(\asymp q^{\varepsilon}/(\varepsilon\log q)\) but error
   \(O(q^{(1+\varepsilon)/2}\log^2)\), which dominates for
   \(\varepsilon<1\). Fortunately (W) needs no prime counting — W2/W3
   dodge (ii) — but any approach that does count is dead.
2. **Effective Chebotarev.** The natural criterion places LW-ness of
   \(p\) as a Frobenius/splitting condition in a Kummer-type extension
   \(K(\zeta_p,u^{1/p})\)-scale whose degree and discriminant GROW
   with \(p\): every Chebotarev application is per-prime, and all
   effective forms (unconditional Lagarias–Odlyzko, or GRH versions
   with \(\sqrt x\log(\mathrm{disc})\) errors, disc \(\approx p^{p}\))
   are vacuous. This is precisely the "growing-range Chebotarev"
   smuggle your 0092 rule forbids; it is structurally, not
   technically, blocked.
3. **Large sieve.** Requires a family to average over. Here the pair
   \(u\) is fixed and the LW condition involves a different modulus
   \(p^2\) per prime with no dual family. The Fermat-quotient
   literature (Bourgain–Ford–Konyagin–Shparlinski, "On the
   divisibility of Fermat quotients" — POINTER, record verification
   assigned to the joint pass) averages over the BASE \(a\), not over
   primes for fixed base; transposed to our setting it would average
   over SEEDS — and the seed-averaged statement is already controlled
   by Phase 5's Theorem 20 for every fixed \(j\) (the whole window is
   finitely many primes once \(j\) is fixed). The wall is pointwise
   only, consistent with the ensemble-vs-pointwise contrast in the
   Phase 6 map.

## 5. Empirical Lucas–Wieferich census (script part C)

For the three canonical pairs, ALL LW primes \(p\le10^5\):

| pair | LW primes | rank of each | pure \(d\)-power rank? |
|---|---|---|---|
| quadratic \((14,81)\) | 65519 | 455 | no |
| cubic \((-2,25)\) | 47 | 24 | no |
| quintic \((-6,49)\) | 53 | 26 | no |

One hit per pair below \(10^5\) — the \(\log\log\)-sparse picture. And
a structural bonus: NONE of the hits has a pure-\(d\)-power rank, so
none can ever appear in any layer of its orbit's tower. A layer defect
requires the CONJUNCTION "LW prime" ∧ "rank a pure \(d\)-power" — two
independently rare conditions — which structurally explains the
certified squarefreeness of every resolved layer and sharpens the
heuristic in §2: the orbit-relevant LW count is a sparse subset of an
already sparse set.

## 6. Summary for the joint map

- (W) ⟸ ANY power-saving weighted LW sparsity bound (W2), and
  independently ⟸ any fixed-power valuation saving (W3). These are
  the two named sufficient ingredients; both are open; the heuristic
  and the census point the same way.
- GRH, effective Chebotarev, and the large sieve are individually
  blocked for structural reasons stated above; no smuggling route
  survives.
- The empirical census (extendable; \(10^6\) is cheap) is a new
  diagnostic directly measuring W2's hypothesis, and the
  rank-compatibility filter shows the orbit-relevant subset is
  emptier still.
