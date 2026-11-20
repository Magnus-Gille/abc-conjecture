# What congruences on signed Frobenius can detect in the full CM factor

Let \(R=(-8,16)\) on \(E:y^2=x^3+16x^2+32x\). For a large prime \(q\) split in \(K=\mathbf Q(\sqrt{-2})\), let \(C_q\) be the product, with full exponents, of the rational primes at which \(R\) has exact CM annihilator \((q)\). It is a factor of the scalar denominator \(B_q\), and \(\log C_q=hq^2+O(q)\) for fixed \(h>0\). For each \(p\mid C_q\), choose a place above it and let \(\pi_p\) be the signed Frobenius generator. In \(\mathcal O=\mathbf Z[\sqrt{-2}]\), it has norm \(p\) and satisfies \(\pi_p\equiv1\bmod q\mathcal O\). Write \(\Gamma=\prod_{p\mid C_q}\pi_p^{v_p(C_q)}\), so \(N\Gamma=C_q\). The assertion below works for any choices of places. [Full-factor height and annihilator](abc_odd_rank_primitive_cm_norm.md) · [Sign of Frobenius](abc_odd_rank_signed_frobenius.md)

**Fix \(A,D>0\) and \(0<\delta<2\).** For all sufficiently large such \(q\), every positive integer \(H\le q^D\) coprime to \(C_q\), and every integer \(2\le k\le q^{2-\delta}\), there are distinct rational primes \(p,r\) and signed Frobenius generators \(\beta,\gamma\) above them with

\[
 \begin{gathered}
 pr\text{ coprime to }B_q,\qquad \beta\equiv\gamma\equiv1\pmod{q\mathcal O},\\
 Z=\beta^k\gamma^{k+1}\equiv\Gamma\pmod{8qH\mathcal O},\qquad
 \left|Z/\Gamma-1\right|<q^{-A}.
 \end{gathered}
\]

In particular the integer \(N Z=p^k r^{k+1}\) is congruent to \(C_q\bmod 8qH\) and differs from it in relative value by \(O(q^{-A})\). Its factorization contains two consecutive positive exponents, hence it is no nontrivial perfect power. Taking \(k\to\infty\) makes \(\log\operatorname{rad}(NZ)/\log(NZ)\to0\). This example preserves a modulus of total polynomial size in \(q\). The full \(q\)-torsion is rational over the two residue fields because Frobenius acts trivially on it. The point \(R\) itself does not reduce to a \(q\)-torsion point there, since \(p,r\nmid B_q\). That last requirement is additional arithmetic information in the actual denominator.

## A construction with prime elements

Take one complex embedding of \(K\), and put \(X=C_q^{1/(4k+2)}\), so that \(X^{2k+1}=|\Gamma|\) and \(\log X\gg q^\delta\). Let \(\theta\) be an argument of \(\Gamma\). Pick prime elements near \(X\) and \(Xe^{i\theta/(k+1)}\) in the respective invertible residue classes \(\Gamma^{-1},\Gamma\) modulo \(8qH\mathcal O\). Use disks of radius \(Xq^{-A-4}/100\).

Mitsui's prime number theorem in a fixed number field counts prime elements in convex subsets of a disk of size \(O(X)\) and in specified invertible ray classes. In the Siegel–Walfisz range, a modulus of norm \(\le (\log X)^m\) and disks of relative radius \(\ge (\log X)^{-m}\), for any fixed \(m\), give \(\gg X^2/(\log X)^{O_m(1)}\) prime elements in either disk for large \(X\). This follows from the area main term, divided by a ray-group factor at most the norm of the modulus and by a logarithm when unweighting. The error is smaller than any fixed inverse power of \(\log X\) times \(X^2\). Both size hypotheses hold uniformly here with \(m\) depending on \(A,D,\delta\). Inert rational primes and their associates account for \(O(X)\) elements. Prime elements of degree one over any prime dividing \(B_q\) account for at most \(4\omega(B_q)=O(q^2)\) elements. We may exclude these along with the prime already selected in the other disk and its conjugate. [Kai, *Notes on Mitsui's Prime Number Theorem with Siegel zeros*](https://arxiv.org/abs/2209.11816)

The finite sign in the CM character has conductor \((\sqrt{-2})^5\), dividing \(8\mathcal O\), and sign \(+1\) on every chosen \(\pi_p\). Thus the prime elements selected in the two classes have the correct Frobenius signs. Their classes modulo \(q\mathcal O\) are both 1. Their product with exponents \(k,k+1\) has residue \(\Gamma^{-k}\Gamma^{k+1}=\Gamma\) at the full modulus. Each element differs from its target by a multiplicative complex error of modulus at most \(q^{-A-4}/100\). The inequality \((1+s)^{2k+1}-1\le e^{(2k+1)s}-1\) bounds the resulting relative complex error by \(q^{-A}\). Finally \(\log N\beta,\log N\gamma=2\log X+O(q^{-A-4})\), which gives the assertion about the radical.
