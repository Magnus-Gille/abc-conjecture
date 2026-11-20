# A fixed-set finiteness result for primitive abc triples

Fix a finite set \(S\) of odd primes. Consider primitive positive triples \(a+b=c\) with \(16\mid abc\) for which there is a prime \(\ell\ge5\) such that
\[
 \ell\mid v_q(abc)\qquad\text{for every odd }q\notin S .
\]
Both \(\ell\) and all the primes dividing \(abc\) outside \(S\) may vary.

If there is **no** primitive triple \(a_0+b_0=c_0\) with \(16\mid a_0b_0c_0\) and all prime factors in \(\{2\}\cup S\), the above class is finite. In particular this holds for every fixed finite \(S\) made up of primes \(1\bmod12\). This is a pointwise finiteness result even though the complete radical of the triples is allowed to vary.

## Excluding arbitrarily large common exponents

Suppose admissible primes \(\ell\) are unbounded. Use signed terms \(A+B=C\), obtained from the given triple by reordering and sign, with \(16\mid B\) and \(A\equiv-1\bmod4\). The Frey curve
\[
 E:\ y^2=x(x-A)(x+B)
\]
is semistable with full rational 2-torsion. At 2, the integral change of model \(x=4X,\ y=8Y+4X\) gives coefficients \((B-A-1)/4,-AB/16\) for \(X^2,X\) on the right of \(Y^2+XY\). Its discriminant is \((ABC)^2/2^8\) and its \(c_4=A^2+AB+B^2\) is odd. At an odd prime dividing \(ABC\) the reduction is multiplicative and \(v_q(\Delta_{\min})=2v_q(ABC)\). All other odd primes have good reduction.

For the unbounded-exponent argument take \(\ell\) larger than \(163\), all primes of \(L=2\prod_{p\in S}p\), and \(\varphi(L)\). The rational isogeny theorem gives irreducibility of \(E[\ell]\). Use modularity and weight-two level lowering for semistable elliptic curves over \(\mathbb Q\): an odd multiplicative prime \(q\ne\ell\) with \(\ell\mid v_q(\Delta_{\min})\) disappears from the mod-\(\ell\) conductor. At \(\ell\), the representation is finite flat if the curve is good or if its Tate parameter has valuation divisible by \(\ell\), as happens here. Thus the lowered representation comes from a weight-two newform at a level dividing \(L\). The character is trivial, since the determinant forces it to reduce trivially and its order divides \(\varphi(L)<\ell\). One can equivalently use the weight and level conclusions in Serre's modularity theorem. These are uses of established modularity theorems, not effective bounds for \(abc\).

There are finitely many such newforms. Fix one \(f\) which works for unboundedly many \(\ell\), and fix a prime \(r\nmid L\). For \(\ell\ne r\), the congruence gives \(a_r(f)\bmod\ell\) equal, modulo a prime of its coefficient field above \(\ell\), to one of the following integers:

* At a good Frey prime, a trace \(t\) with \(|t|\le2\sqrt r\) and \(t\equiv r+1\bmod4\), because the full rational 2-torsion injects on reduction.
* At a multiplicative Frey prime removed from its level, one of \(\pm(r+1)\), from the unramified residual semisimplification of the Tate representation.

For this fixed \(r\) only finitely many integers occur. Equality in characteristic zero with one of them follows since the norm of a nonzero algebraic integer has only finitely many prime divisors. Deligne's bound rules out \(\pm(r+1)\). Hence \(a_r(f)\in\mathbb Z\) and \(a_r(f)\equiv r+1\bmod4\) for all \(r\nmid L\). Strong multiplicity one gives rational coefficient field. The elliptic curve \(E_f/\mathbb Q\) attached to \(f\) has squarefree conductor dividing \(L\), and \(4\mid\#E_f(\mathbb F_r)\) for every \(r\nmid L\).

## Recovering a rational 2-torsion curve from its good reductions

Chebotarev's theorem on the mod-4 Galois representation gives \(\det(I-g)=0\bmod4\) for every element of its image. Its mod-2 image excludes an element of order 3, so it fixes a line in \(\mathbb F_2^2\). If this image is trivial the full 2-torsion is already rational. Otherwise choose a basis in which the mod-2 image is upper unipotent and nontrivial. For \(g=(g_{ij})\), the maps \(g\mapsto g_{12}\bmod2\) and \(g\mapsto g_{21}/2\bmod2\) are additive characters. The determinant identity says that their pointwise product vanishes. The first is nontrivial, so the second vanishes identically: a group cannot be the union of two proper subgroups. The first mod-4 basis vector therefore generates a Galois-stable cyclic subgroup of order 4. Quotient by its order-two subgroup. Its image and the dual isogeny kernel are two different rational order-two subgroups on the quotient. This gives an isogenous curve \(E'\) with full rational 2-torsion, still semistable and good outside \(\{2\}\cup S\).

If \(E'\) has multiplicative reduction at 2, then \(v_2(j)<0\). If it has good reduction, it must be ordinary: the kernel of reduction has at most two elements of order dividing two since the first formal-group quotient has order two and the parameter subgroup \(4\mathbb Z_2\) is torsion-free by the formal logarithm. A supersingular curve over \(\mathbb F_2\) has odd group order, incompatible with four rational 2-torsion points on \(E'\). Hence in the good case \(v_2(j)=0\).

The three rational 2-torsion roots of \(E'\) give a rational Legendre parameter. Reordering their differences gives a primitive \(a_0+b_0=c_0\) with
\[
 j=2^8\frac{(a_0^2+a_0b_0+b_0^2)^3}{(a_0b_0c_0)^2}.
\]
Every odd prime of its product has \(v_q(j)<0\), so belongs to \(S\). Also \(v_2(j)=8-2v_2(a_0b_0c_0)\le0\), giving \(16\mid a_0b_0c_0\). Thus unbounded admissible exponents imply precisely the kind of fixed-support triple excluded in the assertion. Conversely, a single such triple qualifies for all \(\ell\); this observation alone says nothing about infinitely many *distinct* triples.

## Finishing the finiteness argument

When the fixed-support triple is absent there are only finitely many possible \(\ell\). For fixed \(\ell\), write each entry as an \(\ell\)-th power times its \(\ell\)-power-free part. The three latter coefficients are supported on \(\{2\}\cup S\) and each exponent is less than \(\ell\), giving finitely many diagonal curves \(A_1X^\ell+B_1Y^\ell=C_1Z^\ell\). They are smooth and have genus \((\ell-1)(\ell-2)/2>1\). Faltings' theorem gives finitely many rational projective points on each, and positivity and primitivity fix the integer scale. The resulting finiteness of heights is ineffective.

For \(S\subset\{p:p\equiv1\bmod12\}\), the odd terms of a putative fixed-support triple are both \(1\bmod12\). Their difference cannot be the even term since that would introduce a factor 3. If their sum is the even term it is \(2\bmod4\), precluding \(16\mid a_0b_0c_0\). This proves the stated example. Exponents of a general abc triple need not share such a prime divisor away from a fixed \(S\), which prevents an inference to full abc.

The class can contain genuine exceptions. For \(S=\{13\}\), \(13+3^5=2^8\) qualifies with \(\ell=5\) and has radical 78; \(256^4>78^5\). Fixing \(S\) is essential in the proof: allowing arbitrary new primes into \(S\) removes the finite list of modular forms on which the argument depends.

References for the modular step include K. Ribet, *On modular representations of \(\mathrm{Gal}(\overline{\mathbb Q}/\mathbb Q)\) arising from modular forms*, Invent. Math. 100 (1990), 431–476; and N. Freitas and S. Siksek, *The asymptotic Fermat's Last Theorem for five-sixths of real quadratic fields*, Compos. Math. 151 (2015), 1395–1415, §2. Serre's level and weight prescriptions together with the theorem of Khare and Wintenberger give another formulation of the input.
