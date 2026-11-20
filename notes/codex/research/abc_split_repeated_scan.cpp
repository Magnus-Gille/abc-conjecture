// g++ -O3 -std=c++17 abc_split_repeated_scan.cpp -lgmpxx -lgmp -o /tmp/split_scan
// Usage: split_scan BOUND > candidates.tsv, BOUND up to 10^12.
// The companion Python program verifies every retained row, including its CM packet.
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <gmpxx.h>

using U = uint64_t;
using I = int64_t;

U root(U n) {
    U r = std::sqrt((long double)n);
    while ((r+1)*(r+1) <= n) ++r;
    while (r*r > n) --r;
    return r;
}

bool prime(U n) {
    if (n < 2 || n%2 == 0) return n == 2;
    for (U d=3; d*d<=n; d+=2) if (n%d == 0) return false;
    return true;
}

const mpz_class& term(int n) {
    static std::map<int,mpz_class> values = {{0,0},{1,1},{2,1},{3,-9},{4,-14}};
    if (values.count(n)) return values.at(n);
    int k = n/2;
    auto& m = term(k); auto& l = term(k-1); auto& h = term(k+1);
    if (n%2) {
        mpz_class a = term(k+2)*m*m*m, b = l*h*h*h;
        if (k%2) b *= 32; else a *= 32;
        values[n] = a-b;
    } else values[n] = m*(term(k+2)*l*l-term(k-2)*h*h);
    return values.at(n);
}

struct Kummer {
    U p;
    U add(U a,U b) const {U x=a+b; return x<p?x:x-p;}
    U sub(U a,U b) const {return a>=b?a-b:p-(b-a);}
    U mul(U a,U b) const {return (__uint128_t)a*b%p;}
    U sq(U a) const {return mul(a,a);}
    struct Point {U x,z;};
    // Coordinates on y²=x³+4x²+2x. Base point has x=-2.
    Point twice(Point P) const {
        U a=sq(P.x), b=sq(P.z), t=mul(P.x,P.z);
        b=add(b,b); t=add(t,t); t=add(t,t);
        return {sq(sub(a,b)),mul(t,add(add(a,b),t))};
    }
    Point differential(Point P,Point Q) const {
        U a=mul(P.x,Q.x), b=mul(P.z,Q.z);
        U d=sq(sub(mul(P.x,Q.z),mul(P.z,Q.x)));
        return {sq(sub(a,add(b,b))),sub(0,add(d,d))};
    }
    bool kills(int q) const {
        Point P={p-2,1}, Q=twice(P);
        for(int i=30-__builtin_clz((unsigned)q);i>=0;--i) {
            Point sum=differential(P,Q);
            if ((q>>i)&1) {P=sum; Q=twice(Q);}
            else {Q=sum; P=twice(P);}
        }
        return !P.z;
    }
};

int main(int argc,char**argv) {
    U bound = argc>1?std::strtoull(argv[1],nullptr,10):10000000000ULL;
    if(bound<243 || bound>1000000000000ULL) return 2;
    U grid=0, tested=0, hits=0, ranks=0;
    for (int q=11; (U)2*q*q+1<=bound; q+=2) {
        if ((q%8!=1 && q%8!=3) || !prime(q)) continue;
        ++ranks;
        mpz_srcptr scalar = q <= 251 ? term(q).get_mpz_t() : nullptr;
        // Keep even a only, since 1+qa is odd for every odd prime norm.
        for(I b=1;(U)2*(q*b)*(q*b)<bound;++b) {
            U imag=2*(q*b)*(q*b);
            I radius=root(bound-imag);
            I lo=-(radius+1)/(2*q), hi=(radius-1)/(2*q);
            // hi is floor((radius-1)/2q). Here radius >= 1.
            for(I h=lo;h<=hi;++h) {
                I x=1+2*q*h;
                U p=x*x+imag;
                ++grid;
                if(p%3==0 || p%5==0 || p%7==0 || p%11==0 || p%13==0 ||
                   p%17==0 || p%19==0 || p%23==0 || p%29==0 || p%31==0) continue;
                ++tested;
                bool divides;
                if (scalar) divides = mpz_divisible_ui_p(scalar, p);
                else divides=Kummer{p}.kills(q);
                if(divides && prime(p)) {
                    std::cout << q << '\t' << p << '\n';
                    ++hits;
                }
            }
        }
    }
    std::cerr << "split indices " <<ranks<<", odd norms "<<grid<<", after trial sieve "
              <<tested<<", prime scalar hits "<<hits<<'\n';
}
