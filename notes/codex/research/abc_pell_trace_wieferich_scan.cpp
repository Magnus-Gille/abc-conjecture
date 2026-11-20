#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

// Coefficient of sqrt(2) in (1+sqrt(2))^n, modulo an odd prime squared.
u64 pell_coefficient(u64 n, u64 modulus) {
    u64 a = 0, b = 1;
    bool odd = false;
    for (int bit = 63 - __builtin_clzll(n); bit >= 0; --bit) {
        // b_(2i) = 2 b_i^2 - (-1)^i and a_(2i) = 2 a_i b_i.
        u64 a2 = (u128(2) * a * b) % modulus;
        u64 b2 = (u128(2) * b * b + (odd ? 1 : modulus - 1)) % modulus;
        odd = (n >> bit) & 1;
        if (odd) {
            a = (a2 + b2) % modulus;
            b = (b2 + 2 * a2) % modulus;
        } else {
            a = a2;
            b = b2;
        }
    }
    return a;
}

int main(int argc, char** argv) {
    const int limit = argc > 1 ? std::atoi(argv[1]) : 100000000;
    if (limit < 3 || limit > 1000000000) return 2;
    std::vector<bool> composite(limit + 1);
    for (int q = 2; q <= limit / q; ++q) {
        if (!composite[q]) {
            for (int n = q * q; n <= limit; n += q) composite[n] = true;
        }
    }
    u64 eligible = 0, hits = 0;
    for (int p = 3; p <= limit; p += 2) {
        if (composite[p]) continue;
        bool candidate = p % 8 == 1 || p % 8 == 3;
        // Also run the three known hits outside the eligible classes as controls.
        if (!candidate && p != 13 && p != 31 && p != 1546463) continue;
        if (candidate) ++eligible;
        int symbol = p % 8 == 1 || p % 8 == 7 ? 1 : -1;
        u64 modulus = u64(p) * p;
        u64 value = pell_coefficient(p - symbol, modulus);
        if (value % p != 0) return 1;
        if (!value) {
            std::cout << (candidate ? "candidate " : "control ") << p << '\n';
            if (candidate) ++hits;
        } else if (!candidate) {
            return 1;
        }
    }
    std::cout << "limit " << limit << ", eligible primes " << eligible
              << ", eligible hits " << hits << '\n';
}
