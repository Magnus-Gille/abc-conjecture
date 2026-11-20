# Counting abc exceptions at one exact height

For an integer \(C\ge 2\), let \(N_\delta(C)\) count the integers \(1\le a\le C/2\) such that \(\gcd(a,C)=1\) and
\[
 \frac{C}{\operatorname{rad}(a(C-a)C)}\ge C^\delta .
\]
Here \(\operatorname{rad}\) is the product of the distinct prime divisors. Set \(B(\delta)=\limsup_{C\to\infty}N_\delta(C)\), allowing infinity.

**Proposition.** There is an absolute real \(s>3\) with the following property. If infinitely many primitive triples \(u+v=w\) satisfy \(w/\operatorname{rad}(uvw)\ge w^\alpha\) for one fixed \(\alpha>0\), then
\[
 B(\delta)\gg_\alpha\delta^{-s}
\]
for every sufficiently small fixed \(\delta>0\). Consequently an eventual common-height bound \(B(\delta)=O(\delta^{-3})\) as \(\delta\downarrow0\) would imply rational abc. Rational abc itself gives \(B(\delta)=0\) for every \(\delta>0\). The implication from failure of the usual epsilon formulation to the hypothesis follows by taking a fixed exponent strictly between zero and \(\epsilon/(1+\epsilon)\) for an epsilon at which it fails.

## A polynomial transfer

Use a rational polynomial \(f\) of degree \(d\ge2\) which sends \([0,1]\) onto \([0,1]\), vanishes at 0, sends 1 to 0 or 1, and has all finite critical values in \(\{0,1\}\). Its finite fibers above 0 and 1 together have exactly \(d+1\) distinct roots. Indeed, their total multiplicity is \(2d\), and all \(d-1\) zeros of \(f'\), with multiplicity, account for the excess. Their squarefree product thus contains \(t(t-1)\) with cofactor of degree \(d-1\).

Suppose \(t=a/c\) is a reduced fraction in \((0,1)\), and \(f(t)=a'/c^d\) in lowest terms is also interior. For \(R=\operatorname{rad}(a(c-a)c)\) and the analogous \(R'\),
\[
 R'\le K_f c^{d-1}R,\qquad \frac{c^d}{R'}\ge\frac{c}{K_fR}.
\]
To see this, clear the fixed rational coefficients in the factorization of \(f(1-f)\). Outside finitely many coefficient primes, every new prime divides the homogenized cofactor of degree \(d-1\), of absolute value \(O_f(c^{d-1})\) on \(0<a<c\). The coefficient primes contribute a fixed factor. Composition preserves the polynomial hypotheses.

## Many distinct maps of a common degree

For a degree-\(d\) polynomial \(F\) use the formal expansion at infinity, with leading term \(t\),
\[
 (F/\operatorname{lc} F)^{1/d}=t-p+v/t+O(t^{-2}).
\]
For an outer polynomial \(G\) the corresponding series for \(G\circ F\) agrees to \(O(t^{1-d})\) with that for \(F\). This follows by writing \(G(F)/(\operatorname{lc}(G)F^{\deg G})=1+O(t^{-d})\). The coefficient \(p\) therefore detects the innermost map if it is distinguished by \(p\) alone. For \(d\ge3\), the pair \((p,v)\) is available.

Use the following generators of degrees at most 50. Write \(\varphi\) for Euler's totient.

* In degree 2 use \(t^2,2t-t^2,4t(1-t)\). Their centers \(p\) are \(0,1,1/2\).
* For each \(d\ge3\) and positive coprime \(a,b\) with \(a+b=d\), take
  \[
  H_{a,b}(t)=\frac{d^d}{a^a b^b}t^a(1-t)^b .
  \]
  Its maximum 1 is at \(a/d\), and all finite critical values are marked. Its center is \(p=b/d\) in lowest terms, with \(v=-p(1-p)/2\). When \(b>a\), also take \(J(t)=H_{a,b}(at/d)\) and \(1-J(1-t)\). These increasing maps have centers \(b/a>1\) and \(1-b/a<0\), distinct across all such coprime pairs. These choices give \(2\varphi(d)\) maps.
* Write \(n=d-1\). For \(1\le j<n\) with \(2j\ne n\) take
  \[
  P_{n,j}(t)=\frac{\int_0^t x^{n-j}(1-x)^j\,dx}{\int_0^1 x^{n-j}(1-x)^j\,dx}.
  \]
  Its derivative has its roots at the two endpoints. Integration of the three leading monomials gives \(p=j/n\) and \(v=-p(1-p)n/(2(n-1))\). Thus \(p,v\) recover \(n,j\), and distinguish this map from every \(H_{a,b}\) with the same center. There are \(d-2-\mathbf 1_{d\ {\rm odd}}\) such maps.

All generators satisfy the transfer hypotheses. The quadratic centers occur in no higher-degree generator. The expansion therefore recovers the rightmost symbol of every nonempty composition. Cancelling it is valid since substitution of a nonconstant polynomial into distinct polynomials preserves distinctness. Induction distinguishes all words.

With \(m_2=3\) and \(m_d=2\varphi(d)+d-2-\mathbf 1_{d\ {\rm odd}}\) for \(3\le d\le50\), exact rational arithmetic gives \(\rho=\sum_{d=2}^{50}m_d/d^3>1007/1000\). The finite inequality can be checked by the following code.

```python
from fractions import Fraction
from math import gcd

rho = Fraction(3, 8)
for d in range(3, 51):
    phi = sum(gcd(a, d) == 1 for a in range(1, d))
    rho += Fraction(2 * phi + d - 2 - d % 2, d**3)
assert rho > Fraction(1007, 1000)
```

Words of length \(h\) have total weight \(\rho^h\), giving a word of degree \(D\) weight \(D^{-3}\). They have at most \((h+1)^{49}\) different degrees, by recording the counts of each degree. For some fixed \(h\) the exponential exceeds this polynomial. At one fixed degree \(D\), therefore, the family contains \(M>D^3\) distinct maps. Include \(t^D\) if necessary, and use \(M\) for the resulting cardinality.

These degree-\(D\) maps themselves generate distinct words of each fixed length, even after adding \(t^D\). Indeed, if \(F(U)=G(V)\) with \(U,V\) of equal degree \(m\), comparison of leading terms shows \(U^D-\lambda^D V^D\) has degree at most \((D-1)m\), where \(\lambda=\operatorname{lc}(U)/\operatorname{lc}(V)\). Its factor left after removing \(U-\lambda V\) has degree \((D-1)m\), so \(U-\lambda V\) is constant. As both vanish at 0 and map \([0,1]\) onto \([0,1]\), \(U=V\). Cancellation now gives \(F=G\). Distinct words cannot be complementary polynomials, since all vanish at 0.

## Ensuring exactly the same reduced denominator

Let \(S\) contain 2 and every prime dividing a coefficient denominator or the numerator of a leading coefficient of the fixed degree-\(D\) family. At a prime dividing \(c\), if \(c\) is coprime to \(S\), the leading term of the homogenized polynomial is a unit. At \(p\in S\), take \(r=v_p(t)\) sufficiently large. If \(e_f\) is the order of vanishing of \(f\) at 0 and \(h_f\) its first nonzero coefficient, then \(v_p(f(t))=e_f r+v_p(h_f)\), since the lowest term dominates. Thus an input with sufficient valuations has exact output denominator \(c^D\).

Here is an explicit way to obtain such initial inputs without losing the entire starting saving. Choose an addend \(u\) of opposite parity to \(w\), and an integer \(n\ge2\) divisible by \(p-1\) for all odd \(p\in S\). Set \(W=w^n,U=u^n\) and \(z=((W-U)/(W+U))^2\). Its exact denominator is \((W+U)^2\), coprime to \(S\). At odd \(p\in S\), either \(p\mid wu\) and \(z\equiv1\), or Fermat's theorem gives \(z\equiv0\). The radical at \(z\) is at most
\[
 2\operatorname{rad}(uvw)\frac{W-U}{w-u}(W+U)
 \ll_n \operatorname{rad}(uvw)w^{2n-1}.
\]
Here \(1-z=4WU/(W+U)^2\). Set \(t_0=(4z(1-z))^m\) for a fixed large \(m\). It has high positive valuation at every \(p\in S\), including 2. Both maps used after \(z\) satisfy the transfer estimate and have exact denominator at each step, since \(W+U\) is odd. The base height \(c_0\asymp w^L\) with \(L=4nm\), and \(c_0/R_0\gg w/\operatorname{rad}(uvw)\). Constants may depend on the fixed maps and on \(n,m\).

Choose a fixed block length \(\ell\) so that \(M^{\ell-1}>D^{3\ell}\), possible since \(M>D^3\). Start every block with \(t^D\) and allow any of the \(M\) choices in the remaining \(\ell-1\) positions. Above a fixed valuation threshold each map decreases \(r\) by at most a fixed \(b\) at any prime of \(S\). Choose \(r_0\) above that threshold with \((D-1)r_0\ge(\ell-1)b\) and choose \(m\) large enough that the base attains \(r_0\) everywhere in \(S\). Since the first step multiplies each valuation by \(D\), every intermediate valuation and every final valuation in every block is at least \(r_0\).

Put \(q=D^\ell\) and \(A=M^{\ell-1}\). For fixed \(k\) all \(A^k\) words of \(k\) blocks have exact output height \(C=c_0^{q^k}\). The exceptional input ratios giving an endpoint, a collision, or complementary outputs belong to a finite set, by the polynomial identities above. The base heights tend to infinity in lowest terms, so we can discard these inputs. Each remaining output gives a different unordered pair and satisfies \(C/R'\gg w^\alpha/K^{\ell k}\) for a fixed \(K\). For fixed small \(\delta\), choose \(k\) maximal with \(q^k\le\alpha/(2L\delta)\). Then \(C^\delta\ll_\delta w^{\alpha/2}\), enough to absorb the constants as \(w\to\infty\). This gives infinitely many distinct heights with \(\gg_\alpha\delta^{-\log_q A}\) qualifying pairs. Since \(A>q^3\), this proves the proposition.

## The same criterion with square heights and square smaller addends

Define \(B_{\mathrm{sq}}(\delta)\) by counting only square heights \(C=u^2\) and square smaller addends \(v^2\) with \(1\le v\le u/2\), and then taking the limsup over \(u\). The same proposition, with the same exponent \(s>3\), holds for \(B_{\mathrm{sq}}\). Indeed, take the \(N_{2\delta'}(u)\) distinct smaller addends \(v\) at a common height \(u\), and form
\[
 v^2+(u-v)(u+v)=u^2 .
\]
Each pair remains primitive, its square addend determines \(v\), and its radical is at most \((u+v)\operatorname{rad}(uv(u-v))\). Its ratio of height to radical therefore exceeds \(u^{2\delta'}/2\). Choose \(\delta'=2\delta\); for sufficiently large \(u\) this exceeds \((u^2)^\delta\). The constant rescaling of \(\delta\) preserves the multiplicity exponent. In particular it would suffice to prove that for all sufficiently small fixed \(\delta>0\)
\[
 \limsup_{u\to\infty}
 \#\{1\le v\le u/2:\gcd(u,v)=1,\ \operatorname{rad}(uv(u-v)(u+v))\le u^{2-2\delta}\}
 \ll \delta^{-3}
\]
with an absolute implied constant. The argument for any fixed integer power \(m\ge2\) replaces \(u+v\) by \((u^m-v^m)/(u-v)\le m u^{m-1}\).

For a finite illustration take \(u=243\) and \(C=59049\). The values \(v=1,7,13\) give square smaller addends \(1,49,169\), with respective radicals \(4026,12390,8970\). All three qualify at \(\delta=1/10\).

## An upper bound on average over heights

For fixed \(0<\delta<1\) an elementary count gives
\[
 \sum_{C\le X}N_\delta(C)\le X^{1-\delta+o(1)} .
\]
Each counted triple has radical \(d\le X^{1-\delta}\). Its three entries are pairwise coprime, so each of the \(r\) primes in \(d\) has three possible assignments. Since \(d\ge(r+1)!\), one has \(r=O(\log X/\log\log X)\). The sum of all its positive exponents is at most \(3\log_2 X\), since the product of the three entries is at most \(X^3\). The number of exponent vectors is bounded by \(\binom{\lfloor3\log_2 X\rfloor}{r}\). The logarithm of this binomial coefficient times \(3^r\), meaning \(\log(3^r\binom{\lfloor3\log_2 X\rfloor}{r})\), is \(O((\log X)(\log\log\log X)/\log\log X)\). Summing over \(d\) proves the bound. This allows individual heights with many pairs arbitrarily far apart.

## What the counting criterion leaves open

The argument needs a bound on \(B(\delta)\) at fixed \(\delta\). Even the superficially similar upper bound \(\sup_C N_\delta(C)=O(\delta^{-3})\) is false. For an elementary example, fix \(m\) distinct odd primes other than 3, of product \(P\). Choose \(e\) with \(3^{e-1}\ge8P\) and put \(L=\varphi(3^e)\). For a multiple \(k\) of \(L\) let \(T=2^k,\ C=T^2\). There are \(\gg_m k^m\) products \(d=\prod p_i^{Lj_i}\le T/4\), by letting each nonnegative exponent \(j_i\) vary over a box of side proportional to \(k\). The identity
\[
 (T-d)^2+d(2T-d)=T^2
\]
is primitive. Its square addend exceeds \(C/2\) and determines \(d\). Fermat–Euler gives \(3^e\mid T-d\). Hence the radical is at most \(2P(T-d)(2T-d)/3^{e-1}\le C/2\). At \(\delta=1/(2k)\) these triples all qualify. Choosing \(m>3\) disproves the upper bound with a supremum. Here \(\delta\) decreases as \(C\) increases. Establishing even the weaker bound on the limsup at fixed \(\delta\) remains open.
