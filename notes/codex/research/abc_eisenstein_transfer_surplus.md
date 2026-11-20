# Exact radical gain of the degree-96 Eisenstein transfer

For every primitive source triple of height at most 100 except (1,1,2), both odd-coordinate choices were tested with the map
\[
 U_0+\sqrt{-3}V_0=(x^4+\omega y^4)^{12},\qquad
 W=x^8-x^4y^4+y^8,\qquad C=W^{12}=U^2+3V^2,
\]
where U,V are the absolute values of the coefficients, y is the even entry, and x is one of the two odd entries. All prime factors of U,V,W were proved prime. Of 3,042 transfers from 1,521 source triples, 383 have positive output log gain, 2,364 improve the source log gain, and three take a positive source log gain below zero. There are 2,040 distinct parameter pairs, since a pair can belong to both a sum and a difference triple. [Map and congruence restrictions](abc_eisenstein_power_conic.md) · [Factor certificate generator](abc_eisenstein_transfer_surplus.py) · [Exact census comparisons](abc_eisenstein_transfer_summary.py)

## An exact division between source and new prime powers

Let z be the remaining source entry, c the largest entry, R=rad(xyz), and
\[
 E=\frac{U}{\operatorname{rad}(U)}\frac{W}{\operatorname{rad}(W)}
       \prod_{p\mid V,\ p\nmid xyz}p^{v_p(V)-1}.
\]
Then the ratio of the output and source radical gains is exactly
\[
 \frac{W^{12}/\operatorname{rad}(3UVW)}{c/R}
 =\frac{2\,3^{\mathbf1_{3\mid xyz}}(xy)^4zW^{11}}{cUV}\,E .
\]
Indeed the source entries are pairwise coprime. For p dividing xy one has vₚ(V)=4vₚ(xy)+vₚ(6). For odd p dividing z one has vₚ(V)=vₚ(z)+vₚ(3). To see this, put s=x⁴,t=y⁴. Up to sign,
\[
 2V=3st(s^2-t^2)(s-2t)(2s-t)
 (s^2-4st+t^2)(s^2+2st-2t^2)(2s^2-2st-t^2).
\]
At odd p dividing xy all factors other than st are units. At odd p dividing z, s≡t is a unit, all factors except s²−t² are units after the coefficient 3 is removed, and vₚ(x⁸−y⁸)=vₚ(z). At 2, s is odd and 16 divides t, so exactly two factors beyond st contribute one power of 2 each. The powers in V above source primes consequently contribute exactly 2·3^[3|xyz]·(xy)⁴z/R to V/rad(V). Since 3|V and U,V,W are pairwise coprime, the formula follows.

## Examples

“New excess” denotes E. All logarithms are natural. The ordinary abc quality is log C/log rad(3UVW).

| Source | x | Source log gain | Output log gain | New excess |
|---|---:|---:|---:|---:|
| 1+8=9 | 1 | 0.405465 | 0.405591 | 1 |
| 1+8=9 | 9 | 0.405465 | 5.461531 | 23 |
| 3+59=62 | 59 | −5.176150 | 9.141251 | 47·5·11·23² |
| 3+125=128 | 3 | 1.450833 | 3.992066 | 13 |
| 3+125=128 | 125 | 1.450833 | 0.802822 | 1 |
| 1+80=81 | 81 | 0.993252 | −0.216645 | 1 |
| 1+4374=4375 | 1 | 3.036554 | 3.036554 | 1 |
| 1+4374=4375 | 4375 | 3.036554 | 4.048101 | 11 |

The census maximum by output quality occurs at x=9,y=8, with quality 1.0270019248792552. The input triples 1+8=9 and 8+9=17 both give these parameters. Here 23² exactly divides U. The maximum output log gain and maximum improvement both occur at x=59,y=62. Here 47² exactly divides U, while 5²,11² and 23³ exactly divide V outside the source support, and W is squarefree. The three positive-to-negative cases are 1+48=49, 1+63=64 and 1+80=81, each using the larger odd entry. For 1+4374=4375 with x=1, the output log gain exceeds the source by only 1.3660131795808 × 10⁻¹⁵. The exact prime factors for the classic examples are recorded separately. [Full factorizations](abc_eisenstein_transfer_examples.jsonl)

For the last near equality, set q=y⁻⁴ at x=1 and z=c=y+1. If 3 divides the source the rational prefactor in the exact ratio is 6y⁴W¹¹/(UV). The normalized real and imaginary coefficients of (ω+q)¹² are 1−6q−33q²+O(q³) and −6q+33q²+O(q³), respectively. As W/y⁸=1−q+q², the prefactor is 1+q/2+O(q²). Whether E=1 along an infinite sequence is a separate arithmetic question.

Run the following commands in the scratch directory with python-flint installed. The factor generator checks the original power identity and the full integer product of each prime certificate. All comparisons of ratios in the census use rational arithmetic, and the maximum quality uses certified real intervals.

~~~sh
python abc_eisenstein_transfer_surplus.py --bound 100 > /tmp/eisenstein-transfer-100.jsonl
python abc_eisenstein_transfer_summary.py /tmp/eisenstein-transfer-100.jsonl
~~~
