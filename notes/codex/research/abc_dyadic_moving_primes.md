# A bound at the rational target 1 with varying prime divisors

Let \(u,v\) be different coprime positive odd integers, \(h=\max(u,v)\), \(H=\log h\), and \(P=\operatorname{rad}(uv)\). A sufficient condition for an abc disproof is that \(2^{v_2(u-v)}\ge P h^\eta\) at unbounded heights for one fixed \(\eta>0\). Indeed the radical of the associated primitive triple is at most \(2P|u-v|/2^{v_2(u-v)}\). The following restrictions concern these actual integers. All logarithms are natural. [Earlier congruence construction](abc_smooth_congruences.md)

* For every fixed \(0<\delta<1\), uniformly when \(P\le H^{1-\delta}\),
  \[
  v_2(u-v)\log 2\le H^{1-\delta+o(1)}.
  \]
  In particular \(2^{v_2(u-v)}=h^{o(1)}\) in this range.
* Write \(r\) for the number of **distinct positive exponents** in the prime factorization of \(uv\). If \(P\le H^A\) for a fixed \(A>0\), then any sequence of the proposed exceptions must have
  \[
  r\ge (1-o(1))\,\frac{\log H}{\log\log H}.
  \]
  If \(r\le k\) for a fixed integer \(k\ge1\), every such exception at large height requires \(\log P\gg_{\eta,k}(H/\log H)^{1/k}\), even without the assumption \(P\le H^A\).
* If \(r=1\), the dyadic construction cannot yield a fixed positive exponent at unbounded height, with no restriction at all on \(P\). Here \(u=U^m,\ v=V^m\) for squarefree \(U,V\), with \(P=UV\). For odd \(m\), the power of two dividing \(u-v\) is that dividing \(U-V\). For even \(m\), the lifting formula gives \(2^{v_2(u-v)}=2^{v_2(m)}\max(2^{v_2(U-V)},2^{v_2(U+V)})\), since one of \(U-V,U+V\) has valuation 1. In either case \(2^{v_2(u-v)}/P\le m(U+V)/(UV)\le2m=O(\log h)\).

## Dependence on the prime and on the number of exponents

The input is Kunrui Yu's Theorem 1 in *\(p\)-adic logarithmic forms and group varieties III*, Forum Math. 19 (2007), 187–280. We use its explicit dependence on rank. Alvarado and coauthors restate the bound and give the auxiliary-field argument. The formulas for \(C_1^*\) and the height product can also be inspected in SageMath. [Alvarado et al.](https://arxiv.org/abs/1903.00977) · [SageMath formulas](https://github.com/sagemath/sage/blob/develop/src/sage/rings/number_field/S_unit_solver.py#L462-L607)

The following convenient upper bound applies to either parity of the inputs. Write \(L=\log P\). For a prime \(q\nmid uv\), put \(f=1\) if \(q\equiv1\bmod4\) and \(f=2\) otherwise. There is an absolute constant \(D\ge2\) such that
\[
v_q(u^2-v^2)\log q
\ \le\ q^f(r+1)^D(1+\log q)^D
       [D(1+L/\log q)]^r\,\log(3+H). \tag{1}
\]
It also bounds either \(v_q(u-v)\log q\) or \(v_q(u+v)\log q\).

To verify this specialization, group primes according to their exponent in \(uv\). For each exponent \(e\) let \(w_e\) be the product of its primes in \(u\) divided by the product of its primes in \(v\). The \(r\) rational numbers \(w_e\) are multiplicatively independent because their nonempty prime supports are disjoint. Their absolute logarithmic heights have sum at most \(L\). Apply Yu's theorem to \(\Theta=\prod_e w_e^{2e}=(u/v)^2\ne1\), allowing an additional torsion generator \(-1\) with exponent 2. The coefficient bound can be taken as \(\max(3,2H/\log2)\). Since \(q\nmid uv\), \(v_q(\Theta-1)=v_q(u^2-v^2)\).

For odd \(q\) work in \(\mathbb Q(i)\); for \(q=2\) work in \(\mathbb Q(\zeta_3)\). The required auxiliary roots of unity are present. The chosen prime is unramified, the absolute degree is 2 and the residue degree is \(f\). In Yu's constant with \(n=r+1\), the rank factor \(n^n(n+1)^{n+1}/n!\) is at most \((Cr)^r(r+1)^C\) by Stirling, for an absolute \(C\). The residue and logarithm factors are \(q^f(d_K/(f\log q))^{n+2}\), up to constants bounded by \(C^r(r+1)^C(1+\log q)^C\). The torsion generator has modified height \(O(\log q/(n+4))\). The product of the ordinary heights of the independent \(w_e\) is at most \((L/r)^r\) by the arithmetic-geometric mean inequality. Even if each is replaced by its modified height, their product is at most \(((L+C\log q)/r)^r\). Multiplying these bounds, including the factor \(\log q\) on the left and the logarithm of the coefficient bound, gives (1). All constants here are independent of \(q,r,u,v\).

At \(q=2\), (1) gives \(v_2(u-v)\log2\le (r+1)^D[D'(1+L)]^r\log(3+H)\) with absolute \(D'\). Also \(r\le s=\omega(P)\), and \(s!\le P\) implies \(s\le(1+o(1))L/\log L\) as \(L\to\infty\). For \(P\le H^\alpha\) and fixed \(\alpha>0\), the resulting bound is \(H^{\alpha+o(1)}\), uniformly, including bounded \(L\). Setting \(\alpha=1-\delta\) proves the first assertion. Conversely a proposed exception requires \(v_2(u-v)\log2\ge\eta H+L\). Taking logarithms in (1) at \(q=2\) and using \(L\le A\log H\) gives the stated lower bound on \(r\). With \(r\le k\) fixed one instead obtains \(H\ll_{\eta,k} (1+L)^k\log(3+H)\).

## A consequence for genuine primitive sums

Let \(a+b=c\), with positive coprime \(a,b\), \(H=\log c\) and \(P=\operatorname{rad}(ab)\). Suppose \(P\le H^\alpha\) with fixed \(\alpha>0\). Then, for each fixed \(\beta>0\),
\[
\sum_{q\le H^\beta}v_q(c)\log q
\ \le\ H^{\max(\alpha,3\beta)+o(1)}. \tag{2}
\]
When the sum is restricted to \(q\equiv1\bmod4\), \(3\beta\) can be replaced by \(2\beta\). The asymptotics refer to \(c\to\infty\). Primes dividing \(ab\) do not divide \(c\). The only equal-addend primitive triple is \(1+1=2\).

To prove (2), apply (1) to \(u=a,v=b\). Its \(H\) can be enlarged to \(\log c\). Fix an auxiliary \(0<\gamma<\beta\). For \(q\le H^\gamma\) the bracket to the power \(r\) is at most \(H^{\alpha+o(1)}\), using the same factorial estimate as at 2. All polynomial factors in \(r,\log q,\log(3+H)\) cost \(H^{o(1)}\). Summing \(q^2\) in this first range gives \(H^{\alpha+3\gamma+o(1)}\). In the second range \(H^\gamma<q\le H^\beta\), one has \(L/\log q\le\alpha/\gamma\), so the bracket to the power \(r\) is \(H^{o(1)}\) since \(r=O_\alpha(\log H/\log\log H)\). Summing \(q^2\) gives \(H^{3\beta+o(1)}\). Let \(\gamma\) tend to zero after taking the limit superior of logarithmic exponents. Using \(q\) in place of \(q^2\) proves the progression-restricted claim.

In particular take \(\alpha<1,\ \beta<1/3\), both positive. If \(c/\operatorname{rad}(abc)\ge c^\eta\), then the repeated factors of \(c\) at primes \(q>H^\beta\) must satisfy
\[
\prod_{\substack{q>H^\beta\\q^2\mid c}}q^{v_q(c)-1}\ge c^{\eta-o(1)}.
\]
Indeed \(c/\operatorname{rad}(abc)=(c/\operatorname{rad}(c))/P\), and (2) bounds the logarithm of the entire contribution below the cutoff by \(o(H)\). Consequently abc holds on the subclass where \(P\le H^\alpha\) and every prime occurring at least twice in \(c\) is at most \(H^\beta\). Simple prime factors of \(c\) can be arbitrarily large. Neither (1) nor (2) supplies the necessary uniform estimate for all primitive triples.
