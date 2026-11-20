# A growing-degree polynomial identity with exponential real and dyadic gains

For every even \(n\ge2\), put \(x=2n+1\) and form the polynomials
\[
 U_0(X)=\prod_{j\ {\rm even}}(X+2j)^{\binom nj},\qquad
 V_0(X)=\prod_{j\ {\rm odd}}(X+2j)^{\binom nj}\qquad (0\le j\le n).
\]
Specialize at \(X=x\), divide the two values by their gcd, and call the resulting integers \(U,V\). Set \(C=\max(U,V)\), \(D=|U-V|\) and \(R=\operatorname{rad}(UVD)\). These are primitive positive triples from the identity \(U_0+(V_0-U_0)=V_0\). The proof below gives the simultaneous conclusions
\[
 \log(C/D)=(2\log2+o(1))n,\qquad
 v_2(D)=n+v_2((n-1)!),\qquad
 \log\operatorname{rad}(UV)=(10/3+o(1))n.
\]
Thus the difference has an explicit repeated-prime factor of exponential size in \(n\), while the two integers being subtracted are exponentially close in relative size. To see how much survives in the *full* radical, put
\[
 W_n=\sum_{p\ {\rm odd}}\max(v_p(D)-1,0)\log p .
\]
The exact factorization of the ratio yields
\[
 \log(C/R)=W_n-\bigl(10/3-4\log2\bigr)n+o(n).
\]
The constant \(10/3-4\log2=0.5607446\ldots\) is positive. In particular an exponential-in-\(n\) gain for the full triple occurs along a subsequence if and only if \(\limsup W_n/n>10/3-4\log2\). A fixed-exponent abc counterexample on this family requires \(\limsup W_n/\log C>0\), since \(\log\log C=(\log2+o(1))n\). Both statements use all prime factors. The formula supplies no unconditional lower bound of either required size for \(W_n\).

For example, at \(n=4\) the values have gcd 9, the primitive triple is \(299872+82055753=82355625\), and \(2^5\parallel299872\), as the formula predicts. An independent exact computation checks the dyadic depth and the stated prime intervals at every even index through 128. [Verification script](abc_binomial_difference_products.py)

## The real finite difference

For positive \(z\) write
\[
 I_n(z)=-\sum_{j=0}^n(-1)^j\binom nj\log(z+j)
 =\int_0^1\frac{u^{z-1}(1-u)^n}{-\log u}\,du.
\]
The logarithmic integral representation gives the equality and \(I_n(z)>0\). Since \(1-u\le-\log u\le(1-u)/u\), its bounds are the beta integrals \(B(z+1,n)\le I_n(z)\le B(z,n)\). With \(z=x/2=n+1/2\), the factor \(\log2\) from each entry cancels, so \(\log(C/\min(U,V))=I_n(z)\). Stirling's formula gives \(-\log I_n(z)=2n\log2+O(\log n)\). Finally \(D/C=1-e^{-I_n(z)}\sim I_n(z)\).

## The exact dyadic valuation

The same finite difference works \(2\)-adically. Write \(e_j=(-1)^j\binom nj\) and \(L=\sum_j e_j\log_2(1+2j/x)\), using the \(2\)-adic logarithm. The ratio \(\prod_j(1+2j/x)^{e_j}\) is \(1\bmod4\), since \(\sum_j j e_j=0\) for \(n\ge2\). Its numerator and denominator in lowest terms are odd. Consequently \(v_2(D)=v_2(L)\) by the logarithm isometry on \(1+4\mathbb Z_2\).

The iterated finite-difference identity gives, up to sign,
\[
 L=(n-1)!(2/x)^n
 \int_{[0,1]^n}\bigl(1+(2/x)(t_1+\cdots+t_n)\bigr)^{-n}\,d\mathbf t .
\]
Here the integral denotes coefficientwise ordinary integration of a formal power series, followed by evaluation in \(\mathbb Q_2\). The identity follows by applying \(f(z+h)-f(z)=h\int_0^1 f'(z+ht)\,dt\) successively to the logarithm, first formally in \(h\). Both series converge at \(h=2\). Indeed at total order \(j\), the denominators from integrating monomials are products of at most \(n\) integers \(\le j+1\); the factor \(2^j\) dominates their \(2\)-parts for fixed \(n\).

The integral is odd in \(\mathbb Z_2\). Its constant coefficient is 1, and its linear term after evaluation is \(-n^2/x\), even since \(n\) is even. At order \(j\ge2\), each integrated monomial, apart from an integer coefficient and an odd denominator, contributes
\[
 2^j\binom{j}{k_1,\ldots,k_n}\prod_{i=1}^n (k_i+1)^{-1},
 \qquad \sum_i k_i=j.
\]
Since \(v_2(k+1)\le k\) with strict inequality for \(k\ge2\), a term with such a \(k_i\) is even. If all \(k_i\) are 0 or 1, the multinomial coefficient is \(j!\), again even. This proves the exact valuation. Legendre's factorial formula now gives \((v_2(D)-1)\log2=(2\log2+o(1))n\).

## Which primes survive cancellation?

For odd \(p>\sqrt{4n+1}\), each entry \(x+2j\) has valuation at most one. If \(p\) occurs, its signed exponent in \(U/V\) is the sum of \(e_j\) over the unique class \(j\equiv a\bmod p\) corresponding to divisibility. This sum is nonzero for even \(n\).

To prove the assertion, let \(K_{2m}(r)=\sum_{j\equiv r\bmod 2p}\binom{2m}j\), using zero terms outside \(0\le j\le2m\). The signed sum over a class \(a\bmod p\) is, up to sign, \(K_{2m}(a)-K_{2m}(a+p)\). Put \(H_i^{(m)}=K_{2m}(m+i)\) for \(0\le i\le p\). By symmetry these depend only on the circular distance \(i\) from the center \(m\). Their first differences \(\Delta_i=H_i-H_{i+1}\) start, for \(m=0\), with \(\Delta_0=1\) and all the others zero. Convolution by the binomial coefficients \(1,2,1\), with the center advanced by one, gives in the interior
\[
 \Delta'_i=\Delta_{i-1}+2\Delta_i+\Delta_{i+1}.
\]
The boundary rules are \(\Delta'_0=\Delta_0+\Delta_1\) and \(\Delta'_{p-1}=\Delta_{p-2}+\Delta_{p-1}\). Thus \(\Delta_i>0\) for \(0\le i\le\min(m,p-1)\). Beyond distance \(m\) the profile is zero if that distance occurs. Two antipodal residues have distances \(i\) and \(p-i\), unequal since \(p\) is odd. Consequently their weights differ whenever either is nonzero. This proves that every such prime dividing an input survives in the reduced fraction.

All odd primes \(p\le n\) divide some \(x+2j\). For \(p>n\), the odd numbers \(x+2j\) in \([2n+1,4n+1]\) are divisible by \(p\) precisely when \(p\) itself belongs to this interval or \(3p\) belongs to it. Thus the primes in \((\sqrt{4n+1},(4n+1)/3]\) and \([2n+1,4n+1]\) all divide \(UV\); none divides \(D\). The total logarithmic weight of primes below the square-root cutoff is \(O(\sqrt n)\). The prime number theorem on the displayed intervals gives \(\log\operatorname{rad}(UV)=(4/3+2+o(1))n\).

To compare \(n\) with the actual height after cancellation, fix \(0<\epsilon<1/4\). The prime number theorem gives a prime \(p=x+2j\) with \(j/n\in[1/2-\epsilon,1/2+\epsilon]\) for all sufficiently large even \(n\). This prime exceeds \(2n\), so it occurs in just one entry and with signed exponent of absolute value \(\binom nj\). Therefore \(\log C\ge\binom nj\log p\), whereas \(\log C\le 2^{n-1}\log(4n+1)\). Stirling's formula and then \(\epsilon\downarrow0\) give the stated \(\log\log C\) asymptotic.

## Consecutive integers at other real scales

For even \(n\), replace \(x+2j\) by \(x+j\) with \(x/n\to\alpha>0\). Put \(m=\lfloor\alpha\rfloor\), \(H_m=\sum_{k=1}^m1/k\), and \(H_0=0\). The same real integral and cancellation lemma yield
\[
 \frac1n\log\frac{C}{D\operatorname{rad}(UV)}
 \longrightarrow (\alpha+1)\log(\alpha+1)-\alpha\log\alpha-
 H_m-\frac{\alpha+1}{m+1}<0.
\]
Indeed all primes up to \(n\) occur in the block, and outside primes contributing have a multiple \(kp\) in \([x,x+n]\). For \(p>n\) the intervals for different \(k\) are disjoint up to endpoints. After scaling by \(n\), their lengths are \(1/k\) for \(k\le m\), and \((\alpha+1)/(m+1)-1\) for \(k=m+1\). Changing the prime count at \(O(1)\) endpoints or below \(\sqrt{x+n}\) is \(o(n)\) in logarithmic weight. This proves the radical term; the real beta integral gives the first two terms.

For strict negativity, on \(m\le\alpha\le m+1\) the minimum over all \(\alpha>0\) of the affine expression \(H_m+(\alpha+1)/(m+1)\) minus the entropy term is \(H_m+\log(e^{1/(m+1)}-1)\), by differentiation with \(m\) held fixed. For \(m=0\) this is \(\log(e-1)>0\). For \(m\ge1\) it is greater than \(H_m-\log(m+1)>0\). In particular the deficit constant for the consecutive block with \(x=n\) is \(2-2\log2\).

## Combining overlapping polynomial identities over the same primes

The negative constant for one specialization can be overcome unconditionally by allowing products of shifted specializations. For all sufficiently large even \(n\) this gives a primitive triple with
\[
 \log(C/R)\gg n^2/\log n,\qquad
 \log\log C\asymp n,\qquad
 2^{n+v_2((n-1)!)}\mid D .
\]
In particular the full gain exceeds \(\exp(\kappa(\log\log C)^2/\log\log\log C)\) for an absolute \(\kappa>0\). Every prime in \(UV\) is \(O(\log\log C)\). Moreover \(\gg n/\log n\) distinct primes between \(5n/2\) and \(7n/2\) each occur in \(UV\) to exponent at least \(\exp(n/3)\). These statements survive reduction to coprime terms.

Choose \(s=\lfloor n/(8\log n)\rfloor\). For \(0\le i<s\), let \(T_i=U_0(x+2i)/V_0(x+2i)\) with \(x=2n+1\). Each ratio has exact dyadic depth \(e=n+v_2((n-1)!)\), by the proof above for any positive odd initial abscissa. Its real logarithm is \(-I_n(n+1/2+i)\), of magnitude at most \(I_n(n+1/2)<1\) for large \(n\).

Here is a lower bound at many primes that also proves multiplicative independence. A prime \(p=x+2l\) in \([5n/2,7n/2]\) exceeds half of the maximum input \(x+2(n+s-1)\). It occurs just at that one input, to exponent one before the binomial weights. Thus
\[
 v_p(T_i)=(-1)^{l-i}\binom{n}{l-i},\qquad
 (1/4-o(1))n\le l\le(3/4+o(1))n.
\]
Divide each row indexed by \(l\) by \((-1)^l\binom nl\), remove the alternating column signs, and multiply the row by \(B_l=\prod_{k=1}^{s-1}(n-l+k)\). The resulting entries are the integer polynomials
\[
 f_i(l)=l(l-1)\cdots(l-i+1)\prod_{k=i+1}^{s-1}(n-l+k)
\]
of degree at most \(s-1\). They form a basis over \(\mathbb Q\) since their evaluations at \(0,\ldots,s-1\) are lower triangular with nonzero diagonal. Any nonzero integer vector \(z_i\) therefore gives a nonzero polynomial \(F(l)=\sum_i(-1)^iz_i f_i(l)\), with at most \(s-1\) roots. At every other such prime,
\[
 \left|v_p\!\left(\prod_i T_i^{z_i}\right)\right|
   =\binom nl\,|F(l)|/B_l
   \ge\binom nl/B_l\ge\exp(n/3).
\]
Indeed \(B_l\le n^{s-1}\) for large \(n\), and Stirling gives \(\log\binom nl\ge(-\tfrac14\log\tfrac14-\tfrac34\log\tfrac34-o(1))n>(0.56-o(1))n\). The prime number theorem supplies \((1+o(1))n/\log n\) central primes. This proves independence, as well as the stated multiplicities for every nonzero product.

Take \(E=2^n\). The \((E+1)^s\) products \(\prod_i T_i^{a_i}\) with \(0\le a_i\le E\) have different real logarithms in an interval of length at most \(sE\). Two have a positive logarithmic gap at most \(sE/((E+1)^s-1)\). Express their quotient \(>1\) in lowest terms as \(U/V\) and put \(D=U-V,\ C=U\). As \(1-e^{-t}\le t\),
\[
 \frac C D\ge\frac{(E+1)^s-1}{sE}.
\]
All \(T_i\) are \(1\bmod 2^e\) and have odd numerator and denominator, giving \(2^e\mid D\). All prime divisors of \(UV\) are at most \(4n+2s+1\); hence \(\log\operatorname{rad}(UV)=O(n)\) by Chebyshev. Counting all odd primes in \(D\) with full multiplicity already proves
\[
 \frac CR\ge\frac{2^{e-1}}{\operatorname{rad}(UV)}
               \frac{(E+1)^s-1}{sE}.
\]
Taking logarithms gives the asserted \(\gg n^2/\log n\) bound. Each input numerator and denominator has logarithm at most \(2^{n-1}\log(5n)\), so \(\log C\le sE2^{n-1}\log(5n)\). Conversely the multiplicity bound at a surviving central prime gives \(\log C\ge e^{n/3}\log(5n/2)\), since that prime power lies in \(U\) or \(V\le C\). These two inequalities prove \(\log\log C\asymp n\).

This is a finite construction with unbounded degree and height. It proves exponential-in-index radical saving for the complete primitive integer triple. A rational abc disproof would require savings of order \(\log C\) on the logarithmic scale, which is exponentially larger in \(n\) than the quantity certified here.
