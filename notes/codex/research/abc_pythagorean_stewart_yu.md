# A one-fifth exponent for all primitive Pythagorean triples

Let $A,B,C$ be positive, coprime squares with $A+B=C$, and write $R=\operatorname{rad}(ABC)$. Then
$$
                        \log C\ll R^{1/5}(\log(2R))^3.                    \tag{1}
$$
The constant is absolute and effective. The abc conjecture restricted to these triples is equivalent to rational abc. This last assertion concerns the bound $C\ll_\varepsilon R^{1+\varepsilon}$.

## Ten applications of a bound for primitive sums

The primitive Pythagorean parametrization, after exchanging the two legs if needed, gives
$$
 \sqrt{A}=u^2-v^2,\quad \sqrt{B}=2uv,\quad \sqrt{C}=s=u^2+v^2
$$
for coprime integers $u>v>0$ of opposite parity. Put $m=u-v$, $h=u+v$. Then $R=\operatorname{rad}(2uvmhs)$. An odd prime of $R$ divides exactly one of the five factors $u,v,m,h,s$. For example, modulo an odd prime dividing $u-v$ or $u+v$ one has $s\equiv2u^2\ne0$; also $\gcd(m,h)=1$ since they are odd.

Use the following six primitive sums with the indicated multiplicities. The last column records which factors can supply their odd primes.

| Sum | Multiplicity | Factors |
|---|---:|---|
| $v+m=u$ | 1 | $v,m,u$ |
| $u+v=h$ | 1 | $u,v,h$ |
| $m+2v=h$ | 1 | $m,v,h$ |
| $m+h=2u$ | 1 | $m,h,u$ |
| $u^2+v^2=s$ | 3 | $u,v,s$ |
| $m^2+h^2=2s$ | 3 | $m,h,s$ |

Coprimality follows from that of $u,v$, the oddness of $m,h$, and $\gcd(m,h)=1$. Each odd prime in $R$ occurs exactly six times among the ten radicals, while 2 occurs in all ten. Their product is precisely $16R^6$. The smallest radical is thus at most $2^{2/5} R^{3/5}$. In every row the largest term is at least $u$, and $C=s^2\le4u^4$. Apply Stewart and Yu's effective estimate $\log z\ll \operatorname{rad}(xyz)^{1/3}(\log(2\operatorname{rad}(xyz)))^3$ to the row with the smallest radical. This proves (1). C. L. Stewart and K. Yu, *On the abc conjecture, II*, Duke Math. J. **108** (2001), 169–181, Theorem 1.

At $(u,v)=(2,1)$, the triple is $9+16=25$ and $R=30$. The radical product is $2\cdot6^3\cdot10^3\cdot30^3=16\cdot30^6$.

## Transfer to any primitive input

Start with $x+(z-x)=z$, $0<x<z$, $\gcd(x,z)=1$, and $R_0=\operatorname{rad}(x(z-x)z)$. The Pythagorean triple $(2xz,z^2-x^2,z^2+x^2)$ has common gcd $g=1$ for opposite parities and $g=2$ if both $x,z$ are odd. Divide each coordinate by $g$ and square. The resulting primitive triple of squares has height $C'\ge z^4/4$ and radical
$$
 R'\le R_0(x+z)(z^2+x^2)\le 4R_0z^3.
$$
Here $2\mid R_0$, so the factor 2 in the first leg needs no extra coefficient. A bound $C'\ll_\eta(R')^{1+\eta}$ for these triples gives $z^{1-3\eta}\ll_\eta R_0^{1+\eta}$. Taking $\eta=\varepsilon/(4+3\varepsilon)$ gives ordinary abc. In contrast, (1) gives an upper bound for $\log z$ with a factor $z^{3/5}$ after this substitution. [Earlier transfer for square triples](abc_elliptic_quartics.md) · [Arbitrary numbers of marked rational points](abc_marked_rational_radical_bounds.md)
