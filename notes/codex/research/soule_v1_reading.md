# Soulé's weak abc bound and the exceptional fibers in its proof

This reading concerns the supplied version 1 of Christophe Soulé's *On the abc conjecture*, dated 3 November 2026. All section, proposition and equation numbers below refer to that version. [Manuscript](https://arxiv.org/abs/2611.05217v1)

## Exponent in the statement

Theorem B asserts that for every positive ε there is a constant A(ε) such that c ≤ A(ε) rad(abc)^(24+ε) for primitive positive triples a+b=c. Theorem 2 supplies the coefficient 12 in a genus-two canonical-height estimate. In §7.3.2 the map from the genus-two curve y²+y=x⁵ to the y-line has degree 5, and the canonical divisor has degree 2. The resulting factor 5/2 gives 30 in (49). The discriminant estimate (51) has coefficient 4/5 at log rad(abc), giving 24 in Theorem B. Sending ε to zero leaves this coefficient in place. A counterexample family of quality only a little greater than 1 would be compatible with the claimed inequality.

## The square root used in Proposition 9

Work over the algebraic closure in characteristic zero. In §§3 and 5 there is an étale double cover χ from a genus-three curve Y₁ to a genus-two curve Y₀. For a point y of the parameter curve Y, let P₁ and P₂ be the two distinct points over P₀. The double cover of Y₁ used to construct the surface fiber is specified by a line bundle λᵧ with λᵧ² ≅ O(P₁+P₂). In this paragraph and below the square of a line bundle means its tensor square.

By Proposition 5, two points A and B of Y₀ have exceptional fibers. A and B are Weierstrass points. The two preimages of each form a distinct conjugate pair for the hyperelliptic involution on Y₁. In either fiber, O(P₁+P₂) is the hyperelliptic pencil, of degree two.

This pencil has 64 distinct square roots. They form a torsor under the two-torsion of the genus-three Jacobian. A root is effective exactly when it equals O(W) for a Weierstrass point W of Y₁. Indeed, an effective line bundle of degree one is the class of a point W, and 2W belongs to the hyperelliptic pencil exactly at a branch point. There are eight such points. In particular, exceptionality alone gives no section of the chosen square root.

## Why a single choice cannot work above both A and B

The square roots in §5 arise by restricting a line bundle on Y₁ × Y. On each connected geometric component of Y the class

    τ(y) = Nmχ(λᵧ) ⊗ O(−P₀)

is constant. Indeed it varies algebraically, and its square is trivial because χ sends P₁+P₂ to 2P₀. Thus it maps the component into the finite group Jac(Y₀)[2]. Each such component covers Y₀.

If the chosen root is effective at a fiber over A, write it as O(W). Put C = χ(W). Then τ is the class of C−A. The point C differs from both A and B since all points above A and B occur in distinct conjugate pairs, whereas W is fixed by the hyperelliptic involution. Moreover, 2C is linearly equivalent to 2A. Since A is Weierstrass, 2A is a canonical fiber of the genus-two hyperelliptic map, so C is also Weierstrass. Similarly, effectivity anywhere over B would give τ as the class of D−B for a Weierstrass point D different from A and B.

The two classes cannot agree. A nonzero two-torsion class on a genus-two Jacobian is represented by a unique unordered pair of distinct Weierstrass points, as the manuscript also observes in §3.4.3. Here {C,A} and {D,B} are different pairs. Equivalently, an equality of classes would give C+B linearly equivalent to D+A. Those are different effective degree-two divisors, so they would have to belong to the unique hyperelliptic pencil. Two distinct Weierstrass points cannot form a fiber of that pencil.

Consequently at least one of the two exceptional base points has no effective chosen root anywhere above it on the component. The computation in §6.2.3 then gives h⁰(Bᵧ)=2+0=2 and h⁰(Lᵧ)=3 there. Proposition 9(iv) and (v) assert 3 and 4 respectively.

In §6.2.5 equations (23) and (24) use a jump of two in h⁰ at all 4k exceptional points to get a lower bound of 8k on the degree of a torsion sheaf. The asserted jump can be only one. Since torsion length can exceed the dimension killed by a uniformizer, the length requires a separate calculation. The following two checks address it.

## An intersection-number check independent of the count of exceptional points

Let $E=\varphi_* L$ be the rank-two direct image on $Y$. It is locally free because the base is a smooth curve and the direct image is torsion-free. Evaluation gives a section of the rank-two bundle $V=(\varphi^*E)^\vee\otimes L$ on the smooth surface $X$. Its zeros are the common base points of the two local generators of the relative pencil.

Assume the generic pencil has no base point, as required in §6.3.3. The zero scheme then has no horizontal curve. There is also no vertical curve. Every fiber is integral, and the map from E ⊗ k(y) to H⁰(Xᵧ,Lᵧ) is injective by the exact sequence for multiplication by a local uniformizer. Thus the two sections cannot both vanish identically on a fiber. The zero scheme is empty or zero-dimensional, so its length equals the top Chern number of V and is nonnegative. As E comes from a curve, this yields

    0 ≤ ∫ₓ c₂(V) = L² − deg(Lᵧ) deg(E).

Proposition 9(ii) and (iii) give deg(Lᵧ) = 6 and L² = −20k. Consequently deg(E) ≤ −10k/3. Proposition 9(vi) would instead give deg(E) ≥ −3k, forcing the zero scheme to have length at most −2k. The two properties required in the height argument are incompatible for this pencil. A finite étale base change multiplies both intersection numbers by its degree and leaves the contradiction intact.

## Local torsion lengths

Write p for the projection Y₁ × Y → Y, and S for the square-root line bundle used to define the double cover ρ. Then $S^2=\mathcal O(D_1+D_2)$, $B=\rho^* S^2$ and $\rho_*\mathcal O_X=\mathcal O\oplus S^{-1}$. The projection formula splits R¹φ∗B into R¹p∗O(D₁+D₂) and R¹p∗S. We calculate over an algebraic closure, on a connected component, with k = deg(Y/Y₁).

For use in both summands, consider a family of degree-one line bundles on a fixed smooth curve with generically no section. If its class at y equals O(W), its space of sections there is one-dimensional. Over the local discrete valuation ring, a two-term free complex computing cohomology therefore has just one nonunit elementary divisor tᵉ, where t is a uniformizer. Its contribution to torsion length is e. If e ≥ 2, the nonzero section on the fiber lifts modulo t². Its zero divisor would deform the point W over the dual numbers, so the first derivative of the class must lie in the tangent line to the Abel image at W. Thus if that tangent condition fails, e = 1. The implication about the zero divisor follows because the section on the special fiber has one simple zero, so the lifted zero scheme is a relative effective divisor of degree one.

For the first summand, O(D₁+D₂) is the pullback from Y₀ × Y of the graph divisor of y ↦ P₀(y). Pushing down along χ splits the computation into O(P₀) and O(P₀) ⊗ η on Y₀, where η = O(B₀−A) is the nontrivial two-torsion defining χ and B₀ denotes the exceptional point previously called B. The first bundle has constant h⁰ = 1 and contributes no torsion. The second bundle is effective just at P₀ = A or B₀. For example, at A it equals O(B₀). Its derivative is the tangent of the Abel image at A translated to B₀, since y ↦ P₀ is étale. This differs from the Abel tangent at B₀. In genus two the projectivized Abel tangent direction is the canonical image of the point, and distinct Weierstrass points have distinct canonical images. The same computation applies with A and B₀ exchanged. Thus each of the 4k points contributes length one, for a total of 4k.

For the second summand, Sᵧ is effective only at exceptional fibers. If Sᵧ = O(W) over A, write C = χ(W). The earlier norm argument shows C is a Weierstrass point distinct from A and B₀. A lift of the section modulo t² would deform W, so its norm would deform in the Abel tangent direction at C. But Nmχ(Sᵧ) = O(P₀) ⊗ τ with τ constant. Its derivative is nonzero and has the direction at A, which differs from the direction at C. The length is therefore one here as well. The argument also applies to any effective root above B₀. On a given component such roots occur above at most one of A and B₀, hence at no more than 2k points.

If e counts the geometric points with an effective chosen root, the torsion degree in (24) is consequently 4k+e, with 0 ≤ e ≤ 2k. Equations (16), (18) and (22) then give deg(E) = −7k+e ≤ −5k. This calculation uses the square-root family itself and does not require generic base-point freeness. The inequality in (24) would require 4k+e ≥ 8k.

## An explicit model for the two exceptional fibers

Take the smooth projective models of v² = (u²−1)(u²−2)(u²−3)(u²−4) and w² = z(z−1)(z−2)(z−3)(z−4). The map z=u², w=uv is the quotient by the fixed-point-free involution (u,v) ↦ (−u,−v). The fibers over z=0 and z=∞ each consist of two hyperelliptically conjugate points. The eight Weierstrass points upstairs lie over z=1,2,3,4. Thus the possible two-torsion labels for an effective root above z=0 are {0,i}, and those above z=∞ are {∞,i}, with i in {1,2,3,4}. These sets of labels are disjoint.
