# Phase 5, direction 3: one Chebyshev transfer for every degree

Status: theorem-level derivation with exact finite tests through degree
\(20\), plus selected larger cases.  The proof has received an independent
adversarial pass, but the result should remain a companion research note
until a Lucas-sequence specialist checks its priority and the stated
valuation hypotheses.  The transfer itself is classical and compositional;
the contribution proposed here is the degree-uniform normalization,
support separation, and radical telescope.

## 1. Universal integral transfer

Let \(d\geq2\), and let \(a+b=c\) be a primitive positive triple with
\(a,b\) of opposite parity.  Put

\[
D=b-a
\]

and define the homogeneous Chebyshev value

\[
H_d(D,c)=c^dT_d(D/c).
\]

The recurrence

\[
H_0=1,\qquad H_1=D,\qquad
H_{r+1}=2D H_r-c^2H_{r-1}
\]

shows that \(H_d(D,c)\) is an integer.  Define

\[
\boxed{
a'=\frac{c^d-H_d(D,c)}2,\qquad
b'=\frac{c^d+H_d(D,c)}2,\qquad
c'=c^d.
}
\tag{1}
\]

Both \(c\) and \(D\) are odd, so \(H_d(D,c)\) is odd and (1) is
integral.  The two coordinates are positive.  Indeed, equality
\(|H_d|=c^d\) would make \(e^{i\theta}\) a root of unity for
\(\cos\theta=D/c\); then \(2D/c\) would be a rational algebraic integer,
which is impossible because \(\gcd(D,c)=1\) and \(c>1\) is odd.

The transfer is primitive.  If an odd prime \(p\) divided \(a'\) and
\(b'\), it would divide \(c\) and \(H_d(D,c)\).  But

\[
H_d(D,c)\equiv2^{d-1}D^d\pmod c,
\]

and \(\gcd(D,c)=1\).  The prime \(2\) cannot divide both summands because
their sum \(c^d\) is odd.

Writing

\[
x=\frac{b-a}{c},
\]

one has the exact semiconjugacy

\[
\frac{b'-a'}{c'}=T_d(x).
\tag{2}
\]

Iteration therefore gives

\[
c_n=c_0^{d^n},
\qquad
\frac{b_n-a_n}{c_n}
=T_{d^n}\left(\frac{b_0-a_0}{c_0}\right).
\tag{3}
\]

These transfers commute and compose:

\[
\mathcal T_m\circ\mathcal T_n
=
\mathcal T_{mn}
=
\mathcal T_n\circ\mathcal T_m,
\tag{3.1}
\]

because \(c\mapsto c^{mn}\) and \(T_m\circ T_n=T_{mn}\).  Thus a
composite-degree transfer is a block of prime-degree and quadratic
transfers, not a new dynamical map.

For \(d=2\), (1) is exactly

\[
(a,b,c)\longmapsto(4ab,(b-a)^2,c^2).
\]

For odd prime \(d=\ell\), it is exactly

\[
(a,b,c)\longmapsto
(aS_\ell(a,b)^2,bC_\ell(a,b)^2,c^\ell).
\]

## 2. The fixed Lucas sequence and composite layers

Put

\[
\alpha=D+2\sqrt{-ab},
\qquad
\beta=D-2\sqrt{-ab}.
\]

Then

\[
\alpha+\beta=2D,\qquad
\alpha\beta=c^2,\qquad
(\alpha-\beta)^2=-16ab.
\]

Let

\[
U_m=\frac{\alpha^m-\beta^m}{\alpha-\beta}.
\]

This is the integral Lucas sequence

\[
U_0=0,\quad U_1=1,\quad
U_{m+1}=2D\,U_m-c^2U_{m-1}.
\]

Equation (3), or a direct norm calculation, gives

\[
\boxed{a_nb_n=a_0b_0\,U_{d^n}^2.}
\tag{4}
\]

Define the level quotient

\[
Q_{d,j}
=
\frac{U_{d^{j+1}}}{U_{d^j}}.
\]

The homogeneous cyclotomic factorization of a Lucas sequence gives

\[
\boxed{
Q_{d,j}
=
\prod_{\substack{m\mid d^{j+1}\\m\nmid d^j}}
\Phi_m(\alpha,\beta).
}
\tag{5}
\]

Thus a composite degree produces several Lucas atoms in one new layer.
The layer-index sets

\[
\mathcal L_{d,j}
=
\{m:m\mid d^{j+1},\ m\nmid d^j\}
\]

are pairwise disjoint.

## 3. Exact transfer-prime normalization

Call the seed **\(d\)-admissible** when:

1. it is primitive, positive, and of opposite parity;
2. every odd prime \(q\mid d\) divides \(a_0\);
3. \(v_q(U_q)=1\) for every odd \(q\mid d\).

Condition 3 is automatic for \(q\geq5\).  To see this, expand

\[
U_q
=
\sum_{r=0}^{(q-1)/2}
\binom q{2r+1}
D^{q-2r-1}(-4a_0b_0)^r.
\]

After division by \(q\), the first term is \(D^{q-1}\), every interior
term is zero modulo \(q\), and for \(q\geq5\) so is the final term.
The result is nonzero modulo \(q\).  At \(q=3\) the final term can cancel
the first; the explicit valuation condition is genuinely necessary.
For example, \(d=15,(a,b)=(15,2)\) fails it.

To match the cited Lucas-sequence convention \(X^2-sX-t\), take

\[
s=2D,\qquad t=-c^2,\qquad
\Delta=s^2+4t=-16a_0b_0.
\]

Here \(\gcd(s,t)=1\), because \(\gcd(D,c)=1\) and \(c\) is odd.  The
quotient \(\alpha/\beta\) is not a root of unity: otherwise
\(\alpha/c\) would be a root of unity, making \(2D/c\) a rational
algebraic integer, contrary to \(c>1\) and \(\gcd(D,c)=1\).  Thus the
sequence is nondegenerate.  For odd \(q\mid d\), admissibility gives
\(q\mid\Delta\) and \(q\nmid t\).  At \(2\), one has \(2\nmid t\),
\(v_2(s)=1\), and \(v_2(U_2)=1\).  These are precisely the hypotheses
needed below.

For odd \(q\mid d\), one has \(q\mid(\alpha-\beta)^2\) and
\(q\nmid\alpha\beta\).  The standard Lucas law of repetition,
specifically Sanna's Theorem 1.5 and Corollary 1.6 as reproduced in
Theorems 11–12 of Alecci–Miska–Murru–Romeo, gives

\[
v_q(U_m)=v_q(m)+v_q(U_q)-1=v_q(m)
\qquad(q\mid m).
\tag{6}
\]

At \(q=2\), opposite parity makes \(2D\) exactly divisible by \(2\) and
\(c^2\) odd.  The corresponding \(2\)-adic formula gives

\[
v_2(U_m)=v_2(m)
\qquad(2\mid m).
\tag{7}
\]

It follows from (6)–(7) that

\[
v_q(Q_{d,j})=v_q(d)
\qquad(q\mid d).
\]

Hence

\[
\boxed{E_{d,j}:=\frac{|Q_{d,j}|}{d}}
\tag{8}
\]

is a positive integer coprime to \(d\).

This corrects the naïve composite-degree approach.  It is false that one
may simply substitute a composite \(d\) into the prime-degree binomial
normalization term by term; for \(d=9\), for example,
\(v_3\binom93=1<2\).  The fixed Lucas quotient and (6), not individual
binomial coefficients, provide the stable normalization.

## 4. Support separation

Every \(E_{d,j}\) is coprime to \(a_0b_0c_0\).

- For \(p=2\), if \(d\) is even then (7) removes the exact
  \(2\)-part of every quotient. If \(d\) is odd, the recurrence modulo
  \(2\) gives \(U_m\equiv1\pmod2\) at every odd index \(m\).
- If an odd \(p\mid a_0\) or \(p\mid b_0\), then
  \(\alpha\equiv\beta\pmod p\), so
  \(U_m\equiv m\alpha^{m-1}\pmod p\).
  For \(p\nmid d\) this is nonzero; for \(p\mid d\), its exact systematic
  valuation was removed in (8).
- If \(p\mid c_0\), one of \(\alpha,\beta\) is zero and the other is a
  unit modulo \(p\), so \(U_m\) is nonzero modulo \(p\).

The collection

\[
E_{d,0},E_{d,1},E_{d,2},\ldots
\]

is pairwise coprime.  Suppose a prime \(p\nmid d a_0b_0c_0\) divided two
different layers.  By (5), reduction of \(\alpha/\beta\) at a prime
above \(p\) would have exact order \(m\) for an index in each layer:
the residue characteristic does not divide any \(d\)-smooth index, so a
zero of \(\Phi_m\) has exact order \(m\).  The two layer-index sets are
disjoint, a contradiction.  Conjugation only replaces
\(\alpha/\beta\) by its inverse and therefore does not change the order.

Thus the prime-genealogy statement survives composite degrees, but its
natural unit is a multi-atom layer rather than a single branch atom.

## 5. Universal radical telescope

Let

\[
R_n=\operatorname{rad}(a_nb_nc_n),
\qquad
W_{d,n}
=
\prod_{j<n}
\frac{E_{d,j}}{\operatorname{rad}(E_{d,j})}.
\]

Every prime dividing \(d\) already divides the seed radical: each odd
\(q\mid d\) divides \(a_0\) by admissibility, while \(2\mid d\) is covered
by the opposite parity of \(a_0,b_0\).  Hence
\(\operatorname{rad}(d)\mid\operatorname{rad}(a_0b_0)\), so the factor
\(d^n\) in \(|U_{d^n}|\) introduces no new radical support.

Equations (4), (8), and support separation give

\[
R_n
=
R_0\prod_{j<n}\operatorname{rad}(E_{d,j}),
\qquad
|U_{d^n}|
=
d^n\prod_{j<n}E_{d,j}.
\tag{9}
\]

Choose the unique \(\theta\in(0,\pi)\) such that

\[
\cos\theta=\frac{b_0-a_0}{c_0},
\]

then

\[
U_{d^n}
=
c_0^{d^n-1}
\frac{\sin(d^n\theta)}{\sin\theta}.
\]

Substitution in (9) proves the all-degree identity

\[
\boxed{
\frac{R_n}{c_n}
=
\frac{R_0}{c_0}
\frac{|\sin(d^n\theta)|}
{d^n\sin\theta\,W_{d,n}}.
}
\tag{10}
\]

This simultaneously specializes to:

- \(d=2\): the quadratic orbit, with
  \(Q_{2,j}=2(b_j-a_j)\) and \(E_{2,j}=|b_j-a_j|\);
- odd prime \(d=\ell\): the present paper, with
  \(Q_{\ell,j}=S_jC_j\) and
  \(E_{\ell,j}=|S_jC_j|/\ell=A_jB_j\);
- composite \(d\): a bundled multi-atom cyclotomic layer (5).

Every degree, not only every prime degree, also has a two-factor
coordinate split.  Put \(z=\sqrt b+i\sqrt a\).  For odd \(d\), the
binomial expansion defines integral \(C_d,S_d\) by

\[
z^d
=
\sqrt b\,C_d(a,b)+i\sqrt a\,S_d(a,b)
\]

and gives

\[
\mathcal T_d(a,b)
=
\bigl(aS_d(a,b)^2,\ bC_d(a,b)^2\bigr).
\]

For even \(d\), define integral \(C_d,S_d\) instead by

\[
z^d=C_d(a,b)+i\sqrt{ab}\,S_d(a,b);
\]

then

\[
\mathcal T_d(a,b)
=
\bigl(abS_d(a,b)^2,\ C_d(a,b)^2\bigr).
\]

In both cases \(U_d=S_dC_d\), so at level \(j\),
\(|Q_{d,j}|=|S_d(a_j,b_j)C_d(a_j,b_j)|\).  Under
\(d\)-admissibility, \(C_d(a_j,b_j)\) is a unit at every odd \(q\mid d\);
in the even case it is also odd.  The valuation laws above therefore
imply

\[
E_{d,j}
=
\left|\frac{S_d(a_j,b_j)}d\right|
\,|C_d(a_j,b_j)|.
\]

Thus the two-coordinate-factor split is degree-universal; parity only
changes the seed prefactor.  What is special about prime degree is instead
that the whole new Lucas layer is one homogeneous cyclotomic atom.
Composite \(d\) groups several such atoms, and (3.1) shows that this
grouping is compositional.  The useful synthesis is the degree-uniform
normalization and exact radical mechanism, not a claim that the underlying
transfer is new.

## 6. Verification and remaining review gates

`paper/chebyshev_research.py` implements (1), the Lucas sequence, layer
indices, and (8).  `paper/test_research_directions.py` verifies:

- exact recovery of the \(d=2\) and odd-prime transfers;
- exact composition and commutativity of selected degree pairs;
- the parity-dependent two-coordinate-factor split through degree \(20\);
- primitivity and Chebyshev semiconjugacy for composite degrees;
- normalization and pairwise support separation through degree \(20\),
  plus selected larger cases;
- rejection of a bad \(3\)-adic seed;
- the radical telescope in small exactly factorable cases.

Finite tests are not proofs.  Before this becomes a standalone paper, an
independent specialist should check:

1. the use and hypotheses of the Lucas law of repetition at \(2\) and
   discriminant primes;
2. the residue-order proof of cross-layer support separation;
3. priority relative to Lucas atoms, Dickson/Chebyshev transfers, and
   earlier radical-preserving constructions.

## Primary sources

- G. Alecci, P. Miska, N. Murru, and G. Romeo, “On alternative
  definition of Lucas atoms and their \(p\)-adic valuations,”
  *Monatshefte für Mathematik* 207 (2025), 175–196,
  <https://arxiv.org/abs/2308.10216>.
- C. Sanna, “The \(p\)-adic valuation of Lucas sequences,”
  *Fibonacci Quarterly* 54(2) (2016), 118–124,
  <https://www.fq.math.ca/Papers1/54-2/Sanna02242016.pdf>.
- B. E. Sagan and J. P. Tirrell, “Lucas atoms,”
  *Advances in Mathematics* 374 (2020), 107387,
  <https://arxiv.org/abs/1909.02593>.
