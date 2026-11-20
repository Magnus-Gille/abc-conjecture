# Quadratic characters and sparse relations for the primorial conic lattice

Use \(D=\prod_{p\le d}p\), a modulus \(M\) divisible by \(D\), and the first \(d\) split primes \(\ell_i>d\) of \(\mathbb Q(\sqrt2)\). Write \(\eta_i\) for generators of chosen primes above them, of signed norm \(N_i=\pm\ell_i\). A vector \(z\) in the projective kernel modulo \(M\) gives a primitive \(\alpha=b+a\sqrt2\), scalar modulo \(M\), by choosing the generator or its conjugate according to the sign of \(z_i\). Set \(I=\{i:z_i\text{ odd}\}\) and \(s=|I|\). The following results hold for all sufficiently large \(d\).

* Every nonempty \(I\) from a kernel vector has at least seven elements.
* For any fixed \(s\), at most \(d^{o(1)}\) subsets of size \(s\) pass the quadratic tests. For every fixed \(\theta<1/2\), the fraction passing at size \(1\le s\le d^\theta\) is at most \(d^{-(1-2\theta-o(1))s}\), interpreting the asymptotic exponent uniformly.
* The binary linear map of the quadratic tests, including the sign condition at 2, has rank at least \(d^{1/2-o(1)}\). Nevertheless all simultaneous character tests of bounded order admit a nonzero signed vector of support \(O(d/(\log d\,\log\log d))\). Even all congruences modulo \(D^j\), for **any fixed** \(j\), admit vectors of support at most \((1-\delta)d\) and 1-norm at most \(C_{j,\delta}d\), for every \(0<\delta<1\).

These are conditions on the parities of exponents. An even exponent in a nonzero coordinate is invisible to every quadratic test. The conic construction uses \(j\) growing like \(\log d\). [Construction and full-precision short-relation criterion](abc_square_conic_growing_primes.md)

## The quadratic test is a pseudosquare test

For odd \(p\le d\), the projective group \((\mathcal O/p)^\times/(\mathbb Z/p)^\times\) is cyclic of order \(p-(2/p)\). Its unique quadratic character on a unit \(\eta\) is \((N\eta/p)\). In the split case this follows from the Legendre symbols of the product and ratio of the two coordinates. In the inert case it follows by composing the norm to \(\mathbb F_p^\times\) with the quadratic character; the composition is surjective and trivial on scalar units.

In particular set \(q_0=\prod_{i\in I} N_i\), with its sign. The signed norm of \(\alpha\) is \(q_0\) times a positive odd rational integer square. Since \(M\mid a\), the norm \(b^2-2a^2\) is an invertible square modulo every odd \(p\le d\). Also \(a\) is even and \(b\) odd, so \(q_0\equiv1\bmod8\). Equivalently these are linear conditions on the parity vector. Call a subset passing these necessary conditions admissible. For nonempty \(I\), \(q_0\) is a nontrivial odd quadratic discriminant, since it is signed squarefree and \(1\bmod8\). Its primitive quadratic character \(\chi\) has squarefree conductor \(q=|q_0|\), and \(\chi(p)=1\) for **every** prime \(p\le d\), including 2. Thus this discriminant behaves as a square at the entire initial prime interval.

For the ordinary ring class group of the order \(\mathbb Z+M\mathcal O\), the standard exact sequence of an order gives \(\operatorname{Pic}(\mathbb Z+M\mathcal O)=G(M)/\langle\epsilon\rangle\), where \(G(M)\) is the projective residue group and \(\epsilon=1+\sqrt2\); here \(\operatorname{Pic}(\mathcal O)=1\). The chosen split prime ideals give the corresponding Frobenius classes, up to simultaneous convention of inversion which is immaterial to quadratic characters. Quotient the vector of test values by the one vector of test values at \(\epsilon\). The resulting characters factor through the ring class group, so the image rank loses at most one. Since \(N\epsilon=-1\), passing this quotient test means that **one** of \(q_0,-q_0\) is \(1\bmod8\) and is a quadratic residue at every odd \(p\le d\). The absolute conductor \(q=\prod_{i\in I}\ell_i\) is unchanged. Hence the support bounds below and the \(d^{1/2-o(1)}\) image-rank lower bound also hold for these genuine ring class characters. A projective scalar relation additionally fixes the unit correction, as required in the conic construction.

## Excluding up to six odd coordinates

The prime number theorem in the split classes gives \(\max_i\ell_i\le C d\log d\). If \(1\le s\le6\), choose a fixed small \(\eta>0\) with \(6(1/4+\eta)<\sqrt e\), and put \(x=q^{1/4+\eta}\). For some fixed \(u_0<\sqrt e\) and all sufficiently large \(d\) one has \(x\le d^{u_0}\). All \(d\)-smooth integers have character \(+1\). For \(d<x\le d^{u_0}\), the number of integers up to \(x\) with a prime factor greater than \(d\) is at most \(x\sum_{d<p\le x}p^{-1}\le(\log u_0+o(1))x\) by Mertens's theorem. If \(x\le d\) they are absent. In either case \(\sum_{m\le x}\chi(m)\gg x\), since \(\log u_0<1/2\). On the other hand Burgess's character sum estimate for a primitive character of cube-free conductor gives
\[
       \left|\sum_{m\le x}\chi(m)\right|
       \ll_{r,\varepsilon} x^{1-1/r}q^{(r+1)/(4r^2)+\varepsilon}.
\]
Choosing \(r>1/(4\eta)\) and then \(\varepsilon\) small gives \(o(x)\), a contradiction. [Burgess, *On character sums and L-series II*](https://doi.org/10.1112/plms/s3-13.1.524)

## Counting admissible sparse supports

For \(s\le d^\theta\), \(\theta<1/2\), there are \(\gg d/\log d\) primes \(p\equiv1\bmod4\) in \((d/2,d]\). Let \(\mathcal A\) consist of products of \(s\) distinct such primes. Then
\[
 A_0=|\mathcal A|\ge (c d/(s\log d))^s,\qquad n\le d^s\quad(n\in\mathcal A).
\]
All are odd squarefree and \(1\bmod4\). For an admissible \(I\), quadratic reciprocity and \(({-1}/n)=1\) give \((n/q)=1\) for every \(n\in\mathcal A\); the absolute conductor \(q\) uniquely identifies \(I\). Put \(X=(C d\log d)^s\), increased to an integer. By Heath-Brown's quadratic large sieve in its squarefree odd form,
\[
 \sum_{\substack{q\le X\\q\ {\rm odd,\ squarefree}}}
       \left|\sum_{n\in\mathcal A}(n/q)\right|^2
       \ll_\varepsilon X^{2\varepsilon}\,(X+d^s)A_0 .
\]
Each admissible support contributes \(A_0^2\) on the left. Therefore their number satisfies
\[
          K_s\ll_\varepsilon X^{2\varepsilon}
                            (C' s(\log d)^2)^s .                    \tag{1}
\]
For fixed \(s\), taking \(\varepsilon\) arbitrarily small gives \(K_s\le d^{o(1)}\). Uniformly through \(s\le d^\theta\), divide (1) by \(\binom ds\ge(d/s)^s\) to obtain the asserted fraction, again taking \(\varepsilon\) arbitrarily small. [Heath-Brown, *A mean value estimate for real character sums*](https://doi.org/10.4064/aa-72-3-235-275)

## How many independent parity tests are present

The norm signs at 2 give a binary condition because each signed \(\ell_i\) is \(1\) or \(-1\bmod8\). Include this row along with the Legendre rows. Let \(b=\lfloor d^\theta\rfloor\) for fixed \(0<\theta<1/2\). Map all \(b\)-subsets to their vectors of test values. Two equal images differ by an admissible subset of size \(2j\) for some \(j\le b\). For a fixed such subset the number of ordered pairs giving that difference is
\[
         \binom{2j}{j}\binom{d-2j}{b-j}
         \le \binom db\left(\frac{4b}{d-b}\right)^j .
\]
Here \(\binom{d-2j}{b-j}/\binom db=(b)_j(d-b)_j/(d)_{2j}\le (b/(d-b))^j\), where \((\cdot)_j\) is the falling factorial; the bound also follows by first forcing any fixed \(j\) positions to be included. Apply (1) at \(s=2j\) (the same proof applies through \(2d^\theta\)). Uniformly in \(j\le b\), \(K_{2j}\le d^{(2\theta+o(1))j}\) in the sense of an arbitrarily small fixed error in the exponent. The equal-image pair count is at most
\[
    \binom db\ d^{(\max(0,3\theta-1)+o(1))b}.
\]
By Cauchy–Schwarz the number of distinct images is at least
\[
     d^{(1-\theta-\max(0,3\theta-1)-o(1))b}.
\]
The coefficient is positive for each \(\theta<1/2\). Taking binary logarithms proves the stated \(d^{1/2-o(1)}\) rank lower bound, in the sense of exceeding \(d^{1/2-\varepsilon}\) for every fixed \(\varepsilon>0\) eventually. This argument leaves the actual rank below the obvious upper bound \(\pi(d)+O(1)\).

## What finite-depth tests can force

For odd \(p\), reduction from level \(p^j\) to \(p\) has cyclic \(p\)-primary kernel, by the \(p\)-adic logarithm, and cyclic prime-to-\(p\) quotient of order \(p-(2/p)\). The local projective group is abelian, hence cyclic. At 2 it is generated by a bounded number of elements independently of \(j\): the logarithm on \(1+4\mathcal O_2\) gives a free \(\mathbb Z_2\)-module of rank two, and the residual quotient modulo 4 has bounded size. Thus the joint image detected by characters of any fixed exponent \(B\) has order at most \(B^{\pi(d)+O(1)}\).

Take \(r=\lceil C_B d/(\log d\,\log\log d)\rceil\). Then \(\log\binom dr\ge r\log(d/r)>\log(B)(\pi(d)+O(1))\) for \(C_B\) sufficiently large. Two distinct \(r\)-subsets have identical images in the joint quotient. Their difference is a nonzero signed vector of support and 1-norm at most \(2r\). This construction concerns the stated characters, not the deeper local conditions.

For all congruences at fixed depth \(j\), the projective group modulo \(D^j\) has log order at most \((j+o(1))d\). Choose \(0<2\tau<1-\delta\), and an integer \(Q\) with \(\tau\log Q>j+1\). On a fixed set of \(\lfloor\tau d\rfloor\) coordinates take entries in \(\{0,\ldots,Q\}\), zero elsewhere. More than \(\exp((j+o(1))d)\) vectors are available. A collision therefore gives a nonzero kernel vector of support at most \(\tau d\) and 1-norm at most \(Q\tau d\). The same argument works for any tested quotient of log order \(O(d)\). For the full growing precision the available order bound is instead \(\exp((1+o(1))d\log d)\).

## Detecting normalized parity with higher characters

Fix \(h\ge0\). For a nonzero vector with minimum common 2-adic valuation \(h\), write \(z=2^h w\) and \(I'=\{i:w_i\text{ is odd}\}\), which is nonempty. At every \(p\equiv1\bmod 2^{h+3}\), the local projective group is cyclic of order \(p-1\) divisible by \(2^{h+1}\). Take a character \(\lambda_p\) of exact order \(2^{h+1}\). Then \(\lambda_p^{2^h}\) is the unique quadratic character, and
\[
      \lambda_p\left(\prod_i\eta_i^{z_i}\right)
         =\left(\frac{\prod_{i\in I'}N_i}{p}\right).
\]
Consequently a full kernel vector still imposes a quadratic nonresidue sieve on the **normalized** odd support even when its original coordinates were all even.

To perform this test by genuine ring class characters, restrict to rational primes splitting completely in the normal closure of \(\mathbb Q(\sqrt2,\mu_{2^{h+3}},\epsilon^{1/2^{h+1}})\). At these primes both embeddings of \(\epsilon\) have \(2^{h+1}\)-th roots in \(\mathbb F_p^\times\), so \(\lambda_p\) kills the global unit. The character pulled back from this one local factor therefore factors through \(\operatorname{Pic}(\mathbb Z+M\mathcal O)\). For fixed \(h\) Chebotarev supplies \(\gg_h d/\log d\) such primes in \((d/2,d]\). Use these primes in the amplifier above. Equation (1) and its consequences for sparse supports still hold for \(I'\), replacing constants by constants depending on \(h\). In particular only \(d^{o_h(1)}\) supports at each fixed nonzero weight pass all these tests. This argument requires fixed \(h\) for the stated uniform supply of test primes.
