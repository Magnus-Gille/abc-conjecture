# Large gaps before the first possible prime of a given reduction order

On \(E:y^2=x^3-36x\) take \(G=(-3,9)\). There are infinitely many **prime** indices \(r\equiv7\bmod12\) such that every good prime \(p\) of exact reduction order \(r\) satisfies
\[
                        p\gg r^2\log r .
\]
Such primes \(p\) exist for all sufficiently large odd \(r\) by the [Gaussian denominator argument](abc_congruent_six_gaussian_first_primes.md). The lower bound here applies even to the smallest one.

For prime \(r\equiv3\bmod4\), the ideal \((r)\) stays prime in \(\mathbf Z[i]\). Hence it is the only Gaussian annihilator whose contraction to \(\mathbf Z\) is \((r)\). A prime \(p\) of that order splits in \(\mathbf Q(i)\), and its Frobenius has the form \(\pi=1+rz\) for \(z\in\mathbf Z[i]\setminus\{0\}\); in particular \(p=N(1+rz)\).

Fix an integer \(K\ge4\) and put \(M=4\prod_{5\le q\le16K,\;q\ {\rm prime}}q\). Choose a prime \(r\equiv3\bmod M\), \(r\equiv1\bmod3\). These conditions give a reduced class modulo \(3M\). The positive integer 3 is excluded by the second congruence, so the least prime in the class satisfies \(r\ge M+3\). Linnik's theorem gives \(r\ll (3M)^A\) for an absolute constant \(A\). The prime number theorem yields \(\log M\asymp K\), and consequently \(\log r\asymp K\).

For \(z\ne0\), \(Nz\le K\), the integer \(N(1+3z)\) is greater than 1, is \(1\bmod3\), and is at most \((1+3\sqrt K)^2\le16K\). Choose any prime \(q\) dividing it; then \(q\mid M\), including when \(q=2\). Since \(r\equiv3\bmod q\), the same \(q\) divides \(N(1+rz)\). The latter norm is at least \((r-1)^2>16K\) for large \(K\), so it is composite. Thus every possible Frobenius yielding a prime of exact order \(r\) has \(Nz>K\), giving \(p>(r\sqrt K-1)^2\gg r^2\log r\). Letting \(K\) grow proves the assertion.

The constructed gaps concern prime bases. Even with this extra factor of \(\log r\), a first occurrence can have substantial excess valuation; the construction gives no estimate for the sum of those excesses. [Quartic threshold and the remaining abc criterion](abc_congruent_six_large_primitive_primes.md)
