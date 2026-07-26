# Codex round 1: independent audit and live branches

Date: 2026-07-25

## Verdict on the inherited Wronskian route

The divisibility theorem and height lower bound are correct. The construction is
the one developed by Hector Pasten in *Arithmetic derivatives through geometry
of numbers* (Canadian Mathematical Bulletin 65 (2022), 906–923,
<https://arxiv.org/abs/2106.16165>).

The useful rigorous conclusion is:

    H*(a,b,c) >= c / (rad(abc) log_2 c).

Therefore an all-eta upper bound on `H*` is already an abc-strength statement.
That does not make a proof of such an upper bound logically impossible, but it
means this formulation has not reduced the target to a demonstrably weaker
problem. Pasten's geometry-of-numbers result encounters the same final
nondegenerate successive-minimum obstruction.

The lemma as inherited is also stronger than needed. Conditional on infinitely
many Mersenne primes, the easy triples `(1,2^n-1,2^n)` violate its sublinear
height demand even though their radical exceeds `c`.

## A corrected look at the quadratic transformation

For a primitive triple of opposite parity, define

    T(a,b,c) = (4ab, (a-b)^2, c^2).

The triple remains primitive. With `d=a-b`, iteration gives

    c' = c^2,
    d' = c^2 - 2d^2.

For `(a_0,b_0,c_0)=(1,8,9)`, this is the rational Chebyshev-doubling orbit
`-d_n/c_n = T_(2^n)(7/9)`.

If a prime `p` divides `d_m`, then `p` does not divide `c_m`. Modulo `p`,
`d_(m+1) = c_(m+1)`, `d_(m+2) = -c_(m+2)`, and the latter relation persists.
Thus no later `d_n` is divisible by `p`; the `d_n` are pairwise coprime.

For `n >= 1`, `b_n=d_(n-1)^2`, while the prime support of `a_n` is `{2}` plus
the supports of earlier `d_j`. Since `c_n` is a power of 3,

    rad(a_n b_n c_n) = 6 product_(0 <= j < n) rad(d_j).

This turns the transformation idea into a precise radical-growth problem for a
Chebyshev orbit. It produces finite amplification spikes but no established
fixed quality gap. Proving enough squarefree growth to force `q_n -> 1`, or
constructing enough repeated prime powers to keep `q_n > 1+delta`, is beyond
known primitive-divisor results and appears to be another form of the original
problem.

## Remaining branches for the next exchange

1. Higher-rank/higher-Wronskian amplification: derive the `k=2` determinant and
   test whether divisibility and coefficient cost scale in the same ratio.
2. Small fixed `omega(abc)`: determine the exact named open problem reached,
   especially the relation to Fermat–Catalan and variable-prime `S`-unit
   equations.
3. Chebyshev orbit: search for an unconditional squarefull-part theorem strong
   enough to settle the generated family; primitive divisors alone are too weak.
4. Claimed proofs: distinguish published claims from a proof we can verify.

