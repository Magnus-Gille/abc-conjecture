# Source audit: two tempting but insufficient Wieferich routes

Date: 2026-07-31

This note records why two sources that initially look close to the Phase 7
polynomial-window target do not prove it.

## 1. Sanna's rank-of-appearance theorem is outside the diagonal range

Carlo Sanna, *On the divisibility of the rank of appearance of a Lucas
sequence*, arXiv:2008.12506, proves an asymptotic for primes \(p\le x\) for
which a prescribed admissible odd integer \(d\) divides the Lucas rank of appearance
\(\rho_U(p)\).  The uniform statement used in the proof requires

\[
x\ge \exp\!\bigl(B e^{8\omega(d)}d^8\bigr).
\]

Our polynomial window has \(d=m_j\asymp q_j\) and
\(x=q_j^{1+\varepsilon}\).  It is therefore far outside this range.
Moreover, divisibility of the rank is a mod-\(p\) condition; the theorem does
not count the mod-\(p^2\) Lucas--Wieferich lift or its valuation depth.  It is
useful background for the rank filter, but gives no Phase 7 estimate.

## 2. Carella's claimed fixed-base theorems fail at the characteristic function

N. A. Carella, *Results for Wieferich Primes*, arXiv:1712.08166v2, claims
both an asymptotic for fixed-base Wieferich primes and finiteness of primes
with

\[
p^3\mid v^{p-1}-1.
\]

If valid, the latter would settle the deep-lift obstruction in the rational
fixed-base case.  It is not usable: the displayed proof contains elementary
fatal errors.

1. Lemmas 4.1--4.3 use additive-character orthogonality with denominator
   \(\varphi(p^k)\) to detect equality in \(\mathbb Z/p^k\mathbb Z\).
   Orthogonality with that denominator detects congruence modulo
   \(\varphi(p^k)\), not modulo \(p^k\).  The expression is not even invariant
   under changing an integer representative by \(p^k\), since generally
   \(\varphi(p^k)\nmid p^k\).
2. Lemma 8.2 says, "trivially," that
   \(e^{2\pi i\tau^{dpn}/\varphi(p^2)}=1\).  This is false.  For example,
   \(p=5,\tau=2,d=n=1\) gives \(e^{2\pi i32/20}\ne1\).
3. Equations (8.9) and (9.13) separate a shared \(m\)-sum as though
   \(\sum_m a_mb_m=(\sum_m a_m)(\sum_m b_m)\).  No such factorization holds.
4. The asserted evaluation
   \[
   \sum_{1\le m<\varphi(p^2)}
   e^{-2\pi i v m/\varphi(p^2)}=\gcd(v,\varphi(p^2))
   \]
   is also false.  Once \(\varphi(p^2)>v\), the displayed full geometric sum
   equals \(-1\).

Consequently the claimed error bounds and Theorems 1.1--1.3 do not follow.
This rejection comes from checking the proof itself, not merely from the
preprint's publication status or its tension with later literature.

## Conclusion

Neither source changes the Phase 7 frontier.  Sanna's valid rank theorem is
non-diagonal and mod \(p\); Carella's apparently decisive mod-\(p^3\) claim is
unsupported by its proof.
