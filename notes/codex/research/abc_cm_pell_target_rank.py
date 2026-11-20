"""Interval Fourier certificate for the fifty full rank-eleven targets."""

from flint import acb, arb, ctx
from sympy import Poly, QQ, sqrt, symbols

from abc_cm_twist_depth_example import degree_eleven_factors


def verify_norm():
    """Evaluate the primitive torsion factor at both two-torsion abscissas."""
    x = symbols("x")
    _, coefficients = degree_eleven_factors()
    polynomial = Poly.from_list(coefficients, gens=x, domain=QQ)
    field = QQ.algebraic_field(sqrt(2))
    root = field.from_sympy(sqrt(2))
    def evaluate(value):
        result = field.zero
        for coefficient in polynomial.all_coeffs():
            result = result * value + field.from_sympy(coefficient)
        return result
    norm = evaluate(-8+4*root) / evaluate(-8-4*root)
    assert norm == (1+root)**(-48)
    print("Product of 50 targets equals (1+sqrt(2))^-48.")


def verify_log_rank():
    ctx.prec = 192
    root = arb(2).sqrt()
    rho = acb(0, 1/root)
    period_squared = acb(arb(1)/2).elliptic_p(rho).real * 3/16
    theta_minus, theta_plus = -8-4*root, -8+4*root
    logs = {}
    for j in range(10):
        for k in range(5):
            left, right = pow(2,j,11), pow(2,k,11)
            a = (left + right) * 6 % 11
            b = (left - right) * 2 % 11
            parameter = (a + (2*b % 11)*rho) / 11
            abscissa = parameter.elliptic_p(rho)/period_squared - arb(16)/3
            target = (theta_plus-abscissa)/(abscissa-theta_minus)
            logs[j,k] = abs(target).log()
    unit = acb(0, 2*arb.pi()/10).exp()
    powers = [unit**i for i in range(10)]
    components = []
    for r in range(10):
        for s in range(10):
            if (r+s) % 2:
                continue
            value = sum(h * powers[(r*j+s*k) % 10] for (j,k),h in logs.items())
            modulus = abs(value)
            assert modulus > 2
            components.append(modulus)
    assert len(components) == 50
    assert any(value < arb("2.013") for value in components)
    print("All 50 Fourier moduli exceed 2; the minimum lies in (2, 2.013).")


if __name__ == "__main__":
    verify_norm()
    verify_log_rank()
