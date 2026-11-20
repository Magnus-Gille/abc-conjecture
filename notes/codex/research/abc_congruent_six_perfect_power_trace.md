# An Eisenstein trace descent for perfect powers of the denominator

Let \(w=B_n>1\) at an odd index on \(E:y^2=x^3-36x\), with \(G=(-3,9)\). If \(w=z^p\) with \(p\ge5\) prime, then
\[
 p\mid a_n,\qquad p\equiv\pm1\pmod{24},
 \qquad (5/p)=(7/p)=(11/p)=(13/p)=(23/p)=(47/p)=1 .
\]
Here \(a_n^4+3b_n^2=4w^4\) is the primitive signature. These conditions allow a set of relative density \(1/256\) among primes. Its first member is 27,431. A nontrivial cube requires \(3\nmid b_n\). [Arithmetic verifier](abc_congruent_six_perfect_power_trace.py) · [Primitive parametrization and height estimates](abc_full_quartic_signature.md)

## The trace and the denominator of its root

In \(K=\mathbb Q(\sqrt{-3})\) put \(t=\sqrt{-3}\) and \(\alpha=(a^2+bt)/2\). This is an Eisenstein integer of odd norm \(z^{4p}\). It is a unit at 3. Away from 2 and 3 a common prime ideal of \(\alpha,\bar\alpha\) would divide both \(a\) and \(b\), so the ideals are coprime. The ring is a PID, and raising to \(p\ge5\) permutes its six units. Thus \(\alpha=\gamma^p\), \((\gamma,\bar\gamma)=1\), and \(N\gamma=z^4\). Write \(U=\gamma+\bar\gamma\), \(V=(\gamma-\bar\gamma)/t\), and \(Q=z^4\). The residue of \(\alpha\) in \(\mathcal O_K/(2)=\mathbb F_4\) is nonrational, since \(\alpha=(a^2+b)/2+b(-1+t)/2\) with \(b\) odd. Hence \(U,V\) are odd. Also \((U,z)=1\): if a rational prime divided \(z\) and \(U\), a place above it dividing \(\gamma\) would also divide \(\bar\gamma\).

The recurrence for the power sums in the two roots of \(X^2-UX+Q\) gives
\[
 a^2=UL,\qquad
 L=(\gamma^p+\bar\gamma^p)/U
   \equiv (-1)^{(p-1)/2}pQ^{(p-1)/2}\pmod{U^2}.
\]
Indeed the trace polynomial at odd \(p\) has coefficient \((-1)^{(p-1)/2}p\) on \(UQ^{(p-1)/2}\), and all its other terms are divisible by \(U^3\). In particular \(\gcd(U,L)\mid p\). If \(p\nmid U\) then \(|U|=s^2\) and
\[
                     s^4+3V^2=4z^4.
\]
This is primitive by \((U,z)=1\) and the coprimality of the conjugates. It is a new solution of the same signature, so \(z=B_m\) at an odd index.

No nonunit denominator on the orbit can be the \(p\)-th power of another denominator for \(p\ge3\). If \(B_n=B_m^p\), put \(g=\gcd(n,m)\). The odd-index strong divisibility identity gives \(B_g=B_m\). This follows prime by prime from the unique first reduction order and from \(v_l(B_{rk})=v_l(B_r)+v_l(k)\) at every odd denominator prime \(l\) of first order \(r\). Hence \(v_l(n/g)=(p-1)v_l(B_g)\) for every \(l\mid B_g\), so \(B_n^{1-1/p}\le n/g\le n\).

For odd \(n\ge5\), \(\log B_n>0.35n^2-2.2\), which contradicts that inequality. To recover the bound, the duplication estimate gives
\[
 h(x)-\tfrac13\log5184\le2\widehat h\le h(x)+\tfrac13\log1369.
\]
At \(4G\), \(h(x)=\log1442401\), giving \(\widehat h(G)>0.35\). Odd multiples have \(-6\le x\le0\), so \(h(x(nG))\le2\log B_n+\log6\). The remaining index \(n=3\) has \(B_3=37\).

Thus \(p\mid U\) and \(p\mid a\). The congruence for \(L\) yields \(v_p(L)=1\). There are integers \(u,v\) and a sign \(s\) with \(U=spu^2\), \(L=spv^2\). From \(c^2=2w^2-a^2\) and \(3d^2=2w^2+a^2\), the prime divisors of \(a\) have \((2/p)=(3/p)=1\), hence \(p\equiv\pm1\pmod{24}\). Since \(U^2\equiv Q\equiv1\pmod8\), the polynomial \(L\), which depends on \(U^2,Q\), takes its value at \((1,1)\) modulo 8. There it equals \(2\cos(p\pi/3)=1\). Thus \(sp\equiv1\pmod8\) and \(s=(-1)^{(p-1)/2}\). At \(p=3\) with \(3\mid b\), the unit ambiguity in extracting \(\gamma\) also disappears. All unit cubes modulo 3 are rational and the only elements of \(\mu_6\) rational modulo 3 are \(\pm1\). Since \(\alpha\bmod3\) is rational, the unit factor is a cube. Now \(3\nmid U\) follows from \(3\nmid z\) and \(4z^4=U^2+3V^2\), giving the same impossible descent.

## Quadratic characters forced at the exponent

For an odd auxiliary prime \(\ell\ne3,p\) with \(\ell\nmid U\), first suppose \(\ell\nmid z\). Then \(\theta=\gamma/z^2\) reduces to the norm-one torus of order \(h=\ell-(-3/\ell)\). If \(p\equiv\pm1\) modulo the order of \(\theta\), then
\[
 (a/z^p)^2=\theta^p+\theta^{-p}\equiv \theta+\theta^{-1}=U/z^2\pmod\ell .
\]
Thus \((sp/\ell)=1\). If \(\ell\mid z\), the trace polynomial reduces instead to \(a^2\equiv U^p\pmod\ell\), giving the same symbol. Quadratic reciprocity gives \((\ell/p)=1\).

For \(\ell=5,7,11,13\), no prime divisor of \(a\) lies in these classes modulo 24, so \(\ell\nmid U\). The torus orders are 6,6,12,12. Each divides \(p-1\) or \(p+1\), which proves the first four symbol restrictions.

For the last two restrictions, any occurrence of a nontrivial \(p\)-th power implies one at a prime index \(q\). Take the largest prime divisor \(q\) of its index. Every divisor prime \(l\) of \(B_q\) has exact order \(q\) and satisfies \(l\ge(2\sqrt q-1)^2>q\) by the independent rational two-torsion and Hasse's inequality. Its valuation persists at the original index, so \(B_q\) itself is a \(p\)-th power. The height bound and \(B_3=37\) give \(q>3\).

The numerator \(a_q\) is the abscissa denominator root for \([q](G+(0,0))\), and \(G+(0,0)=(12,36)\). This point has order 3 modulo 23 and 6 modulo 47. Thus neither prime divides \(a_q\) for prime \(q>3\). At 23 the torus order is 24. At 47 it is 48, and \(\gamma=\varepsilon\beta^4\) with \(N\beta=z\) by unique factorization and coprime conjugates. Thus \(\theta=\varepsilon(\beta/\bar\beta)^2\) is a square in the torus whenever \(47\nmid z\), since the elements of \(\mu_6\) are squares in its cyclic group of order 48. Now the order of \(\theta\) divides 24, proving the remaining restrictions. In each of the two eligible classes modulo 24 the six characters are independent by the Chinese remainder theorem.

## Comparison with published modular results

Pacetti and Villagra Torcomian study primitive solutions of \(X^4+dY^2=Z^p\) for positive squarefree \(d\), construct the twisted Galois representations of the associated Q-curves, and prove large-exponent exclusions for specified values of \(d\). Their sequel treats the other sign. To put the present equation into their rational model with \(d=3\) by weighted scaling, take \(X=ua,Y=u^2b,Z=vz^4\). This requires \(v^p=4u^4\). Since \(a,b,z\) are odd, integral \(X,Y\) require \(v_2(u)\ge0\), and \(p v_2(v)=2+4v_2(u)\) then forces all three integral coordinates even. Likewise \((3b)^2+3a^4=12z^{4p}\) retains the dyadic valuation two. The published primitive normalization does not supply an upper bound for the exponent here. [Pacetti–Villagra Torcomian I](https://arxiv.org/abs/2007.11486) · [Part II](https://arxiv.org/abs/2103.06965)

The transfer \(\gamma^p+\bar\gamma^p=a^2\) is primitive over the imaginary quadratic field \(\mathbb Q(\sqrt{-3})\), with all three entries units at 2. The cited asymptotic \((p,p,2)\) results over totally real fields have a different field hypothesis. The signature \((4,2,p)\) theorem for \(X^4-Y^2=Z^p\) also uses a different equation. At the rational seed the usual Q-curve \(Y^2=X^3+4aX^2+2(a^2+b\sqrt{-3})X\) has \(j=-2848+544\sqrt{-3}\). This is a nonreal quadratic number. It cannot be a CM invariant since every ring class polynomial is irreducible and has a real root from its principal ideal class. A modular proof along this route must therefore address a non-CM seed representation. [Totally real signature results](https://arxiv.org/abs/2203.07873) · [The difference-of-powers equation](https://arxiv.org/abs/2209.09153)
