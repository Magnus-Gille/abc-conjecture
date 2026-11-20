// Compile with g++ -O3 -std=c++17. Default upper limit 10,000,000.
// Exhaustive first-odd-index elliptic Wieferich check for Q=(-16,-252).
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>

using U = std::uint64_t;
struct Point { U x,y,z; };

template<bool wide> struct Curve {
    U n, a, qx, qy;
    explicit Curve(U modulus) : n(modulus), a((n-4225%n)%n),
        qx((n-16%n)%n), qy((n-252%n)%n) {}

    U sub(U x,U y) const { return x>=y?x-y:n+x-y; }
    U mul(U x,U y) const {
        if constexpr(wide) return ((__uint128_t)x*y)%n;
        else return x*y%n;
    }
    Point twice(Point p) const {
        if(!p.z || !p.y) return {0,1,0};
        U yy=mul(p.y,p.y), zz=mul(p.z,p.z);
        U s=mul(mul(4,p.x),yy), m=(3*mul(p.x,p.x)+mul(a,mul(zz,zz)))%n;
        U x=sub(mul(m,m),(2*s)%n);
        return {x,sub(mul(m,sub(s,x)),mul(8,mul(yy,yy))),mul(2*p.y%n,p.z)};
    }
    Point add_q(Point p) const {
        if(!p.z) return {qx,qy,1};
        U zz=mul(p.z,p.z), h=sub(mul(qx,zz),p.x);
        U t=sub(mul(qy,mul(zz,p.z)),p.y);
        if(!h) return !t?twice(p):Point{0,1,0};
        U hh=mul(h,h), hhh=mul(h,hh), v=mul(p.x,hh);
        U x=sub(sub(mul(t,t),hhh),2*v%n);
        return {x,sub(mul(t,sub(v,x)),mul(p.y,hhh)),mul(p.z,h)};
    }
    bool kills(U k) const {
        assert(k);
        Point p={qx,qy,1};
        for(int i=62-__builtin_clzll(k);i>=0;--i) {
            p=twice(p);
            if((k>>i)&1) p=add_q(p);
        }
        return p.z==0;
    }
};

int main(int argc,char**argv) {
    int bound=argc>1?std::atoi(argv[1]):10000000;
    if(bound<17 || bound>100000000) return 2;
    int limit=bound+3*(int)std::sqrt(bound)+10;
    std::vector<int> factor(limit+1), odd_component(bound+1);
    for(int p=2;p<=limit;++p) if(!factor[p]) {
        factor[p]=p;
        if(p<=limit/p) for(int j=p*p;j<=limit;j+=p) if(!factor[j]) factor[j]=p;
    }
    // A CM trace gives a candidate annihilating multiple. The main loop
    // verifies [candidate]Q=O for every prime, so completeness is independent
    // of the CM trace formula.
    for(int b=2;b*b<bound;b+=2) {
        for(int a=1;a*a+b*b<=bound;a+=2) {
            int p=a*a+b*b;
            if(factor[p]==p) odd_component[p]=(a+b)%4==1?a:-a;
        }
    }
    int good=0, odd=0, exceptional=0;
    for(int p=17;p<=bound;p+=4) if(factor[p]==p) {
        ++good;
        int c=p%13;
        int chi13=(c==1||c==3||c==4||c==9||c==10||c==12)?1:-1;
        int chi5=(p%5==1||p%5==4)?1:-1;
        int multiple=p+1-2*odd_component[p]*chi5*chi13;
        Curve<false> residue(p);
        if(!residue.kills(multiple)) return 3;
        int r=multiple;
        while(!(r%2)) r/=2;
        if(!residue.kills(r)) continue;
        ++odd;
        for(int z=r;z>1;) {
            int l=factor[z];
            while(z%l==0) {
                z/=l;
                if(r%l==0 && residue.kills(r/l)) r/=l;
            }
        }
        // With r the exact odd order (>1), strict positive intermediate
        // multiples in the binary chain reduce to nonidentity; the final
        // addition has opposite reductions. The Jacobian formula gives a
        // unit X there and Z divisible by p. Testing Z=0 mod p² is exact.
        assert(r>1 && residue.kills(r));
        if(Curve<true>((U)p*p).kills(r)) {
            ++exceptional;
            std::printf("Wieferich p=%d, rank=%d\n",p,r);
        }
    }
    std::printf("%d good split primes, %d odd ranks, %d Wieferich primes\n",
                good,odd,exceptional);
}
