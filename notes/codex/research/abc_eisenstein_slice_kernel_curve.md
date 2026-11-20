# The curve for one prescribed pair of squarefree kernels

Fix signed squarefree \(k,l\) which actually occur at an odd index \(n\ge3\) in the [squareclass descent](abc_eisenstein_slice_squareclass_descent.md). Write \(d=|kl|\), \(d_1=1,\ d_2=k,\ d_3=2l,\ D=2kl\). The rational points in question lie on the genus-nine curve
\[
        s^2+kt^2+2lu^2=0,\qquad s^4+ks^2t^2+k^2t^4=3W^4
          \quad\text{in }\mathbf P^3.
\]
Its Jacobian has rational rank at least eleven. In particular the classical Chabauty criterion requiring rank less than genus cannot by itself determine whether another index gives the minimum \(d=2{,}671{,}321\).

## The sign quotients

On the affine chart \(W\ne0\) put \(a_1=s^2/W^2,\ a_2=kt^2/W^2,\ a_3=2lu^2/W^2\). The base conic is \(a_1+a_2+a_3=0\), \(a_1^2+a_1a_2+a_2^2=3\). Adjoining the three square roots of \(a_i/d_i\) gives a connected degree-eight cover with group \((\mathbf Z/2)^3\): each \(a_i\) has two distinct simple zeros which are disjoint from the other zeros and from the poles. The three \(a_i\) have the same two simple poles on the projective conic. Exactly these eight points branch, all with inertia order two. In the concrete projective complete intersection the four homogeneous coordinates are squared to give the three conic coordinates and the coordinate at infinity. Each zero is transverse and no two coordinates vanish there, so this model is smooth. Riemann–Hurwitz gives genus nine.

For any nonempty subset \(I\subset\{1,2,3\}\) take the double cover obtained by adjoining the square root of \(\prod_{i\in I}a_i/d_i\). The seven double-cover Jacobians multiply up to an isogeny onto the genus-nine Jacobian over \(\mathbf Q\). Indeed, the holomorphic differentials split according to the characters of the sign group, the trivial eigenspace has dimension zero on the conic, and the pullback from each double cover supplies exactly the corresponding eigenspace.

For a singleton, write \(a_i=d_i r^2\). Then \((a_i+2a_j)^2=12-3d_i^2r^4\) gives a genus-one quartic. It maps nonconstantly to
\[
             G_{6|d_i|}:\quad Y^2=X^3-(6d_i)^2X
\]
by \((X,Y)=(-3d_i^2r^2,-3d_i^2r(a_i+2a_j))\). For a pair \(i,j\), let \(r=(s_i/s_j)\) where \(s_i^2=a_i/d_i,\ s_j^2=a_j/d_j\). The ratio \(r\) belongs to the two-character subfield since it equals \(s_i s_j/(a_j/d_j)\). Put \(w=1/s_j^2\). Then \(3w^2=d_i^2r^4+d_i d_jr^2+d_j^2\). With \(e=d_i d_j\) this quotient maps nonconstantly to
\[
       H_e:\quad Y^2=X^3+3eX^2+9e^2X
\]
by \((X,Y)=(3d_i^2r^2,9d_i^2rw)\). All six quotients have genus one by their four distinct branch points.

The triple quotient has genus three. Put \(a_1a_2a_3=Dy^2\) there. The \(a_i\) are the three roots of \(z^3-3z-Dy^2\). For each \(i\) the point \((Da_i,D^2y)\) lies on
\[
                  B_d:\quad Y^2=X^3-12d^2X.
\]
Two of these maps have independent differential pullbacks, proportional to \(da_1/y,da_2/y\), because \(da_2/da_1=-(2a_1+a_2)/(a_1+2a_2)\) is nonconstant. Let \(\Delta\) be the product of the three cyclic root differences. The discriminant gives \(\Delta^2=108-27D^2y^4\). This quartic maps nonconstantly to \(Y^2=X^3-(54D)^2X\) by \((X,Y)=(-27D^2y^2,-27D^2y\Delta)\). Since \(|54D|=36\cdot3d\), the latter curve is isomorphic over \(\mathbf Q\) to \(G_{3d}\). This map is invariant under cyclic permutation of the three \(a_i\), which fixes \(y,\Delta\). The first two differentials span a plane with no nonzero invariant for this three-cycle, since \(da_1+da_2+da_3=0\). The three maps therefore account for all three differential dimensions, giving a Jacobian isogenous to \(B_d^2\times G_{3d}\).

## The rank obstruction

In summary the nine-dimensional Jacobian is isogenous over \(\mathbf Q\) to
\[
   \prod_i G_{6|d_i|}\ \times\ \prod_{i<j}H_{d_i d_j}\
             \times B_d^2\times G_{3d}.
\]
At a point from the given orbit, all \(s_i\) are nonzero and the three \(a_i\) are pairwise distinct: their nonzero squareclasses \(1,k,2l\) are distinct. Thus the singleton maps have nonzero ordinates. At the good primes 7 and 11 the congruent-number curves in this display have group orders 8 and 12, since these primes are \(3\bmod4\) and divide none of the twists. Their rational torsion is exactly their full rational 2-torsion. The three singleton curves and \(G_{3d}\) therefore have rank at least one. The earlier squareclass descent gives rank at least one on each of the three \(H_{d_i d_j}\), and at least two on \(B_d\) from the independent abscissa squareclasses of two of the three collinear points. The sum is at least \(3+3+4+1=11\).
