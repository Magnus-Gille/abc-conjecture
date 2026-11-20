# An exhaustive first-depth census for the quartic abc denominator

Let \(G=(-3,9)\) on \(E_6:y^2=x^3-36x\), let \(B_j^2\) be the reduced denominator of \(x(jG)\), and set \(Y=31{,}904{,}497\). At good primes put \(r_p=\operatorname{ord}(G\bmod p)\) and \(e_p=v_p(B_{r_p})\). The good primes are precisely those above 3. Exactly one prime \(5\le p\le Y\) has both \(4\nmid r_p\) and \(e_p\ge2\):
\[
                     (p,r_p,e_p)=(211,106,2).
\]

| Good primes through \(Y\) | Odd order | Twice odd order | Odd prime order | Depth one among the eligible primes |
|---:|---:|---:|---:|---:|
| 1,968,265 | 266,475 | 1,096,986 | 41,146 | 1,363,460 |

## Uniform consequence for the actual abc radical

For each positive odd \(n\), the [quartic orbit](abc_full_quartic_signature.md) has \(C=4B_n^4\) and \(R=\operatorname{rad}(3 B_{2n})\). Its full repeated-prime factor up to the stated cutoff satisfies the exact identity
\[
 \prod_{p\le Y} p^{\max(0,v_p(3B_{2n})-1)}
 = 3^{v_3(n)} 211^{\mathbf 1_{53\mid n}}
    \prod_{\substack{5\le p\le Y\\r_p\mid 2n}}p^{v_p(n)}
 \quad\bigm|\quad 211^{\mathbf 1_{53\mid n}} n.
\]
In particular the product of \(p^{v_p(B_{2n})-1}\) over good primes \(p\le Y\) dividing \(B_{2n}\) divides the same integer. At the odd denominator one has the stronger identity and divisibility
\[
 \prod_{\substack{p\le Y\\p\mid B_n}}p^{v_p(B_n)-1}
 =\prod_{\substack{5\le p\le Y\\r_p\mid n}}p^{v_p(n)}\quad\bigm|\quad n.
\]

Indeed \(p\mid B_j\) exactly when \(r_p\mid j\), and in that case the formal logarithm gives \(v_p(B_j)=e_p+v_p(j/r_p)\) for good \(p\). Moreover \(p\nmid r_p\), since otherwise the full rational two-torsion would give \(4p\mid\#E_6(\mathbf F_p)\), contrary to Hasse's bound for \(p\ge5\). At \(j=2n\) only orders with 2-adic valuation zero or one can occur. The unique extra first-depth unit from prime 211 appears exactly when \(106\mid2n\), or \(53\mid n\), and it cannot appear at an odd index.

For bad primes, write the primitive quartic triple as \(a^4+3b^2=4w^4\). The orbit identity \(B_{2n}=2|abw|\) and oddness of \(a,b,w\) give \(v_2(B_{2n})=1\). The point \(2G=(25/4,-35/8)\) reduces to a nonidentity smooth point on the cuspidal cubic at 3, whose smooth group has order three. Thus \(3\mid B_{2n}\) exactly when \(3\mid n\). Here \(B_6=2\cdot23\cdot1551\cdot37\) has 3-adic valuation one. Applying the formal logarithm to multiples of \(6G\) gives \(v_3(B_{2n})=v_3(n)\) in all cases, accounting for the factor \(3^{v_3(n)}\) when the leading 3 in \(3B_{2n}\) is included. Neither bad prime divides the odd denominator \(B_n=w\).

## Computational certificate

The scanner enumerates all primes with a least-prime-factor sieve. For \(p\equiv3\bmod4\) it tests the annihilator \(M=p+1\). For \(p\equiv1\bmod4\), write \(p=a^2+b^2\) with \(a\) odd and try \(M=p+1\pm2a\). The program verifies \(MG=O\) separately at every prime. Given this check, its correctness does not depend on an unverified formula for the curve's Frobenius trace. Remove powers of 2 from \(M\) until its 2-adic valuation is at most one and test this new multiple of the odd part. If it still annihilates \(G\), factor it and repeatedly test division by each prime factor to obtain the exact order \(r_p\).

To test the depth, compute \([r_p]G\) in Jacobian coordinates modulo \(p^2\). In the double-and-add calculation, every positive intermediate scalar is less than \(r_p\) before the final operation. Its point is therefore finite modulo \(p\). At a mixed addition, a collision with the generator would require the preceding even scalar to be 1 modulo \(r_p\), which cannot happen for such a positive proper scalar. The scanner verifies the absence of a mixed-addition base point and verifies that the final \(X,Y\) are units while \(p\mid Z\). The local parameter \(-x/y=-XZ/Y\) then has depth at least two exactly when \(Z=0\bmod p^2\). Products for this lift use unsigned 128-bit intermediates. Field multiplications at \(p\) use unsigned 64-bit intermediates. [Source](abc_full_quartic_first_depth_scan.cpp) · [Complete output](abc_full_quartic_first_depth_scan_31904497.txt)

Compile with `g++ -O3 -std=c++17 abc_full_quartic_first_depth_scan.cpp -o first_depth_scan` and run `./first_depth_scan 31904497` with assertions enabled. An independent PARI check computes \([106]G\) exactly over the rationals, obtaining abscissa and ordinate valuations \((-4,-6)\) at 211. Separate \(211\)-adic multiplication gives depth two, and finite-field multiplication confirms the orders 106 for \(G\) and 53 for its translate \(G+(6,0)\). PARI also checks each prime through 10,000 and each prime in \([31{,}903{,}497,31{,}904{,}497]\) using its own order and local point routines. [PARI verifier](abc_full_quartic_first_depth_pari.py) · [Output](abc_full_quartic_first_depth_pari.txt)
