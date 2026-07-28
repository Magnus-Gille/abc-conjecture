# Prime-genealogy proposal: proof and software audit

Date: 2026-07-28
Auditor: Codex (conductor)

## Scope and status

The supplied manuscript and Python CLI are treated as an unverified research
proposal. The first pass concentrated on Proposition 15, Corollary 16, and
Theorem 17.

Current verdict: **no counterexample or fatal mathematical error was found in
the local-realization chain after a Codex audit and an independent cross-model
review**. The identified proof gaps were repairable and have been made explicit
in the audited draft. The manuscript is still not publication-ready without
specialist human review, and novelty and priority remain unverified.

The supplied CLI passed its original self-test and reproduced the programmed
seed

\[
(\ell,a_0,b_0)=(3,304260006,39305)
\]

for the condition \((p,n,\varepsilon,h,\chi)=(17,1,A,2,-1)\).

The independent regression suite in `paper/test_chebyshev_abc.py` additionally
checks:

- both branches for \(\ell=3,5,7\), levels \(0,1\), and every odd prime
  \(p\leq199\), including incompatible cases;
- the predicted root counts, simplicity, and Legendre signs;
- Hensel distances at exact valuations \(h=1,2,3\);
- the homogeneous specialization used in the CRT proof;
- simultaneous realization of three conditions for \(\ell=3\);
- the separate \(\ell\geq5\) normalization path;
- rejection of incompatible data.

All eleven independent tests pass.

## Proposition 15

### Argument that survives the audit

For a projective seed \((\rho,1)\), introduce an element \(s\) with
\(s^2=-\rho\). The Cayley transform

\[
\zeta=\frac{1+s}{1-s},
\qquad
s=\frac{\zeta-1}{\zeta+1}
\]

interchanges:

- \(s\in\mathbb F_p\) with \(\zeta\in\mathbb F_p^\times\);
- \(s^p=-s\) with \(\zeta^p=\zeta^{-1}\), hence with the norm-one subgroup
  of \(\mathbb F_{p^2}^\times\).

The branch atom vanishes exactly when \(\zeta\) has order
\(\ell^{n+1}\) in branch \(A\), or \(2\ell^{n+1}\) in branch \(B\).
Inversion sends \(s\) to \(-s\), so the map from exact-order elements to
\(\rho=-s^2\) has fibers \(\{\zeta,\zeta^{-1}\}\). This gives
\(\varphi(m)/2=d_n\) roots. Since the branch polynomial has degree at most
\(d_n\), the constructed roots exhaust it and are simple.

### Repairs applied

The following gaps were present in the supplied proposal and are repaired in
the audited draft.

1. Add a polynomial-setup lemma proving that the level coordinates are
   homogeneous of degree \(\ell^n\), and that each branch multiplier has
   degree \(d_n=\ell^n(\ell-1)/2\). State explicitly that
   \(\mathcal F_{n,A}\in\mathbb Z_{(p)}[X,Y]\).
2. Replace the undefined phrase “nondegenerate root.” Prove directly that
   neither exceptional projective point is a root:

   \[
   \mathcal F_{n,\varepsilon}(0,1)=1,
   \qquad
   \mathcal F_{n,\varepsilon}(-1,1)\ne0\pmod p.
   \]

   The second value follows from the homogeneous atom at
   \((\omega,\bar\omega)=(2,0)\) and is a power of \(2\), up to the
   invertible factor \(\ell^{-1}\) in branch \(A\).
3. Define the split/nonsplit quadratic algebra explicitly, rather than saying
   “the residue algebra containing \(s\).”
4. State why the compatible sign \(\chi\) is unique: an odd
   \(\ell\)-power cannot divide both \(p-1\) and \(p+1\).
5. In the converse, explicitly derive exact order from a zero of the
   cyclotomic polynomial using \(p\nmid m\), then place the element in the
   split or norm-one group according to \(\left(\frac{-\rho}{p}\right)\).

## Corollary 16

The Hensel argument is correct for a simple root. The statement should say
“the unique \(p\)-adic lift in the residue class \(\rho\bmod p\),” since the
polynomial can have several roots in \(\mathbb Z_p\).

The Taylor estimate should be written as a congruence:

\[
f(\widehat\rho+\lambda p^h)
\equiv
\lambda p^h f'(\widehat\rho)
\pmod{p^{2h}}.
\]

Because \(f'(\widehat\rho)\) and \(\lambda\) are units and \(2h\ge h+1\),
the valuation is exactly \(h\).

## Theorem 17

### Argument that survives the audit

At each prescribed prime, choose a lifted root and impose

\[
b_0\equiv1\pmod{p^{h+1}},
\qquad
a_0\equiv\widehat\rho+p^h\pmod{p^{h+1}}.
\]

For the homogeneous branch polynomial of degree \(d_n\),

\[
\mathcal F_{n,\varepsilon}(a_0,b_0)
=
b_0^{d_n}
\mathcal F_{n,\varepsilon}(a_0/b_0,1).
\]

The imposed congruences give
\(a_0/b_0\equiv\widehat\rho+p^h\pmod{p^{h+1}}\), and the leading unit
\(b_0^{d_n}\) does not change the valuation. Corollary 16 therefore gives
the prescribed valuation.

Exact order excludes all earlier branch indices and the opposite index at
the target level. Once the eventual integer seed is admissible, Theorem 3
excludes the prime from every later multiplier.

The local moduli, \(2\), and \(\ell^2\) are pairwise coprime. The prescribed
class for \(b_0\) is a unit modulo their product \(M\). Thus every positive
\(b_0\) in that class satisfies \(\gcd(b_0,M)=1\), and CRT can additionally
impose \(a_0\equiv1\pmod{b_0}\). This forces primitivity while preserving
all local prescriptions and yields infinitely many seeds as \(b_0\) varies.

### Repairs applied

The following gaps were present in the supplied proposal and are repaired in
the audited draft.

1. Display the homogeneity identity and the congruence for \(a_0/b_0\);
   “since the polynomial is homogeneous” is too compressed.
2. Explain the earlier/opposite atom exclusion by listing their distinct
   cyclotomic orders.
3. Justify
   \[
   \left(\frac{D_K}{p}\right)
   =
   \left(\frac{-a_0b_0}{p}\right)
   \]
   by noting that \(D_K\) differs from the squarefree representative of
   \(-a_0b_0\) only by a rational square and a power of \(2\), while
   \(p\nmid2a_0b_0\).
4. Define \(M\) precisely and state why the selected \(b_0\)-class is a
   unit class.
5. Rename the result “simultaneous finite local realization” unless a
   specialist confirms that “local-global theorem” is appropriate. The
   proof is an explicit Hensel-plus-CRT construction, not a Hasse principle.

## Software findings

The supplied self-test is useful but was far too small to support the initial
reported coverage claims by itself. The submitted code contained no command
that reproduced “278 admissible seed orbits” or “110 local roots.”

The deterministic harness `paper/verify_prime_genealogy.py` now reproduces
those counts without random sampling:

- 278 admissible orbits and 11,398 exact assertions across
  \(\ell=3,5,7,11,13,17,19\);
- 12 declared split, inert, and incompatible local cases;
- 110 roots with the predicted signs and 110 lifts modulo \(p^3\);
- the programmed \(17^2\) example;
- the canonical cubic and quintic examples.

The new independent tests also harden direct API argument validation. This
materially improves reproducibility but remains finite evidence, not proof.
Release artifacts should pin the audited code and result file by hash.

## Independent cross-model review

An independent GPT-5.5 reviewer (high reasoning) audited Lemmas 1--4,
Propositions 9--15, Corollary 16, and Theorem 17 adversarially. It reran the
repository tests and separately checked 4,980 bounded local
root-count/sign cases. It found no counterexample or fatal proof error.

The reviewer identified five real but repairable omissions:

1. prove the branch-atom identities as universal polynomial identities before
   specializing to finite quadratic algebras;
2. state and prove that each programmed prime is absent from \(c_0\), not only
   from \(a_0b_0\);
3. justify that the biquadratic extension in Proposition 11 is unramified at
   the relevant prime;
4. use an integer representative of each \(p\)-adic Hensel lift in the finite
   CRT congruence;
5. state the induction hypothesis explicitly in Lemma 2.

All five points are incorporated in `paper/prime-genealogy-draft.md`. This is
independent model review, not specialist peer review. A follow-up closure
review of the patched lines confirmed all five findings closed and found no
incomplete or incorrect repair. The remaining material risk is a hidden
equivalence or local-algebra subtlety that only a specialist in Lucas atoms
and cyclotomic valuations may recognize.

## References and novelty

The two future-dated adjacent references were checked against their primary
records and are real:

- Ross, Shen, and Cai, arXiv:2512.03468 (2025);
- Kym, arXiv:2605.24909 (2026).

The 2025 Alecci--Miska--Murru--Romeo paper does state a full \(p\)-adic
valuation theory for Lucas atoms. Ratliff--Rush--Shah (2004) does construct
infinite pairwise radical-preserving homogeneous cyclotomic families.

No source located in the bounded search states the manuscript's exact
orbit-plus-realization package. That is evidence for a targeted specialist
priority review, not evidence sufficient for an unconditional novelty claim.

## Provenance

The supplied proposal named “OpenAI GPT-5.6 Pro,” while Magnus described the
source only as “ChatGPT Pro.” A subscription surface is not a model
identifier. The audited manuscript now says “ChatGPT Pro” for the originating
session and names GPT-5.5 only for the later independent review, whose model
identity was exposed by the current host.

The preferred authenticated M5 delegation path was attempted for a bounded
proof-obligation extraction, but this shell lacked the configured Keychain
item and the approved M5 loopback service was not listening. No M5 output was
used in this audit.
