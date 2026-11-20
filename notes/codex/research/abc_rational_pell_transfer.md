# A rational Pell family captures the full abc conjecture

The integer equation \(y^2-2x^2=1\) yields a [test for repeated prime factors of Pell numbers](abc_two_small_legs_and_pell_radicals.md). Allow rational solutions and clear denominators. For every fixed positive multiple \(k\) of four, rational abc is equivalent to its restriction to the following triples:

* The triple is \(X^4+(YD)^2=U^2\), with \(X,Y,D\) nonzero coprime in pairs, \(U=X^2+D^2\), and \(Y^2=2X^2+D^2\).
* The same \(U\) is the hypotenuse of a second, distinct primitive triangle, with legs \(2|XD|,\ |X^2-D^2|\).
* There is a positive integer \(L\) with \(U=L^k V\), \(\gcd(L,V)=1\), and \(L^k\asymp V\). The comparison constants can be absolute. In particular \(\operatorname{rad}(U)\ll U^{1/2+1/(2k)}\).

The following proof constructs a subfamily satisfying all three properties. The transfer controls the abc ratio of the triangle whose even leg is \(X^2\).

One can express the same equivalence as a single inequality in two integers. For every \(\eta>0\), is there a \(c_\eta>0\) such that, for all nonzero coprime \(s,t\) with \(s\) odd and \(t\) even,
\[
 \operatorname{rad}\!\left(\left|2st(s^8-16t^8)\right|\right)
 \ \ge\ c_\eta\max(|s|,|t|)^{\,8-\eta}\,?
\]
The radical is exactly that of the constructed triangle, since \(XDYU=2st(s^8-16t^8)\), and its height \(U^2=(s^4+4t^4)^2\) is comparable to \(\max(|s|,|t|)^8\). Thus abc implies the displayed statement for every such pair, and the transfer below proves the converse.

## Transfer of the fixed exponent

Start with positive coprime integers \(A+B=C\) and let \(R=\operatorname{rad}(ABC)\). Take the even entry and either odd entry as \(a,b\), and write \(h=\max(a,b)\). Then \(C/2\le h\le C\), and \(ab(a^2-b^2)\) is a multiple, up to sign, of \(ABC\). Its other factor is either \(|a-b|\) or \(a+b\), at most \(2h\). Put
\[
 L=a^2+b^2,\qquad H+iT=(a+ib)^k,\qquad s=H+T,\qquad t=T .
\]
Both \(H\) and \(s\) are odd, \(T\) is even and nonzero, and \(\gcd(s,t)=1\). Indeed, \(a+ib\) and \(a-ib\) are coprime in the Gaussian integers, since a common prime would divide \(2a\) and \(2b\) and the norm \(L\) is odd. The same disjoint factorization excludes \(T=0\). Nonzero \(a,b\) of opposite parity are necessarily distinct.

For \(m=k/4\) and \(Z=(a+ib)^4\) the identity
\[
 T=4ab(a^2-b^2)\sum_{j=0}^{m-1} Z^{m-1-j}\overline Z^{\,j}
\]
follows by subtraction of conjugates. The sum is a rational integer of absolute value \(O_k(h^{k-4})\). Hence \(\operatorname{rad}(|T|)\ll_k R h^{k-3}\).

Now set
\[
 X=2st,\quad D=s^2-2t^2,\quad Y=s^2+2t^2,\quad
 U=s^4+4t^4=X^2+D^2 .
\]
Then \(Y^2=2X^2+D^2\). The odd integers \(D,Y\) are coprime to \(X\) and to each other, using \(\gcd(s,t)=1\) and \(s\) odd. These identities give the two primitive triangles in the statement. Their unique positive even legs are distinct, since equality \(X^2=2|XD|\) would force \(|X|=2|D|\), but \(4\mid X\) and \(D\) is odd.

The factorization
\[
 U=\big((s-t)^2+t^2\big)\big((s+t)^2+t^2\big)
   =L^k V,\qquad V=(s+t)^2+t^2
\]
has coprime factors. Both are odd and their difference is \(4st\), which is coprime to either factor at odd primes. They are positive definite quadratic forms in \(H,T\), so \(V\asymp H^2+T^2=L^k\). In particular \(U^2\asymp_k h^{8k}\).

For the squared triple of height \(U^2\), let \(R'=\operatorname{rad}(|XDY|U)\). From \(|s|\ll_k h^k,\ |DY|\ll_k h^{4k},\ V\ll_k h^{2k},\ L\le2h^2\) we obtain
\[
 R'\le 2\,|s|\operatorname{rad}(|T|)\,|DY|\,L V
       \ll_k R h^{8k-1}.
\]
Consequently \(U^2/R'\gg_k C/R\). If \(C/R\ge C^\delta\) along an unbounded sequence for one fixed \(\delta>0\), the images satisfy \(U^2/R'\ge (U^2)^{\delta/(16k)}\) for all sufficiently large heights. This is an infinite sequence of primitive fixed-exponent violations. The converse holds because each output is itself a rational abc triple. The construction transfers a failure if one exists.

## Why the denominator matters

The denominator of the rational Pell coordinate \(X/D\) is \(|D|\) in lowest terms. For this transfer, every \(\eta>0\) gives
\[
 |D|\gg_{k,\eta} h^{2k-2-\eta}.
\]
Indeed \(D=H^2+2HT-T^2\) is a homogeneous binary form of degree \(2k\) with simple real projective roots. Writing \(a+ib=\sqrt L e^{i\theta}\) gives \(D=L^k(\cos(2k\theta)+\sin(2k\theta))\), which proves simplicity. There is no root at infinity or at a rational slope: \(D=0\) would give \(s^2=2t^2\), and \(H,T\) cannot vanish together. Thus every root is a real algebraic irrational. Away from the roots, compactness gives \(|D|\gg_k h^{2k}\); near any root \(\xi\) in the coordinate \(a/b\), one has \(b\asymp_k h\) and \(|D|\asymp_k h^{2k}|a/b-\xi|\). Roth's theorem gives the stated lower bound. Its constant is ineffective. In particular the transfer does not put arbitrary hypothetical violations on the integer slice \(|D|=1\).

There is also a degree constraint on reducing \(\operatorname{rad}(U)\) by polynomial factorization. For a nonconstant rational function \(s/t\) of degree \(d\) on the projective line, the four roots of \(z^4+4\) have at least \(4d-(2d-2)=2d+2\) distinct inverse images, by Riemann–Hurwitz. In this construction \(d=k\) and equality holds. In the coordinate \(a/b\), the functions \(H+iT\) and \(H-iT\) are \((a+ib)^k\) and \((a-ib)^k\). Their ratio is a power of a Möbius transformation. Composing with another Möbius transformation gives \(s/t=1+H/T\), with its two totally ramified values \(1+i\) and \(1-i\). Both satisfy \(z^4+4=0\). Thus the exponent \(1/2+1/(2k)\) corresponds exactly to the reduced degree of this divisor relative to its full degree \(4k\). This geometric count permits further arithmetic repetitions at special inputs.

## An unconditional count for the octic inequality

Fix \(0<\eta<1\). Among admissible pairs with \(H<\max(|s|,|t|)\le 2H\), the number satisfying
\[
 \operatorname{rad}(|2st(s^8-16t^8)|)<\max(|s|,|t|)^{8-\eta}
\]
is \(O_{\eta,\sigma}(H^{5/3-\eta/6+\sigma})\) for every \(\sigma>0\). In particular these exceptions have density zero among the admissible pairs.

Indeed the six absolute values of
\[
 s,\quad t,\quad s^2-2t^2,\quad s^2+2t^2,\quad
 (s-t)^2+t^2,\quad(s+t)^2+t^2
\]
are coprime in pairs. For the four odd factors this follows from \(\gcd(D,Y)=\gcd(DY,U)=1\) and from \(\gcd((s-t)^2+t^2,(s+t)^2+t^2)=1\) as above. Each is coprime to \(st\). The extra 2 in the radical already divides \(t\). Write \(d=1\) for a linear factor and \(d=2\) for a quadratic one. At least one of the six values has radical at most \((2H)^{d-\kappa}\), where \(\kappa=(2+\eta)/6\), since the degrees sum to ten.

For each \(\alpha>0\), there are \(O_\alpha(Z B^\alpha)\) integers \(n\le B\) of radical at most \(Z\). Bound their count by \(Z B^\alpha\sum_{n\ge1}n^{-\alpha}/\operatorname{rad}(n)\); the Euler product has local factors \(1+1/(p(p^\alpha-1))\) and converges. A linear factor takes \(O_\alpha(H^{1-\kappa+\alpha})\) qualifying absolute values, each allowing \(O(H)\) choices for the other coordinate. Each quadratic factor takes \(O_\alpha(H^{2-\kappa+2\alpha})\) qualifying absolute values.

For the latter, each particular value \(n\ge1\) has \(H^{o(1)}\) representations in this box. The four forms are norms in the fixed fields \(\mathbb Q(\sqrt2),\mathbb Q(\sqrt{-2}),\mathbb Q(i)\). An element of absolute norm \(n\) generates one of at most \(\tau(n)\) ideals of norm \(n\), by prime ideal factorization in a quadratic field. In the imaginary fields each principal ideal has a bounded number of generators. In the real field, the two conjugates have absolute value \(O(H)\), so the first has absolute value between a constant times \(1/H\) and a constant times \(H\). The powers of a fixed fundamental unit allow \(O(\log(2H))\) generators in that interval. Each element determines the coordinates of the corresponding form. Since \(n=O(H^2)\), the divisor bound completes the count. Its exponent still permits infinitely many exceptions at one fixed \(\eta\).

As an arithmetic check, there are 53,258 coprime positive pairs with \(s\) odd, \(t\) even and \(\max(s,t)\le512\). At \(\eta=1/5\), exactly 61 satisfy the displayed strict inequality, including 23 of the 39,926 pairs with \(256<\max(s,t)\le512\). These counts use a sieve for the six separate radicals and the exact integer comparison \(R'^5<\max(s,t)^{39}\). The conjectured lower bound permits a constant \(c_\eta\), so the finite exceptions to the inequality with constant one do not settle it.
