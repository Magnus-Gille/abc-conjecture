# Squarefree cofactors of the two quadratic factors

Let $n=7+12j$, $j\ge0$, and let $L_n$ denote the Lucas numbers. Define

$$A=(L_n-6)^2-20,\qquad B=(L_n-9)^2-5.$$

Write $A=d_As_A^2$ and $B=d_Bs_B^2$ with $d_A,d_B$ positive and squarefree. Thus $s_H^2$ is the largest square dividing $H$ for $H=A,B$. Two unconditional estimates hold.

* The exact minima over the entire progression are $d_A=509$ and $d_B=395$. Each is attained only at $n=7$.
* As $n$ grows, $d_A\gg n/\log^3(2n)$ and $d_B\gg n^2/\log^4(2n)$. The constants are effective. In particular, any $p$ with $p^2\mid B$ satisfies $p\ll L_n\log^2(2n)/n$. For $p^2\mid A$ the bound is $p\ll L_n\log^{3/2}(2n)/\sqrt n$.

The family is primitive with $1728(L_n-11)+5(F_nB)^2=A^3$. In this construction, a repeated prime of size at least $\exp(\delta n)$ at infinitely many indices, with fixed $\delta>0$, would disprove abc. Both upper bounds on $p$ still allow that scale for $0<\delta<\log((1+\sqrt5)/2)$. [Family and radical](hall_pell_direction.md)

## Uniform growth of the cofactors

Write $(c,k)=(6,20)$ or $(9,5)$, $x=L_n-c$, and $x^2-k=ds^2$. For $n\ge7$ we have $x\ge20$ and $2x-1>k$, so $d>1$. Put $\alpha=(1+\sqrt5)/2$, $U=\alpha^n$, and $\lambda=x+s\sqrt d$. Since $n$ is odd,

$$2U-\lambda=2c+2/U+k/\lambda,\qquad 0<1-\lambda/(2U)<12/U.$$

Here $0<k/\lambda\le1$ and $U>24$. Let $\epsilon>1$ generate the totally positive norm-one units of $\mathbb Q(\sqrt d)$, and write $R=\log\epsilon$. A norm-one unit exceeding 1 has integral trace at least 3, giving an absolute positive lower bound for $R$. The real quadratic class number formula gives

$$R\ll \sqrt d\,\log(2d).$$

Indeed $R$ is at most twice the ordinary regulator, the field discriminant is at most $4d$, and $L(1,\chi_D)\ll\log(2D)$ by periodicity and partial summation. The quadratic class number is at least one.

Choose an integer $m$ such that $\gamma=\lambda\epsilon^{-m}$ lies between $\sqrt{k/\epsilon}$ and $\sqrt{k\epsilon}$. The conjugate $k/\gamma$ satisfies the same bounds. The element $\gamma$ is an algebraic integer, so the absolute logarithmic height of $\gamma/2$ is $O(1+R)$. Also $|m|\ll n+1$ and $h(\epsilon)=R/2$. Apply the real logarithm bound of Matveev to the nonzero difference

$$ (\gamma/2)\epsilon^m\alpha^{-n}-1=\lambda/(2U)-1. $$

All numbers are positive and lie in a field of degree at most four. For three logarithms the estimate bounds the negative logarithm of the absolute difference by a constant times the product of their modified heights times $\log(2+\max |b_i|)$, where the $b_i$ are the exponents. The upper bound $12/U$ therefore gives $n\ll(1+R)^2\log(2n)$. This proves $d_A\gg n/\log^3(2n)$ upon substituting the regulator bound. In making this substitution one can first restrict to $d\le n^2$, since larger $d$ already satisfy both claimed inequalities. [Matveev, Izvestiya Mathematics 64 (2000), 1217–1269](https://doi.org/10.1070/IM2000v064n06ABEH000314)

For $B$ the progression gives $L_n\equiv9\pmod{10}$ and hence $5\mid x$. Now

$$\frac{\lambda^2}{5}=\frac{2x^2-5}{5}+\frac{2xs}{5}\sqrt d$$

is a totally positive algebraic integer of norm one, so it equals $\epsilon^\ell$ with $0<\ell\ll n$. The nonzero difference $(5/4)\epsilon^\ell\alpha^{-2n}-1$ has absolute value at most $24/U$. Two of the three inputs have fixed heights, giving $n\ll(1+R)\log(2n)$. This yields the stronger bound on $d_B$. Each bound on $p$ follows from $p\mid s$ and $s\le L_n/\sqrt d$.

## Certifying the exact minima

Let $u_j=L_{7+12j}$. Its recurrence is $u_0=29$, $u_1=9349$, $u_{j+2}=322u_{j+1}-u_j$. At $j=0$ the values are $A=509$ and $B=395=5\cdot79$, both squarefree. To check which cofactors up to these values can occur, try each squarefree $d$ and $j\bmod60$. For each modulus in the table keep a residue only if $(u_j-c)^2-k$ equals $d$ times a square modulo that modulus. The recurrence returns to its initial pair after 60 steps modulo each listed modulus, so this finite check covers every index.

| Factor | Cofactors tested | Moduli | Surviving cofactors |
|---|---:|---|---|
| $A$ | $1\le d\le509$ | $3,5,8,11,17,19,41,61$ | $269,509$ |
| $B$ | $1\le d\le395$ | $3,7,8,23,25$ | $395$ |

The cofactor 269 actually occurs at the negative index $n=-5$, which belongs to the same progression modulo 12. Any congruence test valid for this entire two-sided recurrence must retain its residue class. To finish the positive-index problem, use an explicit norm-one unit for each of the three surviving equations.

| $d$ | $k$ | Chosen $\epsilon$ | Possible $\gamma$ after reduction |
|---:|---:|---|---|
| 269 | 20 | $13449+820\sqrt{269}$ | $17\pm\sqrt{269}$ |
| 509 | 20 | $(855627+37925\sqrt{509})/2$ | $23\pm\sqrt{509}$ |
| 395 | 5 | $159+8\sqrt{395}$ | $20\pm\sqrt{395}$ |

For this table it suffices that $\epsilon$ is an integral unit of norm one exceeding 1. As above choose $m$ with $\gamma=\lambda\epsilon^{-m}$ and both $\gamma$ and its conjugate in $[\sqrt{k/\epsilon},\sqrt{k\epsilon}]$. Write $2\gamma=X+Y\sqrt d$ with integral $X,Y$. Then $X>0$, $X^2-dY^2=4k$ and $|Y|\le\sqrt{k\epsilon/d}$. Enumerating these integers verifies the last column, allowing both choices at an interval endpoint.

For these three fields the explicit three-logarithm inequality gives $n<10^{25}$. To see the numerical margin, use degree at most 4, exponent bound $3n$, and all three modified heights $A_i=100$ for $\gamma/2,\epsilon,\alpha$. These exceed $4h(\eta),|\log\eta|,0.16$ for each input $\eta$ in the table. For example $\epsilon<10^6$ has height $(\log\epsilon)/2$ and both conjugates of $\gamma$ are positive and below $50$. From $\lambda<2U$ and the tabulated $\gamma,\epsilon$ one obtains $|m|<3n$. Matveev's real-field bound and the upper bound $12/U$ give

$$n\log\alpha < \log12+10^{19}(1+\log(3n)).$$

Indeed $1.4\cdot30^6\cdot3^{4.5}\cdot4^2(1+\log4)\cdot100^3<10^{19}$. The displayed inequality fails at $10^{25}$ and at every larger value.

To reduce this cutoff, put $\tau=\log\alpha/\log\epsilon$ and $\mu=\log(\gamma/2)/\log\epsilon$. Since $12/U<1/2$ and $\log\epsilon>1$, the same upper bound gives $|n\tau-m-\mu|<24/U$. Given integers $P,Q$ with $Q>0$ this implies

$$\|Q\mu\| \le n|Q\tau-P|+24Q/U,$$

where the left side is the distance to the nearest integer. The verifier supplies a pair for each field with $Q<10^{30}$, $10^{25}|Q\tau-P|<1/100$ and $\|Q\mu\|>1/10$ for both signs of $\gamma$. It certifies these inequalities with interval arithmetic. Hence $U<267Q$ and $n<160$, since $\alpha>8/5$ and $(8/5)^{160}>267\cdot10^{30}$. Exact integer evaluation for $n=7,19,\ldots,151$ then leaves only the two values at $n=7$. [Reproducible certificate](hall_pell_cofactor_check.py)

Run the finite check with Python's standard library from the directory containing the verifier.

    python3 -B hall_pell_cofactor_check.py
