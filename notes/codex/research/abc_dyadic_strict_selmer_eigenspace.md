# A class-group eigenspace detects a repeated primitive prime exactly

Let \(E':y^2=x^3+16x^2+32x\), \(R=(-8,16)\), \(K=\mathbb Q(\sqrt{-2})\), and \(\mathcal O=\mathbb Z[\sqrt{-2}]\). Let \(p\mid w_n\) for a power of two \(n\ge8\) in the dyadic family. Then \(p>7\) splits in \(K\), \(R\) has exact order \(n\) modulo \(p\), and the positive formal depth of \([n]R\) equals \(v_p(w_n)\). Choose one place \(v\mid p\) of \(K\), and let \(\pi\mid p\) generate the prime whose CM endomorphism has differential of valuation one at \(v\). Set
\[
 V=E'[\pi],\qquad k=K(V),\qquad \Delta=\operatorname{Gal}(k/K).
\]
Here \(V\) is a one-dimensional \(\mathbf F_p\)-space on which \(\Delta\) acts by a character \(\chi\). Then
\[
 \boxed{\quad
 \dim_{\mathbf F_p}\operatorname{Hom}_{\Delta}
       (\operatorname{Cl}(k)/p\operatorname{Cl}(k),V)
 = \begin{cases}
 0,& v_p(w_n)=1,\\
 1,& v_p(w_n)\ge2 .
 \end{cases}\quad}
\]
This holds for every such \(p\). The character is the action on the connected CM kernel at the chosen place. The conjugate choice gives the conjugate criterion. The whole class number can have other \(p\)-divisibility. [Local multiplicity and the division tower](abc_dyadic_kummer_inertia.md) · [Dyadic prime factors](abc_octic_dyadic_fermat_audit.md)

## The local conditions determining the eigenspace

The extension \(k/K\) has degree dividing \(p-1\). In fact inertia at \(v\) has order \(p-1\), since the nonzero points of the connected degree-\(p\) kernel have an Eisenstein formal parameter of degree \(p-1\). Inflation–restriction identifies \(H^1(K,V)\) with \(H^1(k,V)^\Delta\). Since \(V\) becomes trivial over \(k\), the everywhere-unramified classes on the right are exactly the displayed equivariant homomorphisms, by unramified class field theory. Being unramified descends to \(K\) in the cohomological sense of restriction to inertia being zero. Indeed each local inertia subgroup over \(k\) has prime-to-\(p\) index in the corresponding one over \(K\), so restriction on its degree-one cohomology is injective. All archimedean places of \(K\) are complex.

At an odd good place of residue characteristic different from \(p\), the unramified local condition coincides with the \(\pi\)-Kummer condition. The isogeny is finite étale on the good model, giving the inclusion, and the dimensions agree by reduction to the finite residue group. At the unique dyadic place the two conditions are zero. Indeed the integral \(j\)-invariant gives potentially good reduction. In good reduction the group over the residue field \(\mathbf F_2\) has order at most five. In additive reduction its connected nonsingular group has order two and the geometric component group has order at most four by the Kodaira–Néron classification. Together with the pro-2 formal kernel, both cases give \(E'(K_2)[p]=0\) and \(E'(K_2)/p=0\). For a finite module the dimension of unramified \(H^1\) is the dimension of local invariants, by computing Frobenius coinvariants on inertia invariants, so this dimension is zero as well.

Both good reductions above \(p\) have \(p\nmid\#E'(\mathbf F_p)\). The cardinality is even by rational two-torsion and is strictly less than \(2p\) by Hasse at \(p\ge7\). At the conjugate place the \(\pi\)-isogeny has unit differential, the finite reduction quotient has order prime to \(p\), and there is no rational \(\pi\)-torsion. Both conditions are zero there. At \(v\) the nontrivial inertia action on \(V\) makes unramified \(H^1\) zero. The local \(\pi\)-Kummer group is one-dimensional: the formal logarithm identifies its quotient with \(p\mathbb Z_p/p^2\mathbb Z_p\). Thus, writing \(\operatorname{Sel}_{\pi}\) for the isogeny Selmer group, the class-group homomorphisms identify with
\[
 \ker\bigl(\operatorname{Sel}_{\pi}(E'/K)\longrightarrow E'(K_v)/[\pi]E'(K_v)\bigr).
\]

The same kernel is the strict localization kernel
\[
 \ker\bigl(\operatorname{Sel}_p(E'/\mathbb Q)\longrightarrow
                       E'(\mathbb Q_p)/pE'(\mathbb Q_p)\bigr).
\]
To see this, quadratic restriction identifies the rational \(p\)-Selmer group with the conjugation invariants of the \(p\)-Selmer group over \(K\). Global restriction is an isomorphism onto invariants since \(p\) is odd. The local Kummer conditions descend too: the obstruction in local \(H^1\) of the elliptic curve is killed by restriction followed by corestriction only if it was already zero, since the local degrees divide two. Over \(K\) the \(p\)-Selmer group splits into its \(\pi\) and \(\bar\pi\) parts. Conjugation exchanges them, identifying the invariant subspace with one part by \(c\mapsto c+\bar c\) in the reverse direction. At \(K_v=\mathbb Q_p\) the \(\bar\pi\)-Kummer group is zero, so vanishing on the selected component is equivalent to vanishing of the rational localization.

## Verifying the rational Tate–Shafarevich group

The curve has Cremona label 256a1. Scaling \((x,y)=(4X,8Y)\) gives the minimal integral model \(Y^2=X^3+4X^2+2X\), and translating \(X\) gives the coefficient list \([0,1,0,-3,1]\). The conductor is 256, the rational torsion has order two and the Tamagawa product is two. These three exact integers can also be reproduced by the PARI/GP commands below. The rank is one and \(R\) generates the free part: its image under the rational dual two-isogeny generates the free part of the isogenous rank-one curve. Cremona's BSD row gives the numerical values \(5.03785409361931\), \(1.20940185721471\), \(0.480125797508298\) for the real period, leading \(L\)-value and regulator respectively, and \(1.00000000000000\) for the analytic order. [Cremona BSD data](https://github.com/JohnCremona/ecdata/blob/master/allbsd/allbsd.00000-09999) · [Generator and isogeny](abc_dyadic_kummer_inertia.md)

```gp
E=ellinit([0,4,0,2,0]);
ellglobalred(E)   /* conductor 256, Tamagawa product 2 */
elltors(E)        /* order 2 */
ellrootno(E)      /* -1 */
vector(4,i,ellap(E,[2,3,5,7][i]))  /* [0,-2,0,0] */
```

R. L. Miller proved the full BSD formula for 16,714 of the 16,725 rank-at-most-one curves in the conductor range below 5000. Creutz and Miller completed the verification for **all** the curves in this range, using second isogeny descents for the remaining cases. Their completed result applies here, independently of which primes are covered by Miller's original exceptional-case tables. [Miller](https://arxiv.org/abs/1010.2431) · [Creutz and Miller, published paper](https://doi.org/10.1016/j.jalgebra.2012.09.029) · [Authors' statement of the completed range](https://arxiv.org/abs/1105.4018)

Here are bounds that certify the integral order independently of rounding the BSD row. Put \(c=\pi_{\rm real}/8\) and \(E_1(z)=\int_1^\infty e^{-zt}\,dt/t\). For sign minus, splitting the modular Mellin integral at 1 and differentiating the completed \(L\)-function gives
\[
 L'(E',1)=2\sum_{j\ge1}(a_j/j)E_1(cj).
\]
Indeed the integrand for the completed derivative is \(2f(it/16)\log t\) on \(t\ge1\), where \(f\) is the weight-two newform; integration by parts gives the formula above. The even coefficients vanish by additive reduction. We have \(a_1=1,a_3=-2,a_5=a_7=0\), and \(|a_j|/j\le \tau(j)/\sqrt j\le2\). Since \(E_1(jc)\le e^{-(j-1)c}E_1(c)\), the total absolute contribution after the first term relative to it is at most
\[
 (2/3)e^{-2c}+2e^{-8c}/(1-e^{-2c})<1.
\]
In particular the analytic rank is one. For an upper bound, use \(c>3/8\) and integrate \(1-t+t^2/2\) against \(dt/t\) from \(3/8\) to 1. The integral above 1 is at most \(e^{-1}\), giving \(E_1(c)\le\log(8/3)-5/8+55/256+e^{-1}<1\). Dropping the negative third term and using \(E_1(z)\le e^{-z}/z\), the tail of the derivative from \(j\ge9\) is at most \(4e^{-9c}/(9c(1-e^{-2c}))<1/4\). Therefore \(0<L'(E',1)<9/4\).

On the minimal model the full real period for the Néron differential \(dX/(2Y)\) is
\[
 \Omega=4\int_0^\infty\frac{dt}{\sqrt{t^4+4t^2+2}}\ge\frac8{\sqrt7}>3.
\]
The two real components have equal period. On the identity component use \(X=t^2\); split its integral at \(t=1\) to obtain the bound. In the BSD Néron–Tate pairing convention the regulator is \(2\widehat h(R)\), where \(h(x(P))=2\widehat h(P)+O(1)\). The explicit doubling bound on the isogenous generator gives \(\widehat h(R)>1/5\). The proven BSD formula now gives
\[
 0<\#\Sha(E'/\mathbb Q)
   =\frac{2L'(E',1)}{\Omega\,\operatorname{Reg}(E'/\mathbb Q)}<15/4<4.
\]
The order of this finite group is a square by the Cassels–Tate pairing, so it is one. [Explicit canonical height lower bound](abc_octic_dyadic_fermat_audit.md)

## Consequence for the prime exponent

The rational \(p\)-Selmer group therefore has dimension one and is generated by \(R\) modulo \(p\). Its localization is zero exactly when \(R\in pE'(\mathbb Q_p)\). Since the reduction group has order prime to \(p\), write \(R=T+F\) with \(T\) its unique prime-to-\(p\) torsion lift and \(F\) in the formal group. The formal logarithm and \(p\nmid n\) show that this localization vanishes exactly when \([n]R\) has depth at least two. This proves the boxed formula. The one-dimensional unramified eigenspace in that case comes from the rational Mordell–Weil generator; it is compatible with the alternating pairing on \(\Sha\). The equality gives an exact class-group test, with no estimate here for the frequency of a nonzero eigenspace as \(p\) varies.
