# Provisional joint-conclusion outline

Status: **not a conclusion and not signed**  
Purpose: prepare the final report without pre-empting Claude's pending audit.

## Proposed outcome

Outcome (c): neither a proof nor a disproof was obtained, and the two agents
cannot advance any examined line without solving an already recognized open
problem or re-proving an abc-equivalent statement.

## What was established rigorously

1. The inherited arithmetic-derivative/Wronskian calculation is sound through
   \[
   \frac{c}{\log_2 c}\le R\,H.
   \]
   Therefore every nondegenerate certificate satisfies
   \(H\ge c/(R\log_2c)\).

2. The method is not new: it is Hector Pasten's published framework
   (arXiv:2106.16165).  Pasten proves that a power-saving improvement of the
   geometry-of-numbers height bound gives abc, and that the corresponding
   Small Derivatives Conjecture is equivalent to abc.  The unproved lemma in
   `firsttryabc.md` is therefore not a bridge to abc; in the properly excluded
   formulation it is another form of the destination.

3. The literal all-triples lemma in `firsttryabc.md` is too strong.
   For a Mersenne-prime triple \((1,2^n-1,2^n)\), nondegeneracy forces
   \(H\ge n2^{n-1}\), although \(R=2(2^n-1)>c\).  This does not refute abc;
   it refutes only the over-broad auxiliary lemma, conditionally on infinitely
   many Mersenne primes.

4. The exact Reyssat computation was independently reproduced:
   \(H^*=601\), attained by \((601,-38,-79,-586)\), with
   \(W=-abc/R\).  This validates the finite calculation but supplies no
   uniform theorem.

5. Higher first-order Wronskians cannot amplify the estimate.  The quotient
   \(T/T^\circ\) has rank one, all alternating determinants of two or more
   derivative rows vanish, and multiplying ordinary Wronskians returns the
   same inequality with a geometric-mean height.

6. Bounded support closes only the smallest case.  Pasten/Mihăilescu classify
   \(\omega(abc)\le2\), and those triples are harmless.  At
   \(\omega(abc)=3\), one already encounters variable-prime equations
   \(p^\alpha+q^\beta=r^\gamma\) and variable-\(S\) unit equations.
   Fixed-\(S\) and fixed-signature finiteness do not provide the uniform
   radical bound.  Verified fixed-\(\omega\) logarithmic-form bounds remain
   exponentially weaker than abc.

7. The quadratic transformation from \((1,8,9)\) does amplify quality at
   finite iterates, correcting `firsttryabc.md`, and gives an unconditional
   infinite family with \(R_n<(2/3)c_n\).  It does not give a fixed gap.
   After a Baker--Wüstholz estimate removes the real Chebyshev factor,
   \[
   \log(c_n/R_n)=\log Q_n+O(n^2),
   \quad
   Q_n=\prod_{j<n}|d_j|/\operatorname{rad}(d_j).
   \]
   Thus a disproof from this family is equivalent to positive-power
   accumulation of Wieferich-type repeated divisibility; showing its quality
   tends to one requires the opposite sub-power bound.  Neither is known.

8. The disproof-side skeleton count predicts
   \(T^{\theta-1+o(1)}\) triples at height \(T\) whose radical is
   \(T^\theta\).  This predicts only finitely many triples above every fixed
   quality \(1+\delta\), but it relies on an unproved independence assumption
   about additive correlations of powerful parts and is evidence, not proof.
   Known construction theorems guarantee only sub-polynomial excess; they do
   not prove a fixed quality gap, nor do they necessarily prove the selected
   sequences have quality tending to one.

## Current-status seal still pending Claude's final audit

- Scholze--Stix identify the critical IUT-III Corollary 3.12 comparison as
  invalid under consistent identifications.
- Project LANA's official 17 July 2026 interim report still suspends judgment
  and identifies unresolved ambiguity in deriving Corollary 3.12 from
  Theorem 3.11.
- Joshi's claimed alternate route requires direct source-level checking.
  Claude owns that audit; its result must be incorporated cautiously as our
  audit finding, not asserted as community consensus.

## Required before finalizing

1. Claude resolves the Joshi source audit.
2. Claude corrects and co-signs the disproof-side one-sided-bound issue.
3. One final exchange produces no new viable line.
4. Draft `CONCLUSION.md`; both agents post `SIGNED 2026-07-25`.
5. Send the agreed outcome through Ratatoskr, then report completion.
