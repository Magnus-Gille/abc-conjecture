# First multiplicity as an unramified degree in a CM division field

Let \(K=\mathbb Q(\sqrt{-2})\), \(\mathcal O=\mathbb Z[\sqrt{-2}]\), and fix
\[
 E': y^2=x^3+16x^2+32x,\qquad R=(-8,16).
\]
The full CM ring \(\mathcal O\) acts on \(E'\) over \(K\). Let \(n\ge8\) be a power of two and \(p\mid w_n\) one of the primes of its elliptic Fermat factor. The established properties used here are that \(p>3\) splits in \(K\), the reduction of \(R\) has exact order \(n\), and \([n]R\) has formal depth \(e=v_p(w_n)\). Depth on the formal group means the valuation of the parameter \(-x/y\), with \(v_p(p)=1\). [Dyadic factor and reduction orders](abc_octic_dyadic_fermat_audit.md)

Choose a place \(v\mid p\), so \(K_v=\mathbb Q_p\). Let \(\pi\in\mathcal O\) be a generator of the prime factor of \(p\) whose CM endomorphism has differential of valuation one at \(v\). Its conjugate has unit differential there. For every integer \(m\ge1\) put
\[
 K_m=K(E'[\pi^m]),\qquad L_m=K_m([\pi^m]^{-1}R).
\]
The latter field adjoins the coordinates of all points mapping to \(R\). It suffices to adjoin any one of them because their differences lie in \(E'[\pi^m]\).

The extension \(L_m/K_m\) is cyclic of degree \(p^m\). At each place over \(v\) its inertia group has order \(p^{\max(0,m-e+1)}\), and it is unramified at every other finite place. Consequently
\[
 \boxed{\ [\text{maximal everywhere-unramified subextension of }L_m/K_m:K_m]
     =p^{\min(m,e-1)}.\ }
\]
In particular, if \(p^{m+1}\mid w_n\), the class group of \(K_m\) has a cyclic quotient of order \(p^m\). Conjugation by \(\operatorname{Gal}(K_m/K)\) on this quotient is its action on \(E'[\pi^m]\). The formula specifies a subextension of this particular division field. Other unramified extensions of \(K_m\) need not come from \(R\).

## The global translation group

The point \(R\) is primitive modulo torsion in \(E'(\mathbb Q)\). Indeed the rational dual two-isogeny to \(E:v^2=u^3-8u^2+8u\) sends \(R\) to \(A=(1,1)\), which generates \(E(\mathbb Q)\) modulo torsion. If \(R=[\pi]P\) with \(P\in E'(K)\), write \(\pi=a+b\sqrt{-2}\), of norm \(p\). Applying \([\bar\pi]\) and taking the trace to \(\mathbb Q\) gives
\[
 [p](P+\bar P)=[2a]R .
\]
Primitivity forces \(p\mid 2a\), whereas \(0<|a|\le\sqrt p\) for an odd split prime. Thus \(R\notin[\pi]E'(K)\). [Group generator](abc_octic_full_mixed_orbit.md) · [Dual isogeny](abc_octic_dyadic_fermat_audit.md)

As an \(\mathcal O\)-module \(E'[\pi^m]\) is isomorphic to \(\mathcal O/(\pi^m)\) and its additive group is cyclic of order \(p^m\). Hence \(G_m=\operatorname{Gal}(K_m/K)\) is abelian, acting by scalars. It contains an element acting nontrivially on \(E'[\pi]\). To verify this locally, \([\pi]\) has degree \(p\) and zero differential on the good special fibre at \(v\), so its reduction is purely inseparable of degree \(p\). Its formal series first has a unit coefficient in degree \(p\), and its linear coefficient has valuation one. Weierstrass preparation of \([\pi](z)/z\) therefore gives an Eisenstein polynomial of degree \(p-1\) for the parameters of its nonzero kernel points. This remains Eisenstein over every finite unramified extension of \(K_v\), so the nontrivial scalar also occurs in local inertia.

For an abelian group \(G\) acting on \(E'[\pi]\), a scalar \(g\in G\) with \(g-1\) invertible gives \(H^1(G,E'[\pi])=0\). Indeed a cocycle \(f\) satisfies \((g-1)f(h)=(h-1)f(g)\) by comparing \(f(gh)\) and \(f(hg)\), so it is a coboundary. Inflation–restriction now shows that the nonzero Kummer class of \(R\) in \(H^1(K,E'[\pi])\) stays nonzero over \(K_m\). In particular \(R\) has no \(\pi\)-preimage over \(K_m\).

The action of \(\operatorname{Gal}(L_m/K_m)\) on a division point is by translation through a subgroup of \(E'[\pi^m]\). If this subgroup were proper, it would be killed by \([\pi^{m-1}]\). Applying this multiplier to a \(\pi^m\)-division point would give a \(\pi\)-preimage rational over \(K_m\), a contradiction. This proves the asserted global degree. The division locus is defined over \(K\), so \(L_m/K\) is Galois and conjugation on its translation subgroup is the torsion character.

## Inertia at the prime of connected reduction

The reduced point \(R\bmod p\) has a unique lift \(T\in E'[n](\mathbb Q_p)\), since \(n\) is prime to \(p\) and the \(n\)-torsion is finite étale. The difference \(R-T\) has depth \(e\), because \([n]\) preserves positive formal depth. The formal logarithm is an isometric group isomorphism on the depth-one group over \(\mathbb Q_p\) for this odd good prime. There is therefore \(F_0\in E'(\mathbb Q_p)\) of depth one such that
\[
 R=T+[\pi^{e-1}]F_0 .
\]
The torsion point \(T\) has a rational \(\pi^m\)-preimage in \(E'[n](\mathbb Q_p)\) for every \(m\), since \([\pi]\) acts invertibly on this group.

Set \(B=\mathbb Q_p^{\mathrm{nr}}\) inside a fixed algebraic closure, and \(B_m=B(E'[\pi^m])\). The point \(F_0\) has no \(\pi\)-preimage over \(B\). Any such point would reduce to the identity by pure inseparability, hence belong to the formal group over a finite unramified extension. There its parameter has positive integral valuation. The formal series for \([\pi]\) sends every such parameter to one of valuation at least two, contrary to the depth of \(F_0\). The abelian group \(\operatorname{Gal}(B_m/B)\) still contains a nontrivial scalar on \(E'[\pi]\) by the Eisenstein argument. The same cocycle calculation and inflation–restriction imply \(F_0\notin[\pi]E'(B_m)\).

For \(m\le e-1\), the displayed decomposition already gives a \(\pi^m\)-preimage of \(R\) over \(\mathbb Q_p\). For \(m>e-1\), let \(j=m-e+1\). Over \(B_m\) the field of the \(\pi^m\)-preimages of \(R\) is the field of the \(\pi^j\)-preimages of \(F_0\). One can add a rational preimage of \(T\) to any of the latter points to obtain a preimage of \(R\), and \(B_m\) contains all the required torsion. Since \(F_0\) has no \(\pi\)-preimage over \(B_m\), the translation subgroup at level \(j\) has full order \(p^j\), by the same cyclic-group argument as above. Composing a completion of \(K_m\) at \(v\) with \(B\) gives its maximal unramified extension. The calculated degree over \(B_m\) is therefore exactly the inertia order.

## The other places

At all odd places away from \(p\), the curve has good reduction and \([\pi^m]\) is finite étale on the good model. At the conjugate place above \(p\) it is also finite étale, since its differential there is a unit. Properness extends \(R\) to an integral section, and pulling back the isogeny along this section gives a finite étale division locus. These facts persist after base change to \(K_m\), proving unramifiedness at all the indicated places.

At the dyadic place \(E'\) has potentially good reduction since \(j(E')=8000\) is integral. It acquires good reduction over the fixed field \(F=K(E'[3])\). Indeed its inertia action on the 3-adic Tate module is finite by potential good reduction. The kernel of reduction modulo 3 in \(\mathrm{GL}_2(\mathbb Z_3)\) is torsion-free, so passing to \(F\) kills the finite inertia action. The good reduction criterion then applies. The degree of \(F/K\) divides \(|\mathrm{GL}_2(\mathbb F_3)|=48\). The extension \(L_m F/K_m F\) is unramified at the dyadic places by the preceding étale argument. Any dyadic ramification index in the \(p\)-extension \(L_m/K_m\) divides the ramification index in \(L_mF/K_m\). The latter divides \([F:K]\), which is prime to \(p>3\). Thus \(L_m/K_m\) is unramified there as well.

All archimedean places are complex. The inertia groups over \(v\) have the same order and lie in a cyclic global translation group, hence coincide. Quotienting by this subgroup gives the maximal unramified subextension and the stated degree; the class-group implication follows by unramified abelian class field theory.

This finite-level test explains a limitation of the dyadic torsion data. Locally, two characteristic-zero lifts of the same reduced point differ by a formal point on which every integer prime to \(p\) is invertible. Taking its unique prime-to-\(p\) divisions translates, compatibly, the entire prime-to-\(p\) systems of division fibres of the two lifts. Formal depth at \(p\) can still differ. Detecting multiplicity by the ramification formula above uses the moving \(\pi\)-division field, whose class groups are not bounded here.
