// First-occurrence denominator depths on y^2=x^3-396x+3024 at P=(10,8).
// Build with g++ -O3 -std=c++17 and run with a prime bound no larger than 10000000.
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using U=std::uint64_t;
using Wide=__uint128_t;
U add(U a,U b,U q){U c=a+b;return c>=q?c-q:c;}
U sub(U a,U b,U q){return a>=b?a-b:a+q-b;}
U times(U a,U b,U p){return a*b%p;} // Fields p <= 10^7 here
U wide_times(U a,U b,U q){return (Wide)a*b%q;}
struct Point{U x,y,z;};
const Point infinity{1,1,0};

Point twice(Point P,U p){
    if(!P.z||!P.y)return infinity;
    U xx=times(P.x,P.x,p),yy=times(P.y,P.y,p),zz=times(P.z,P.z,p);
    U s=times(P.x,yy,p)*4%p;
    U m=sub(3*xx%p,396*times(zz,zz,p)%p,p);
    U x=sub(times(m,m,p),2*s%p,p);
    U y=sub(times(m,sub(s,x,p),p),8*times(yy,yy,p)%p,p);
    return {x,y,2*times(P.y,P.z,p)%p};
}

Point plus_base(Point Q,U p){
    if(!Q.z)return {10%p,8%p,1};
    U zz=times(Q.z,Q.z,p);
    U h=sub(10*zz%p,Q.x,p);
    U t=sub(8*times(zz,Q.z,p)%p,Q.y,p);
    if(!h)return t?infinity:twice(Q,p);
    U hh=times(h,h,p),hhh=times(h,hh,p),v=times(Q.x,hh,p);
    U x=sub(sub(times(t,t,p),hhh,p),2*v%p,p);
    U y=sub(times(t,sub(v,x,p),p),times(Q.y,hhh,p),p);
    return {x,y,times(Q.z,h,p)};
}

bool kills(unsigned n,U p){
    assert(n);
    Point Q{10%p,8%p,1};
    for(int i=30-__builtin_clz(n);i>=0;i--){
        Q=twice(Q,p);
        if(n&(1u<<i))Q=plus_base(Q,p);
    }
    return !Q.z;
}

// For the exact field order r, every proper positive binary prefix is < r.
// All intermediate points are affine mod p, until the last operation lands
// at infinity. Hence the usual Jacobian formulas have no base-point ambiguity:
// a final mixed addition has t nonzero mod p when h vanishes mod p.
Point jacobian_lift(unsigned r,U p){
    U q=p*p;
    Point P{10%q,8%q,1};
    for(int i=30-__builtin_clz(r);i>=0;i--){
        assert(P.z%p);
        U xx=wide_times(P.x,P.x,q),yy=wide_times(P.y,P.y,q),zz=wide_times(P.z,P.z,q);
        U s=4*wide_times(P.x,yy,q)%q;
        U m=sub(3*xx%q,396*wide_times(zz,zz,q)%q,q);
        U x=sub(wide_times(m,m,q),2*s%q,q);
        U y=sub(wide_times(m,sub(s,x,q),q),8*wide_times(yy,yy,q)%q,q);
        P={x,y,2*wide_times(P.y,P.z,q)%q};
        if(!(r&(1u<<i)))continue;
        assert(P.z%p);
        zz=wide_times(P.z,P.z,q);
        U h=sub(10*zz%q,P.x,q),t=sub(8*wide_times(zz,P.z,q)%q,P.y,q);
        assert(h%p||t%p);
        U hh=wide_times(h,h,q),hhh=wide_times(h,hh,q),v=wide_times(P.x,hh,q);
        x=sub(sub(wide_times(t,t,q),hhh,q),2*v%q,q);
        y=sub(wide_times(t,sub(v,x,q),q),wide_times(P.y,hhh,q),q);
        P={x,y,wide_times(P.z,h,q)};
    }
    assert(P.x%p&&P.y%p&&P.z%p==0);
    return P;
}

// f_n=psi_n(P) for odd n, psi_n(P)/16 for even n.  At odd primes these
// are equivalent for zero tests. The signed initial window is n=-2,...,5.
U division_value(unsigned n,U q){
    std::array<U,8> f{q-1,q-1,0,1,1,(q-1536%q)%q,229376%q,18656264192ULL%q};
    unsigned center=1;
    for(int i=30-__builtin_clz(n);i>=0;i--){
        int bit=(n>>i)&1;
        std::array<U,8> sq{},cube{},next{};
        for(int j=0;j<8;j++){
            sq[j]=wide_times(f[j],f[j],q);
            cube[j]=wide_times(f[j],sq[j],q);
        }
        for(int j=0;j<8;j++){
            int offset=bit+j-3;
            int b=(offset+8)/2-4+3; // floor(offset/2), indexed in f
            if(offset%2){
                U v=wide_times(f[b+2],cube[b],q),w=wide_times(f[b-1],cube[b+1],q);
                if((center+b-3)&1)w=wide_times(w,65536,q);else v=wide_times(v,65536,q);
                next[j]=sub(v,w,q);
            }else{
                U v=wide_times(f[b+2],sq[b-1],q),w=wide_times(f[b-2],sq[b+1],q);
                next[j]=wide_times(f[b],sub(v,w,q),q);
            }
        }
        f=next;
        center=2*center+bit;
    }
    return f[3];
}

int main(int argc,char**argv){
    int bound=argc==2?std::atoi(argv[1]):10000000;
    if(bound<5||bound>10000000)return 1;
    int limit=bound+2*static_cast<int>(std::sqrt(bound))+5;
    std::vector<int> spf(limit+1),odd_square(bound+1);
    for(int i=2;i<=limit;i++){
        if(spf[i])continue;
        spf[i]=i;
        if((U)i*i<=(U)limit)for(int j=i*i;j<=limit;j+=i)if(!spf[j])spf[j]=i;
    }
    for(int a=1;a*a<=bound;a+=2)
        for(int b=2;a*a+b*b<=bound;b+=2)odd_square[a*a+b*b]=a;
    int count=0,hits=0;
    U order_sum=0,lift_sum=0;
    for(int p=5;p<=bound;p++){
        if(spf[p]!=p)continue;
        int r=p+1;
        if(p%4==1){
            int a=odd_square[p];
            assert(a);
            r=p+1-2*a;
            if(!kills(r,p))r=p+1+2*a;
        }
        assert(kills(r,p));
        int remaining=r;
        while(remaining>1){
            int ell=spf[remaining];
            while(remaining%ell==0)remaining/=ell;
            while(r%ell==0&&kills(r/ell,p))r/=ell;
        }
        U q=(U)p*p;
        U f=division_value(r,q);
        assert(f%p==0);
        Point lift=jacobian_lift(r,p);
        assert((lift.z==0)==(f==0));
        if(!f){
            std::cout<<"hit "<<p<<" "<<r<<"\n"<<std::flush;
            ++hits;
        }
        order_sum+=r;
        lift_sum+=f/p;
        ++count;
        if(count%100000==0)std::cout<<"checkpoint "<<count<<" "<<p<<" "<<order_sum<<" "<<lift_sum<<"\n"<<std::flush;
    }
    std::cout<<"bound "<<bound<<" primes "<<count<<" hits "<<hits<<" order_sum "<<order_sum<<" lift_sum "<<lift_sum<<"\n";
}
