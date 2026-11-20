# Restrictions on short relations among the chosen split prime generators

Use the actual balanced generators \(\eta_i\) of the first \(d\) split prime ideals chosen above \(d\) in the square-conic construction, with different underlying rational primes \(\ell_i\). The same conclusions hold for any such distinct generators satisfying \(d<\ell_i\le C_0d\log d\) and the same embedding bound, for a fixed \(C_0\). The original modulus imposes depth at least \(k\asymp\log d\) at every prime \(p\le d\). [Construction and fixed-power criterion](abc_square_conic_growing_primes.md)

Fix \(K>0\). Uniformly for all its nonzero kernel vectors \(\|z\|_1\le Kd\), the common divisor \(n=\gcd_i|z_i|\) is bounded in terms of \(K\) and the fixed construction constants. Moreover, for a set of integer ranks \(d\) of logarithmic density one, **the number of odd entries of \(z/n\)** is at least
\[
             c_K\frac{\log\log d}{\log\log\log d}.
             \tag{1}
\]
Here logarithmic density one means that the complementary ranks through \(X\) have sum of reciprocals \(o(\log X)\). The assertion is uniform over all eligible vectors at each such rank. There is also an all-ranks obstruction. If some entries of \(z\) are odd, at least seven of them are odd, once \(d\) is sufficiently large.

## Bounding the common exponent

Set \(w=z/n\). Assemble \(\gamma=b+a\sqrt2\) from \(w\), using conjugate generators for negative exponents, so that the parameter for \(z\) is exactly \(\gamma^n\). Both embeddings of \(\gamma\) are at most \(\exp(O(Kd\log d/n))\) in absolute value. The coefficient \(a_j\) of \(\sqrt2\) in \(\gamma^j\) is nonzero for every \(j\ge1\), by the different valuations at the two prime ideals over any \(\ell_i\) in the support. Consequently
\[
                  \log|a_j|\ll K j d\log d/n.
\]
For \(d/2<p\le d\) with \(p\nmid n\), the projective order \(r_p\) of \(\gamma\) modulo \(p\) divides both \(n\) and \(p-(2/p)\). Also \(p^k\mid a_{r_p}\). Indeed \(\gamma^{r_p}\) is already projectively principal at \(p\), and exponentiation by the \(p\)-unit \(n/r_p\) is an automorphism of the finite principal \(p\)-group modulo \(p^k\). Only \(O_K(1)\) primes in this interval divide \(n\le Kd\).

The primes with \(r_p\le\sqrt n\) consequently number at most
\[
   \frac{\sum_{j\mid n,\,j\le\sqrt n}\log|a_j|}{k\log(d/2)}
       \ll_K\frac{d}{\log d}\frac{\tau(n)}{\sqrt n}.
\]
At \(\sqrt n<r_p\le\sqrt d\), sum the Brun–Titchmarsh upper bound in the two classes \(p\equiv\pm1\bmod r_p\), using \(\varphi(r_p)\gg r_p/\log\log(3n)\). This bounds their number by \(O(d\,\tau(n)\log\log(3n)/(\sqrt n\log d))\). The remaining \(r_p>\sqrt d\) contribute \(O((1+\sqrt d)\tau(n))\) by direct progression counting. Since \(\tau(n)=n^{o(1)}\) and \(n\le Kd\), the total would be \(o(d/\log d)\) along any sequence \(n\to\infty\). The prime number theorem gives a contradiction. Choose a fixed integer \(N_K\) bounding all such \(n\).

The order of each individual \(\eta_i\) is particularly large. If \(V\) denotes its projective order modulo the prescribed modulus, then uniformly in \(i\)
\[
    \log V\ \ge\ \left(\frac1{2\log2}-o(1)\right)\log d\log\log d .
\]
Indeed if the constant were smaller by a fixed positive amount, the standard maximal-order divisor bound would give \(\tau(V)<d^{1/2-\epsilon}\) for some \(\epsilon>0\). For \(r_p\le\sqrt d\) sum the logarithms of the nonzero coefficients of \(\eta_i^j\) over \(j\mid V,\ j\le\sqrt d\), using \(\log|a_j|\ll j\log d\); each prime counted costs \(\log(d/2)\). Larger \(r_p\mid V\) force \(p\equiv\pm1\bmod r_p\). Together these count \(O(\sqrt d\,\tau(V))=o(d/\log d)\) primes. In particular, on any fixed set of \(t\) coordinates there cannot be \(t\) independent relations of length \(O(d)\) when \(t<(1/(2\log2)-\epsilon)\log\log d\): their determinant would bound the group order on those coordinates by \(O(d)^t\).

## The quadratic character of the primitive exponent vector

Fix a positive integer \(L\) divisible by 8 and by \(2\operatorname{lcm}(1,\ldots,N_K)\), and put \(\alpha=1/\varphi(L)\). For every \(p\le d\) with \(p\equiv1\bmod L\), the quadratic ring splits and the reductions of \(\gamma\) are a pair of units \(x,y\bmod p\). The ratio \(x/y\) has order dividing \(n\). Since \(2n\mid p-1\), it is a square. The norm \(xy\) therefore is a square as well. The primitive quadratic character \(\chi\) of \(\mathbb Q(\sqrt{N(\gamma)})\) satisfies
\[
               \chi(p)=1\qquad(p\le d,\ p\equiv1\bmod L).
               \tag{2}
\]
There is at least one odd coordinate of \(w\); each such coordinate contributes its own distinct odd prime \(\ell_i\) to the conductor. With \(t\) odd coordinates the conductor is at most \(8(C_0d\log d)^t\).

The all-ranks assertion for odd entries of \(z\) itself is a direct application of Burgess's character sum bound. If \(1\le t\le6\) of its entries are odd, the norm of the original parameter yields a nonprincipal primitive quadratic character of conductor \(q\le8(C_0d\log d)^6\). The norm is an odd square modulo 8 since that parameter is scalar modulo \(2^k\). Its signed squarefree part is thus \(1\bmod8\), the conductor is odd and squarefree, and the character at 2 equals one. At each odd \(p\le d\) the norm is a unit square since the parameter is scalar. Set \(x=d^{8/5}\). The proportion of \(j\le x\) having any prime divisor \(>d\) is at most \(\sum_{d<p\le x}1/p=\log(8/5)+o(1)<1/2\). All the other \(j\) have character one. This gives a positive fixed lower bound for the mean character sum to \(x\). Since \(x>q^{1/4+\epsilon}\) for a fixed \(\epsilon>0\) and large \(d\), Burgess's bound for cube-free conductor gives a mean tending to zero. When the interval is longer than the modulus one may use periodicity and the same bound. [Burgess, *On character sums and L-series II*](https://doi.org/10.1112/plms/s3-13.1.524)

## A large-sieve count across ranks

For large \(Y\) consider ranks \(Y\le d\le Y^2\), and characters in (2) having at most \(t\) odd coordinates in \(w\). An upper bound on their conductors is \(Q=Y^{3t+1}\). Set \(P=Q^2=Y^B\), \(B=6t+2\). Let \(\mathcal A\) be the positive integers \(\le P\) whose prime divisors are all \(\le Y\) and \(1\bmod L\). The classical multiplicative large sieve for primitive characters, with coefficients \(1_{\mathcal A}\), gives
\[
   \#\{\chi\}\,|\mathcal A|^2
          \ll (Q^2+P)|\mathcal A|.
          \tag{3}
\]
In fact every character being counted takes the value one on every element of \(\mathcal A\). This uses one common test set for all the ranks in the interval. [Multiplicative large sieve in Chapter 7 of Iwaniec and Kowalski, *Analytic Number Theory*](https://www.ams.org/books/coll/053/)

For integers \(1\le t\ll\log\log Y\) one has the elementary lower estimate
\[
 |\mathcal A|\ \gg_L\
       P(\log Y)^{\alpha-1}\exp[-O_L(t\log(2t))].
       \tag{4}
\]
To prove it, form \(a\le Y^{1/8}\) using prime factors \(\le Y^{1/32}\) all \(1\bmod L\). The sum of \(1/a\) over these \(a\) is \(\gg_L(\log Y)^\alpha\). Without the size restriction this follows from the Euler product and Mertens' estimate in the fixed progression. The mean of \(\log a\) under the normalized reciprocal weights is at most \(\sum_{p\le Y^{1/32}}\log p/(p-1)\le(1/32+o(1))\log Y\), so truncation retains at least half of the sum.

Put \(m=2B\). Independently choose \(m-1\) primes \(q_j\equiv1\bmod L\) in \([Y^{1/2-1/(8m)},Y^{1/2}]\). Their reciprocal sum in each position is \(\gg_L1/m\), uniformly here, by partial summation and the prime number theorem for the fixed progression with its classical error term. The remaining factor \(X'=P/(a\prod q_j)\) lies between \(Y^{3/8}\) and \(Y^{5/8}\). Choose a final prime \(1\bmod L\) in \([X'/2,X']\), with \(\gg_L X'/\log Y\) choices. Every resulting product belongs to \(\mathcal A\). The small-prime part \(a\) is identifiable, and the \(m\) large primes give the same product in at most \(m!\) orders. Multiplication of the counts proves (4).

Take \(t=\lfloor c\log\log Y/\log\log\log Y\rfloor\) for sufficiently small fixed \(c>0\) depending on \(K\). Equations (3) and (4) bound the number of eligible characters by \(O_K((\log Y)^{1-\alpha/2})\). For each of them choose an odd prime \(\ell\) of its conductor. It must satisfy \(d<\ell\le C_0d\log d\). The possible \(d\) in this block thus have total reciprocal weight \(O(\log\log Y)\) for each character. The exceptional ranks in the whole block have reciprocal weight \(O_K((\log Y)^{1-\alpha/2}\log\log Y)=o(\log Y)\). Summing over the blocks with successive endpoints \(X,X^{1/2},X^{1/4},\ldots\), and slightly reducing \(c\) to cover variation within each block, proves (1).

## A short sparse relation through the smaller local depths

Fix an integer \(j\ge1\) and \(0<\sigma<1\). Choose any \(\lfloor\sigma d\rfloor\) of the available split generators. There exists a nonzero vector on just those coordinates with \(\|z\|_1\ll_{j,\sigma} d\) whose parameter is projectively scalar to depth \(j\) at every prime \(p\le d\), and to depth \(k\asymp\log d\) at every \(p\le d/\log d\). This gives simultaneous prescribed square divisibility for all the primes in the interval if \(j\ge2\).

In fact take \(M'=(\prod_{p\le d}p)^j (\prod_{p\le d/\log d}p)^k\). Chebyshev's bound gives \(\log M'=O_j(d)\). The projective group modulo \(M'\) has size at most \(M'\prod_{p\le d}(1+1/p)=\exp(O_j(d))\). Choose a sufficiently large fixed integer \(B=B(j,\sigma)\). The exponent vectors supported on the selected coordinates with each entry in \(0,\ldots,B\) then outnumber the group. Subtracting two with identical class gives the claimed vector, and the private split primes ensure its projective parameter is globally nontrivial. The part still required by the original fixed-power criterion has growing depth at the larger primes.

## Sensitivity to one extra prime

Keeping the same actual generators and all original local requirements, one can add a single prime \(q\) to the modulus to preclude every bounded-linear-length relation. Put \(Q_1=\exp(d\sqrt{\log d})\), \(T=d\exp(\tfrac12\sqrt{\log d})\). There are at most \(2^d\binom{\lfloor T\rfloor+d}{d}=\exp((1/2+o(1))d\sqrt{\log d})\) exponent vectors of 1-norm at most \(T\). Every nonzero one produces a nonzero irrational coefficient with log absolute value \(O(T\log d)\), so that coefficient has at most \(O(T\log d/\log Q_1)\) prime factors between \(Q_1\) and \(2Q_1\). Comparing with the number of primes in that interval, almost every such \(q\) divides none of those coefficients. For these \(q\), the modulus \(Mq\) has minimum nonzero 1-norm exceeding \(T\). Nevertheless \(\log q=o(\log M)\) and \((Mq)/\operatorname{rad}(Mq)=M/\operatorname{rad}(M)\) exactly.

The bounded-common-exponent and parity-support conclusions concern the original modulus. They still permit \(O(d)\)-length vectors with a fixed positive fraction of coordinates unoccupied. The extra-prime construction shows that the leading sizes of the modulus and radical certificate by themselves cannot guarantee the short relation needed for a fixed abc exponent.
