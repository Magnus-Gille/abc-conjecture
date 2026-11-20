# Simultaneous prescribed valuations with two multiplicative parameters

Fix a nonempty finite set \(\mathcal P\) of odd good primes at which the full rank-eleven binary form \(F=F_{11}\) has a simple projective root of unit quadratic norm. For instance take \(683,1409\). Write \(D=\prod_{p\in\mathcal P}p\). In the degree-968 family of primitive positive triples there are infinitely many triples and integers \(k\to\infty\) such that
\[
 \begin{split}
   v_p(F(a,b))&=k,\qquad v_p(C)=8k \quad(p\in\mathcal P),\\
   \log C&\ll_{\mathcal P}D^{k/2},\\
   \frac C{\operatorname{rad}(ABC)}&\gg_{\mathcal P}D^{k-1}
                       \gg_{\mathcal P}(\log C)^2 .
 \end{split}
\]
The same fixed prime set is used at every depth. One can select the residue class of the next nonzero local digit independently at every marked prime. The construction uses two exponents in the original rational parameter space. The individual parameters need not be units of norm one. The radical of their norm stays bounded. [Triple, height and radical inequality](abc_cm_pell_whole_triple.md)

## A fixed group that reaches all local lifts

Work in \(\mathcal O=\mathbf Z[\sqrt2]\), writing \(\alpha=b+a\sqrt2\) for the projective parameter. By the ordinary Chinese remainder theorem pick a fixed \(\gamma\in\mathcal O\) whose coefficient pair represents the chosen root modulo each \(p\), with \(p\nmid N(\gamma)\). Put
\[
       \eta_1=1+D\sqrt2,\qquad \eta_2=1+2D\sqrt2.
\]
The absolute norms \(2D^2-1\) and \(8D^2-1\) are odd, greater than one, and coprime. Their gcd divides 3 and the first norm is nonzero modulo 3. No odd prime ideal can divide both \(\eta_i\) and its conjugate because their sum is 2. At a prime ideal over a divisor of the corresponding norm, the ratio \(\eta_i/\bar\eta_i\) therefore has nonzero valuation while the other generator ratio is a unit. In particular \(\eta_1^x\eta_2^y\) is projectively scalar over \(\mathbf Q\) only at \(x=y=0\).

At each marked \(p\), the projective classes of units modulo \(p^j\) are units in \(\mathcal O/p^j\) modulo scalar units in \(\mathbf Z/p^j\). The kernel of reduction to precision one has size \(p^{j-1}\), by the elementary counts of units in the split or unramified quadratic algebra. The ratio \(\eta_1/\bar\eta_1\) differs from 1 to exact depth one since \(D\) is squarefree and \(p\) is odd. Binomial lifting gives \(\eta_1\) projective order \(p^{j-1}\). Thus it generates this whole kernel. At all marked primes together it generates the product of the kernels, since their orders are coprime.

Let \(\Lambda_j\subset\mathbf Z^2\) consist of exponents for which \(\eta_1^x\eta_2^y\) is projectively scalar at all marked primes to precision \(j\). Then
\[
 [\mathbf Z^2:\Lambda_j]=D^{j-1},\qquad D\Lambda_j\subseteq\Lambda_{j+1}\subseteq\Lambda_j.
\]
Every simultaneous lift of the original projective residues to precision \(j\) is attained by one translate of \(\Lambda_j\), after multiplying by \(\gamma\). This holds because the parameters under consideration are local units, and any two lifts of the same projective residue differ by an element of the principal kernel.

## Short representatives at infinitely many precisions

Let \(s_j\) be a shortest nonzero vector of \(\Lambda_j\) in the Euclidean norm, breaking ties by any fixed rule. Minkowski's theorem gives \(\|s_j\|\ll D^{(j-1)/2}\). The directions of \(s_j\) change infinitely often. Otherwise, for a fixed primitive direction \(w=(w_1,w_2)\) every \(s_j\) from some point on would be a multiple of \(w\). Put \(z=\prod_i(\eta_i/\bar\eta_i)^{w_i}\). It is different from 1, lies in the principal units at all marked primes, and has finite depth \(e_p=v_p(z-1)\ge1\) at each, using either place in the split case. Thus a multiple \(t w\in\Lambda_j\) requires \(p^{\max(0,j-e_p)}\mid t\) for each \(p\). The shortest such multiple has norm \(\gg_w D^j\) for large \(j\), contradicting Minkowski.

At a change of direction, \(s_j,s_{j+1}\) are two independent vectors in \(\Lambda_j\). Both have length \(O_{\mathcal P}(D^{(j-1)/2})\), as follows either from the same Minkowski bound at \(j+1\) or by using \(D s_j\) as a candidate vector. Their parallelogram supplies a representative of this size for every translate of \(\Lambda_j\): subtract integer multiples of both vectors to put any given representative in the centered parallelogram. They need not form a basis of the full lattice.

At such \(j\ge3\), take \(k=j-1\). Hensel's lemma at each simple root provides a projective class modulo \(p^{k+1}\) of exact valuation \(k\), or one having any prescribed nonzero next digit in a fixed local coordinate. Choose a short exponent pair in the corresponding simultaneous translate. Replace negative powers of \(\eta_i\) by positive powers of its conjugate, which changes only the global scalar. Form the integral representative \(\gamma\prod_i\eta_i^{x_i}\) in this manner and divide its coefficients by their gcd. Every marked prime is a unit in its norm, so this preserves its projective class there. The prime divisors of the primitive norm \(J=b^2-2a^2\) are among those of \(N(\gamma)N(\eta_1)N(\eta_2)\), a fixed integer. The height \(H=\max(|a|,|b|)\) satisfies \(\log(2H)\ll_{\mathcal P}1+|x|+|y|\). The fixed map has \(\log C=968\log H+O(1)\), and
\[
 \frac C{\operatorname{rad}(ABC)}\gg
 \frac{|F(a,b)|}{\operatorname{rad}(|F(a,b)|)\operatorname{rad}(|J|)} .
\]
The marked prime contribution to its numerator ratio is exactly \(D^{k-1}\). This proves the assertions. The unbounded exact valuations force the triples to vary. Finitely many degenerate parameters can be omitted.

## A two-prime check

For \(D=683\cdot1409=962347\) take \(\gamma=1+646161\sqrt2\). The two roots come from the known Pell indices 1213 and 3706 respectively. At \(k=8\), one solution is
\[
    x=-99834565206991281806231,\qquad y=45401227675107833523491 .
\]
The modular computation evaluates the unnormalized abscissa polynomial \(G_{11}\) at the resulting parameter. After dividing by \(p^8\), its residues modulo \(683,1409\) are 223 and 257, respectively. Its conversion to the primitive binary form multiplies by a unit at both primes. Thus \(683^8\) and \(1409^8\) each divide the primitive form exactly, giving exact exponent 64 in \(C\) at both primes. The verifier reconstructs the cosets by digit lifting, reduces their exponent lattices in dimension two, then checks the actual parameter evaluations. [Exact verifier](abc_rank_two_marked_depth.py)

The implied constants depend on the marked set. A squared logarithm in the lower bound grows more slowly than every fixed positive power of \(C\). In fact fixed-prime logarithmic forms bound the saving contributed by these fixed primes in this fixed finitely generated parameter group by a power of \(\log C\). Contributions from other primes are not bounded by that argument.
