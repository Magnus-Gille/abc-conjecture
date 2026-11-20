# All odd denominators with squarefree kernel supported below 140450

On \(E_6:y^2=x^3-36x\), let \(G=(-3,9)\), let \(B_n^2\) be the reduced positive denominator of \(x(nG)\), and write \(D_n=\prod_{v_p(B_n)\text{ odd}}p\). For positive odd \(n\),
\[
  P^+(D_n)\le 140449\quad\Longleftrightarrow\quad n\in\{1,3,5,7\},
\]
with \(P^+(1)=1\). The respective kernels are \(1,37,13\cdot3121,14281\cdot140449\). Negative odd indices follow by reflection.

The only substantial inputs beyond finite-field and rational arithmetic are the [square-denominator classification](abc_full_quartic_square_classification.md), which gives \(D_q>1\) for each odd prime index \(q\), and the [orbit formulas](abc_full_quartic_signature.md), including the fact that every prime of \(B_n\) is \(1\bmod12\) for odd \(n\).

## Reduction to prime indices and six composite indices

Write \(Y=140449\). For \(p\mid B_d\) at an odd index, the order \(r_p=\operatorname{ord}(G\bmod p)\) divides \(d\), and \(r_p>1\) since \(G\) is integral. The full rational two-torsion gives \(4r_p\mid\#E_6(\mathbf F_p)\). Hasse's inequality implies \(p\ge(2\sqrt{r_p}-1)^2>2r_p\) for \(r_p\ge3\). The elliptic formal logarithm at these good primes gives \(v_p(B_{dh})=v_p(B_d)+v_p(h)\) whenever \(p\mid B_d\).

Suppose \(n>1\) is eligible and \(q\) is its largest prime divisor. Choose \(p\mid D_q\), which has exact reduction order \(q\). Since \(p>2q\), it cannot divide \(n\). Its odd valuation persists in \(B_n\), giving \(q<Y\). Thus every prime divisor of \(n\) is below \(Y\). Now for *every* divisor \(d\mid n\), any odd-exponent prime \(p>Y\) at \(B_d\) would also retain its odd valuation in \(B_n\). Hence each such divisor is itself eligible.

For every prime index \(q\mid n\), the nontrivial kernel \(D_q\) must therefore be a product of primes in the finite set \(S_q=\{p\le Y:p\equiv1\bmod12,\ r_p=q\}\). Compute the exact reduction order at each of the 3223 candidate bases. A verified annihilating integer \(M\) can be found by trying \(p+1\pm2a\) with \(p=a^2+b^2\), \(a\) odd. The script factors \(M\), removes each redundant prime factor as long as the quotient annihilates \(G\), and certifies the remaining order \(r_p\) by \(r_pG=O\) and \((r_p/\ell)G\ne O\) for every prime \(\ell\mid r_p\). These checks make the correctness of the finite census independent of the way the candidates \(M\) were suggested. Exactly 449 bases have odd prime order and the 404 distinct orders range up to 35089. No set \(S_q\) has more than three elements.

## Squareclass tests

For an odd auxiliary prime \(\ell\ge5\), take \(P=(-2,8)\) on \(E_0:Y^2=X^3+36X^2+36X\). In primitive slope coordinates \(X(qP)=-2(x/y)^2\), the orbit formula gives \(B_q=(x^2+3y^2)/4\). Thus at finite reduction the quadratic character of \(B_q\) equals the character of \(8(6-X(qP))\). At infinite reduction, \(\ell\mid y\) and \(B_q\equiv(x/2)^2\bmod\ell\) is a nonzero square. Skip a test if \(\ell\in S_q\) or the predicted character is zero. At each other prime the character of any proposed \(D_q\) must equal this predicted sign. Testing all subsets of each \(S_q\) at the auxiliary primes from 5 through 89 leaves just three possible indices with one kernel each, as listed in the theorem. Direct rational multiplication certifies the actual denominators at 1, 3, 5 and 7. [Local formula](abc_full_quartic_square_denominators.md)

Every composite supported on \(3,5,7\) has a divisor in the table below. Compute \(B_d\) by exact rational multiplication. Remove all factors \(p\le Y\) of \(B_d\), which are precisely the enumerated bases with \(r_p\mid d\). The residual integer is a quadratic nonresidue at the indicated prime. Consequently each of these six divisors has some odd-exponent prime above \(Y\), and the preceding reduction excludes every composite index.

| Divisor \(d\) | Bit length of residual integer | Prime witnessing nonsquareness |
|---:|---:|---:|
| 9 | 46 | 5 |
| 15 | 55 | 7 |
| 21 | 233 | 5 |
| 25 | 335 | 23 |
| 35 | 711 | 11 |
| 49 | 1508 | 13 |

Run `python3 abc_congruent_six_smooth_odd_support.py` using the Python standard library. The transcript includes the small factors removed at each composite divisor. [Verifier](abc_congruent_six_smooth_odd_support.py) · [Output](abc_congruent_six_smooth_odd_support.txt)
