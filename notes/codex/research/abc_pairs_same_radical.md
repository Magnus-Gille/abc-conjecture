# Two close abc triples with the same radical

There are infinitely many pairs of distinct primitive positive triples whose largest terms \(C_1>C_2\) and common radical \(R_*\) satisfy, for absolute constants \(k_1,k_2>0\),
\[
 0<\frac{C_1}{C_2}-1\le e^{-k_1\sqrt{\log C_2}},\qquad
 \frac{C_2}{R_*}\ge
 \exp\!\left(k_2\frac{\sqrt{\log C_2}}{\log\log C_2}\right).
 \tag{1}
\]
Here the radical of a triple is the product of all distinct primes in its three entries. The two triples even match prime supports entry by entry after a suitable ordering. The proof is an elementary consequence of two exact transformations and a counting argument for smooth integers. No assertion of priority is made.

## Exact transfer from any seed

Start with primitive \(a+b=c\), \(a>b>0\), and \(R=\operatorname{rad}(abc)\). Put
\[
 h=\gcd(3,a-b),\qquad U=(a-b)/h,\quad V=(a+2b)/h,\quad W=(2a+b)/h.
\]
Then \(U+V=W\) and \(U,V,W\) are pairwise coprime, since the gcd of any two undivided forms is exactly \(h\). The operation on the sorted addends is an involution: for the companion seed \(V+U=W\), its normalized three forms are \(b,a,c\) in this order.

Polynomial expansion gives the two identities
\[
 bW^3+cU^3=aV^3=C_1,\qquad
 Wb^3+Uc^3=Va^3=C_2.                                                       \tag{2}
\]
To see that the first is primitive, a prime dividing both \(aV^3\) and \(bW^3\) would have to divide \(a,b\), or \(V,W\), or \(a,W\), or \(b,V\). In the last two cases the unnormalized linear forms show that it divides \(a,b\) as well. The second follows by the involution. Corresponding entries have the same prime supports. Precisely one prime, 2, divides both \(abc\) and \(UVW\): for each odd prime in \(a,b,c\) reduce the undivided three forms modulo that prime, and observe that \(h\) is odd for the parity check. Thus
\[
 R_*=\frac{R\operatorname{rad}(UVW)}2,\qquad
 \frac{C_1}{C_2}=\left(\frac{a+2b}{ha}\right)^2.
\]
The two heights are always distinct for \(0<b/a<1\). Write \(z=b/a\). Using \(\operatorname{rad}(UVW)\le UVW\) gives
\[
 \frac{C_1/R_*}{c/R}
 \ \ge\ \frac{2(1+2z)^2}{(1+z)(2+z)(1-z)}>1.
\]
Subtracting the denominator from the numerator yields \(7z+10z^2+z^3>0\). The companion height is within a factor nine of this one, and both heights are \(\asymp c^4\). For example \(2+1=3\) gives \(125+3=128\) and \(5+27=32\), both with radical 30.

There is also a direct infinite iteration. If \(abc=D u^3\) with \(D\) cube-free, the first output has product \(D(uUVW)^3\), so it preserves \(D\) and multiplies \(u\) by an even integer at each step. Sorting the addends permits iteration. Heights grow, since \(C_1\ge c^4/54>c\) for \(c\ge4\), and \(c=3\) was checked above. At the \(n\)-th step,
\(\operatorname{rad}(D u_n^3)\le\operatorname{rad}(D)\,u_n/2^{n-1}\) and \(c_n/u_n\ge(4D)^{1/3}\). As \(\log c_n=O_{c_0}(4^n)\), this proves \(c_n/\operatorname{rad}(a_n b_n c_n)\gg_{c_0}\sqrt{\log c_n}\) for every starting triple with \(c_0>2\). The strict increase in the ratio gives no fixed positive exponent by itself.

## Simultaneously forcing closeness and small radical

Use the first \(k\) primes other than 3, written \(p_1,\ldots,p_k\). Let \(M=2p_k\), and form all products \(\prod p_i^{e_i}\) with \(0\le e_i\le M\). Their \(N=(M+1)^k\) logarithms are distinct and lie between 0 and \(L=M\sum\log p_i\). At least \(N/2\) products share a nonzero residue mod 3. Ordering their logarithms yields two integers \(P>Q\) with
\[
 0<\log(P/Q)\le 3L/N
\]
for sufficiently large \(k\). Set \(d=\gcd(P,Q)\), \(a=Q/d,\ b=(P-Q)/d,\ c=P/d\). They form a primitive triple. The ratio \(z=b/a\ll L/N\) tends to zero, and \(3\mid b,\ 3\nmid a\), which makes \(h=1\). Since its radical is at most \(b\prod p_i\),
\[
 \frac{c}{R}\ge \frac{P}{(P-Q)\prod p_i}
 \ge\frac{N}{3L\prod p_i}\ \ge\ \frac{2^k}{3L}.
\]
Use (2). The height ratio is \((1+2z)^2\), and \(C_2/R_*\gg c/R\). The elementary prime estimates \(k\ll p_k\ll k\log(2k)\) give \(L\ll k^2(\log k)^2\), while \(\log N\gg k\log k\). Also \(\log C_2\ll L\). Consequently \(z\le\exp(-\Omega(\sqrt{\log C_2}))\) and \(k\gg\sqrt{\log C_2}/\log\log C_2\). The lower bound \(2^k/(3L)\to\infty\) forces unbounded heights. This proves (1).

For comparison, one can force a relative height difference of order \(C_2^{-1/4}\) with a logarithmic radical saving. Take \(c=2^n,\ a=c-1,\ b=1,\ n=2\cdot3^j\). Then \(3\mid a,\ h=1\), and \(v_3(2^n-1)=j+1\) by lifting the exponent. Therefore \(c/R\ge 3^j/2\), while \(C_1/C_2=((c+1)/(c-1))^2\). This supplies a fixed power in the height difference. To disprove abc one needs a fixed power in \(C_i/R_*\), a different quantity.

## The common radical always separates at the second step

Apply (2) again to each of the two output triples. The two children on the first branch share one radical, and those on the second branch share another. These two radicals **always differ**, for every primitive \(a>b>0\).

For a calculation invariant under reordering, put \(t=a/b\) and consider the signed triple ratio (permuting the three signed terms of sum zero is allowed). One of the ratios for the first output is
\[
 T(t)=-t(t+2)^3/(2t+1)^3 .
\]
It satisfies \(T(1/t)=1/T(t)\) and \(T(-1-t)=-1-T(t)\), so changing the order permutes its output. The companion input has ratio \(J(t)=(t+2)/(t-1)\), hence the first-level branches are \(T(t), T(J(t))\).

Outside 2 and 3 every prime occurring in a second-step companion linear form is new to its branch, by the exact prime-support calculation above. Inserting the numerator and denominator of \(T\) into the three linear forms shows that these new primes are the prime divisors (outside 2,3) of the following three quartics, homogenized at \((a,b)\):
\[
\begin{split}
 f_1(t)&=t^4-10t^3-12t^2-4t-2,\\
 f_2(t)&=t^4+14t^3+24t^2+14t+1,\\
 f_3(t)&=2t^4+4t^3+12t^2+10t-1.
\end{split}
\]
The corresponding forms for the second branch are the primitive numerators of \(f_i(J(t))\), up to sign. In a convenient order these are
\[
 g_1=t^4+2t^3-4t-2,\quad g_2=t^4+2t^3+2t+1,\quad
 g_3=2t^4+4t^3-2t-1 .
\]
Only powers of 3 can come from the determinant of \(J\) or from normalizing \(T\). The absolute resultants \(|\operatorname{Res}(f_i,g_j)|\) in this order are \(82944=2^{10}3^4\) on the diagonal and \(43659=3^4\cdot7^2\cdot11\) elsewhere. The two first-level radicals coincide. Hence if the second-level radicals also coincided, every prime in any \(f_i(a,b)\) would belong to \(\{2,3,7,11\}\): an outside prime would need to occur in some \(g_j(a,b)\), giving a projective common zero modulo that prime.

None of the \(f_i\) has a projective root modulo 7. Modulo 11 their affine root sets are respectively \(\{4,8\},\ \{2,6\},\ \{3,7\}\), and there is no root at infinity. Thus at most one of \(f_2(a,b),f_3(a,b)\) is divisible by 11. On primitive pairs neither form vanishes modulo 4 or 81. These small modular facts can all be checked by the exact code below. It follows that at least one of the two positive integers \(f_2(a,b), f_3(a,b)\) is at most \(2\cdot27=54\). Yet for \(a\ge b+1,\ b\ge1\) they are at least 253 and 131 respectively, as is seen by substituting \(a=b+j,\ j\ge1\). This proves the separation claim.

~~~python
from math import gcd
from sympy import Poly, resultant, symbols
t = symbols("t")
f = [t**4-10*t**3-12*t**2-4*t-2,
     t**4+14*t**3+24*t**2+14*t+1,
     2*t**4+4*t**3+12*t**2+10*t-1]
g = [t**4+2*t**3-4*t-2, t**4+2*t**3+2*t+1, 2*t**4+4*t**3-2*t-1]
assert all(abs(resultant(F,G,t)) == (82944 if i==j else 43659)
           for i,F in enumerate(f) for j,G in enumerate(g))
def value(F,a,b):
    return sum(int(c)*a**i*b**(4-i) for (i,),c in Poly(F,t).terms())
for q in (4,81):
    assert all(value(F,a,b)%q for F in f[1:]
               for a in range(q) for b in range(q) if gcd(gcd(a,b),q)==1)
for p,expected in [(7,[[],[],[]]),(11,[[4,8],[2,6],[3,7]])]:
    assert [[a for a in range(p) if value(F,a,1)%p==0] for F in f]==expected
    assert all(value(F,1,0)%p for F in f)
~~~
