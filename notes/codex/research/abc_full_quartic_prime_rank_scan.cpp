// By default emit all primes p = 1 (mod 12) at which (-3,9) has odd prime order.
// With --power-exponents emit pairs (odd prime q, prime p = +/-1 mod 24) with qG=(0,0).
// The two candidate annihilators from the sum-of-two-squares representation are checked
// by multiplication for every p. Completeness only uses a checked annihilator.
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using Word = std::uint64_t;
struct Point { Word x, y, z; };

Word sub(Word a, Word b, Word p) { return a >= b ? a - b : p - (b - a); }
Word mul(Word a, Word b, Word p) { return a * b % p; }

Point twice(Point v, Word p) {
    if (!v.z || !v.y) return {1, 1, 0};
    Word xx = mul(v.x, v.x, p), yy = mul(v.y, v.y, p), zz = mul(v.z, v.z, p);
    Word m = sub(3 * xx % p, 36 * mul(zz, zz, p) % p, p);
    Word s = 4 * mul(v.x, yy, p) % p;
    Word x = sub(mul(m, m, p), 2 * s % p, p);
    Word y = sub(mul(m, sub(s, x, p), p), 8 * mul(yy, yy, p) % p, p);
    return {x, y, 2 * mul(v.y, v.z, p) % p};
}

Point plus_generator(Point v, Word p) {
    if (!v.z) return {p-3, 9, 1};
    Word zz = mul(v.z, v.z, p);
    Word h = sub(mul(p-3, zz, p), v.x, p);
    Word t = sub(9 * mul(v.z, zz, p) % p, v.y, p);
    if (!h) return t ? Point{1, 1, 0} : twice(v, p);
    Word hh = mul(h, h, p), hhh = mul(h, hh, p), s = mul(v.x, hh, p);
    Word x = sub(sub(mul(t, t, p), hhh, p), 2 * s % p, p);
    Word y = sub(mul(t, sub(s, x, p), p), mul(v.y, hhh, p), p);
    return {x, y, mul(v.z, h, p)};
}

Point point_multiple(unsigned index, Word p) {
    Point v{p-3, 9, 1};
    for (int bit = 30 - __builtin_clz(index); bit >= 0; --bit) {
        v = twice(v, p);
        if (index & (1u << bit)) v = plus_generator(v, p);
    }
    return v;
}

int main(int argc, char **argv) {
    bool power_exponents = argc == 3 && std::string(argv[2]) == "--power-exponents";
    if (argc != 2 && !power_exponents) return 1;
    int bound = std::stoi(argv[1]);
    if (bound < 13 || bound > 81000000) return 1;
    // Both candidate group orders are at most p+1+2*sqrt(p).
    int limit = bound + 19000;
    std::vector<int> least(limit + 1);
    for (int i = 2; i <= limit; ++i) {
        if (least[i]) continue;
        least[i] = i;
        if (i <= limit/i) {
            for (int j = i*i; j <= limit; j += i) if (!least[j]) least[j] = i;
        }
    }
    std::vector<short> odd_component(bound + 1);
    for (int a = 1; a*a <= bound; a += 2) {
        for (int b = 2; a*a + b*b <= bound; b += 2) {
            odd_component[a*a + b*b] = (a+b) % 4 == 1 ? a : -a;
        }
    }
    int covered = 0, hits = 0;
    for (int p = 13; p <= bound; p += 2) {
        if (power_exponents ? (p % 24 != 1 && p % 24 != 23) : p % 12 != 1) continue;
        if (least[p] != p) continue;
        ++covered;
        int a = 0;
        if (p % 4 == 1) {
            a = odd_component[p];
            if (!a) throw std::runtime_error("missing sum of squares");
            if (p % 8 == 5) a = -a;
        }
        int multiple = p+1-2*a;
        if (point_multiple(multiple, p).z) {
            multiple = p+1+2*a;
            if (point_multiple(multiple, p).z) throw std::runtime_error("missing annihilator");
        }
        while (multiple % 2 == 0) multiple /= 2;
        while (multiple > 1) {
            int q = least[multiple];
            Point point = point_multiple(q, p);
            bool matches = power_exponents ? (point.z != 0 && point.x == 0) : point.z == 0;
            if (matches) {
                std::cout << q << ' ' << p << '\n';
                ++hits;
                break;
            }
            do { multiple /= q; } while (multiple % q == 0);
        }
    }
    std::cerr << covered << " primes tested, " << hits
              << (power_exponents ? " reductions to (0,0)\n" : " prime-order reductions\n");
}
