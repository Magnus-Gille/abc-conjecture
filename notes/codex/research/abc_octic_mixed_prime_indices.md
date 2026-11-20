# Exact slopes and first failed cubeful tests on the mixed orbit

The seed \((s,t)=(7,4)\) has \(Y=s^2+2t^2=81\) and \(U_-=(s-t)^2+t^2=25\). On \(C:y^2=(x^2+2)((x-1)^2+1)\) choose the point above \(x=7/4\) with \(y=45/16\). The following computations keep the slope signed when evaluating \(U_-\). The value \(Y\) is unchanged on making the slope positive.

With \(g=x^2-x+2\), the right-hand side of the quartic is \(g^2-x^2\). Set
\[
 u=2(y+g),\qquad v=2(u-1)x-u.
\]
Then \(v^2=u^3-8u^2+8u\) and \(x=(v+u)/(2(u-1))\). On this elliptic curve put \(A=(1,1)\). The seed is \(P=(49/4,217/8)=2A\); its conjugate is \(\iota P=(1,-1)=-A\). Thus the difference \(T=3A\) has odd orbit \(P_m=[(3m+1)/2]A\).

For every odd positive \(m\), the reduced fraction \(s_m/t_m=x(P_m)\) has
\[
 s_m\text{ odd},\qquad
 v_2(t_m)=\max(v_2(3m-1),v_2(3m+1))\ge2 .
\]
Indeed the involution takes \(B\) to \(A-B\): the two points in each degree-two fiber sum to the same point, and the seed fiber gives \(A\). Exactly one of \(k=(3m+1)/2,1-k\) is even; write it as \(h\). The point \(2A\) is in the formal group with \(v_2(-u/v)=1\). Since \(a_1=0\), the doubling series is \(2z+O(z^3)\), so the formal parameter at \([h]A\) has valuation \(v_2(h)\). Its elliptic coordinates have valuations \(-2v_2(h),-3v_2(h)\), giving the asserted slope valuation. The two odd norms are coprime, since their difference is \(2s_mt_m\) and \(\gcd(s_m,t_m)=1\). Their product is a square by the curve equation, so both norms are squares for every odd index.

| Inert index \(m\) | Sign of slope | Digits in numerator, denominator | \(v_2(t_m)\) | Least \(p\) with \(v_p(Y_m)=2\) | \(\#E(\mathbf F_p)\) | \(\operatorname{ord}_p(A)\) |
|---:|:---:|---:|---:|---:|---:|---:|
| 5 | + | 24, 23 | 4 | 131 | 150 | 15 |
| 7 | − | 46, 46 | 2 | 617 | 588 | 21 |
| 13 | + | 158, 159 | 3 | 2,939 | 3,042 | 39 |
| 23 | + | 496, 497 | 2 | 57,593 | 57,132 | 23 |
| 31 | + | 902, 899 | 2 | 11,657 | 11,532 | 93 |

In each row \(\operatorname{ord}_p(T)=m\), \(v_3(Y_m)=4\), and \(v_5(U_{-,m})=2+2v_5(m)\). At \(m=5\) the first exponent-two prime of \(U_-\) is 29; at the other four indices it is 5. For \(m=7\) the square \(U_-\) in the signed convention is \(U_+\) after making the slope positive. The first row has exact slope
\[
 \frac{237298085475105876957727}{24722582904347380924144}.
\]
The CSV contains every full reduced slope. The standard-library script reproduces them, tests integer square roots, checks every prime up to each reported first failure, and independently computes the two reduction orders and the full group size. The optional extended calculation finds that at \(m=53\) the least failed prime is 9,623,953; among all smaller primes, only 3 divides \(Y_{53}\), to exponent four.

[Exact slopes](abc_octic_mixed_prime_slopes.csv) · [Verification program](abc_octic_mixed_prime_indices.py)

## Checking multiplicities at all eligible new primes through ten million

Let \(A_\ell=\sqrt{Y_\ell}/9\). For \(p\le10^7\) and inert rational prime ranks \(\ell\ge5\), the exhaustive scan found **65** first-appearance pairs \((\ell,p)\) on \(Y\), across 44 distinct ranks. In all 65 cases \(v_p(Y_\ell)=2\). In particular, none had \(p^2\mid A_\ell\). The largest observed rank was 1,279, with \(p=9,820,163\). At rank 5 the four new \(Y\) primes within the bound were 131, 281, 491 and 294,241. All four had valuation two.

For coverage, \(p\mid Y_\ell\) implies \(p\) splits in \(K=\mathbf Q(\sqrt{-2})\). At such good primes the CM Frobenius is \(\pi\in\mathbf Z[\sqrt{-2}]\), \(p=N(\pi)\), and \(\#E(\mathbf F_p)=N(1-\pi)\). For a new prime, \(T=3A\) has reduction order \(\ell\). As \(\ell\) is inert, \(\ell\mid N(1-\pi)\) implies \(1-\pi\in\ell\mathbf Z[\sqrt{-2}]\). Thus
\[
 p=(1+a\ell)^2+2b^2\ell^2,\qquad b\ge1,
\]
after conjugation; \(b=0\) cannot give a rational prime. In particular it suffices to run through \(\ell\le\lfloor\sqrt{10^7/2}\rfloor\). A prime sieve and direct enumeration give 50,139 candidate pairs.

At \(A=(1,1)\), the division polynomials start \(\psi_1,\ldots,\psi_4=1,2,-45,868\). Since the candidates are coprime to 30, all divisions in the usual duplication recursion are by units. Divisibility of \(\psi_{3\ell}(A)\) by \(p\) detects the exact new rank \(\ell\) of \(T\); \(p^2\) detects the extra multiplicity. For an independent check, at every rank hit the program computes \(P_\ell\) and its slope directly modulo \(p^3\), identifies the correct factor, and tests its valuation against the division-polynomial result. The same candidate set had nine rank hits on \(U_-\), all of valuation two. Coverage on \(U_-\) is limited to this split-prime candidate set.

[Reproducible multiplicity scan](abc_octic_mixed_wieferich.py)
