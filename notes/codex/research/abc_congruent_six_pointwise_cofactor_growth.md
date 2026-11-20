# Superpolylogarithmic growth of the squarefree kernel at every odd index

On \(E_6:y^2=x^3-36x\) let \(G=(-3,9)\), let \(B_n\) be the positive square root of the reduced abscissa denominator of \([n]G\), and put \(D_n=\prod_{v_p(B_n)\ {\rm odd}}p\). Write \(\omega_1(d)=\#\{p\mid d:p\equiv1\pmod{24}\}\); \(\omega\) counts distinct prime factors, and \(\Omega\) counts prime factors with multiplicity. There is an absolute constant \(A>1\), depending only on the fixed genus and curves here, such that for odd \(n\ge1\), \(D=D_n\),
\[
                  1+\Omega(n)\le (1+\omega(D)) A^{1+\omega_1(D)}.          \tag{1}
\]
In particular, at **every** sufficiently large odd \(n\),
\[
                 \log D_n\gg \log\log n\,\log\log\log n .                 \tag{2}
\]
Thus \(D_n>(\log n)^a\) eventually for each fixed \(a>0\). When \(\omega_1(D_n)\le k\) for a fixed \(k\), one has the stronger pointwise estimate \(\log D_n\gg_k\sqrt{\log n\,\log\log n}\). No numerical value for the uniform Mordell–Lang constant is required here.

## The curve for a cofactor and its rational points

The [full parametrization](abc_full_quartic_signature.md) gives \(a^4+3b^2=4w^4\), \(w=B_n\), with primitive odd coordinates and \(3\nmid aw\). All rational primes dividing \(w\) are \(1\bmod12\). Indeed such a prime is good, \(G\) has odd reduction order, and the rational two-descent characters at \(x(G)=-3\) imply both \(-1\) and 3 are squares there. Write \(w=d z^2\) with \(d=D_n\). In \(K=\mathbf Q(\sqrt3)\) the coprime factors \(2d^2z^4\pm b\sqrt3\) multiply to \(a^4\). The [real quadratic descent](abc_full_quartic_square_classification.md) applies unchanged: the class number is one, the factors are totally positive, \(a\) is prime to 6, and parity followed by conjugation permits the unit \(\epsilon=2+\sqrt3\) multiplying a fourth power. One obtains a rational point on
\[
 C_d:\quad d^2 Z^4=f(U,V),\qquad f=U^4+6U^3V+18U^2V^2+18UV^3+9V^4,
\]
with \(Z=z\), \(a=|U^2-3V^2|\). Each positive odd index with kernel \(d\) supplies such a point, and a projective point cannot represent two positive indices. Its ratio \(|U^2-3V^2|/(dZ^2)\) recovers \(a/w\), hence \(x([n]G)=-3a^2/w^2\); two equal abscissas give equal or opposite multiples, and \(G\) has infinite order.

Over \(K\) the quartic becomes \(\epsilon(U+\sqrt3V)^4+\epsilon^{-1}(U-\sqrt3V)^4=4d^2 Z^4\). It is a smooth plane quartic of genus three. Its Jacobian has a rational isogeny decomposition
\[
          \operatorname{Jac}(C_d)\ \sim_{\mathbf Q}\ E_6\times
             \operatorname{Res}_{K/\mathbf Q} J_d,\qquad
             J_d:\ y^2=x^3-4\epsilon d^2 x.                                \tag{3}
\]
The quotient by the sign of \(Z\) is the fixed genus-one curve \(W^2=f(U,V)\) via \(W=dZ^2\). The binary-quartic invariants are \(I=108, J=0\), so its Jacobian \(y^2=x^3-27Ix-27J\) scales by \((x,y)=(9x',27y')\) to \(E_6\). On putting \(X=(U+\sqrt3V)/Z, Y=(U-\sqrt3V)/Z\), the nonconstant map \((-Y^2,\epsilon X^2Y)\in J_d\) is invariant under the sign of \(X\); conjugation gives the other map invariant under the sign of \(Y\). The three pulled-back differential lines belong to the three distinct nontrivial characters of the Klein four group of projective coordinate sign changes. They span the three-dimensional differential space. Together the maps on Jacobians give an isogeny over \(K\), and the conjugate pair of maps descends to the stated restriction of scalars over \(\mathbf Q\).

## The refined two-descent rank estimate

Set \(k=\omega_1(d)\). We claim
\[
                 \operatorname{rank} J_d(K)\le1+4k,\qquad
                 \operatorname{rank}\operatorname{Jac}(C_d)(\mathbf Q)\le2+4k.\tag{4}
\]
Use the abscissa squareclass maps of the usual two-isogeny descent on \(J_d\) and its dual \(y^2=x^3+16\epsilon d^2x\). For either coefficient \(a_0=-4\epsilon d^2\) or \(16\epsilon d^2\), the squareclass image is represented by elements of even valuation away from primes dividing \(2d\), as follows from \(y^2=x(x^2+a_0)\). The value at the nonidentity kernel point is the class of \(a_0\) and has the same support. Every prime of \(d\) splits in \(K\), since it is \(1\bmod12\). The fundamental unit is \(\epsilon\), and \(\delta=1+\sqrt3\) generates the unique dyadic prime with \(\delta^2=2\epsilon\).

If a descent representative \(e\) has valuation 1 at \(\delta\) after scaling by squares, the local descent equation \(s^2=e u^4+(a_0/e)v^4\) is impossible: the two term valuations are \(1+4v_\delta(u)\) and \(3+4v_\delta(v)\) on \(J_d\), or \(1+4v_\delta(u)\) and \(7+4v_\delta(v)\) on the dual. They are odd and unequal whenever both terms are nonzero, and a single nonzero term also has odd valuation.

At either prime above \(p\mid d\) with \(p\equiv13\bmod24\), suppose again that \(e\) has valuation 1. The two coefficients in the local descent equation now both have valuation 1. At a primitive local pair both \(u,v\) must be units for cancellation. After division by a uniformizer, cancellation forces \(-a_0/d^2\) to be a square in the residue field, by moving one term across the equality and clearing \(e^2/d^2\). This would make \(\epsilon\) a square on \(J_d\), or \(-\epsilon\) on the dual. But \(\epsilon=\delta^2/2\), \((2/p)=-1\), and \((-1/p)=1\). Both are excluded.

Consequently only the two primes over each of the \(k\) prime divisors \(1\bmod24\) can supply odd valuations. By class number one the ambient squareclass space has dimension at most \(2+2k\), allowing the two unit classes \(-1,\epsilon\). On the dual, all abscissas and the torsion class are totally positive; at least the sign class \(-1\) is therefore excluded, giving dimension at most \(1+2k\). The two-isogeny rank formula subtracts two from the sum of these dimensions and proves the first inequality in (4). The second follows from (3) and \(\operatorname{rank} E_6(\mathbf Q)=1\).

The uniform Mordell–Lang theorem for curves over a fixed-degree number field bounds \(\#C(\mathbf Q)\) for a smooth genus-three curve by \(c^{1+\mathrm{rank}\,\mathrm{Jac}(C)(\mathbf Q)}\), with \(c\) independent of the curve. Applying it to (4) and increasing the absolute constant once gives at most \(A^{1+\omega_1(d)}\) positive odd indices for a fixed admissible kernel \(d\). Empty twists contribute zero. This bounds cardinalities without assuming any bound for the height of a rational point. [Dimitrov, Gao and Habegger, *Uniformity in Mordell–Lang for curves*, Annals of Mathematics 194 (2021), 237–298](https://arxiv.org/abs/2001.10276)

If \(\omega_1(d)=0\), the uniform count can be replaced by the explicit bound of six positive odd indices. The Jacobian rank is at most two and \(C_d\) has good reduction at 7: its diagonal form over the unramified extension adjoining \(\sqrt3\) has unit coefficients, since \(7\nmid d\). Every nonzero square in \(\mathbf F_7\) has two fourth roots, so multiplication of \(f(U,V)\) by \(d^{-2}\) preserves the number of points above each projective slope. Thus \(\#C_d(\mathbf F_7)=\#C_1(\mathbf F_7)=8\), as counted in the square-classification verifier. Coleman's bound at \(7>2g\) gives \(\#C_d(\mathbf Q)\le8+2g-2=12\). Each represented index gives two distinct rational projective points \((U:V:\pm Z)\), since \((U,V)\ne(0,0)\) and \(Z\ne0\). Both recover the same index, and points representing different positive indices are disjoint by their recovered abscissas.

## Ordered divisors turn the count into a pointwise bound

List the prime factors of \(n\) with repetition as \(q_1\ge\cdots\ge q_t\), where \(t=\Omega(n)\). Set \(m_0=1\), \(m_j=\prod_{i=1}^j q_i\). These are distinct positive odd integers. For any \(p\mid B_{m_j}\), let \(s\) be the order of the reduction of \(G\) at \(p\). Since \(G\) is integral at every good prime, \(s>1\), and \(s\mid m_j\) implies \(s\ge q_j\). The full rational two-torsion and the odd order \(s\) give \(4s\mid\#E_6(\mathbf F_p)\). Hence Hasse gives \(p\ge(2\sqrt s-1)^2>s\), so every prime in \(m_{j+1}/m_j\) or the longer remaining product \(n/m_j\) is strictly below \(p\). The formal group preserves the positive depth under all these multipliers. Thus
\[
           D_{m_0}\mid D_{m_1}\mid\cdots\mid D_{m_t}=D_n.
\]
This includes repeated factors of the index; at \(m_0\) one has \(B_1=1\). A nested chain of squarefree divisors of \(D\) takes at most \(1+\omega(D)\) distinct values. Each value occurs among these indices at most \(A^{1+\omega_1(D)}\) times by the preceding count, which proves (1).

If \(\omega_1(D)=0\), the same holds for every prefix kernel. The value 1 occurs only at \(m_0=1\) by the square classification. Every other value occurs at most six times by Coleman's bound. Hence \(1+\Omega(n)\le 1+6\omega(D)\), including \(n=1\).

For \(n>1\) the [square-denominator classification](abc_full_quartic_square_classification.md) gives \(D_{q_1}>1\). Any prime dividing it is strictly above \(q_1\), as just shown, and remains in \(D_n\). It follows that \(\log n\le\Omega(n)\log D\). Write \(H=\log D\), \(k'=\omega(D)\). The product of \(k'\) distinct primes is at least \((k'+1)!\), so \(H\gg k'\log(2k')\). Taking logarithms in (1) gives
\[
             \log\log n\le \log H+\log(1+k')+(1+\omega_1(D))\log A.
\]
If \(H\ge(\log\log n)^2\), (2) follows immediately. Otherwise the first two terms on the right are \(O(\log\log\log n)\); hence \(k'\ge\omega_1(D)\gg\log\log n\), and the factorial estimate proves (2). For bounded \(\omega_1(D)\), (1) instead yields \(\log n\ll_k (1+k')H\ll_k H^2/\log(2H)\). This first gives \(\log H\gg\log\log n\) and then the stated square-root estimate.

There is an explicit estimate when all primes of \(D_n\) are \(13\bmod24\). Every prefix cofactor \(d\mid D_n\) then has Jacobian rank at most two by (4), below the genus three. Its quartic has good reduction at 7, as follows also from the diagonal form over the unramified quadratic extension. In \(\mathbf F_7^\times\), the fourth powers are precisely the squares, so rescaling \(Z\) identifies this reduction with \(C_1\bmod7\). It has exactly eight points by the [finite computation](abc_full_quartic_square_classification.py). The Chabauty–Coleman bound at the good prime \(7>2g\) therefore gives \(\#C_d(\mathbf Q)\le8+2g-2=12\). Each positive index provides two distinct points \((U:V:Z)\) and \((U:V:-Z)\) because \(Z\ne0\) and \((U,V)\ne(0,0)\); the abscissa recovery above rules out sharing between distinct indices. Thus a cofactor can occur at most six times, and \(d=1\) occurs just once by the square classification. The ordered chain has at most \(\omega(D_n)\) other cofactor values, giving the numerical bound \(\Omega(n)\le6\omega(D_n)\) in this case.
