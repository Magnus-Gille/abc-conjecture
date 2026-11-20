# How much degree is needed to mark a moving CM point?

Let \(A=(1,1)\) on \(E:v^2=u^3-8u^2+8u\), with \(\tau=\sqrt{-2}\) its complex multiplication. For a positive integer \(b\) consider any Belyi map on \(E\) whose fibers above \(0,1,\infty\) contain both \(\pm[b\tau]A\). Its degree \(d_b\) satisfies, for all sufficiently large \(b\),
\[
 d_b\ge\begin{cases}2b^2+1& b\text{ odd},\\ 32b^2+1& b\text{ even}.\end{cases}
\]
The bounds also hold for the degree of a Belyi map on the abscissa line marking \(u([b\tau]A)\) and the four abscissas of \(E[2]\). Thus the fixed-degree construction for \(b=1\) cannot extend with bounded degree to arbitrarily large moving multipliers. A degree estimate alone gives no uniform control on coefficients or on heights at a single input when the map varies. [Fixed map and abc application](abc_short_cm_contacts.md)

## Collision primes

For \(p>d_b\) the Galois closure of a degree-\(d_b\) cover has group of order prime to \(p\), since it embeds in the symmetric group. By prime-to-\(p\) specialization of tame covers of the three-pointed projective line, after a finite extension the cover has good reduction, with special points over \(0,1,\infty\) remaining distinct. This uses the good reduction theorem for tame three-point covers (Grothendieck, *SGA 1*, Exposé XIII). Distinctness includes unramified points. The number of geometric points in the three generic fibers is \(d_b+2-2g\) by Riemann–Hurwitz. Any collision would lower this count in the special fibers and exceed the total available different of their separable reduction. On an elliptic curve with good reduction the smooth proper model with its origin is unique; translations extend as well. On the abscissa line one can normalize three fixed branch abscissas to \(0,1,\infty\). They stay distinct at all odd primes and determine the same good model. Therefore if the two elliptic marks specialize together, or if the marked abscissa specializes to a branch abscissa, the degree is at least \(p\).

On \(E':y^2=x^3+16x^2+32x\) take \(R=(-8,16)\). The rational two-isogeny from \(E\) sends \(A\) to \(2R\) and has the same kernel as \(\tau\); the identification with the twist is an isomorphism at odd primes. Every odd prime dividing the abscissa denominator at \([4b]R\) therefore forces \([2b\tau]A=O\) in reduction. The two distinct generic marks then coincide in the special fiber at a two-torsion point. It suffices to find a large prime divisor of that denominator.

## Exact annihilator ideals at even indices

Use \(D(\alpha)\) for the **logarithm** of the norm of the odd square-root denominator ideal of \(x([\alpha]R)\), and \(F(\mathfrak a)\) for the weighted sum of first depths at places whose exact annihilator of \(R\) is \(\mathfrak a\). At odd places the formal logarithm is an isometry, and summing lifting increments gives
\[
 D(\alpha)=\sum_{\mathfrak a\mid(\alpha)}F(\mathfrak a)+O(\log(2\operatorname N\alpha)).
\]
This identity allows both split and inert places, with logarithms of residue field norms. It only uses good reduction at odd places. For odd \(n\), the fixed real component and ideal Möbius argument already give \(F((n))=2\widehat h(R)\Phi_K((n))+O(2^{\omega_K(n)}\log(2n))\), positive for large \(n\), where \(\Phi_K\) is the ideal Euler totient and \(\omega_K(n)\) counts the prime ideals dividing \((n)\). [Odd-index proof](abc_octic_mixed_cm_prime_mass.md)

For \(4\mid n\) we prove the same formula without an elliptic logarithm lower bound. For each odd ideal divisor \((\beta)\) of \((n)\), put \(P=[n/(2\beta)]R\). The canonical-height difference between the abscissas of \(2P\) and \(\tau P\) is \(\widehat h(R)n^2/\operatorname N\beta+O(1)\) in absolute logarithmic abscissa-height normalization, by the degrees of the two multipliers. At either complex embedding the difference of their \(\log^+|x|\) terms is bounded near \(O\) and \(J'=(0,0)\), since both abscissas have double poles in the variable \(P\) there. The only other poles of either term occur at the two non-\(J'\) two-torsion points \(T_+,T_-\), and the discrepancy is bounded by a constant plus twice the logarithmic proximity to them. Both lie on the bounded real component. The odd-norm multiplier \(\beta\) permutes them since it acts invertibly on \(E'[2]\) and preserves \(\ker\tau=\{O,J'\}\). Meanwhile \([\beta]P=[n/2]R\) stays on the real identity component, a fixed positive torus distance from them. Its \(\sqrt{\operatorname N\beta}\)-Lipschitz multiplier bounds the proximities by \(O(\log(2n))\). At the dyadic place both denominator contributions are \(O(\log(2n))\): the complementary multipliers send each point to \(\pm[n]R\), cannot decrease depth in a sufficiently deep stable formal logarithm neighborhood, and the depth of integer multiples of a fixed point at a fixed place is \(O(\log(2n))\) by formal lifting. These bounds also hold at the conjugate embedding.

As a result
\[
 D(n/\beta)-D(n/(\tau\beta))=\widehat h(R)n^2/\operatorname N\beta+O(\log(2n)).
\]
The difference retains precisely the annihilator terms with full dyadic ideal exponent. Möbius inversion on the odd part leaves \(F((n))\) with main term \(\widehat h(R)n^2\prod_{\mathfrak q\mid(n),\,\mathfrak q\nmid2}(1-1/\operatorname N\mathfrak q)=2\widehat h(R)\Phi_K((n))\). There are at most \(2^{\omega_K(n)}\) nonzero Möbius terms. The error is \(n^{o(1)}\) and the main term is \(n^{2-o(1)}\). Thus some odd place has annihilator exactly \((n)\).

## A split witness and its size

For odd \(b\), take \(n=b\). All odd denominator primes at this odd index split: they divide the primitive norm \(s_n^2+2t_n^2\). For even \(b\), take \(n=4b\), so \(8\mid n\). At a place of exact annihilator \((n)\), the rational reduction of \(R\) has order \(n\). Also \([n/2]R\) is a nonzero two-torsion point distinct from \(J'\), since otherwise \(\tau n/2\notin(n)\) would annihilate \(R\). An inert prime would have group size \(p+1\). The full rational two-torsion together with \(R\) forces \(2n\mid p+1\), hence \(p\equiv-1\bmod16\). Then \(J'\) has a rational half, while the independent point \([n/2]R\) also has a rational half. This contradicts the Weil pairing on \(E'[4]\) since \(p\equiv3\bmod4\). [Explicit rational half](abc_dyadic_cm_largest_prime.md)

At the resulting split place, Frobenius is \(\pi=1+n(a+c\tau)\) of norm \(p\), since it fixes \(R\). Here \(c\ne0\) because \(p\) is prime. This gives \(p=(1+na)^2+2n^2c^2\ge2n^2+1\). The prime divides the denominator at \([4b]R\), proving the degree bounds.

## What happens for the prime 205883

The scalar realizing \(\tau\) at one place is \(8443\bmod34387\). Multiplying it by 4 instead of 1 gives the signed representative \(-615\); multiplying it by 57 gives \(-167\). These smaller indices require different marks. For \(b=4\), the prime \(22151840117633\) has order 16 for \(R\) and forces degree at least \(22151840117633\). For \(b=57\), the prime \(7393900643053507997\) has order 19 for \(A\), and hence \([57]A=O\) there; it forces degree at least \(7393900643053507997\). The lower bounds are unconditional and concern these two specific choices of marks. [Finite certificates](abc_moving_mark_degree_verify.py)
