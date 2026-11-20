# Prime support through \(n^4\) in the dyadic CM packets

For every power of two \(16\le n\le8192\), the integer \(w_n\) has a prime factor strictly exceeding \(n^4\). At \(n=8\) its sole prime factor is 2273, below \(8^4=4096\). For seven of the ten indices from 16 through 8192, every prime factor exceeds the cutoff. Each of the remaining three has precisely one prime below it. [Packet definition and split CM criterion](abc_dyadic_cm_largest_prime.md) · [Exact arithmetic verifier](abc_dyadic_cm_prime_support.py)

Let \(S_n=\prod_{p\le n^4}p^{v_p(w_n)}\). The norm-pair column counts all \(b>0,\ a\in\mathbb Z\) satisfying \((1+na)^2+2n^2b^2\le n^4\) before any sieve.

| \(n\) | Norm pairs | Digits in \(w_n\) | Exact \(S_n\) | Digits in \(w_n/S_n\) |
|---:|---:|---:|---:|---:|
| 8 | 61 | 4 | 2,273 | 1 |
| 16 | 268 | 14 | 1 | 14 |
| 32 | 1,102 | 54 | 1 | 54 |
| 64 | 4,482 | 214 | 1 | 214 |
| 128 | 18,068 | 855 | 67,649,537 | 847 |
| 256 | 72,526 | 3,417 | 1 | 3,417 |
| 512 | 290,642 | 13,666 | 339,767,297 | 13,657 |
| 1,024 | 1,163,655 | 54,662 | 1 | 54,662 |
| 2,048 | 4,656,634 | 218,645 | 1 | 218,645 |
| 4,096 | 18,630,663 | 874,580 | 1 | 874,580 |
| 8,192 | 74,530,936 | 3,498,318 | 65,229,783,041 | 3,498,307 |

Every \(S_n>1\) in the table is a prime of exponent one. For \(n=8,128,512,8192\), respectively, its norm representations use \((a,b)=(-2,4),(64,4),(28,16),(-2,22)\). The verifier also proves \(w_{16}=22151840117633\) prime and gives the complete factorization \(w_{32}=2401379840999699201\cdot100264636730315412574143047918721793\).

To certify small support, compute the packet by exact integer doubling. For each possible \(b>0\), set \(D=\lfloor\sqrt{n^4-2n^2b^2}\rfloor\). Enumerate \(-\lfloor(D+1)/n\rfloor\le a\le\lfloor(D-1)/n\rfloor\). Every possible small prime is one of these norm values. Multiply the norms modulo \(w_n\) and take the gcd with \(w_n\). This gcd has exactly the small prime support, since every prime dividing a norm of size at most \(n^4\) is also at most \(n^4\). For speed the verifier crosses out norm values divisible by odd primes \(\ell\le521\) with \(\ell<2n^2\). These norms are strictly larger than \(\ell\), so no prime norm value is removed. The gcd support is unchanged. Trial division of \(w_n\) by the certified primes of the gcd then gives their complete multiplicities. An independent run through 4096 used the full product without sieving.

## A stronger necessary congruence

In fact every \(p\mid w_n\), \(n\ge8\) dyadic, has a representation
\[
 p=(1+2na')^2+2(2n)^2b'^2,\qquad b'\ne0 .
\]
The table uses the larger disk defined by \(n\) and works independently of this refinement.

Write \(\tau^2=-2\), and use the known annihilator \({\rm ann}_{\mathcal O}(R\bmod p)=(n)\) and the original representation \(p=x^2+2y^2\), \(x=1+na,\ y=nb\ne0\). Then \(x\equiv1\bmod8,\ p\equiv1\bmod8\) and \(\gcd(x,y)=1\). Each odd prime \(\ell\mid y\) satisfies \((\ell/p)=(p/\ell)=1\), since \(p\equiv x^2\bmod\ell\). Together with \((2/p)=(-1/p)=1\) this gives \((y/p)=1\). Likewise \((x/p)=(p/|x|)=(2/|x|)=1\) by Jacobi reciprocity and \(x\equiv1\bmod8\), with the trivial character if \(|x|=1\). Thus either reduction of \(\tau=\pm x/y\bmod p\) is itself a square.

On \(E':y^2=x^3+16x^2+32x\), the abscissa map of \([\tau]\) is \(-\tfrac12(x+16+32/x)\). Points \(C\) with abscissa \(\pm4\tau\) have ordinate \(\pm16\tau\); choose the sign giving \([\tau]C=R=(-8,16)\). The abscissas of \(\tau\)-preimages of \(C\) solve \(X^2+(16\pm8\tau)X+32=0\), of discriminant \(\pm256\tau\). This is a nonzero square modulo \(p\). For either rational abscissa the ordinate is rational as well, since the isogeny ordinate formula scales it by \((1-32/X^2)/\tau^3\), a nonzero rational scalar at this split place because \(C\) has nonzero ordinate. Hence \(R\) is divisible by \(\tau^2\) in \(E'(\mathbb F_p)\). If \(\tau^2 D=R\) and \({\rm ann}(R)=(n)=(\tau^{2k})\), then \({\rm ann}(D)=(\tau^{2k+2})=(2n)\): \(\tau^{2k+2}D=0\) but \(\tau^{2k+1}D\ne0\). Frobenius fixes \(D\), so its multiplier \(\pi\) is \(1\bmod 2n\), as claimed.

This congruence forces \(p\ge12n^2-4n+1\): the only smaller candidate is \(8n^2+1\), divisible by 3 since \(n\) is dyadic. The support prime at \(n=8192\) has \((\pi-1)/(2n)=-1\pm11\tau\), a \(\tau\)-adic unit. In particular, the modulus \(2n\) cannot always be enlarged to \(2n\tau\).

In the explicit ellipse sieve, passage from \(n\) to \(2n\) quarters the area, with exactly the same odd-prime local densities. Thus the coefficient 16 obtained with the original lattice becomes 4 in the limiting logarithmic mass bound at \(X=cn^4\). The corresponding explicit threshold for the largest prime factor, conditional on rational abc, increases from \(\widehat h(R)/32\) to \(\widehat h(R)/8\). [Explicit ellipse sieve](abc_octic_dyadic_fermat_audit.md)
