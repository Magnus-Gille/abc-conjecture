# A single auxiliary prime per exponent for the 3-free part of \(s_n\)

Let \(s_n=u_n^2+8v_n^2\) on the dyadic orbit with \(n=2^k,\ k\ge3\), and put \(S_n=s_n/3^{v_3(s_n)}\). For each \(q\in\{2,3,5,7,11,17,23,31,47\}\), there is an auxiliary prime \(\ell\) at which 3 is a \(q\)-th power and \(s_n\) is a unit outside the \(q\)-th powers for every \(k\ge3\). Thus \(S_n\) is never a \(q\)-th power for these exponents. More strongly, no relation \(s_n=3^e z^q\) is possible for any \(e\in\mathbb Z,\ z\in\mathbb Q^\times\). [Standard-library verifier](abc_dyadic_s_three_free_characters.py)

| \(q\) | \(\ell\) | Transient | Period |
|---:|---:|---:|---:|
| 2 | 23 | 0 | 1 |
| 3 | 109279 | 0 | 11 |
| 5 | 1477631 | 5 | 18 |
| 7 | 51479 | 0 | 15 |
| 11 | 2690689 | 3 | 5 |
| 17 | 21319 | 0 | 20 |
| 23 | 39508481 | 5 | 33 |
| 31 | 1079297 | 5 | 5 |
| 47 | 482546369 | 1 | 200 |

All auxiliary primalities are certified by division through their square roots. Write \(U=u^2,V=v^2,\ \chi(z)=z^{(\ell-1)/q}\bmod\ell\). At a finite ratio \(x=U/V\), the state consists of \(x\) and \(h=\chi(V)\). Here \(\chi(s_n)=h\chi(x+8)\). Doubling sends
\[
 N=(x^2-32)^2,\quad D=4x(x^2+16x+32),\quad
 (x,h)\longmapsto
 \begin{cases}
 (N/D,h^4\chi(D)),&D\ne0,\\
 (\infty,h^4\chi(N)),&D=0.
 \end{cases}
\]
At infinity the scale is \(h=\chi(U)=\chi(s_n)\) and the next state is \((\infty,h^4)\). The initial pair at \(n=8\) is \((U,V)=(961,196)\). Each row checks \(\chi(3)=1\), and checks \(\chi(s_n)\notin\{0,1\}\) at every state up to the first repetition of the full state. This covers every later index, independently of \(v_3(s_n)=2+v_3(k-1)\).

## All remaining exponents

Assume \(S_{2m}=z^q\) for some dyadic \(m\ge8\) and prime \(q\) outside the table. The \(s\)-packet Frey curve over \(K=\mathbb Q(\tau)\), \(\tau^2=-2\), has \(a=w_m,\ b=8u_m^2v_m^2,\ g=a^2+b\tau,\ A=4a,\ B=2g\), and equation \(y^2=x^3+Ax^2+Bx\). Now \(g\bar g=s_{2m}=3^e z^q\). The two-dimensional descended representation has cyclotomic determinant. It is finite flat at \(q\), and away from 2 and 3 the prime-to-\(q\) residual conductor vanishes. At 3 the extension \(K/\mathbb Q\) splits and \(C\) has multiplicative reduction. Its residual conductor exponent is at most one, including when \(q\mid e\); in the complementary case the Tate parameter valuations at the conjugate places are \(e,2e\bmod q\). These local assertions follow as in the single-packet argument, with the factor \(3^e\) retained. [Frey-curve construction](abc_dyadic_fourth_factor.md) · [Trace checks](abc_dyadic_st_power_audit.py)

For clarity, the dyadic conductor exponent of the descended representation is at most 9. The model's discriminant over \(K\) has valuation 18. If the model is nonminimal then \(v_\tau(\Delta_{\min})\le6\). On a minimal model the initial low-type tests in Tate's algorithm all pass to the cubic step, since \(a_6=b_6=0\) and \(v_\tau(b_8)=v_\tau(-B^2)=4\). The cubic is \(T^3+T=T(T+1)^2\bmod\tau\). Thus the type is \(I_j^*, j\ge1\), with at least six geometric components; Ogg gives \(f_K(C)\le18+1-6=13\). The induced representation over \(\mathbb Q\) therefore has exponent at most \(6+13=19\). Its two constituents differ by \(\chi_{-8}\), of last upper inertia break 2. They have finite inertia at 2 since \(v_\tau(j)=12\), and their determinants are unramified there. Every nonidentity finite-order element of \(\mathrm{SL}_2\) in characteristic zero fixes no nonzero vector. If a constituent has an upper inertia break \(r>2\), the other has the same last break and both conductors are \(2(1+r)\); each is therefore at most 9. When all upper breaks are at most 2, each conductor is at most 6.

At the inert good primes 31 and 47 the two trace conditions are
\[
             {\rm tr}\bar\rho({\rm Fr}_{31})=0,\qquad
             ({\rm tr}\bar\rho({\rm Fr}_{47}))^2=98\bmod q.
\]
At 31 one has \(31\mid u_8\) and \(31\mid v_m\) at all later indices, while \(a=w_m\) stays a unit. The normalized curve over \(\mathbb F_{31^2}\) descends to \(y^2=x^3+4x^2+2x\) of trace 0 over \(\mathbb F_{31}\); its trace over the quadratic extension is \(-62\). At 47 the direct quadratic-field point count on \(y^2=x^3+4x^2+2(1+4\tau)x\) gives trace 4 over \(\mathbb F_{47^2}\). The identity \(({\rm tr}\rho({\rm Fr}_p))^2={\rm tr}\rho({\rm Fr}_p^2)+2p\) gives the displayed comparisons.

In the reducible case the finite parts of the two characters are inverse. They have no ramification at 3, since if either were ramified then both would be, of combined conductor exponent at least two. Their \(2\)-conductors each divide 16 by equality and the sum bound nine. Thus their values at \(31\equiv-1\bmod16\) are equal signs, giving trace \(\pm32\bmod q\), a contradiction.

Otherwise Serre modularity in weight two gives an eigenform of trivial character at a level dividing \(3\cdot512\). Use the full 225-dimensional cusp space at level 1536 and let \(D=T_{47}^2-98,\ U=T_{31}\). The two trace conditions force \(q\) to divide both \(\det D\) and \(\det(D+U)\), since these operators act on the same eigensystem. Their nonzero integer determinants have gcd
\[
        2^{225}\,3^{32}\,5^{32}\,7^{118}\,11^8\,17^{28}\,23^2\,31^4 .
\]
Every prime divisor, and the auxiliary characteristic 47, has already been excluded by the corresponding congruence above. [Full Hecke-space verifier](abc_dyadic_s_three_free_forms.py)

It follows that \(S_n>1\) and \(S_n\) is not a proper power at any dyadic \(n\ge8\). The initial cofactor \(S_8=281\) is prime; \(S_4=1\) precedes the theorem. Any \(s_n\) in range with just two prime factors has the form \(3^e p\) with \(v_p(s_n)=1\). In particular a squarefull \(s_n\) would require at least three distinct prime divisors.
