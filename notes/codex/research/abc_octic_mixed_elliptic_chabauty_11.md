# Complete rational points for the mixed fourth-power condition

The smooth plane quartic
\[
 D:w^4=m^4+4m^3n+10m^2n^2-4mn^3+n^4
\]
has exactly eight rational points,
\[
 [1:0:\pm1],\quad [0:1:\pm1],\quad [2:1:\pm3],\quad [-1:2:\pm3].
\]
Equivalently, with positive coprime \(s,t_0\), \(s\) odd and \(t_0\) even, the only simultaneous solution of \(s^2+2t_0^2=\text{fourth power}\) and \((s\pm t_0)^2+t_0^2=\text{square}\) is \((7,4)\) with the minus sign. This fixed-power theorem does not impose a restriction on all cubeful numbers, whose prime exponents may be relatively prime.

## Global input

Let \(L=\mathbf Q(t)\) with \(t^4=2t^2+1\). The single-cover descent shows that a nondegenerate signed primitive solution yields
\[
 z=u-2/u,\quad v^2=z^2+8,\quad w_0^2=F(z)=(z^2-4z-8)^2+16z^2
\]
with \(z,v,w_0,u\) rational and, over \(L\), a point
\[
 \mathcal E:\quad W^2=(z^2+8)B(z),\qquad
 B(z)=z^2-4(1+t)z+8(t^3+t^2-t).
\]
Here \(u=A/B_0\) comes from \(s+t_0\sqrt{-2}=\pm(A+B_0\sqrt{-2})^4\). The single-cover proof is needed: simply squaring the elliptic-cover equation over \(L\) would admit additional twists. The same descent proves the rank of \(\mathcal E(L)\) is at most two. [Global covering and rank proof](abc_octic_mixed_quartic_field_chabauty.md) · [Rank verifier](abc_octic_mixed_quartic_field_verify.py)

Use the positive infinity as origin. Put \(a=1+1/t\), \(\beta=-2(1+t)\), \(\gamma=4t^3+2t^2-8t+2\), and \(h=-12t^3-4t^2+28t+4\). The elliptic model is
\[
     E:Y^2=X(X-a)(X-at^2),\quad
     U=2(W+z^2+\beta z+\gamma),\quad V=2Uz+\beta U-2h,
\]
with \(X=(U+4(1+t)^2)/16\), \(Y=V/64\). Two points in \(E(L)\) are
\[
 P=((1+t)^2/4,h/32),\qquad
 Q=((2t^3+5t^2+2t+2)/4,(-5t^3-11t^2-8t-5)/8).
\]
The former is the other infinity and the latter is a point above \(z=-1\). The involution changing the sign of \(W\) sends \(R\) to \(P-R\), because every fiber of \(z\) has divisor linearly equivalent to the sum of the two infinities.

## Two independent logarithms at eleven

The polynomial of \(t\) is irreducible modulo 11, and its discriminant is a power of two, so the completion \(K=L_{11}\) is unramified of degree four, with residue field \(k=\mathbf F_{11^4}\). The cubic has good reduction. Direct point counting gives \(d=\#E(k)=14596\), prime to 11. Define
\[
 \mathcal L(R)=\log_{\!E}([d]R)\in 11\mathcal O_K.
\]
For the integral formal parameter \(z_E=-X/Y\), the formal logarithm satisfies \(\log_E(z_E)\equiv z_E\bmod121\) when \(11\mid z_E\). Thus \(\mathcal L(R)/11\bmod11\) is an exact finite calculation. Reduce \(R\) modulo 11 to determine its order \(r\), compute \([r]R\) in Jacobian coordinates \((X_J,Y_J,Z_J)\) modulo 121 and take \((d/r)(-X_JZ_J/Y_J)/11\bmod11\). All denominators in the verifier are checked units.

In the coefficient basis \((1,t,t^2,t^3)\), the span of these vectors for \(P,Q\) has reduced echelon rows \((1,0,0,9),(0,1,7,10)\). The two exact logarithms are therefore independent. By the rank bound they span every global logarithm over \(\mathbf Q_{11}\). Moreover their normalized integral vectors span a direct summand, since a two-by-two minor is a unit. Thus every global logarithm, divided by 11 and reduced modulo 11, is killed by
\[
 \Phi(c_0,c_1,c_2,c_3)=(c_2-7c_1,\ c_3-9c_0-10c_1).
\]
Every linear form on the residue space annihilating that span lifts to an integral linear form on \(\mathcal O_K\) annihilating the *exact* logarithm span, by solving at the invertible minor. Neither a full Mordell–Weil basis nor a saturation assumption is needed.

## The local calculation

Choose one sign of \(W\) in an unramified chart. The other sign is equivalent under \(R\mapsto P-R\), so the condition that the logarithm lies in the global span is unchanged. At finite \(z_0\in\mathbf F_{11}\) away from \(z_0^2+8=0\), use the parameter \(z=z_0+11j\). Require both rational square conditions locally and take a square root of \((z^2+8)B(z)\) lifting a fixed root in \(k\). When \(z_0^2+8=0\), the rational parameter is \(v=11j\); take the unique analytic root \(z=\sqrt{v^2-8}\) reducing to \(z_0\) and set \(W=v\sqrt{B(z)}\). At infinity use \(1/z=11j\) and the branch mapping to \(P\). The numerator of its apparent pole in the map to \(E\) is rationalized by the identity
\[
 (z^2+\beta z+\gamma)^2-(z^2+8)B(z)=2hz+\gamma^2-64(t^3+t^2-t).
\]
Thus the chosen chart extends integrally over the whole disk, including its center.

These are all the residue disks consistent with the rational square tests and the quartic-field square root. The rows give \(\Phi(\mathcal L(R)/11)=C+D_1j\pmod{11}\).

| \(z_0\) | \(C\) | \(D_1\) | Allowed \(j\bmod11\) |
|---|---:|---:|---:|
| \(1\) | \((6,8)\) | \((2,5)\) | none |
| \(6\), parameter \(v\) | \((0,0)\) | \((3,9)\) | 0 |
| \(9\) | \((6,10)\) | \((3,2)\) | none |
| \(10\) | \((8,9)\) | \((8,9)\) | 10 |
| \(\infty\), parameter \(1/z\) | \((0,0)\) | \((0,7)\) | 0 |

[Standard-library verifier for all residues, orders and logarithm vectors](abc_octic_mixed_elliptic_chabauty_11.py)

An independent PARI/GP implementation uses number-field residue maps, Hensel lifts and elliptic multiplication over the local field to check the same five disks. The row vectors for the two global points before row reduction are \((6,9,8,1)\) and \((0,4,6,7)\). It reproduces the listed surviving digits. [Independent PARI/GP verification](abc_octic_mixed_chabauty_crosscheck.gp)

For completeness, the nonzero linear coefficients on the three surviving disks prove uniqueness on each *entire* disk. Denote its rational local coordinate by \(\eta\) (one of \(z-z_0,v,1/z\)). The displayed maps are integral analytic maps of smooth disks: all square roots used as analytic functions have unit derivative, and the square root vanishing at \(W=0\) was factored as \(v\sqrt{B(z)}\). The smooth group law and a formal coordinate at the identity show that for \(v_{11}(\eta_1-\eta_2)=k\ge1\), the formal coordinate of \([d](R(\eta_1)-R(\eta_2))\), divided by \(\eta_1-\eta_2\), reduces modulo 11 to a fixed tangent vector, independent of the points in the disk. Replacing the formal coordinate by its logarithm gives the same reduction, since higher terms have valuations strictly above \(k\). Applying \(\Phi\) to the tangent vector gives \(D_1\), as computed by setting \(\eta_1-\eta_2=11\). Choose a component of \(\Phi\) nonzero on this vector, and lift it to an integral linear form annihilating the exact global span. Its value on the logarithm difference has valuation exactly \(k\). Hence two different parameters cannot both give logarithms in the global span.

There is an exact point in each remaining disk whose logarithm belongs to the span: the infinity \(P\), a point above \(z=-1\), and the point with \(v=0\) and \(z^2=-8\) reducing to 6. At the last point \(W=0\), hence \(2R=P\) by the involution, so its logarithm is \(\mathcal L(P)/2\). The rational values are consequently only \(z=-1,\infty\).

Finally \(u-2/u=-1\) gives \(u=1,-2\). In the primitive fourth-power parametrization the numerator \(A\) is odd, ruling out \(-2\); \(u=1\) gives \((s,t_0)=\pm(7,4)\). Infinity gives \(t_0=0\). For \(D\), coprime \(m,n\) are necessarily of opposite parity, since both odd would give \(w^4\equiv12\pmod{16}\). The pair \(s=m^2+2mn-n^2,\ t_0=2mn\) is then coprime and covered by the result. If \(mn\ne0\), the slope \(s/t_0=7/4\) gives \(m/n=2,-1/2\). If \(mn=0\) the two axes give the other four points. Both signs of \(w\) have been included.
