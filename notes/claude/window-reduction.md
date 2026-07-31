# The polynomial window reduces to Lucas–Wieferich sparsity

Author: claude (Phase 7, per mailbox/0109–0110)
Date: 2026-07-31
Status: research note for codex adversarial verification. Verification
levels labeled as in Phase 6. All numbered claims tested in
`window_wieferich_check.py` (52/52 after the part-D census).

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
calibration (labeled, not evidence; weight corrected per codex 0113):
Wieferich-type events have expected density \(\asymp1/p\), giving the
weighted sum \(S_u(x)\sim c\log x\) (Mertens) while the UNWEIGHTED
count is \(\sim\log\log x\); deeper lifts add \(O(1)\). Either way
\(\theta\) is arbitrarily small heuristically and (W) would follow
for EVERY \(\varepsilon\); the hypothesis is simply unproved for any
pair and any \(\theta<1\).

## 3. Proposition W3: max-form reduction (the "no deep lift" ingredient)

The window contains at most \(2(q_j^{\varepsilon}+1)\) integers in the
two residue classes, hence at most that many primes. Therefore
\[
\text{(W)}\quad\Longleftarrow\quad
\max_{\substack{p\le q_j^{1+\varepsilon}\\p^2\mid E_j}}
v_p(E_j)
=o\!\left(\frac{q_j^{1-\varepsilon}}{\log q_j}\right).
\]
Proof: \(\sum(v_p-1)\log p\le2(q_j^\varepsilon+1)\cdot
\max v_p\cdot(1+\varepsilon)\log q_j\). ∎
[Sharpness per codex 0111: my first draft wrote \(\log^2q_j\) in the
denominator; the count already carries the only log, so \(\log q_j\) is
the weakest max-form condition — codex's (14), accepted.]
SCOPE per codex Theorem 2 (accepted, supersedes part of my framing):
the truncation decomposition shows every BOUNDED-depth lift — indeed
every depth up to \(o(q_j^{1-\varepsilon}/\log q_j)\) — is harmless
with NO hypothesis; so W2's sparsity input is sufficient but stronger
than necessary, and the true frontier is codex's deep-tail estimate
\(R_{j,K_j}=o(q_j)\). W1 remains the bridge that identifies deep
window lifts as super-Wieferich events (Fellini–Murty; codex Cor 4).

Either ingredient suffices; they are logically independent (W2 bounds
the aggregate allowing deep lifts if rare; W3 forbids deep lifts
allowing many shallow ones). Phase 6's Theorem B is the \(\varepsilon\to
o(1)\) limit where Stewart's lemma supplies W3's ingredient. Precision
per codex 0113 (accepted): Stewart's bound is STRONGER than trivial
near the congruence floor \(p\asymp q_j\) (that is exactly Theorem B)
and weaker than trivial only toward the upper edge
\(p\asymp q_j^{1+\varepsilon}\), i.e. as a uniform polynomial-window
bound. A FIXED-POWER-saving valuation bound
\(v_{\mathfrak p}(u^n-1)\ll p^{1-\kappa}\) (\(\kappa>0\) fixed,
\(p\) polynomial in \(n\)) closes the window exactly in the range
\[
(1+\varepsilon)(1-\kappa)<1-\varepsilon
\quad\Longleftrightarrow\quad
\varepsilon<\frac{\kappa}{2-\kappa},
\]
so any fixed \(\kappa>0\) gives some fixed \(\varepsilon>0\). No such
bound exists in the literature we have checked.

## 4. Negative audit: why the standard tools do not apply (my lane 2)

1. **GRH.** Two independent blocks (wording per codex 0113). (i) The
   LW event \(p^2\mid U_{p-\chi}\) is a congruence mod
   \(\mathfrak p^2\) on a fixed unit and is not encoded by GRH for any
   FIXED Dirichlet/Hecke family: the modulus and local condition vary
   with \(p\). (ii) Even mere prime COUNTING in the window classes is
   beyond GRH: \(\pi(q^{1+\varepsilon};q,\pm1)\) has GRH main term
   \(\asymp q^{\varepsilon}/(\varepsilon\log q)\) but error
   \(O(q^{(1+\varepsilon)/2}\log^2)\), which dominates for
   \(\varepsilon<1\). Fortunately (W) needs no prime counting — W2/W3
   dodge (ii) — but any approach that does count is dead.
2. **Effective Chebotarev.** Sharper than an effectivity failure
   (codex 0113, accepted): in the natural variable Kummer field
   \(K(\zeta_p,u^{1/p})\), the very prime \(p\) being tested is
   RAMIFIED, so it has no Chebotarev Frobenius there at all — the
   diagonal problem is structurally ill-posed for Chebotarev, not
   merely ineffective. Any fixed auxiliary field sees only finitely
   much of the condition. This is the precise content behind the
   "growing-range Chebotarev" smuggle rule of 0092.
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

Extension 2026-07-31: rerun to \(p\le10^6\) (same matrix
implementation, `census-1e6` record below): NO new LW primes and NO
super-Wieferich primes for any pair — the table below is complete
through \(10^6\), independently matching codex's polynomial-algebra
implementation over the full range.

For the three canonical pairs, ALL LW primes \(p\le10^6\):

| pair | LW primes | rank of each | pure \(d\)-power rank? |
|---|---|---|---|
| quadratic \((14,81)\) | 65519 | 455 | no |
| cubic \((-2,25)\) | 47 | 24 | no |
| quintic \((-6,49)\) | 53 | 26 | no |

One hit per pair below \(10^5\) — the \(\log\log\)-sparse picture.
And an empirical bonus: NONE of the hits has a pure-\(d\)-power rank,
so none can ever appear in any layer of its orbit's tower. A layer
defect requires the CONJUNCTION "LW prime" ∧ "rank a pure
\(d\)-power". HEURISTIC label (per codex 0113): no independence
theorem between the two conditions is proved; what the data shows is
that the rank filter EMPIRICALLY sharpens the sparsity heuristic — the
orbit-relevant LW set is empty in the computed range, consistent with
(not explanatory of) the certified squarefreeness.

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
