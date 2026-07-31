# Lean formalization plan for the composite-atom lemma

Date: 2026-07-31

Status: planning artifact only. Lean 4 and Lake are not installed in the
current environment, and no toolchain change has been made.

## Certification target

Formalize the algebraic core of the companion's all-degree local theorem:

1. for every index `k >= 3`, the homogeneous cyclotomic specialization
   `Phi_k(r+t,r-t)`, under `r^2 = Y` and `t^2 = -X`, descends to a unique
   homogeneous polynomial `A_k in Z[X,Y]` of degree `phi(k)/2`;
2. for every prime `p` with `p ∤ 2k`, its roots over `F_p` are exactly the
   Cayley images of exact-order-`k` elements in the split or norm-one cyclic
   group, modulo inversion;
3. the roots are simple, the two splitting cases have the stated Legendre
   sign, and distinct indices have disjoint root sets;
4. a simple root has the exact valuation under a unit perturbation of its
   Hensel lift;
5. the layer factorization uses exactly
   `Lambda(d,j) = {k : k | 2*d^(j+1) and k ∤ 2*d^j}`.

The finite-field and layer statements are the natural first certificate.
The seed-density argument and analytic majorant can be formalized later;
they should not be presented as machine-checked until that second stage is
complete.

## Proposed decomposition

### Stage A: pinned environment and executable examples

- Add a repository-local Lean project with a pinned Lean 4/mathlib release.
- Record the exact toolchain file and lockfile.
- Translate the existing small composite-index examples into executable
  Lean examples, while retaining the independent Python checkers.

### Stage B: cyclotomic descent

- Define the homogeneous cyclotomic polynomial by homogenizing the
  univariate integer cyclotomic polynomial.
- Prove symmetry for indices above two.
- Express a symmetric homogeneous polynomial of even degree in `e1^2` and
  `e2`, then substitute `e1^2 = 4Y` and `e2 = X+Y`.
- Prove homogeneity and degree `phi(k)/2` without computation.

### Stage C: finite-field Cayley equivalence

- Work over `F_p` and its quadratic extension.
- Define `s = (zeta-1)/(zeta+1)` and `rho = -s^2`.
- Prove that Frobenius fixes `rho` in both the split and norm-one cases.
- Prove the inverse construction, exceptional-point exclusions, and the
  inversion fibers `{zeta,zeta^-1}`.
- Use cyclicity to obtain the exact root count and compatibility condition
  `k | p-1` or `k | p+1`.

### Stage D: simplicity, Hensel, and index separation

- Derive simplicity from separability of `x^k-1` when `p ∤ k` and the
  Cayley change of variable.
- Prove that a shared projective root would give one element two distinct
  exact orders.
- State the Hensel theorem with an explicit representative modulo
  `p^(h+1)` and prove the valuation by the first Taylor term.

### Stage E: layer identity

- Formalize `alpha = Omega^2`, `beta = barOmega^2` and the homogeneous
  cyclotomic product for `U_N`.
- Prove the quotient identity and the exact divisor-lattice set `Lambda`.
- Prove that division by `d` is a unit at every prime in the local theorem.

## Acceptance gate

The result is called formally certified only when a clean clone can run the
pinned Lake build with no admitted lemmas, `sorry`, unsafe axioms, or
generated proof files omitted from version control. The theorem statement
must match the paper's hypotheses literally; a finite enumeration theorem
is not a substitute for the universally quantified result.
