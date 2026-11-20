# What field discriminants detect in an abc triple

Take positive coprime integers \(a+b=c\). For an odd prime \(\ell\ge5\) put
\[
R=\operatorname{rad}(abc),\qquad
R_\ell=\prod_{\substack{p\mid abc\\\ell\nmid v_p(abc)}}p,\qquad
K=\mathbb Q\!\left(\sqrt[\ell]{ab/c^2}\right),\qquad
d(K)=\frac{\log|\operatorname{Disc}(K)|}{[K:\mathbb Q]}.
\]
The positive real root specifies the embedding. All logarithms are natural. The following two inequalities hold for every triple. The constants shown are independent of the triple and of \(\ell\).
\[
0\le d(K)-(1-1/\ell)\log R_\ell\le\log\ell,
\qquad
0\le\log R-\log R_\ell\le\frac{3}{\ell}\log c. \tag{1}
\]

## Local calculation

Write \(q=ab/c^2\). By coprimality the exponent of \(q\) at a prime dividing \(a,b,c\) is respectively \(v_p(a),v_p(b),-2v_p(c)\). As \(\ell\) is odd, the primes where this exponent is nonzero modulo \(\ell\) are precisely those in \(R_\ell\).

If \(R_\ell=1\), then \(q\) is a rational \(\ell\)-th power and \(K=\mathbb Q\). Otherwise choose \(p\mid R_\ell\). For a place of \(K\) over \(p\) with ramification index \(e\), the equality \(\ell v_{\mathfrak p}(\sqrt[\ell]{q})=e v_p(q)\) forces \(\ell\mid e\). Since \([K:\mathbb Q]\le\ell\), the degree is exactly \(\ell\) and \(p\) is totally ramified. At \(p\ne\ell\) this is tame and the discriminant exponent is \(\ell-1\). At \(p\nmid\ell R_\ell\) the generator can be multiplied by an integral power of \(p\) to make its \(\ell\)-th power a local unit. The resulting monic binomial has unit discriminant at \(p\), so the field is unramified.

For the upper bound at \(\ell\), multiply \(q\) by a rational \(\ell\)-th power to obtain a positive integer \(u\) with each exponent in \(\{0,\ldots,\ell-1\}\). If \(\ell\nmid R_\ell\), then \(u\) is a unit at \(\ell\). The polynomial discriminant of \(x^\ell-u\) has valuation \(\ell\) there, bounding the field discriminant valuation. If \(\ell\mid R_\ell\), first replace \(q\) by \(q^k\) with \(kv_\ell(q)\equiv1\bmod\ell\). This generates the same field since \(\gcd(k,\ell)=1\). Normalization now gives \(v_\ell(u)=1\), so the polynomial discriminant has valuation \(2\ell-1\). Total ramification gives the lower bound \(\ell-1\) for the field discriminant exponent. These bounds prove the first inequality in (1). Each prime omitted from \(R_\ell\) divides \(abc\) to at least its \(\ell\)-th power. Taking their product and using \(abc\le c^3\) proves the second.

For example, \(1+32=33\) has \(R=66\), \(R_5=33\) and \(u=33^3\). Its quintic field has discriminant \(3{,}706{,}003{,}125=33^4\,5^5\). As an arithmetic check, PARI's field-discriminant routine verified (1) for exponents 5 and 7 on 196 primitive triples, including every triple with \(c\le35\).

## The quantitative question

Let \(\rho=\liminf_{c\to\infty}\log R/\log c\) over primitive positive triples and let \(\lambda_\ell=\liminf_{c\to\infty}d(K)/\log c\) over the same triples. The family \(1+(2^j-1)=2^j\) has \(R<2c\), hence \(\rho\le1\). Rational abc is equivalent to \(\rho=1\), by absorbing the finitely many triples below a height threshold into the abc constant. Formula (1) gives
\[
0\le \rho-\frac{\lambda_\ell}{1-1/\ell}\le\frac3\ell.
\]
In particular abc is equivalent to \(\lambda_\ell\to1\) as the primes \(\ell\) tend to infinity. Each \(\liminf\) here takes the height to infinity with \(\ell\) fixed.

There is an unconditional growth statement at each fixed \(\ell\). The smooth projective model \(C_\ell\) of \(z^\ell=t(1-t)\) is a degree-\(\ell\) cover of the line, totally ramified at \(0,1,\infty\) and unramified elsewhere. Riemann–Hurwitz gives genus \((\ell-1)/2\ge2\). The point with \(t=a/c\) and \(z=\sqrt[\ell]{q}\) is defined over \(K\). Hermite's finiteness theorem leaves only finitely many fields of degree at most \(\ell\) and bounded absolute discriminant. Each of these fields has only finitely many points on \(C_\ell\) by Faltings' theorem. The reduced fraction \(a/c\) determines the triple. Consequently both \(d(K)\) and \(R_\ell\) tend to infinity along every sequence with \(c\to\infty\). This argument supplies no positive lower bound on \(\lambda_\ell\).

One can compute the slope a conjectural height theorem would give. For the covering map \(\pi\), Riemann–Hurwitz gives \(K_{C_\ell}\sim_{\mathbb Q}(1-3/\ell)\pi^*\mathcal O(1)\). Indeed the ramification divisor is \((\ell-1)\) times the three ramification points and each of those points multiplied by \(\ell\) is a full fiber. The bounded-degree form of Vojta's conjecture, applied with empty divisor, would therefore give
\[
d(K)\ \ge\ (1-3/\ell-\eta)\log c-O_{\ell,\eta}(1)
\]
for every \(\eta>0\), with finitely many exceptional points absorbed into the constant. Inserting this into (1) and letting \(\ell\) increase would give abc. This lower bound is conditional. The 2026 abstract of Han, Luo and Yu bounds the number of cosets covering an intersection with a finite-rank group. That conclusion allows a single point of arbitrarily large height as the field varies. [Han, Luo and Yu](https://arxiv.org/abs/2609.17233)

## Two unconditional exclusions

For every prime \(\ell\equiv1\bmod4\), the only primitive positive triple with \(R_\ell\) supported on \(\{2\}\) is \(1+1=2\). Indeed the two odd terms are \(\ell\)-th powers and the even term is \(2^\alpha\) times an odd \(\ell\)-th power, where \(\alpha\ge1\). Since \(\ell\) is odd, signs can be placed on the roots to get \(A^\ell+2^\alpha B^\ell+C^\ell=0\). Ribet's theorem excludes \(\alpha>1\) and, for these primes, gives only the trivial solutions for \(\alpha=1\). [Ribet, *On the equation \(a^p+2^\alpha b^p+c^p=0\)*](https://arxiv.org/abs/math/9508208)

For triples \(1+n=n+1\), if \(R_5\) is supported on \(\{2,3\}\), the complete list is \(n=1,2,3,8\). To see why the calculation is exhaustive, write \(n=B u^5,\ n+1=C v^5\) with \(B,C\) fifth-power-free. Each of 2 and 3 can be absent from both coefficients, or enter exactly one of them with exponent \(1,2,3,4\). This gives 81 ordered coefficient pairs. The pair \(B=C=1\) gives no positive solution since consecutive positive fifth powers differ by at least 31. The remaining 80 equations are \(C v^5-B u^5=1\). The code below enumerates all their positive solutions using PARI's unconditional certification flag. It uses the Python package cypari. [PARI documentation for thueinit and thue](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#thueinit)

~~~python
from itertools import product
from cypari import pari

assign = [(0, 0)] + [(e, 0) for e in range(1, 5)] + [(0, e) for e in range(1, 5)]
found = set()
for (i, j), (k, l) in product(assign, repeat=2):
    B, C = 2**i * 3**k, 2**j * 3**l
    if B == C:
        continue
    for v, u in pari(f"thue(thueinit({C}*x^5-{B},1),1)"):
        v, u = int(v), int(u)
        if min(v, u) > 0:
            n = B * u**5
            assert n + 1 == C * v**5
            found.add(n)
assert sorted(found) == [1, 2, 3, 8]
~~~

These exclusions allow arbitrary height but prescribe the primes that appear to exponents indivisible by \(\ell\). For general triples those primes vary. A lower bound for their product with the required height exponent, or an infinite family violating such a bound for a fixed positive exponent, remains unresolved here.
