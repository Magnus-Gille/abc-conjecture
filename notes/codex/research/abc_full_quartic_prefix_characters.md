# Quadratic characters of the denominator along descending prime factors

Let \(E_6:Y^2=X^3-36X\), \(G=(-3,9)\), and let \(w_n=B(nG)\) be the positive square root of the denominator of the reduced abscissa at positive odd \(n\). Put \(d_n=\operatorname{sf}(w_n)\). Define
\[
 M=144923830996024080
  =2^4 3^3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19\cdot29\cdot37\cdot41\cdot53\cdot89,
 \quad \mathcal S=\{q\text{ odd prime}:q\not\equiv\pm1\pmod M\}.
\]
The primes in \(\mathcal S\) have natural density \(1-1/11018538949017600\) among the primes. At every odd \(n\), for every \(q\in\mathcal S\) and \(1\le a\le v_q(n)\), the squarefree part \(d_n\) contains a different prime \(p_{q,a}\) with exact scalar rank divisible by \(q^a\). In particular
\[
 d_n\ge\prod_{q\in\mathcal S,\,q\mid n}
           2^{v_q(n)}q^{v_q(n)(v_q(n)+1)/2}.
\]
For \(Q=q^a\) each factor \(2Q\) can be replaced by \((2\sqrt Q-1)^2\). For \(q\equiv3\bmod4\), \(q\ge7\), it can be replaced by \(8Q^2-4Q+1\); at \(q=3\) it can be replaced by \(4Q^2+1\). For example \(d_{3^e}\ge\prod_{a=1}^e(4\cdot9^a+1)\) with every witness retained at the final index. [Full elliptic parametrization](abc_full_quartic_signature.md) · [Standard-library finite verifier](abc_full_quartic_prefix_characters.py)

## Five scalar characters

For odd \(m\) coprime to the modulus in the middle column, the product in the last column equals \((d/m)\), the Jacobi symbol in the index:

| \(d\) | Period | Character evaluated on the denominator |
|---:|---:|---|
| 2 | 8 | \((w_m/5)\) |
| 3 | 24 | \((w_m/577)\) |
| 5 | 10 | \((w_m/17)\) |
| 13 | 26 | \((w_m/41)(w_m/233)\) |
| 17 | 34 | \((w_m/241)\) |

The first identity holds at every odd \(m\). On the units of their common modulus, these five quadratic characters are independent by the distinct rational prime squareclasses. They therefore detect \(31/32\) of primes using multiplicative scalar characters alone, ignoring finitely many small primes in this density statement.

The restriction to units is intrinsic to finding more scalar characters. Suppose a sign on the odd integers is periodic modulo \(N=2^k u\), is invariant under sign change, and is completely multiplicative with values in \(\{1,-1\}\) at *every* odd index. At two indices congruent modulo \(2^k\), multiplication by \(u\) makes them congruent modulo \(N\). The sign at \(u\) cancels, so the sign factors through the dyadic unit group. Its invariance under \(-1\) leaves only the trivial character and \((2/m)\), by the structure of \((\mathbf Z/2^k\mathbf Z)^\times\).

## Distinguishing all unit classes up to sign

On the isogenous curve \(E_0:Y^2=X^3+36X^2+36X\), \(P=(-2,8)\), the full parametrization gives \(X(mP)=-2x^2/y^2\) and \(w_m=(x^2+3y^2)/4\), with \((x,y)=1\). At \(h\ge5\) prime, on finite reductions the local quadratic character of \(w_m\) equals \((8(6-X(mP))/h)\); at the identity it is one. Its period divides \(r_h=\mathrm{ord}_h(P)\). If one of the finite expressions vanishes, the uninterpreted squareclass could depend on deeper data, but the symbol modulo \(h\) is exactly zero. The finite checks below verify that none vanishes on the units used.

For each modulus \(L\) below, use all auxiliary primes \(5\le h\le10000\) with \(r_h\mid L\). On each of the \(\varphi(L)/2\) unit classes modulo sign the verifier computes the vector of these characters by finite-field addition. Every such vector has nonzero entries and occurs exactly once. The complete check is small at each individual modulus.

| \(L\) | Primes used | Distinct vectors |
|---:|---:|---:|
| 120 | 40 | 16 |
| 240 | 46 | 32 |
| 264 | 22 | 40 |
| 312 | 28 | 48 |
| 408 | 29 | 64 |
| 696 | 26 | 112 |
| 984 | 25 | 160 |
| 4440 | 57 | 576 |
| 6360 | 61 | 832 |
| 7560 | 79 | 864 |
| 10680 | 55 | 1408 |
| 15960 | 64 | 1728 |

If two units have all these signs equal, their residues agree up to sign at each modulus. Each modulus contains 24, so the signs in these comparisons must agree: a unit cannot equal its negative modulo 24. The least common multiple of the moduli is \(M\). Thus equality of the full vectors implies equality modulo \(M\) up to a single sign.

## Fresh primes along the index

Form the successive prefixes of the prime factorization of \(n\) in decreasing order, with repetition. When a copy of \(q>89\) is appended to a prefix \(m\), both \(m\) and \(mq\) are coprime to \(M\). If \(q\not\equiv\pm1\bmod M\), the two indices are distinct up to sign modulo \(M\). Some local character therefore changes. For \(7\le q\le89\), the same argument uses \(L=120\): both prefixes are prime to 30 and \(q\not\equiv\pm1\bmod120\). At \(q=3,5\), the universal character \((2/m)\) changes on multiplication by \(q\), even if \(q\) divides \(m\).

The EDS divisibility \(w_m\mid w_{mq}\) and the sign change force a prime of odd exponent in \(w_{mq}/w_m\). At a good \(p\mid w_m\), the exact reduction rank \(r\) for \(G\) divides \(m\) and exceeds 1, as \(G\) is integral. Its prime divisors are at least \(q\), so \(r\ge q\). Since \(E_6\) has full rational two-torsion, \(4r\mid\#E_6(\mathbf F_p)\) at these odd ranks. Hasse gives \(p\ge(2\sqrt r-1)^2>r\ge q\). All divisors of \(w_n\) are good primes. The formal valuation rule leaves their old depths unchanged on multiplying by \(q\). Thus the odd-exponent prime is new, and its exact rank divides \(mq\) but not \(m\); if \(q^a\parallel mq\), that rank is divisible by \(q^a\). Again \(p>q\), so every later multiplier preserves the new odd valuation. Different steps have different witnesses. The Hasse bound gives the claimed individual factors. An earlier index prime equal to the witness may already have contributed an ordinary lifting valuation in \(mq\). The odd exponent certified here refers to \(w_n\), without requiring odd valuation at the first rank.

Finally \(p\mid w_n\) implies \(p\equiv1\bmod12\). If \(q\equiv3\bmod4\), it is inert in \(\mathbf Z[i]\). Its exponent \(a\) in the scalar order forces the Gaussian annihilator of the reduction to be divisible by \((q^a)\), using the unique place above \(q\). Frobenius at the split prime \(p\) is therefore \(1\bmod q^a\) in \(\mathbf Z[i]\). The rational two-torsion also makes it \(1\bmod2\). Consequently \(p=(1+2Q u)^2+4Q^2v^2\), with \(v\ne0\). If \(u\ne0\) this is at least \(8Q^2-4Q+1\). If \(u=0\) and \(q\ne3\), reduction modulo 3 forces \(3\mid v\). At \(q=3\) the unconditional lower bound \(4Q^2+1\) suffices.
