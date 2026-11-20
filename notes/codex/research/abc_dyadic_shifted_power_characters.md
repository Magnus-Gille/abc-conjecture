# Finite power tests for two quadratic factors along the dyadic orbit

Let \(R=(-8,16)\) on \(E':y^2=x^3+16x^2+32x\). For \(k\ge3\) and \(n=2^k\), use the positive coprime coordinates \(x([2^{k-1}]R)=u_n^2/v_n^2\) of the dyadic orbit. Define
\[
 s_n=u_n^2+8v_n^2,\qquad t_n=u_n^2+16v_n^2.
\]
For **each of the 70 primes \(q\le349\)**, no \(s_n\) in this range of indices is a \(q\)-th power. A second set of direct tests excludes \(q=2,3,5,47\) for all \(t_n\). The initial index \(k=2\) is outside these statements and gives \(s_4=9,t_4=17\). [Dyadic coordinates and recurrence](abc_octic_dyadic_fermat_audit.md) · [Standard-library verifier](abc_dyadic_shifted_power_characters.py)

## A restriction on the index of a possible power

Write \(M=2^{k-1}\). Over a good odd prime where an affine point \(Q\) has a unit ordinate, \(x-x(Q)\) is a local parameter at \(Q\). If \([M]R\) reduces to \(Q=\pm R\), the valuation of \(x([M]R)+8\) is the formal depth of \([M\mp 1]R\). The denominator \(v_n\) is a unit there, so this valuation equals \(v_p(s_n)\). On the odd-prime formal group, multiplication by an integer increases depth by its \(p\)-adic valuation. This follows from the formal logarithm, which preserves valuations on \(p\mathbb Z_p\).

For \(p=3\) the point \(R\) has exact order three in the reduction and \([3]R\) has depth two, as \(x([3]R)=-200/81\). If \(m=k-1\), take the sign \((-1)^m\). Then
\[
 v_3(s_n)=2+v_3((2^m-(-1)^m)/3)=2+v_3(m).
\]
For the last equality, lifting the exponent applied to \((-2)^m-1\) gives \(v_3((-2)^m-1)=1+v_3(m)\). Therefore a \(q\)-th power with prime \(q\ge5\) requires \(3^{q-2}\mid k-1\).

At the prime \(p=117041\), the verifier computes
\[
 x([7]R)=-61290606728/117041^2.
\]
Thus \(R\) has exact reduction order seven and \([7]R\) has depth one. Because \(3\mid k-1\), one has \(M\equiv1\bmod7\), and so
\[
 v_{117041}(s_n)=1+v_{117041}(M-1).
\]
A \(q\)-th power would require \(117041\mid M-1\). The order of 2 modulo 117041 is 14630, as checked by modular powers at 14630 and its quotients by each of its five prime divisors. This proves the necessary condition
\[
 k\equiv 1\pmod{L_q},\qquad L_q=\operatorname{lcm}(14630,3^{q-2})\qquad(q\ge5).
\]

## Checking full periods

The signed integral recursion starts from \((31,14,2273)\) at \(k=3\) and acts by
\[
 (u,v,w)\longmapsto(u^4-32v^4,\ 2uvw,\ w^4-128u^4v^4).
\]
Possible signs in \(u,v\) leave the tested values unchanged. For each \(q\) the script supplies a prime \(\ell\equiv1\bmod q\) and follows the orbit until the first repeated state. Let its cycle start at index \(k_0\) and have length \(h\). For a prefix state at \(j<k_0\) to be relevant one needs \(L_q\mid j-1\). A cycle state at \(j\) is relevant precisely when \(\gcd(L_q,h)\mid j-1\), by the Chinese remainder theorem. The script sets \(L_q=1\) for \(q=2,3\). Every relevant \(s\) value is nonzero and has \(s^{(\ell-1)/q}\ne1\bmod\ell\). Of the 70 certificates, 58 exclude every state before applying the progression restriction. The largest individual computation visits 23,581 states.

For \(s_n\), the three residues reached modulo 3 all have \(s_n\equiv0\). Instead, modulo 23 the complete set \(\{11,14,20,21,22\}\) consists of nonsquares. For cubes, \(s_n\equiv2\bmod7\) at every state. For \(t_n\), the following tests cover all states without an index restriction.

| \(q\) | Auxiliary prime | Distinct states |
|---:|---:|---:|
| 2 | 3 | 3 |
| 3 | 7 | 2 |
| 5 | 71 | 7 |
| 47 | 419429 | 1321 |

## Connection to the positive-sign generalized Fermat equation

The identity \(s_{2n}=w_n^4+128(u_nv_n)^4\) makes a positive \(q\)-th power here a primitive solution of \(X^4+2Y^2=Z^q\), with \(X=w_n\) odd and \(Y=8u_n^2v_n^2\) even. Dieulefait and Jiménez Urroz report solving that equation for prime \(q>349\). The finite checks above cover every smaller prime exponent including 349, independently of any modular-form computation. The companion local Frey-curve proof treats the large exponents on this orbit directly. [Authors' preprint](https://arxiv.org/abs/math/0611663) · [Companion argument](abc_dyadic_fourth_factor.md)
