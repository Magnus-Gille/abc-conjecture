# The Pell-unit slice with a square norm

For positive integers \(s,t\), with \(s\) odd and \(t\) even, the only pair satisfying \(s^2-2t^2=1\) and \((s\pm t)^2+t^2\) a square is
\[
 (s,t)=(17,12),\qquad (s-t)^2+t^2=169.
\]
There are no plus-sign solutions. The same classification holds for \(|s^2-2t^2|=1\), since the prescribed parity gives \(s^2-2t^2\equiv1\pmod8\).

The unit equation implies \(s>t\) and \(\gcd(s,t)=1\). Write \(X=s-t\) for the minus norm or \(X=s+t\) for the plus norm. Then \((X,t,z)\) is a positive primitive Pythagorean triple with odd leg \(X\), so
\[
 X=a^2-b^2,\qquad t=2ab,\qquad z=a^2+b^2,
 \qquad a>b>0,\quad\gcd(a,b)=1,
\]
where \(a,b\) have opposite parity. For the minus norm, substituting \(s=X+t\) gives \(F(a,b)=1\), where
\[
 F(a,b)=a^4+4a^3b-6a^2b^2-4ab^3+b^4.
\]
For the plus norm, \(s=X-t\) gives \(F(a,-b)=1\).

The irreducible quartic Thue equation was solved in PARI/GP 2.15.4 using \(\texttt{thue(thueinit(x^4+4*x^3-6*x^2-4*x+1,1),1)}\). The flag 1 selects unconditional initialization. The integer solutions are
\[
 (-3,-2),\ (-2,3),\ (-1,0),\ (0,-1),\
 (0,1),\ (1,0),\ (2,-3),\ (3,2).
\]
They form two orbits under \((a,b)\mapsto(-b,a)\), which preserves \(F\) since \(F(a,b)=\operatorname{Re}((1-i)(a+ib)^4)\). Odd right-hand side forces opposite parity. The axis orbit has \(t=0\). Of the four remaining representatives, only \((3,2)\) satisfies \(a>b>0\) for the minus sign, giving \(X=5,t=12,s=17,z=13\). None has the form \((a,-b)\) with \(a>b>0\), as required for the plus sign. Direct evaluation at the solution gives \(U_+=985\).

[Reproducible PARI/GP script](abc_octic_pell_unit_thue.gp) · [PARI documentation for thueinit](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#thueinit)
