# Initial valuations at every dyadic index and every prime up to one trillion

For \(4\le n=2^k\) and rational primes \(p\le10^{12}\), there are exactly six pairs with \(p\mid w_n\). All six have \(v_p(w_n)=1\). The last column is the nonzero residue of \(w_n/p\) modulo \(p\). [Portable verifier](abc_dyadic_initial_depth_scan.py)

| \(n\) | Prime \(p\) | \(w_n/p\bmod p\) |
|---:|---:|---:|
| 4 | 7 | 1 |
| 8 | 2,273 | 1 |
| 64 | 242,636,033 | 64,047,156 |
| 128 | 67,649,537 | 7,276,566 |
| 512 | 339,767,297 | 181,919,147 |
| 8,192 | 65,229,783,041 | 16,173,440,797 |

For \(n\ge8\), the primes of \(w_n\) occur at exact scalar reduction order \(n\) of \(R=(-8,16)\) on \(y^2=x^3+16x^2+32x\). The local calculation at the nonzero two-torsion ordinate gives the same exponent in the square-root denominator of \(x(nR)\). The CM norm condition supplies an integer pair with \(p=(1+2na)^2+8n^2b^2\), and one may take \(b>0\). In particular \(p\ge8n^2+1\), so every dyadic \(n\ge524288\) is excluded at this prime bound. [Packet, CM and local calculations](abc_octic_dyadic_fermat_audit.md)

For the four indices through 32 the verifier checks the complete packet factorizations, with elementary Lucas primality certificates for the larger factors. At all thirteen remaining dyadic indices, from 64 through 262144, inclusive, it enumerates exactly 90,375,083 norm pairs using integer square roots. It removes a pair only if its represented integer has a prime divisor \(\ell<300\). Every represented integer on this part of the search exceeds 300. The root count is implemented by solving \((a+(2n)^{-1})^2=-2b^2\pmod\ell\), and both signs are retained when \(-2\) is a square. This leaves 15,840,691 pairs.

For \(n\le1024\) the verifier computes the integer \(w_n\) and takes gcds with products of candidate norms. Any prime norm dividing the packet divides its batch gcd. Larger indices use the homogeneous doubling recurrence directly modulo each candidate, so no gigantic exact packet or modular inverse is required. The procedure tests primality at every divisor it retains. Finally it evaluates the packet modulo \(p^2\) at every genuine prime hit, giving the table. The same support already occurs below \(10^{11}\); above \(10^{12}\) the first depths remain unclassified.
