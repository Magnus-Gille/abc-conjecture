# Odd depths on both denominator halves of the shifted factor

Let \(n=2m\ge16\) be dyadic, and for \(j=m-1,m+1\) let \(D_j\) be the part coprime to 6 of the denominator \(B_j(R)\) on \(E':y^2=x^3+16x^2+32x\), \(R=(-8,16)\). Each \(D_j\) is a nonpower of each of the four exponents \(2,3,5,7\). Thus for each such \(q\) there are **two distinct primes outside 3** in \(s_n\) whose depths are not divisible by \(q\), one in each half. In particular every \(s_n\) at these indices has two distinct odd-depth primes outside 3, irrespective of the number of prime divisors. The two halves are coprime since meeting the abscissa of \(R\) modulo an odd prime requires meeting precisely one of \(R,-R\). [Exact division of \(s_n\) into the two odd denominator parts](abc_dyadic_normalized_s.md)

If \(s_n\) is squareful and exactly two primes other than 3 divide it, each has exponent at least 11, with every prime factor of that exponent at least 11. Hence \(s_n=3^h p^2r^3\) is impossible for any \(h\) and distinct primes \(p,r\ne3\). For \(n=8\) the equality also fails since \(s_8=9\cdot281\). For every fixed \(q\ge2\) and every fixed bound \(H\), the half-denominator genus-\((2q-1)\) argument in the linked note, applied with all primes \(\le H\) removed, shows that each sufficiently late half has some prime \(p>H\) with \(q\nmid v_p(D_j)\). Thus the second largest such prime in the full \(s_n\) tends to infinity. Only the explicit four-exponent claim gives an all-index cutoff here.

## An integral normalization of the odd divisions

Scale \((x,y)\mapsto(x/4,y/8)\) to \(E_0:y^2=x^3+4x^2+2x\) and \(P=(-2,2)\). Write \(W_j=\psi_j(P)\) for the standard integral division polynomial value. For every odd \(j\ge1\), the odd part of \(B_j(R)\) is
\[
                        |W_j|\,2^{-(j^2-1)/4}.
\]
At odd primes the integral model has good reduction, the point is integral, and the coprime multiplication coordinates give \(v_\ell(B_j)=v_\ell(W_j)\). At 2 take \(\lambda^4=2\), over a fixed extension of \(\mathbf Q_2\), and substitute \(x=\lambda^2 X,\ y=\lambda^3Y\) in the model \(E_0\). The new coefficients are \(2\sqrt2,1\), and \(P\) becomes \((-\sqrt2,\lambda)\), reducing to \((0,0)\). At this residue point of \(Y^2=X^3+X\), every odd division polynomial is a unit: \(\psi_1,\psi_3\) reduce to 1, and in the odd-index recurrence exactly one product of odd-index factors survives, since the even division polynomials vanish at \(Y=0\). Division polynomials scale by \(\lambda^{j^2-1}\) under the change of model. This proves the asserted normalization.

The initial values on \(E_0,P\) are \(W_0=0,\ W_1=1,\ W_2=4,\ W_3=-36,\ W_4=-448\). Modulo each odd auxiliary prime, use the usual recurrences
\[
\begin{aligned}
 W_{2h+1}&=W_{h+2}W_h^3-W_{h-1}W_{h+1}^3,\\
 W_{2h}&=(W_h/4)(W_{h+2}W_{h-1}^2-W_{h-2}W_{h+1}^2).
\end{aligned}
\]
The seven values \(W_{m-3},\ldots,W_{m+3}\) determine the corresponding seven at \(2m\). Include \(t=m/2\bmod(\ell-1)\) in the state and double it at each step. Thus at \(j=m\pm1\) the normalization exponent is \(t^2\pm t\bmod(\ell-1)\). For \(q=2\), the chosen \(\ell\) are \(1\bmod4\); for odd \(q\), \(-1\) is a \(q\)-th power. Consequently the sign of \(W_j\) does not affect the character.

## The finite certificate

To test the possibility \(|W_j|2^{-(j^2-1)/4}=3^h z^q\), regard each residue \(h\bmod q\) separately. The auxiliary primes in each table entry jointly exclude that residue for the indicated half, over all \(m=8,16,\ldots\). Ordered entries correspond to \(h=0,\ldots,q-1\). Braces indicate that two primes are needed for the specified residue class.

| \(q\) | \(j=m-1\) | \(j=m+1\) |
|---:|---|---|
| 2 | \(\{113,353\},5\) | \(\{233,353\},5\) |
| 3 | \(1279,7,\{1759,1663\}\) | \(79,7,\{283,1279\}\) |
| 5 | \(71,271,31,71,31\) | \(71,271,31,71,31\) |
| 7 | \(113,113,3361,127,113,29,71\) | \(113,113,127,5839,29,29,29\) |

The verifier iterates the complete state to its first repetition, handles the prefix directly, and checks incompatible cyclic classes using the gcd of the two periods. A zero residue is always counted as a possible power. The argument checks every index without assuming an equidistribution property. [Standard-library verifier](abc_dyadic_normalized_s_halves.py)
