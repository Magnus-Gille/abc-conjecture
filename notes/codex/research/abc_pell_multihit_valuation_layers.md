# Three or more visits to a prime-power layer of the rank-eleven Pell sequence

Put \(F_n=|F_{11}(a_n,b_n)|\), with \(b_n+a_n\sqrt2=(1+\sqrt2)^n\), and \(g=(1+\sqrt2)^4\). For \(1\le n\le N\) regard the occurrence of \(p^j\mid F_n\) as a layer of weight \(\log p\). Write \(c_{p,j}(N)=\#\{n\le N:p^j\mid F_n\}\). For \(3\le s\le50\),

\[
 \sum_{\substack{p,j\ge1\\c_{p,j}(N)\ge s}}
       c_{p,j}(N)\log p
       \ll_s N^{3/2}+N^{1+2/s}.                                  \tag{1}
\]

At good layers of local order \(r_{p,j}>N\), the sharper \(O_s(N^{1+2/s})\) holds on its own. In particular the total logarithmic mass of layers seen in at least three terms is \(O(N^{5/3})\), and in at least four terms it is \(O(N^{3/2})\). These estimates permit arbitrary prime powers and count every occurrence of each qualifying layer. [The two-visit logarithmic estimate](abc_pell_lcm_sharp_rate.md) · [The rank-50 certificate](abc_cm_pell_target_rank.md)

## A small integer relation among indices

For \(s\) positive integers \(n_1,\ldots,n_s\le N\) there exist integers \(b_1,\ldots,b_s,h\), with the \(b_i\) not all zero, such that

\[
                 h=\sum_{i=1}^s b_i n_i,\qquad
                 \max_i|b_i|,\ |h|\ll_s N^{1/s}.
\]

Indeed choose \(H=\lceil(3sN)^{1/s}\rceil\). The \((H+1)^s\) sums \(\sum c_i n_i\), \(0\le c_i\le H\), belong to the integer interval \([0,sHN]\). Sorting them into consecutive intervals of length \(H\) gives at most \(sN+1\) boxes. Two coefficient vectors lie in the same box, and subtracting them proves the assertion.

## Capturing all long-order layers

Fix one place over each good \(p\) in a common splitting field. At a hit \(g^n\equiv u\bmod p^j\) for a unique one of the 50 targets \(u\). If \(r_{p,j}>N\), two hits at different \(n\le N\) cannot have the same target. Choose \(s\) hits and the resulting distinct \(u_1,\ldots,u_s\). The relation just found gives

\[
           g^{-h}\prod_{i=1}^s u_i^{b_i}-1\equiv0\bmod p^j.       \tag{2}
\]

For \(s<50\) the expression in (2) is nonzero by multiplicative independence of every proper subset of the targets together with \(g\). For \(s=50\) the primitive relation is \(g^{12}\prod_i u_i=1\). An identically zero expression would require all \(b_i=b\) and \(h=-12b\); but \(h=b\sum_i n_i\), and the indices are positive, forcing \(b=0\). Thus the expression in (2) has a nonzero numerator ideal. This uses the full independence certification for the rank-eleven factor.

Across all possible index tuples, the number of possible \((b_1,\ldots,b_s,h)\) in this box is \(O_s(N^{1+1/s})\). Each of the finitely many target assignments gives a numerator norm of logarithm \(O_s(N^{1/s})\), by the absolute height inequality. Take the product over all these possibilities, omitting identically zero expressions. Every captured prime power divides this integer. Its logarithm bounds the total weight of all distinct captured layers because each prime is covered through its largest captured exponent. There are at most 50 occurrences per long-order layer. This proves their asserted contribution. The total incidence mass of all layers of order at most \(N\) is \(O(N^{3/2})\) by the rank-two short-period estimate and partial summation. The omitted fixed primes contribute \(O(N)\), proving (1). [Short-order incidence proof](abc_cm_pell_lcm.md)

The same argument also gives a one-modulus statement. Suppose an arbitrary integer \(D\) divides each of \(F_{n_1},\ldots,F_{n_s}\), \(n_i\le N\), and the prime powers comprising \(D\) have order greater than \(N\) and are good. Use the *same* small relation for all its prime divisors, multiplying over the finite possible target tuples only. Then \(\log D\ll_s N^{1/s}\). Orders greater than \(N\) may be replaced by the requirement that the chosen target labels at the full precision of each prime power are all distinct. In particular, an exponentially large divisor of \(F_n\), if later seen in these distinct positions \(s\) times, requires an index \(\gg_s (\log D)^s\).

## Consequences for full valuations at repeated prime bases

At each prime keep just its two largest valuations among \(F_1,\ldots,F_N\), with ties assigned arbitrarily. The total logarithmic mass of all valuations omitted in doing this is \(O(N^{5/3})\). Indeed the omitted mass at \(p^j\) is \(\max(c_{p,j}(N)-2,0)\log p\). Keeping three instead gives error \(O(N^{3/2})\). This controls full valuations even when the exponents grow with \(N\).

More generally, at an index \(n\le N\), count the full mass \(v_p(F_n)\log p\) of primes such that at least two other indices \(m\le N\) have
\[
          v_p(F_m)\ge v_p(F_n)/K,\qquad K\ge1.
\]
Every one of the first \(\lceil v_p(F_n)/K\rceil\) layers occurs at least three times, one of those times at \(n\), so all the counted mass through \(N\) is \(O(KN^{5/3})\). For at least three other indices the bound is \(O(KN^{3/2})\). Consequently, at tolerance \(\delta n\) on \(N\le n<2N\), the number of exceptional indices is \(O_\delta(KN^{2/3})\) and \(O_\delta(KN^{1/2})\), respectively, when comparisons are made among indices through \(2N\). A positive-density concentration of repeated-prime excess must therefore use primes with few other hits at comparable precision or much larger valuations at the current term. These comparisons do not detect a large prime square used by a single term.

## Layers with many distinct targets anywhere in one complete period

For a good \(p\), let \(r_p=\operatorname{ord}_p(g)\), \(w_p=v_p(g^{r_p}-1)\), and \(h_{p,j}\) be the number of the 50 targets in the cyclic group generated by \(g\bmod p^j\) at the chosen place. Fix \(1\le s\le50\) and write \(t=\min(s+1,50)\). Put
\[
        Y=N^{2t/(t+1)}(\log(2N))^{t/(t+1)} .
\]
Then
\[
 \sum_{n\le N}
   \sum_{\substack{p\le Y\ {\rm good},\ 1\le j\le\min(v_p(F_n),w_p)\\
                         h_{p,j}\ge s}}\log p=o(N^2).               \tag{3}
\]
For \(s=1\) the prime range has exponent \(4/3\), and for \(s\ge49\) it has exponent \(100/51\). The extra precision \(j>w_p\) is treated separately by the ordinary order growth. [Valuation bounds including ordinary lifts](abc_pell_composite_valuation_mass.md)

Indeed let \(m_p\) be the largest \(j\le w_p\) at which \(h_{p,j}\ge s\), or zero if there is none. Choose \(t-1\) of these distinct targets. Together with \(g\) they are multiplicatively independent, even for \(s=50\), because only 49 targets are needed in that case. Their reductions generate a group of order \(r_p\) at the indicated precision.

For any fixed \(t\) multiplicatively independent \(S\)-units, and ideals \(I\) outside \(S\) where their generated group has size at most \(H\), one has \(\log N I=o(H^{1/t})\) uniformly as \(H\to\infty\). For the \(O\)-bound use a short relation of length \(O_t(H^{1/t})\). If the little-oh fails, every nonzero relation has length \(\gg H^{1/t}\) along a subsequence by the numerator-norm bound. The lattice has covolume at most \(H\), so by Minkowski's successive minima theorem all its successive minima are \(O(H^{1/t})\). Take two independent short vectors. The resulting two \(S\)-units have height \(O(H^{1/t})\) and reduce to one modulo \(I\). The logarithmic gcd theorem puts an infinite subsequence on a fixed equation \(x^a y^b=c\) with \((a,b)\ne(0,0)\), just as in the rank-two argument. This gives a fixed nonzero combination vector of bounded length in all the lattices, a contradiction. Thus \(m_p\log p=o(r_p^{1/t})\), uniformly since the set of target tuples is finite. The proof uses \(t\ge2\).

The distinct-layer endpoint contribution to (3) is consequently \(o(Y^{1+1/t}/\log Y)=o(N^2)\) by the elementary prime count upper bound, since \(r_p\le p+1\). For the terms \(N/r_p\) in local occurrence counts, the weight of layers with \(r_p\le R\), \(j\le w_p\) and \(h_{p,j}\ge s\) is \(O_s(R^{1+1/t})\). For such a layer use a \(t\)-dimensional monomial box of side \(\lfloor R^{1/t}\rfloor+1\) in the same independent elements. It gives a nonzero relation modulo the layer with coefficients \(O(R^{1/t})\). The log product of all possible numerator norms is \(O_s(R^{1+1/t})\). Partial summation therefore bounds the remaining aggregate by \(O_s(NY^{1/t})=o(N^2)\), proving (3).
