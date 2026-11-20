# First denominator depth in the class groups of a one-sided CM torsion tower

Let \(E:y^2=x^3+16x^2+32x\), \(R=(-8,16)\), \(K=\mathbf Q(\sqrt{-2})\), and \(\mathcal O=\mathbf Z[\sqrt{-2}]\). Let \(p>7\) split in \(K\), put \(r=\operatorname{ord}(R\bmod p)\), and let \(e=v_p(B_r)\), where \(B_r^2\) is the reduced denominator of \(x([r]R)\). Take a place \(v\mid p\) and a generator \(\pi\) of the prime whose CM endomorphism has nonunit differential at \(v\). Set
\[
 V_m=E[\pi^m],\qquad k_m=K(V_m),\qquad \Delta_m=\operatorname{Gal}(k_m/K).
\]
For every \(m\ge1\), as abelian groups,
\[
 \boxed{\quad \operatorname{Hom}_{\Delta_m}(\operatorname{Cl}(k_m),V_m)
       \simeq \mathbf Z/p^{\min(m,e-1)}\mathbf Z. \quad}                     \tag{1}
\]
In particular, whenever \(q\) is a prime and the reduction of \(R\) has full CM annihilator \((q)\), its entire first exponent \(v_p(B_q)\) is determined by (1). All eligible denominator primes at odd \(q\) split since \(R\) has odd order, is a double, and its abscissa \(-8\) is a square modulo \(p\) by the duplication formula. At these full-annihilator primes the ordinary order is \(q\).

There is a single infinite-level formulation. Put \(k_\infty=\bigcup_m k_m\), \(\Delta=\operatorname{Gal}(k_\infty/K)\), and let \(\chi:\Delta\to\mathbf Z_p^\times\) be the character on the \(\pi\)-adic Tate module. Write \(X\) for the Galois group of the maximal everywhere-unramified abelian pro-\(p\) extension of \(k_\infty\), using inertia groups in the algebraic extension. With its conjugation action and additive notation,
\[
  \boxed{\quad X/\overline{\langle gx-\chi(g)x:g\in\Delta,\ x\in X\rangle}
      \simeq\mathbf Z/p^{e-1}\mathbf Z.\quad}                                  \tag{2}
\]
These identities extend the mod-\(p\) criterion and identify every equivariant unramified homomorphism at every level. The proofs use the known rational Mordell–Weil group and Tate–Shafarevich group for this specific curve. [Mod-\(p\) argument and rational arithmetic](abc_dyadic_strict_selmer_eigenspace.md) · [Inertia of the particular Kummer extension](abc_dyadic_kummer_inertia.md)

## Descent of all unramified classes

The additive group of \(V_m\) is cyclic of order \(p^m\). Its CM scalar image is abelian. At \(v\), inertia contains an element whose scalar on \(V_1\) differs from 1. Indeed the reduction of \([\pi]\) is purely inseparable of degree \(p\). Its formal series has linear coefficient of valuation one and first unit coefficient in degree \(p\). Weierstrass preparation of \([\pi](z)/z\) gives an Eisenstein polynomial of degree \(p-1\), also Eisenstein over unramified extensions. Thus the inertia action on the nonzero kernel parameters has degree \(p-1\). This proves the scalar assertion for every finite level and for the infinite tower.

If an abelian profinite group acts on \(V_m\) and has such an element \(g\), its continuous cohomology vanishes in every degree. Indeed the central element acts as the identity on cohomology by the inner-automorphism homotopy, whereas \(g-1\) on coefficients is an automorphism. Apply this in degrees one and two. For either field \(L=k_m\) or \(k_\infty\), restriction gives an isomorphism
\[
  H^1(K,V_m)\simeq
  \operatorname{Hom}_{\rm cont}(G_L,V_m)^{\operatorname{Gal}(L/K)}.
\]
The unramified condition on the right corresponds exactly to unramifiedness at each place on the left. In fact restriction on an inertia group's degree-one cohomology is injective if the quotient inertia image in \(\operatorname{Gal}(L/K)\) has vanishing \(H^1\) with coefficients in \(V_m\). At \(v\) the scalar assertion proves this. At the dyadic place the image has order dividing 48. The integral \(j\)-invariant gives potential good reduction, and adjoining \(E[3]\) kills inertia on the 3-adic Tate module since the level-three congruence kernel is torsion-free. The resulting extension has degree dividing 48. At every remaining place the torsion tower is unramified, including the other place above \(p\), where the isogeny is étale. This proves the claimed injectivity everywhere.

At good odd places away from \(p\), the unramified condition equals the \(\pi^m\)-Kummer condition. Reduction to the finite residue field shows equality by finite-field Lang's theorem, or the étale isogeny and the equality of the sizes of kernel and cokernel on the finite group. At the dyadic place both conditions are zero. Potential good reduction gives either good or additive reduction. In good reduction the residue group over \(\mathbf F_2\) has size at most five. In additive reduction the connected nonsingular group has order two and the component group order at most four. The formal kernel is pro-2. Hence \(E(K_2)[p]=0\) and multiplication by \(p\) is bijective there. Also the unramified cohomology is the Frobenius cokernel on the finite group of inertia invariants, and its size is that of the local invariants, which are trivial.

At both places above \(p\), the residue group has even order by rational two-torsion and has order below \(2p\) by Hasse. Its order is prime to \(p\). At the place conjugate to \(v\), the \(\pi^m\)-Kummer group is zero by étaleness on the formal group and invertibility on the residue group. The étale kernel injects into the geometric residue group, so its local invariants are trivial. Consequently unramified cohomology is again zero. At \(v\), inertia has a scalar acting without nonzero invariants on \(V_m\), so unramified cohomology is zero. Thus equivariant everywhere-unramified classes identify precisely with
\[
     \ker\left(\operatorname{Sel}_{\pi^m}(E/K)
            \longrightarrow E(K_v)/[\pi^m]E(K_v)\right).                       \tag{3}
\]

## The length of the strict Selmer group

Quadratic restriction identifies \(\operatorname{Sel}_{p^m}(E/\mathbf Q)\) with the conjugation invariants of \(\operatorname{Sel}_{p^m}(E/K)\). Global restriction is an isomorphism onto invariants since the degree is two. The local Kummer conditions descend because restriction followed by corestriction is multiplication by the local degree, a unit on the relevant \(p\)-primary obstruction group. The two isogeny summands over \(K\), attached to \(\pi^m\) and \(\bar\pi^m\), are exchanged by conjugation. Projection of the invariant group onto the \(\pi^m\) summand is therefore an isomorphism, and the \(\bar\pi^m\)-Kummer condition at \(v\) is zero. It follows that (3) identifies with the kernel of rational \(p^m\)-Selmer localization at \(p\).

The curve is 256a1, with free generator \(R\), rational torsion of order two and \(\Sha(E/\mathbf Q)=0\). The cited mod-\(p\) argument gives a numerical-inequality certificate for this last input using the proved full BSD formula for this conductor. Hence \(\operatorname{Sel}_{p^m}(E/\mathbf Q)=\langle R\rangle\simeq\mathbf Z/p^m\mathbf Z\). Write \(R=T+F\) over \(\mathbf Q_p\), using the unique prime-to-\(p\) torsion lift \(T\) of its residue and the formal point \(F\). Since \(p\nmid r\), the formal logarithm of \(F\) has valuation precisely \(e\). The formal logarithm identifies the local quotient by \(p^m\) with \(p\mathbf Z_p/p^{m+1}\mathbf Z_p\). Localization thus sends the generator to a unit times \(p^{e-1}\) in \(\mathbf Z/p^m\mathbf Z\). This proves that (3) is cyclic of the order in (1). Unramified abelian class field theory identifies it with the Hom group in (1). [Full BSD in this conductor range](https://doi.org/10.1016/j.jalgebra.2012.09.029)

For \(L=k_\infty\) the identical calculation gives the same cyclic group for \(\operatorname{Hom}_{\Delta,\rm cont}(X,V_m)\). After choosing a basis of the Tate module, these groups are the order-dividing-\(p^m\) characters of the quotient in (2). All continuous characters of the compact abelian pro-\(p\) quotient into \(\mathbf Q_p/\mathbf Z_p\) have finite image and occur at some level. The character groups embed into each other and stabilize at cyclic order \(p^{e-1}\). Pontryagin duality gives (2).

## A finite-layer vanishing consequence

Write \(\Delta_m=D_m\times\Gamma_m\) for its prime-to-\(p\) and \(p\)-primary factors. Let \(A_m\) be the direct summand of \(\operatorname{Cl}(k_m)[p^\infty]\) on which \(D_m\) acts by the Teichmüller lift of its action on \(V_1\). The minimal number of generators of \(A_m\) over \(\mathbf Z_p[\Gamma_m]\) equals the dimension of \(\operatorname{Hom}_{\Delta_m}(\operatorname{Cl}(k_m),V_m[p])\). Indeed reducing \(A_m\) modulo \(p\) and the augmentation ideal of \(\Gamma_m\) gives its generator space by Nakayama's lemma. The displayed Hom space is its dual after a choice of basis. It is also the subgroup killed by \(p\) of the Hom group in (1). Therefore
\[
 e=1\implies A_m=0\ \text{at every }m,\qquad
 e\ge2\implies A_m\ \text{is nonzero and cyclic over }\mathbf Z_p[\Gamma_m]\ \text{at every }m .
\]

For example \(B_5=281\) and \(5\) is inert in \(K\), so \(p=281\) has full annihilator \((5)\) and \(e=1\). Every one of its indicated tame class-group summands vanishes. At the split prime \(p=205883\) the known first depth two for \((1,1)\) on the rationally two-isogenous curve gives \(e=2\) for \(R\). The isogeny has unit differential and changes the residue order by at most a factor of two, hence preserves first depth. Here (1) has order \(p\) at every level. This latter example has composite order on the isogenous curve and illustrates the general first-depth theorem. Neither class-group formula estimates its right-hand side uniformly as \(p\) varies. [Small prime-index denominator](abc_odd_rank_signed_frobenius.md) · [Exceptional repeated divisor](abc_cm_ideal_census.md)

## A class-number divisor in the full torsion field

Put \(F_m=K(E[p^m])\) and \(s=\min(m,e-1)\). Its class group has a quotient isomorphic as an abelian group to \((\mathbf Z/p^s\mathbf Z)^2\). In particular,
\[
                           p^{2s}\mid h(F_m).
\]
To obtain both quotients in the same field, apply the restriction proof separately to \(V_m\) and its conjugate over \(F_m\). For \(V_m\), the added ramification at the conjugate place to \(v\) requires a descent check. The inertia there acts trivially on \(V_m\). An inertia restriction unramified over \(F_m\) therefore factors through a homomorphism on the abelian inertia image in \(\operatorname{Gal}(F_m/K)\). Frobenius centralizes this image, whereas it acts on \(V_m\) by a scalar differing from 1 modulo \(p\), since the étale kernel has no nonzero rational residue \(p\)-torsion. The homomorphism is thus zero already. The previous arguments at the other places apply. A generator of each Hom group of order \(p^s\) has image of order \(p^s\). The two tame characters differ because inertia at \(v\) acts nontrivially on \(V_1\) and trivially on its conjugate. Their idempotents split the joint image into the two separate cyclic images, proving the assertion. [Detailed common-field descent and module argument](abc_cm_class_towers_audit.md)
