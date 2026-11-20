# Bounding the index from the product of its four squarefree parts

At a positive odd index \(n\), write \(D_n=\operatorname{sf}(w_na_nc_nd_n)\) and \(D=D_n\). Here \(\operatorname{sf}\) is the product of the primes of odd valuation. The four coordinates are pairwise coprime and are the denominator roots of \(n(G+T)\) for the four rational two-torsion points \(T\), including the identity. The following estimates use the [coordinate identities](abc_full_quartic_signature.md), [two-square-arm theorem](abc_full_quartic_two_square_arms.md) and [square-denominator classification](abc_full_quartic_square_chabauty.md).

## Prime divisors of the index

For every odd prime \(q\), choose one good odd-depth prime \(p\) of \(w_q\) and one of \(a_qc_q\). Both exist by the cited classifications; neither coordinate product is divisible by 3. The two primes differ. More generally, for \(p>3\) dividing \(F_q\) in some arm \(F\), the reduction order of \(G+T_F\) is \(q\). Thus either \(\operatorname{ord}_p(G)=q\) and \(T_F=O\), or \(\operatorname{ord}_p(G)=2q\) and \(qG=T_F\) on reduction. Both \(q\) and the arm are determined by \(p\). Full rational two-torsion gives \(p\ge(2\sqrt q-1)^2>2q\). For the \(w\) arm, if \(q\equiv3\bmod4\), it gives \(p\ge(2q-1)^2>2q^2\) by Gaussian multiplication at the split witness prime. [CM size estimate](abc_full_quartic_prefix_characters.md)

On the distinct prime divisors of \(n\), draw both edges \(q\to p\). The terminal vertices are the children \(p\nmid n\). Distinct edges have distinct children, and all edges increase. Hence these edges form a rooted forest. Every terminal \(p\) divides \(D\), since its odd depth at \(q\) is unchanged at \(n\). Multiplying the two inequalities \(p>2q\) for each \(q\) and cancelling all internal children gives the effective bounds
\[
 \begin{split}
 D&\ \ge 4^{\omega(n)} \operatorname{rad}(n)
          \prod_{\substack{q\mid n\\q\equiv3\ (4)}}q\prod_{q\ {\rm root}}q ,
       \qquad \omega(n)+\#\{\text{roots}\}\le\omega(D),\\
 P^+(n)&<\sqrt D/2\qquad(n>1).
 \end{split}
\]
Indeed both children of the largest prime divisor are terminal. The leaf count is the binary forest identity \(L=I+\#\{\text{roots}\}\). A terminal prime can appear in the product only once.

There is an absolute finite set \(S_0\) outside which each of the four arms at prime index has an odd-depth good prime: in each arm a failure would give squarefree part 1 or 3, each attained by only finitely many indices by [uniform multiplicity](abc_full_quartic_four_squarefree_parts.md). Draw all four edges outside \(S_0\) and the two known ones at the other vertices. Missing factors of \(2q\) over this fixed finite set cost only an absolute constant. With the roots of this enlarged forest one obtains
\[
        D\gg 2^{4\omega(n)}\operatorname{rad}(n)^3
        \prod_{\substack{q\mid n\\q\equiv3\ (4)}}q\prod_{q\ {\rm root}}q .
\]
Consequently \(D\gg n^3\) for all squarefree \(n\), and \(D\gg n^4\) for squarefree indices supported on primes \(3\bmod4\). If every exponent in \(n\) is at most \(E\) then \(n\ll_E D^{E/3}\). For prime indices one gets \(D_q\gg q^4\) and \(D_q\gg q^5\) at inert \(q\). The finite exceptional set need not be computed for these asymptotic statements.

## Inheritance and effective search

For any divisor \(m\mid n\), \(D_m\mid D\,\operatorname{rad}(n)\). A good prime of odd depth at \(m\) which loses its parity at \(n\) must divide \(n/m\), by the formal-group valuation formula applied to the appropriate translated point. The only possible bad prime is 3, whose valuation in \(d_j\) is \(v_3(j)\), so the same holds there. If \(n/m\) is a square, the multiplier adds only even valuations, which proves \(D_m\mid D\) exactly. In particular
\[
 \tau\bigl(\sqrt{n/\operatorname{sf}(n)}\bigr)\le N(D),\qquad
 \tau(n)\le2^{\omega(D)}N(D)=O(D^{\beta+o(1)}),
\]
where \(N(Y)\) counts all positive odd indices with total kernel at most \(Y\) and \(\beta<1/8\) is the [inverse-sieve exponent](abc_full_quartic_four_arm_inverse_sieve.md). For the first assertion the admissible divisors include \(\operatorname{sf}(n)j^2\) for every \(j\mid\sqrt{n/\operatorname{sf}(n)}\). The second uses \(e+1\le2(\lfloor e/2\rfloor+1)\). Parities need only be fixed at primes dividing \(n\) that can cause an ordinary lift in some arm at an odd divisor.

In fact twist multiplicity improves the divisor count to \(\tau(n)\ll C^{\omega(D)}=D^{o(1)}\), with an absolute constant. Write \(K\) for the constant in the one-arm bound \(K^{1+\omega(d)}\). For every \(j\mid \sqrt{n/\operatorname{sf}(n)}\), the squarefree part of the same chosen arm at \(\operatorname{sf}(n)j^2\) divides its kernel \(D_F\) at \(n\). Summing over its divisors and choosing the arm with the fewest support primes gives
\[
 \tau\bigl(\sqrt{n/\operatorname{sf}(n)}\bigr)
      \le K(1+K)^{\min_F\omega(D_F)}
      \le K(1+K)^{\omega(D)/4}.
\]
The four-child leaf count gives \(3\omega(n)\le\omega(D)+O(1)\). Thus \(\omega(D)\gg\log\tau(n)-O(1)\), including indices with many distinct repeated prime factors.

There is a common effective support set for every \(n\) with \(D_n\mid A\), for fixed squarefree \(A\). Process all odd primes \(q<\sqrt{A}/2\) in descending order, retaining a prime precisely when all good odd-depth primes of its four coordinate values at \(q\) belong to the primes of \(A\) or to previously retained primes. It suffices to divide out those known primes and 3, then square-test the remainder. If \(q\) actually divides such an \(n\), all these primes are either in \(A\) or are larger prime factors of \(n\), so descending induction never removes \(q\). The retained set itself carries the binary forest, since each retained \(q\) has its predetermined two children in the allowed set. Hence the squarefree product \(Q(A)\) of all retained primes satisfies \(4^{\omega(Q(A))}Q(A)\le A\) and \(\omega(Q(A))\le\omega(A)-1\) when the retained set is nonempty. In particular \(\operatorname{rad}(n)\mid Q(A)\) for every such index. The largest exponent \(v_q(n)\) is at most \(2K(1+K)^{\omega(A)/4}\) by the square-multiplier estimate. The lcm of **all** the indices with \(D_n\mid A\) consequently divides \(Q(A)^{\lceil 2K(1+K)^{\omega(A)/4}\rceil}\). For fixed \(\omega(A)\) this bounds the simultaneous lcm polynomially in \(A\).

The binary bound \(\operatorname{rad}(n)\le D\) has an effective consequence. If \(D\le Y\), every \(q\mid n\) is less than \(\sqrt Y/2\), and \(\operatorname{sf}(w_q)\mid D\,\operatorname{rad}(n)\) is at most \(Y^2\). In the [effective prime-power test](abc_full_quartic_inverse_kernel_sieve.md), strip \(B_q\) by primes through \(Y\), require a square remainder and \(\operatorname{sf}(w_q)\le Y^2\), then take the CRT modulus \(4q\operatorname{sf}(w_q)=O(Y^{5/2})\). Linnik's theorem gives the detecting prime \(h\ll Y^{C}\) with an absolute effective constant after enlarging \(C\). The periodic certificate gives \(v_q(n)\le h+2+\log(2Y)/\log q\). Thus
\[
               n\le \exp(Y^{O(1)})
\]
with effective constants; the exact census of all indices with total kernel at most \(Y\) fits the same bound in bit operations. One can form the product of the permitted powers over all \(q\le\sqrt Y/2\), enumerate its divisors, and square-test the four coordinate remainders after stripping primes through \(Y\). The earlier one-arm search bound was \(\exp(\exp(O((\log(2Y))^2)))\). Separately, genus-three uniform multiplicity already gives the stronger noneffective-in-this-computation growth bound \(\log n\le\exp(O(\log(2D)/\log\log(3D)))\) as \(D\to\infty\); the inverse count with fixed exponent \(\beta\) alone cannot improve that bound.

## Arbitrary exponents at the certified prime multipliers

Let \(M=144923830996024080\), and let \(\mathcal S\) consist of the odd primes \(q\not\equiv\pm1\bmod M\). The [prefix character certificate](abc_full_quartic_prefix_characters.md) supplies, for each \(q\in\mathcal S\) and \(1\le j\le e_q=v_q(n)\), a distinct odd-depth prime in \(w_n\) whose rank is divisible by \(q^j\). Its size exceeds \(2q^j\), or \(2q^{2j}\) when \(q\equiv3\bmod4\).

Use three prime-index child edges from the arms \(a,c,d\) at \(q\in\mathcal S\), and all four at \(q\notin\mathcal S\), apart from the finite exceptions \(S_0\). At an exceptional vertex use the \(ac\) child and, when \(q\notin\mathcal S\), the \(w\) child. The terminal witnesses of this forest are distinct from all the prefix witnesses: they either lie in another coordinate, or are \(w\)-witnesses of prime rank outside \(\mathcal S\). Multiplying both collections and cancelling internal children therefore gives
\[
 D\gg
 \prod_{\substack{q\in\mathcal S,\ q\mid n\\q\equiv1\ (4)}}
    q^{e_q(e_q+1)/2+2}
 \prod_{\substack{q\in\mathcal S,\ q\mid n\\q\equiv3\ (4)}}
    q^{e_q(e_q+1)+2}
 \prod_{\substack{q\notin\mathcal S,\ q\mid n\\q\equiv1\ (4)}}q^3
 \prod_{\substack{q\notin\mathcal S,\ q\mid n\\q\equiv3\ (4)}}q^4 .
\]
For integral \(e\ge1\), \(e(e+1)/2+2\ge5e/2\) and \(e(e+1)+2\ge4e\). Hence \(D_n\gg n^{5/2}\) whenever the primes outside \(\mathcal S\) occur at most once. If all prime divisors are \(3\bmod4\), the same hypothesis gives \(D_n\gg n^4\). Integers excluded by this divisibility hypothesis have upper density at most \(\sum_{q\equiv\pm1\bmod M}q^{-2}=O(M^{-2})\); this describes a concrete set at every scale. The all-index inverse estimate gives stronger density conclusions without this explicit divisibility description.

One may adjoin any fixed finite set of primes to \(\mathcal S\), changing the implied constant. For each such \(q\), only finitely many positive odd \(m\) make \(B_{qm}/B_m\) a square by [the fixed-multiplier finiteness proof](abc_congruent_six_smooth_odd_primitive.md). At every other descending prefix the same fresh-witness proof applies. The factors lost at the finitely many exceptional \(m\) are bounded independently of \(n\), since \(q^j\mid qm\) at each such step.

## A fourth-power pointwise bound with exceptional prime factors allowed

For the [four-arm prefix theorem](abc_full_quartic_four_arm_prefixes.md) take its modulus \(M_4=11210216592196440\) and certified primes \(q\not\equiv\pm1\bmod M_4\). At each excluded prime \(q\equiv\pm1\bmod M_4\), select the smallest good odd-depth prime \(p_F(q)\) in each arm at index \(q\) where such a prime exists. Disallow the divisibility patterns \(q^2\mid n\) and \(q p_F(q)\mid n\) for these \(q\). On all remaining odd indices,
\[
       D_n\gg16^{\Omega(n)}n^4
                    \prod_{\substack{q\mid n\\q\equiv3\ (4)}}q^{v_q(n)} .
\]
Indeed the four-arm prefix witnesses supply this bound for every certified prime factor counted with its exponent. An excluded prime factor has exponent one, and each selected odd-depth witness at its prime index survives at \(n\), since the forbidden pattern ensures \(p_F(q)\nmid n\). Its order for the translated arm is exactly \(q\), distinct from all the prefix orders in that arm, each of which is divisible by a certified prime. Distinct excluded prime indices give distinct orders as well. Outside the finite \(S_0\) the four prime-index witnesses give at least \(16q^{4+{\bf1}_{q\equiv3\bmod4}}\); missing factors at the finitely many other \(q\) cost one absolute constant since their index exponents are at most one.

The remaining indices have relative natural density among odd integers at least \(1-\pi^2/(M_4-1)^2>1-8\cdot10^{-32}\). For each excluded \(q\) the forbidden patterns have combined upper density at most \(q^{-2}+\sum_F (qp_F(q))^{-1}<3q^{-2}\). Their total is at most \(6\zeta(2)/(M_4-1)^2\), by summation over \(kM_4\pm1\) with positive integral \(k\). The omitted tails of the periodic conditions have uniformly vanishing upper density by the same convergent series, giving existence of the natural density. This statement allows excluded primes to divide the index and has an implicit multiplicative constant. The coefficient-one bound of the four-arm prefix theorem applies to the certified prime factors at every index.
