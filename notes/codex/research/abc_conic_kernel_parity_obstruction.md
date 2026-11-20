# Parity and common powers in the conic congruence lattice

Use the $d$ chosen rational primes $d<\ell_i\ll d\log d$ split in $\mathbf Q(\sqrt2)$, the balanced generators $\eta_i$, and the kernel lattice from the [growing-prime conic construction](abc_square_conic_growing_primes.md). Its modulus $M$ is divisible by $p^k$ at every $p\le d$, with $k=(1+o(1))\log d$. For a nonzero kernel vector $z$, write
\[
 t=\#\{i:z_i\text{ is odd}\},\qquad m=\gcd_i |z_i|.
\]
Two unconditional restrictions are
\[
 t=0\quad\hbox{or}\quad t\ge \log_2(\log d)-O(1),
 \qquad m\ll K\log\log(3K)\quad\hbox{if }\|z\|_1\le Kd .
\]
The subscript 2 denotes logarithm to base 2. The second bound holds for fixed $K\ge2$ and sufficiently large $d$ depending on $K$, with an absolute implied constant. In particular a primitive exponent vector has growing support, and a one-coordinate kernel vector cannot be short. The parity bound applies to all vectors in the lattice. Its image in $\mathbf F_2^d$ is a linear code with the displayed minimum nonzero Hamming weight. Even exponent vectors are outside the nonzero-distance assertion.

## Scalar norm and a short quadratic character sum

Construct $\alpha=b+a\sqrt2$ from $z$ using $\eta_i$ or its conjugate according to sign, as in the conic construction. Its norm is prime to $M$, and $M\mid a$. Let $\Delta$ be the signed squarefree part of $N\alpha$. Every odd prime $p\le d$ therefore has $(\Delta/p)=1$. Also $b$ is odd and $a$ is even, so $N\alpha\equiv1\pmod8$ and $\Delta\equiv1\pmod8$. If $t>0$, $|\Delta|$ is precisely the product of the $t$ primes with odd exponent. The primitive quadratic character of signed discriminant $\Delta$ is
\[
  \chi(n)=\prod_{z_i\ \mathrm{odd}}(n/\ell_i)
\]
by quadratic reciprocity, and $\chi(n)=1$ for every $1\le n\le d$. Take $X=\lfloor d^{3/2}\rfloor$. Any integer at which $\chi$ differs from one has a prime factor exceeding $d$. The reciprocal prime sum thus gives
\[
 \frac1X\sum_{n\le X}\chi(n)\ge 1-2\sum_{d<p\le X}\frac1p
                         =1-2\log(3/2)+o(1)>0.18 .
\]

Here is the cancellation estimate using the factorization of the conductor. Write $\ell_1,\ldots,\ell_t$ for the factors that occur, and take $H=\lfloor d^{1/8}\rfloor$. It is enough to consider $t\le\log_2\log d$. At differencing step $j$ choose $1\le h_i\le H$ for $i\le j$, and form all subset shifts $\sum_{i\le j}\epsilon_i h_i\ell_i$. For each of the remaining prime characters take its product over the $2^j$ shifts, counting multiplicities. Denote the resulting bounded function by $f_j(n)$, and by $A_j$ the average, over the $h_i$, of the absolute value of its mean on $1\le n\le X$.

For $j<t-1$ translate $f_j$ by $h\ell_{j+1}$ and average over $1\le h\le H$. Cauchy–Schwarz and expanding the square give
\[
 A_j^2\le C\big(H^{-1}+H\max_i\ell_i/X+2^t/d+A_{j+1}\big)
\]
with an absolute $C$. In detail, passing to the translated interval costs $O(H\max\ell_i/X)$, the equal-shift terms contribute $1/H$, and the difference of two distinct shifts has triangular weight at most $2/H$ after combining both signs. Translating the remaining correlation back to the original interval costs the same endpoint bound. The $\ell_{j+1}$ character occurs squared and equals one except when one of its earlier shifts vanishes modulo that prime, a set of density at most $2^j(1/\ell_{j+1}+1/X)$. Removing it leaves precisely the function at the next step. Jensen’s inequality allows averaging this estimate over all earlier shifts.

At the final prime $\ell_t$, the shifts are pairwise distinct modulo $\ell_t$ apart from a fraction at most $3^{t-1}/H$ of the shift tuples. For each nonzero difference pattern with coefficients in $\{-1,0,1\}$, fix all but one associated $h_i$. At most one of its $H<\ell_t$ values can solve the resulting linear congruence. For a good tuple the polynomial of shifted linear factors is squarefree. The classical Weil bound for the quadratic character over $\mathbf F_{\ell_t}$ bounds its complete mean by $2^{t-1}/\sqrt{\ell_t}$. Decomposing the interval into periods therefore gives
\[
 A_{t-1}\ll 3^t/H+2^t/\sqrt d+\max_i\ell_i/X .
\]
All the errors inside the recursion and this terminal bound are $O(d^{-1/9})$ in the indicated range of $t$. Iterating the square roots gives
\[
 A_0\le C_1\big(C_2d^{-1/9}\big)^{1/2^{t-1}}
\]
with absolute constants. To see the uniformity, let $B<1$ dominate the terminal value and the error at every step. If $A_{j+1}\le K_0 B^u$ with $u\le1$, then $A_j\le\sqrt{C(1+K_0)} B^{u/2}$; choose $K_0$ fixed and sufficiently large. Comparing with the lower bound $0.18$ proves $2^t\gg\log d$. The complete sum estimate and the Burgess bound used below are standard finite-field and interval character-sum bounds. [Iwaniec and Kowalski, *Analytic Number Theory*, Chapters 11 and 12](https://doi.org/10.1090/coll/053)

## How much a common exponent can contribute

For any $r^a\mid m$ with $r$ an odd prime, write $\alpha=\beta^{r^a}$ with the same oriented generators and exponents divided by $r^a$. At every odd $p\le d$ with $p\ne r$ and $r\nmid p-(2/p)$, raising to $r^a$ is an automorphism of the projective unit group modulo $p^k$. Consequently the $\sqrt2$ coefficient of $\beta$ is divisible by $p^k$. All coefficient elements used here are nonzero because their prime ideal support uses only one of the two primes over each $\ell_i$. The archimedean balanced-generator bound gives
\[
          \log|[\sqrt2]\beta|\le (K/(2r^a)+o(1)/r^a)d\log d.
\]
The notation $[\sqrt2]\beta$ denotes the coefficient of $\sqrt2$. The little-oh term is uniform for fixed $K$.

For each fixed odd $r$, the eligible $p$ have Chebyshev weight $(1-1/(r-1)+o(1))d$ by the prime number theorem in residue classes modulo $8r$. If $r\to\infty$ along a subsequence, the excluded weight is $o(d)$ uniformly. For $r\le\sqrt d$, Brun–Titchmarsh in the two residue classes $1,-1\bmod r$ bounds this weight by $O(d/(r-1))$. For $r>\sqrt d$, the elementary interval count gives $O((1+d/r)\log d)$. The possibly omitted prime $p=r$ costs at most $\log d$. Thus every odd prime power $r^a\mid m$ is $O(K)$ for sufficiently large $d$.

For $2^a\mid m$ use $\alpha=\beta^{2^a}$. At $p\equiv5,7\bmod8$, the projective group modulo $p^k$ has 2-primary part of order exactly two. Hence $\beta^2$ is scalar there. These two classes have Chebyshev weight $(1/2+o(1))d$ and the coefficient bound for $\beta^2$ gives $2^a\le 2K+o(1)$. The prime-power bounds give a finite set of possibilities for $m$ at fixed $K$.

Finally write $\alpha=\gamma^m$. Restrict to $p\equiv5,7\bmod8$ for which $r\nmid p-(2/p)$ for every odd prime $r\mid m$, omitting $p\mid m$. Their Chebyshev weight is $(\delta_m+o(1))d$ with
\[
              \delta_m=\tfrac12\prod_{r\mid m,\ r\text{ odd}}(1-1/(r-1)).
\]
For each of the two classes modulo 8 exactly one invertible class modulo $r$ is forbidden, giving this product by the Chinese remainder theorem. At all these primes $\gamma^2$ is scalar. Comparing its coefficient height with $k(\delta_m+o(1))d$ yields $m\le(K+o(1))/\delta_m$. The reciprocal odd-prime product is $O(m/\varphi(m))$: its quotient by the corresponding Euler factors is bounded by $\prod_{r\ge3}(1+1/(r(r-2)))$. The standard Mertens bound $m/\varphi(m)\ll\log\log(3m)$ now gives the result.

## Exponents equal to two modulo four

There is a separate unconditional constraint for $v_2(m)=1$. Write $\alpha=\beta^2$ and let $\Delta_1$ be the signed squarefree part of $N\beta$. Then
\[
           |\Delta_1|\ge d^{\,2\sqrt e-o(1)} .
\]
In particular at least four of the $z_i$ are congruent to $2\pmod4$. Here $\sqrt e$ uses the base of the natural logarithm. The condition on $m$ guarantees a nontrivial odd prime factor of $\Delta_1$.

At each odd $p\le d$ the element $\beta=u+v\sqrt2$ satisfies $2uv\equiv0\pmod p$, since its square is scalar. Its norm therefore has square class either $1$ or $-2$. In particular it is a square at each $p\le d$ that splits in $K_0=\mathbf Q(\sqrt{-2})$. Let $\chi$ be the primitive quadratic character of $\Delta_1$, using its fundamental discriminant, and let $\psi=(-2/\cdot)$. For every odd prime ideal of $K_0$ of norm at most $d$, the character of its norm equals one. A split prime uses the preceding norm condition and an inert prime ideal has norm $p^2$.

Take $1<u<\sqrt e$ fixed and $X=d^u$. The number of odd ideals of $K_0$ of norm at most $X$ is $cX+O(\sqrt X)$ with $c>0$. Indeed $K_0$ has class number one, so this follows by counting its generators in the norm ellipse and excluding multiples of the unique prime above two. If an odd ideal contributes anything other than one to the sum of $\chi$ of its norm, it contains a prime ideal factor of norm exceeding $d$. Counting these factors with multiplicity as an upper bound on bad ideals shows that
\[
  \sum_{N\mathfrak a\le X,\ N\mathfrak a\text{ odd}}\chi(N\mathfrak a)
     \ge cX(1-2\log u+o(1)).
\]
The main term uses the reciprocal prime ideal sum between $d$ and $X$. The lattice counting errors are $O(\sqrt X\sum_{N\mathfrak p\le X}1/\sqrt{N\mathfrak p})=O(X/\log X)$ by partial summation and the prime ideal theorem.

The odd Dirichlet coefficients on the left are those of the convolution of $\chi$ and $\chi\psi$, restricted to odd arguments. Both have the same nontrivial squarefree odd conductor $q=|\Delta_1|$. If $q\le d^{2\sqrt e-\eta}$ for fixed $\eta>0$, choose $u<\sqrt e$ sufficiently close to $\sqrt e$ that $\sqrt X\ge q^{1/4}d^{\eta/8}$. Burgess's interval character-sum bound gives $O(Yd^{-c_\eta})$ for both odd-restricted sums through any $Y\in[\sqrt X,X]$. Indeed one may split the odd arguments into residue classes modulo 8 to remove the fixed two-part and apply the shifted-interval bound for squarefree $q$. Its standard form is $O_{r,\epsilon}(Y^{1-1/r}q^{(r+1)/(4r^2)+\epsilon})$ for every fixed integer $r\ge1$. The Dirichlet hyperbola formula at $\sqrt X$ then gives $O(Xd^{-c_\eta}\log X)$ for the convolution, contradicting the positive lower bound. Finally, any three of the chosen primes have product at most $(C d\log d)^3$, whereas $2\sqrt e>3$.

## A conditional bound after removing the entire common power of two

Under GRH for the Dedekind zeta functions involved, every short vector $\|z\|_1\le Kd$ has $\gg_K\sqrt d/\log d$ coordinates at the **smallest** 2-adic valuation attained by a nonzero coordinate. Indeed write $2^v\parallel m$, $\alpha=\beta^{2^v}$, and let $\Delta_v$ be the signed squarefree part of $N\beta$. Its odd prime factors are precisely the coordinates counted. The bound on the 2-part gives $2^v=O_K(1)$. In the fixed-degree compositum
\[
        E=\mathbf Q(\zeta_{2^{v+3}},\sqrt{\Delta_v})
\]
there is a Galois element fixing the cyclotomic field and negating $\sqrt{\Delta_v}$, since some odd prime ramifies in the quadratic field. Its log discriminant is $O_K(1+\log|\Delta_v|)$ by the compositum discriminant bound. Effective Chebotarev under GRH gives an unramified prime $p\ll_K(1+\log|\Delta_v|)^2$ in this class.

At such a prime the quadratic torus is split, and its cyclic group of order $p-1$ has 2-part divisible by $2^{v+1}$. If $p\le d$, the projective class of $\beta$ has order dividing $2^v$ because $\alpha$ is scalar. That class is a square in the cyclic torus. The norm of a projective square is a square modulo $p$ (multiplying an element by a scalar changes its norm by a square). This contradicts $(\Delta_v/p)=-1$. Thus $p>d$ and $\log|\Delta_v|\gg_K\sqrt d$. Dividing by $\log(Cd\log d)$ gives the asserted count. Even this GRH estimate permits support that is a fixed proper fraction of $d$.
