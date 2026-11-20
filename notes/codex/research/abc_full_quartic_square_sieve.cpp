// Compile with g++ -std=c++17 -O3; an optional bound caps the cofactor census.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
#include <iomanip>
using std::vector;
using i64 = std::int64_t;

static int mod(i64 a, int p) {
    return int((a % p + p) % p);
}

static vector<int> primes(int limit) {
    vector<bool> ok(limit + 1, true);
    vector<int> result;
    for (int p = 2; p <= limit; ++p) {
        if (!ok[p]) continue;
        result.push_back(p);
        for (i64 j = i64(p) * p; j <= limit; j += p) ok[j] = false;
    }
    return result;
}

struct Local {
    int p;
    vector<signed char> chi, orbit;
    int period() const { return int(orbit.size()); }
};

static Local original_orbit(int p) {
    Local h{p, vector<signed char>(p, -1), {1}};
    h.chi[0] = 0;
    for (int x = 1; x < p; ++x) h.chi[x * x % p] = 1;
    vector<int> inv(p);
    inv[1] = 1;
    for (int x = 2; x < p; ++x) inv[x] = p - i64(p / x) * inv[p % x] % p;
    const int a = mod(-2, p), b = 8 % p;
    int x = a, y = b;
    while (true) {
        h.orbit.push_back(h.chi[mod(8 * (6 - x), p)]);
        if (x == a && mod(y + b, p) == 0) break;
        int slope = x == a
            ? mod(i64(3 * a * a + 72 * a + 36) * inv[2 * b % p], p)
            : mod(i64(y - b) * inv[mod(x - a, p)], p);
        int xnew = mod(i64(slope) * slope - 36 - x - a, p);
        y = mod(i64(slope) * (x - xnew) - y, p);
        x = xnew;
    }
    return h;
}

struct Natural {
    static constexpr int base = 1000000000;
    vector<int> digits{24};
    int residue(int r) const {
        i64 value = 0;
        for (auto it = digits.rbegin(); it != digits.rend(); ++it)
            value = (value * base + *it) % r;
        return int(value);
    }
    void multiply(int factor) {
        i64 carry = 0;
        for (int& digit : digits) {
            i64 value = i64(digit) * factor + carry;
            digit = value % base;
            carry = value / base;
        }
        if (carry) digits.push_back(int(carry));
    }
};
static std::ostream& operator<<(std::ostream& out, const Natural& number) {
    auto it = number.digits.rbegin();
    out << *it++;
    for (; it != number.digits.rend(); ++it)
        out << std::setw(9) << std::setfill('0') << *it;
    return out;
}

static Natural square_modulus(const vector<Local>& rows) {
    Natural modulus;
    for (int a = 1; a < 24; a += 2) {
        bool passes = true;
        for (const auto& h : rows) if (24 % h.period() == 0)
            passes &= h.orbit[a % h.period()] >= 0;
        assert(passes == (a == 1 || a == 23));
    }
    auto prime_list = primes(10000);
    for (;;) {
        std::map<int, vector<const Local*>> tests;
        for (const auto& h : rows) {
            const int r = h.period();
            const int factor = r / std::gcd(r, modulus.residue(r));
            if (std::binary_search(prime_list.begin(), prime_list.end(), factor))
                tests[factor].push_back(&h);
        }
        vector<int> gains;
        for (const auto& [ell, group] : tests) {
            bool extends = true;
            for (int k = 1; k < ell && extends; ++k) {
                bool excluded = false;
                for (const Local* h : group) {
                    int r = h->period(), m = modulus.residue(r);
                    if (h->orbit[(1 + k * m) % r] < 0) { excluded = true; break; }
                }
                extends &= excluded;
            }
            if (extends) gains.push_back(ell);
        }
        if (gains.empty()) return modulus;
        for (int ell : gains) modulus.multiply(ell);
    }
}

class CofactorTests {
    vector<const Local*> seed, rest;
    vector<vector<int>> indices;
public:
    i64 count = 0;
    std::map<i64, vector<int>> passed;
    CofactorTests(const vector<Local>& rows, int period) : indices(4096) {
        for (const auto& h : rows) if (period % h.period() == 0) {
            if (h.p % 12 != 1 && seed.size() < 12) seed.push_back(&h);
            else rest.push_back(&h);
        }
        assert(seed.size() == 12);
        for (int a = 1; a < period / 2; a += 2) {
            int pattern = 0;
            for (auto* h : seed) {
                auto c = h->orbit[a % h->period()];
                assert(c != 0);
                pattern = 2 * pattern + (c == 1);
            }
            indices[pattern].push_back(a);
        }
    }
    void test(i64 d) {
        ++count;
        int pattern = 0;
        for (auto* h : seed) {
            int c = h->chi[d % h->p];
            assert(c != 0);
            pattern = 2 * pattern + (c == 1);
        }
        for (int a : indices[pattern]) {
            bool pass = true;
            for (auto* h : rest) {
                int c = h->orbit[a % h->period()];
                if (c && c != h->chi[d % h->p]) { pass = false; break; }
            }
            if (pass) passed[d].push_back(a);
        }
    }
};

template<class Visit> static void products(const vector<int>& ps, int i, i64 d,
                                          i64 bound, const Visit& visit) {
    visit(d);
    for (; i < int(ps.size()) && ps[i] <= bound / d; ++i)
        products(ps, i + 1, d * ps[i], bound, visit);
}

static void census(i64 bound, CofactorTests& tests) {
    int root = int(std::sqrt(double(bound)));
    while (i64(root + 1) * (root + 1) <= bound) ++root;
    while (i64(root) * root > bound) --root;
    auto all_small = primes(root);
    vector<int> allowed;
    for (int p : all_small) if (p % 12 == 1) allowed.push_back(p);
    products(allowed, 0, 1, bound, [&](i64 d) { tests.test(d); });
    vector<i64> cofactors;
    products(allowed, 0, 1, root, [&](i64 d) { cofactors.push_back(d); });
    std::sort(cofactors.begin(), cofactors.end());
    const int block = 1 << 19;
    for (i64 lo = root + 1; lo <= bound; lo += block) {
        i64 hi = std::min(bound + 1, lo + block);
        vector<char> is_prime(hi - lo, true);
        for (int p : all_small) {
            if (i64(p) * p >= hi) break;
            i64 start = std::max(i64(p) * p, (lo + p - 1) / p * p);
            for (i64 z = start; z < hi; z += p) is_prime[z - lo] = false;
        }
        for (i64 p = lo + mod(1 - lo, 12); p < hi; p += 12) if (is_prime[p - lo]) {
            for (i64 d : cofactors) {
                if (p * d > bound) break;
                tests.test(d * p);
            }
        }
    }
}

int main(int argc, char** argv) {
    const i64 bound = argc > 1 ? std::stoll(argv[1]) : 2005752169LL;
    assert(bound >= 1 && bound <= 2005752169LL);
    vector<Local> rows;
    for (int p : primes(10000)) if (p >= 5) rows.push_back(original_orbit(p));
    std::cout << "Square index modulus " << square_modulus(rows) << '\n';
    CofactorTests tests(rows, 2520);
    census(bound, tests);
    std::cout << "Squarefree candidates through " << bound << ": " << tests.count << '\n';
    for (const auto& [d, aa] : tests.passed) {
        std::cout << d;
        for (int a : aa) std::cout << " +/-" << a;
        std::cout << " modulo 2520\n";
    }
    for (auto [d, period] : {std::pair<i64,int>{40573,12600}, {2005752169,17640}}) {
        CofactorTests extra(rows, period);
        extra.test(d);
        std::cout << d;
        for (int a : extra.passed[d]) std::cout << " +/-" << a;
        std::cout << " modulo " << period << '\n';
    }
}
