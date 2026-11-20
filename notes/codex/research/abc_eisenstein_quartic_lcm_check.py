"""Check the lcm and radical-gain certificates through index 209. Uses python-flint."""

from flint import fmpz
from abc_eisenstein_slice_paired_verify import quartics


def check_index_fifteen(f_plus, f_minus):
    odd_primes = (
        (263, 10391, 43346903, 1446943978951150703297493532273,
         1732566019222314022863922381851624254433623),
        (167, 139969, 23083224719, 30126145559, 99260990613819842617,
         300692875219581864963039873385042291751),
    )
    for value, two_exponent, primes in zip((f_plus, f_minus), (5, 4), odd_primes):
        product = fmpz(2) ** two_exponent
        for p in primes:
            assert fmpz(p).is_prime()
            product *= p
        assert product == abs(value)
    assert f_plus.gcd(f_minus) == 16


def check():
    common_multiple = fmpz(1)
    product_over_lcm = fmpz(1)
    for index in range(3, 210, 2):
        x, y, f_plus, f_minus = quartics(index)
        x, y = fmpz(x), fmpz(y)
        pair = abs(f_plus * f_minus)
        j = pair // 512
        assert pair == 512 * j and j.gcd(6) == 1
        shared = common_multiple.gcd(j)
        product_over_lcm *= shared
        common_multiple = (common_multiple // shared) * j
        if index == 15:
            check_index_fifteen(f_plus, f_minus)
        if index == 209:
            assert shared == 191 and j % 191**2 == 0 and j % 191**3 != 0
            norm = x*x + 3*y*y
            height = (norm // 4) ** 12
            assert 10**101143 < height < 10**101144
            z_squared = -(f_plus + f_minus) // 4
            z = z_squared.sqrt()
            assert z*z == z_squared
            imaginary_factor = (
                x*y * (x*x-y*y) * (x*x-9*y*y) * (x*x-3*y*y)
                * (x*x-6*x*y-3*y*y) * (x*x+6*x*y-3*y*y)
            )
            support = abs(z * f_plus * f_minus * imaginary_factor * norm)
            for p, e in ((2, 27), (191, 2)):
                assert support % p**e == 0 and support % p**(e+1) != 0
            numerator = height * 2**26 * 191
            assert 50846 * support < numerator < 50847 * support
    assert common_multiple.bit_length() == 3956311
    assert product_over_lcm.bit_length() == 874
    print("Verified the exact lcm and radical-gain certificates through odd index 209.")


if __name__ == "__main__":
    check()
