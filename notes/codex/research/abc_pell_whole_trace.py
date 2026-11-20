"""Reconstruct the squarefree trace polynomial and certify the local targets.

The integer polynomial operations use python-flint. The rank checks for
individual irreducible factors use PARI's nffactor through cypari.
"""

from functools import cache
from flint import fmpz_poly, nmod_poly


def primitive(f):
    return f // f.content()


def build():
    x = fmpz_poly([0, 1])
    cubic = x**3 + 16*x**2 + 32*x
    third = 3*x**4 + 64*x**3 + 192*x**2 - 1024
    fourth = 2*x**6 + 64*x**5 + 320*x**4 - 10240*x**2 - 65536*x - 65536

    @cache
    def psi(n):
        # Remove the factor 2y at even n.
        if n <= 4:
            return (fmpz_poly([]), fmpz_poly([1]), fmpz_poly([1]), third, fourth)[n]
        m = n//2
        if n % 2 == 0:
            return psi(m)*(psi(m+2)*psi(m-1)**2 - psi(m-2)*psi(m+1)**2)
        first, second = psi(m+2)*psi(m)**3, psi(m-1)*psi(m+1)**3
        if m % 2 == 0:
            return (4*cubic)**2*first - second
        return first - (4*cubic)**2*second

    den = psi(11)**2
    num = x*den - 4*cubic*psi(10)*psi(12)
    raw = den*num*(num+16*den)*(num+8*den)*(num**2+16*num*den+32*den**2)
    finite_support = primitive(raw//raw.gcd(raw.derivative()))
    branch_pair = x*x+16*x+32
    rest, remainder = divmod(finite_support, branch_pair)
    assert not remainder
    assert (num.degree(), den.degree(), finite_support.degree(), rest.degree()) == (121, 120, 485, 483)
    assert rest.gcd(rest(-16-x)) == 1
    assert rest(-8) and rest.gcd(branch_pair) == 1

    # Multiply the two orientations before passing from x+8 to its square.
    even = rest(x-8)*rest(-x-8)
    assert all(even[i] == 0 for i in range(1, even.degree()+1, 2))
    pair = fmpz_poly([even[2*i] for i in range(484)])
    s2 = x*x
    # T = x * (x^2)^483 * pair(32*(1-x^(-2))).
    leading = 32*(s2-1)
    value, power = fmpz_poly([pair[483]]), s2
    for i in range(482, -1, -1):
        value = value*leading + pair[i]*power
        power *= s2
    trace = x*value
    assert trace.degree() == 967 and primitive(trace).gcd(primitive(trace).derivative()) == 1
    for s, t in ((17,12), (99,70)):
        assert s*s-2*t*t == 1
        def evaluate(u):
            out, v = 0, 1
            for c in reversed(rest.coeffs()):
                out = out*u + c*v
                v *= s
            return out
        assert trace(s) == s*evaluate(-8*(s+t))*evaluate(-8*(s-t))
    return rest, trace


def check_independence(rest):
    from cypari import pari

    modulus = 1009
    z = nmod_poly([0, 1], modulus)
    sqrt2 = next(t for t in range(modulus) if t*t % modulus == 2)
    first = (-8-4*sqrt2)*z+(-8+4*sqrt2)
    second = z+1
    pari("K=nfinit(y^2-2)")
    certificates = []
    for factor, exponent in rest.factor()[1]:
        assert exponent == 1
        if factor.degree() == 1:
            assert factor == fmpz_poly([0,1])
            continue
        coeffs = ",".join(str(int(c)) for c in factor.coeffs())
        pari("factors=nffactor(K,Polrev([" + coeffs + "],x))[,1]")
        for j in range(1, int(pari("#factors"))+1):
            v = pari("Vec(subst(liftall(factors[" + str(j) + "]),y," +
                     str(sqrt2) + ")*Mod(1," + str(modulus) + "))")
            c = [int(e.lift()) for e in v]
            h, power = nmod_poly([c[0]], modulus), second
            for coeff in c[1:]:
                h = h*first + coeff*power
                power *= second
            d = h.degree()
            assert d == len(c)-1 and h[0] and h[d]
            difference = (int(h[2])*int(h[0])*int(h[d-1])**2
                          - int(h[d-2])*int(h[d])*int(h[1])**2) % modulus
            assert difference
            certificates.append((d, difference))
    assert len(certificates) == 10
    return sorted(certificates)


if __name__ == "__main__":
    rest, trace = build()
    print("trace degree", trace.degree(), "nonlinear target certificates",
          check_independence(rest))
