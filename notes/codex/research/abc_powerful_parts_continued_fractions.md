# A product bound for abc triples with the same prescribed prime powers

Fix pairwise coprime positive integers \(A,B,C\), put \(S=\operatorname{rad}(ABC)\), and consider primitive positive triples
\[
 a+b=c,\qquad a=Ax,\quad b=By,\quad c=Cz .
\]
Then \(G=C/(Sxy)=c/(Sxyz)\) is a certified lower bound on \(c/\operatorname{rad}(abc)\), since \(\operatorname{rad}(ABCxyz)\le Sxyz\). If \(A,B,C\) are the full powerful parts of the respective terms, meaning the products of the exact prime powers with exponent at least two, equality holds. In that case \(x,y,z\) are squarefree and coprime to \(S\) and to one another.

## What square divisibility alone certifies

If every marked prime is used only to exponent two, write \(ABC=D^2\) with \(D\) squarefree. Then \(S=D\), and \(G=D/(ab)\le1\) in every primitive triple, regardless of how many distinct squares are marked. Indeed \(D^2\mid abc\) and \(c=a+b\le ab+1\) imply \(D^2\le ab(ab+1)<(ab+1)^2\). The integrality of \(D\) covers even the borderline case \(a=1\). Constructions that combine prescribed squares with known higher powers can have a larger certificate.

More precisely, put \(U=\prod_{p\parallel abc}p\) and \(V=\prod_{p^3\mid abc}p^{v_p(abc)-2}\). Cancelling prime by prime yields the exact identity
\[
 \left(\frac{c}{\operatorname{rad}(abc)}\right)^2
 =\frac{c}{ab}\frac{V}{U}.
\]
For \(a\le b\), a fixed gain \(c/\operatorname{rad}(abc)\ge c^\eta\) therefore forces \(V\ge(a/2)U c^{2\eta}\). In particular every positive abc hit requires a prime cube in one of its terms.

## The multiplicative bound

For any collection of distinct such triples with \(SG_i>1\),
\[
                   \prod_i SG_i\le C.                                      \tag{1}
\]
If \(a_i\le b_i\) and \(SG_i b_i/c_i>1\) for every member, then also
\[
                   \prod_i SG_i\frac{b_i}{c_i}\le B.                       \tag{2}
\]
In particular (1) applies to every actual abc hit with the same full powerful parts. For every fixed \(0<\eta<1\), **strictly fewer than \(1/\eta\)** distinct triples for the same prescribed parts can have \(G_i\ge c_i^\eta\). Indeed, for one or more such triples, \(C\ge2\), \(S\ge2\), and \(c_i\ge C\), so \(C\ge S^m C^{m\eta}>C^{m\eta}\) for a collection of size \(m\).

To prove (1), the congruence \(Ax+By\equiv0\pmod C\) makes \(x_2 y_1-x_1 y_2\) a multiple of \(C\). It is nonzero for distinct triples since each pair \((x,y)\) is primitive. Each product \(x_i y_i<C\). Two different points cannot have equal \(x\) or equal \(y\), since their determinant would have absolute value below \(C\). Sorting by increasing \(x_i\) forces strictly decreasing \(y_i\), as two coordinates increasing would again give determinant of absolute value below \(C\). Thus
\[
 x_{i+1}y_i\ge C+x_i y_{i+1}> C,\qquad
 x_{i+1}/x_i>SG_i,\qquad x_m\le C/(SG_m).
\]
Multiplying and using \(x_1\ge1\) gives (1), strictly if \(m\ge2\). The set in question is finite because \(x_i y_i<C\). Applying the same argument to \((x_i,z_i)\) modulo \(B\) proves (2), since \(B/(x_i z_i)=SG_i b_i/c_i\). The size restrictions in (2) hold automatically if \(a_i\le b_i\), \(G_i>1\), and \(S\ge2\).

Both arguments also give height separation. If all triples in a collection have \(a_i\le b_i\) and \(G_i>1\), order them by increasing \(x_i\). Then \(c_i\) strictly decreases and
\[
   \frac{a_{i+1}}{a_i}>SG_i,\qquad
   \frac{c_i}{c_{i+1}}>SG_{i+1}\frac{b_{i+1}}{c_{i+1}}\ge SG_{i+1}/2.
\]
This follows by bounding the same nonzero determinant first by \(x_{i+1}y_i\) and then, for the second inequality, by \(x_{i+1}z_i\) modulo \(B\).

For a fixed full powerful part \(D\) of the product \(abc\), each prime power in \(D\) can be assigned to one of the three coordinates. The number of triples of gain at least \(c^\eta\) is consequently at most \(3^{\omega(D)}/\eta\), regardless of the exponents in \(D\).

## Computing every candidate by Euclid's algorithm

The [inherited factors calculation](abc_inherited_factors.md) already uses the following continued-fraction test for powers inherited from a seed. Formula (1) adds a product bound across all the candidates for a fixed assignment. For \(C>1\), take the least nonnegative \(k\equiv-A B^{-1}\bmod C\). For a candidate write \(kx-Ch=y>0\). Then \(h/x\) is reduced by \(\gcd(x,y)=1\), and
\[
 \frac{k}{C}-\frac{h}{x}=\frac{y}{Cx},\qquad
 \frac{1}{x^2\lvert k/C-h/x\rvert}=\frac{C}{xy}=SG .
\]
If \(SG>2\), Legendre's criterion puts \(h/x\) among the convergents of \(k/C\). It is not the final convergent. If \(q'\) denotes the denominator preceding \(x\), the reciprocal approximation coefficient is \(\alpha+q'/x\), with \(\alpha\) the next complete quotient. Consequently the next partial quotient lies within two of \(SG\). Conversely, for each convergent \(h/x\) form \(y=kx-Ch\), reject nonpositive \(y\), and put \(z=(Ax+By)/C\). A positive result with \(\gcd(Ax,By)=1\) yields a triple and certifies exactly the lower bound \(G=C/(Sxy)\). To require full powerful parts, also test that the residuals are squarefree and coprime to \(S\) and the prescribed parts are powerful (allowing 1). Thus a single finite continued fraction enumerates all abc hits with fixed ordered full powerful parts. It uses \(O(\log C)\) Euclidean divisions.

For a finite example take \((A,B,C)=(1,2^{12},7^7)\). Here \(k=40011\), and \(k/C=[0;20,1,1,2,1,1,16,201]\). Two different triples with those full powerful parts are
\[
 1+163885056=163885057,\qquad 247+823296=823543.
\]
The respective residuals are \((1,40011,199)\) and \((247,201,1)\), with \(40011=3\cdot13337\), \(247=13\cdot19\), and \(201=3\cdot67\). The lower convergents \(0/1\) and \(12/247\) give exact excesses \(823543/(14\cdot40011)\) and \(823543/(14\cdot247\cdot201)\), approximately 1.470 and 1.185. The following digits are 20 and 16, respectively. Testing all the displayed convergents shows these are the only hits with these full powerful parts, at any height.

For comparison across possible residue classes, if \(T>2\), at most \(\lfloor C/T\rfloor(1+\log\lfloor C/T\rfloor)\) residues \(k\bmod C\) admit positive \(x,y\) with \(xy\le C/T\), \(\gcd(x,C)=1\), and \(kx\equiv y\bmod C\), provided \(C/T\ge1\). For \(T>C\) there are none. Each pair determines at most one residue and the bound follows by summing \(\lfloor C/(Tx)\rfloor\). This does not give a distribution estimate on the particular residues \(-AB^{-1}\) coming from powerful integers. Formula (1) controls multiplicity for each choice of prescribed parts. The infinitely many possible choices remain the obstacle to a global conclusion.

## Moving exact squares on a fixed conic

Take fixed positive squarefree integers \(d_1,d_2,d_3\) and primitive triples of the form
\[
 a=d_1x^2,\qquad b=d_2y^2,\qquad c=d_3z^2 .
\]
Let \(S_0\) be a finite set of primes containing the divisors of \(d_1d_2d_3\). For a positive integer \(n\), write \(n_{S_0}=\prod_{p\in S_0}p^{v_p(n)}\) and \(Q_{\rm out}(n)=\prod_{p\notin S_0}p^{\max(v_p(n)-1,0)}\). Then for every \(\epsilon>0\),
\[
 \operatorname{rad}(abc)\gg_{d_i,S_0,\epsilon}
       \frac{c^{1-\epsilon}}{Q_{\rm out}(xyz)}.                              \tag{3}
\]
Thus a fixed gain \(c/\operatorname{rad}(abc)\ge c^\eta\) on this conic requires \(Q_{\rm out}(xyz)\gg c^{\eta-\epsilon}\). Outside \(S_0\) a contributing prime has exponent at least four in \(abc\). In particular, fix any finite set \(S_0\). Among primitive triples in which *every* prime divisor of \(abc\) outside \(S_0\) occurs exactly twice, only finitely many attain any fixed gain exponent. This last statement follows because the odd part of each exponent pattern comes from \(S_0\), so the three squarefree kernels belong to a finite list. Valuations at primes in \(S_0\) are unrestricted. For example \(49+576=625\) meets the condition for \(S_0=\{2,5\}\) and has radical 210.

Here is the proof of (3). If the conic \(d_1X^2+d_2Y^2=d_3Z^2\) has a rational point, it is parametrized over \(\mathbb Q\) by three integral homogeneous quadratic forms \(F_1,F_2,F_3\). They are a nonsingular linear change of the three monomials \(s^2,st,t^2\): the complete linear system of the plane conic corresponds to degree two on the projective line. For primitive parameters \((s,t)\), the evaluation gcd divides the absolute determinant of the change of basis, by its adjugate. Thus \((x,y,z)\) is, up to sign, the evaluations divided by a bounded integer. Their largest absolute value is comparable to \(h^2\), for \(h=\max(|s|,|t|)\). Since \(c=a+b\) and the coefficients are fixed, \(c\asymp h^4\). The sextic \(F=F_1F_2F_3\) has six distinct projective roots over \(\overline{\mathbb Q}\). Indeed each coordinate line cuts the conic in two distinct points and no point has two zero coordinates.

For clarity, the rational real and \(p\)-adic Subspace Theorem gives for this fixed sextic
\[
       \frac{|F(s,t)|}{|F(s,t)|_{S_0}}\gg_{F,S_0,\delta} h^{4-\delta}
       \quad(F(s,t)\ne0,\;\delta>0),                                       \tag{4}
\]
where the denominator in (4) denotes the positive integer \(S_0\)-part of the absolute value. At each place \(v\) in \(S_0\cup\{\infty\}\), let \(\delta_v\) be the minimum projective distance of \([s:t]\) to a geometric root of \(F\), using the projective determinant divided by the two maximum coordinate norms. Factoring the sextic shows \(|F(s,t)|_v/\|(s,t)\|_v^6\asymp_{F,v}\delta_v\). Distinctness of the roots keeps the other five normalized factors bounded away from zero when the minimum is small. In dimension two the Subspace Theorem gives \(\prod_v\delta_v\gg h^{-2-\delta}\) for these primitive rational parameters: select the linear form for a nearest root and an independent coordinate form of maximal size whenever the contact is small. At other parameters where a local contact is bounded below, a fixed independent pair of coordinate forms suffices for the usual inequality. More explicitly one may choose the coordinate form independent of the root form whose size is largest among the independent coordinates. Its size is at most the local parameter norm, so the product used in the theorem is at most a fixed constant times the product of the \(\delta_v\). There are finitely many choices of forms. Proper exceptional lines contain only finitely many primitive vectors. This is the classical projective simultaneous approximation formulation of the theorem. Multiplication using \(\|(s,t)\|_\infty=h\) and \(\|(s,t)\|_p=1\) gives (4). Bounded evaluation gcds permit replacing \(|F(s,t)|\) by \(xyz\) at bounded cost.

Finally \(\operatorname{rad}(abc)\ge (xyz)/( (xyz)_{S_0} Q_{\rm out}(xyz))\). Apply (4) with \(\delta=4\epsilon\) to obtain (3). The bound allows arbitrary square divisors from moving primes. Its constant depends on the fixed squarefree kernels and the finite prime set.
