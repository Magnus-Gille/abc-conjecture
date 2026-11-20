// Build with c++ -O3 -std=c++17 abc_cyclotomic_ninth_prime_roots.cpp -o ninth-roots.
// With no arguments the inclusive prime range is [1, 2^32-1]. Accepts high or low high.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>

using Integer = std::uint64_t;
constexpr Integer max_prime = 4294967295ULL;
constexpr Integer height_factor = 16;  // Search A^2 < 16p, including A^2 < p.

Integer integer_sqrt(Integer value) {
    Integer root = static_cast<Integer>(std::sqrt(static_cast<long double>(value)));
    while ((root + 1) * (root + 1) <= value) ++root;
    while (root * root > value) --root;
    return root;
}

Integer power_mod_prime(Integer base, Integer exponent, Integer p) {
    Integer result = 1;
    while (exponent) {
        if (exponent & 1) result = result * base % p;
        base = base * base % p;
        exponent >>= 1;
    }
    return result;
}

Integer multiply_mod_square(Integer x, Integer y, Integer p) {
#if defined(__SIZEOF_INT128__)
    return static_cast<__uint128_t>(x) * y % (p * p);
#else
    // For a compiler without a double-width integer, multiply two base-p digits.
    const Integer x0 = x % p, y0 = y % p, low = x0 * y0;
    const Integer high = (low / p + (x / p) * y0 % p + (y / p) * x0 % p) % p;
    return high * p + low % p;
#endif
}

Integer add_mod(Integer x, Integer y, Integer modulus) {
    return x >= modulus - y ? x - (modulus - y) : x + y;
}

struct Counts {
    Integer primes = 0, positive = 0, negative = 0, positive_strict = 0, negative_strict = 0;
};

bool square_divides(Integer a, Integer b, Integer p, bool positive) {
    const Integer modulus = p * p;
    const Integer x = multiply_mod_square(multiply_mod_square(a, a, p), a, p);
    const Integer y = multiply_mod_square(multiply_mod_square(b, b, p), b, p);
    const Integer cross = multiply_mod_square(x, y, p);
    const Integer ends = add_mod(multiply_mod_square(x, x, p), multiply_mod_square(y, y, p), modulus);
    return positive ? add_mod(ends, cross, modulus) == 0 : ends == cross;
}

void record(Integer a, Integer b, Integer p, bool positive, Counts& counts) {
    assert(a > b && b > 0 && a * a < height_factor * p && std::gcd(a, b) == 1);
    assert(square_divides(a, b, p, positive));
    const bool strict = a * a < p;
    if (positive) {
        ++counts.positive;
        counts.positive_strict += strict;
    } else {
        ++counts.negative;
        counts.negative_strict += strict;
    }
    std::cout << (positive ? 9 : 18) << ',' << a << ',' << b << ',' << p << ',' << strict << '\n';
}

void reconstruct(Integer root, Integer p, Integer height, Counts& counts) {
    // r = sign*t*root (mod p^2). Remainders decrease and denominators increase.
    const Integer modulus = p * p;
    Integer old_r = modulus, r = root, old_t = 0, t = 1;
    bool positive = true;
    while (r > height && t <= height) {
        const Integer quotient = old_r / r;
        const Integer next_r = old_r - quotient * r, next_t = old_t + quotient * t;
        old_r = r; r = next_r; old_t = t; t = next_t;
        positive = !positive;
    }
    if (r > height || t > height) return;
    assert(r && t && multiply_mod_square(root, t, p) == (positive ? r : modulus - r));
    record(std::max(r, t), std::min(r, t), p, positive, counts);
}

void test_prime(Integer p, Counts& counts) {
    ++counts.primes;
    const Integer height = integer_sqrt(height_factor * p - 1);
    // At p=19 the wider box falls outside the uniform reconstruction bound.
    if (p <= 2 * height_factor) {
        for (Integer a = 2; a <= height; ++a) {
            for (Integer b = 1; b < a; ++b) {
                if (std::gcd(a, b) != 1) continue;
                for (bool positive : {true, false}) {
                    if (square_divides(a, b, p, positive)) record(a, b, p, positive, counts);
                }
            }
        }
        return;
    }
    Integer y = 1;
    for (Integer base = 2; y * y % p * y % p == 1; ++base) {
        y = power_mod_prime(base, (p - 1) / 9, p);
    }
    const Integer y2 = multiply_mod_square(y, y, p);
    const Integer y4 = multiply_mod_square(y2, y2, p);
    const Integer y8 = multiply_mod_square(y4, y4, p);
    const Integer y9 = multiply_mod_square(y8, y, p);
    assert(y9 % p == 1);
    // Lift u=y+tp with t= -((y^9-1)/p)*y/9 mod p. Here p=1 mod 9.
    const Integer error = (y9 - 1) / p, inverse_nine = (8 * p + 1) / 9;
    const Integer digit = ((p - error) * y % p) * inverse_nine % p;
    const Integer u = y + digit * p;
    const Integer u2 = multiply_mod_square(u, u, p), u4 = multiply_mod_square(u2, u2, p);
    assert(multiply_mod_square(multiply_mod_square(u4, u4, p), u, p) == 1);
    // Exponents 1,2,4 represent all six primitive roots up to inversion.
    for (Integer root : {u, u2, u4}) reconstruct(root, p, height, counts);
}

int main(int argc, char** argv) {
    Integer low = 1, high = max_prime;
    if (argc == 2) high = std::stoull(argv[1]);
    else if (argc == 3) { low = std::stoull(argv[1]); high = std::stoull(argv[2]); }
    else if (argc != 1) throw std::invalid_argument("usage: ninth-roots [low] [high]");
    if (!low || low > high || high > max_prime) throw std::invalid_argument("require 1 <= low <= high <= 2^32-1");

    // Sieve just the candidates p=18k+1. A prime d>=5 removes one class of k mod d.
    const Integer first = std::max<Integer>(1, (low + 16) / 18), last = (high - 1) / 18;
    const Integer limit = integer_sqrt(high);
    std::vector<bool> composite(limit + 1);
    struct Progression { Integer prime, next; };
    std::vector<Progression> sieve;
    for (Integer d = 2; d <= limit; ++d) {
        if (composite[d]) continue;
        for (Integer m = d*d; m <= limit; m += d) composite[m] = true;
        if (d <= 3) continue;
        Integer inverse = 1;
        while (d * inverse % 18 != 1) ++inverse;
        Integer k = (d * inverse - 1) / 18;
        const Integer start = std::max(first, (d*d + 16) / 18);
        if (k < start) k += ((start - k + d - 1) / d) * d;
        sieve.push_back({d, k});
    }
    Counts counts;
    std::cout << "n,A,B,p,p>A^2\n";
    for (Integer begin = first; begin <= last; ) {
        const Integer end = std::min(last + 1, begin + 262144);
        std::vector<unsigned char> marked(end - begin);
        for (auto& progression : sieve) {
            Integer k = progression.next;
            for (; k < end; k += progression.prime) marked[k - begin] = 1;
            progression.next = k;
        }
        for (Integer k = begin; k < end; ++k) {
            if (!marked[k - begin]) test_prime(18*k + 1, counts);
        }
        begin = end;
    }
    std::cout << "range=" << low << ".." << high << " primes=" << counts.primes
              << " wide(phi9,phi18)=" << counts.positive << ',' << counts.negative
              << " strict(phi9,phi18)=" << counts.positive_strict << ',' << counts.negative_strict << '\n';
}
