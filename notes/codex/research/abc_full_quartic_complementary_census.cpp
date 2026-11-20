// Exhaustive squarefree-part census for the product a*c. Compile with C++17.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
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

static int power(i64 a, int n, int p) {
    int result = 1;
    a = mod(a,p);
    for (; n; n >>= 1, a = a*a%p)
        if (n & 1) result = int(result*a%p);
    return result;
}

struct Point { int x,y; };
static constexpr Point identity{-1,0};
static Point plus(Point a, Point b,int p) {
    if (a.x<0) return b;
    if (b.x<0) return a;
    if (a.x==b.x && (a.y+b.y)%p==0) return identity;
    i64 num = a.x==b.x ? 3LL*a.x*a.x-36 : a.y-b.y;
    int den = a.x==b.x ? 2*a.y : a.x-b.x;
    int slope = int(i64(mod(num,p))*power(den,p-2,p)%p);
    int x=mod(i64(slope)*slope-a.x-b.x,p);
    return {x,mod(i64(slope)*(a.x-x)-a.y,p)};
}
static Point multiple(int k,Point g,int p) {
    Point q=identity;
    while(k) {
        if (k&1) q=plus(q,g,p);
        k/=2;
        if(k) g=plus(g,g,p);
    }
    return q;
}

static vector<Local> character_tables(int period) {
    vector<Local> rows;
    for (int p:primes(200000)) {
        if (p%4!=1) continue;
        Point g{p-3,9%p};
        if(multiple(period,g,p).x>=0) continue;
        Local h{p,vector<signed char>(p,-1),{}};
        h.chi[0]=0;
        for (int i=1;i<p;++i) h.chi[i64(i)*i%p]=1;
        int inv9=power(9,p-2,p);
        Point q=identity;
        do {
            int value;
            if (q.x<0) value=(p-1)%8==0 ? 1 : -1;
            else {
                int square=mod(-i64(q.x)*(q.x+6)%p*inv9,p);
                int fourth=power(square,(p-1)/4,p);
                value=fourth==0 ? 0 : fourth==1 ? 1 : -1;
            }
            h.orbit.push_back(static_cast<signed char>(value));
            q=plus(q,g,p);
        } while(q.x>=0);
        rows.push_back(std::move(h));
    }
    return rows;
}

class CofactorTests {
    vector<const Local*> seed, rest;
    vector<vector<int>> indices;
public:
    i64 count = 0;
    std::map<i64, vector<int>> passed;
    CofactorTests(const vector<Local>& rows, int period) : indices(4096) {
        for (const auto& h : rows) if (period % h.period() == 0) {
            if (h.p % 24 != 1 && h.p % 24 != 23 && seed.size() < 12) seed.push_back(&h);
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
    for (int p : all_small) if (p % 24 == 1 || p % 24 == 23) allowed.push_back(p);
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
        for (int r : {1,23}) for (i64 p = lo + mod(r-lo,24); p < hi; p += 24) if (is_prime[p-lo]) {
            for (i64 d : cofactors) {
                if (p * d > bound) break;
                tests.test(d * p);
            }
        }
    }
}


int main() {
    constexpr i64 bound=5000000000LL;
    vector<Local> rows=character_tables(2520);
    assert(rows.size()==85);
    CofactorTests tests(rows,2520);
    census(bound,tests);
    const std::map<i64,vector<int>> expected{{1,{1}},{1081,{3}},{1216806121,{5}}};
    assert(tests.count==85279401 && tests.passed==expected);
    std::cout<<rows.size()<<" local primes, "<<tests.count<<" squarefree candidates\n";
    for (const auto& [f,indices]:tests.passed) {
        std::cout<<f;
        for(int n:indices) std::cout<<" +/-"<<n;
        std::cout<<" modulo 2520\n";
    }
}
