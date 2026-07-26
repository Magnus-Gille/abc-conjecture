# Exact obstruction for the quadratic/Chebyshev orbit

Agent: `codex`  
Date: 2026-07-25

Start with

\[
(a_0,b_0,c_0)=(1,8,9),\qquad d_n=a_n-b_n,
\]

and iterate

\[
(a,b,c)\longmapsto(4ab,(a-b)^2,c^2).
\]

Then

\[
c_{n+1}=c_n^2,\qquad d_{n+1}=c_n^2-2d_n^2,
\]

so

\[
c_n=9^{2^n},\qquad
-\frac{d_n}{c_n}=T_{2^n}(7/9).
\]

As shown in `round1.md`, the \(d_n\) are pairwise coprime and

\[
R_n=\operatorname{rad}(a_nb_nc_n)
    =6\prod_{j<n}\operatorname{rad}(d_j).
\]

## Separate the archimedean and repeated-prime losses

Put

\[
t_j=\frac{|d_j|}{c_j}
    =|T_{2^j}(7/9)|,\qquad
Q_n=\prod_{j<n}\frac{|d_j|}{\operatorname{rad}(d_j)}.
\]

Since

\[
\prod_{j<n}c_j=9^{2^n-1}=\frac{c_n}{9},
\]

we have the exact identity

\[
\boxed{\frac{R_n}{c_n}
 =\frac23\,\frac{\prod_{j<n}t_j}{Q_n}.}
\tag{1}
\]

Here \(Q_n\) measures all repeated prime-power divisibility in the orbit.

## The Chebyshev-value product is rigorously sub-power

Let

\[
z=\frac{7+4i\sqrt2}{9}.
\]

Then \(|z|=1\), \(z\) is algebraic, and \(z\) is not a root of unity:
if it were, \(z+z^{-1}=14/9\) would be a rational algebraic integer and
hence an integer.

For \(N=2^j\),

\[
t_j=|T_N(7/9)|
   =\frac12|z^N+z^{-N}|
   =\frac12|z^{2N}+1|.
\]

A standard lower bound for a nonzero linear form in logarithms of fixed
algebraic numbers gives constants \(A,C>0\), independent of \(N\), such
that

\[
|z^{2N}+1|\ge C N^{-A}.
\]

(Equivalently, apply Baker--Wüstholz to
\(2N\log z-(2m+1)\pi i\), with the closest integer \(m\).)
Consequently

\[
0\le-\sum_{j<n}\log t_j=O(n^2)
                  =o(\log c_n),
\tag{2}
\]

because \(\log c_n=2^n\log9\).

Combining (1) and (2),

\[
\boxed{\log\frac{c_n}{R_n}=\log Q_n+O(n^2).}
\tag{3}
\]

Thus the possible exceptional smallness of individual real Chebyshev
values is not the unresolved issue; linear forms in logarithms controls
their total contribution.

## Exact quality thresholds

Let

\[
q_n=\frac{\log c_n}{\log R_n}.
\]

Equation (3) gives:

1. \(q_n\to1\) if and only if
   \[
   \log Q_n=o(\log c_n).
   \]

2. For fixed \(\delta>0\),
   \[
   q_n\ge1+\delta
   \quad\Longleftrightarrow\quad
   \log Q_n
   \ge\frac{\delta}{1+\delta}\log c_n-o(\log c_n).
   \]

Therefore this orbit disproves abc only if its accumulated repeated-prime
quotient has positive-power growth along an infinite subsequence.  Proving
that the orbit's quality tends to one requires the opposite, sub-power
bound.

## Why known primitive-divisor theory does not decide it

Ordinary primitive-divisor results only ensure that new primes occur.  Here
pairwise coprimality already gives an even stronger elementary statement:
every prime divisor of \(d_j\) is absent from every other \(d_k\).  This
says nothing about whether \(p^2\mid d_j\), which is what contributes to
\(Q_n\).

Modulo a prime ideal, \(p\mid d_j\) corresponds to a prescribed dyadic
order for \(z\); the lift \(p^2\mid d_j\) is a Wieferich-type lift of that
order.  Controlling the aggregate of these lifts is a squarefree/radical
growth problem in arithmetic dynamics.  Even existence theorems for
squarefree primitive divisors over number fields are generally conditional
on Vojta-type conjectures (for example Ghioca--Nguyen--Tucker,
arXiv:1608.01361), and one squarefree primitive divisor per term would
still be much weaker than the proportional radical bound required by (3).

There is also a classical recurrence description.  If
\[
A_m=3^mT_m(1/3)=\tfrac12V_m(2,9),
\]
where \(V_m(2,9)\) is the Lucas \(V\)-sequence, then
\[
|d_j|=|A_{2^{j+1}}|.
\]
Thus the same obstruction can be called aggregate squarefree-part growth
at dyadic indices of a fixed Lucas sequence; primes with
\(p^2\mid d_j\) are Lucas/number-field Wieferich lifts.

More explicitly, take
\(\alpha=1+2\sqrt{-2}\), \(\beta=1-2\sqrt{-2}\), and
\(u=\alpha/\beta\).  For \(p\nmid6\) and a prime ideal above \(p\),
\[
p\mid d_j\quad\Longrightarrow\quad
\operatorname{ord}_{p}(u)=2^{j+2}.
\]
If \(p\) splits in \(\mathbf Q(\sqrt{-2})\), this forces
\(p\equiv1\pmod {2^{j+2}}\); if it is inert, it forces
\(p\equiv-1\pmod {2^{j+2}}\).  The stronger divisibility
\(p^2\mid d_j\) says that this order fails to acquire the usual extra
factor \(p\) on lifting modulo \(p^2\), which is precisely the
Lucas/number-field Wieferich phenomenon.

As a bounded check, `chebyshev_square_lifts.py` iterated the recurrence
modulo \(p^2\) for every prime \(p\le10^7\) and every \(0\le j\le50\).
It found no \(p^2\mid d_j\) among the 664,577 tested primes (excluding
2 and 3).  This is consistent with rare Wieferich lifts, but it proves
nothing beyond the tested range and is not used in the reduction.

## Branch verdict

The transformation supplies a rigorous infinite family of abc hits, but it
does not supply a fixed quality gap.  After the archimedean factor is
removed rigorously, the question is exactly the unresolved positive-power
versus sub-power growth of \(Q_n\).  No unconditional theorem found controls
that quantity strongly enough in either direction.
