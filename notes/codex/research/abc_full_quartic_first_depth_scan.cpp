// Enumerate all good primes on y^2=x^3-36x at G=(-3,9) whose first depth is at least 2
// and whose reduction order is not divisible by 4. Build without -DNDEBUG.
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using U = std::uint64_t;
using W = __uint128_t;
struct Point { U x,y,z; };
static constexpr Point O{1,1,0};
U sub(U a,U b,U q){return a>=b?a-b:a+q-b;}
template<bool wide> U mul(U a,U b,U q){
    if constexpr(wide) return (W)a*b%q;
    return a*b%q;
}
// Jacobian coordinates. When lifting the exact order, all proper positive
// binary prefixes are smaller than the order and therefore finite mod p.
template<bool wide> Point times_generator(unsigned n,U p){
    assert(n);
    const U q = wide ? p*p : p;
    const U bx=q-3, by=9%q;
    Point v{bx,by,1};
    for(int i=30-__builtin_clz(n);i>=0;i--){
        if constexpr(wide) assert(v.z%p);
        if(v.z && v.y){
            U xx=mul<wide>(v.x,v.x,q),yy=mul<wide>(v.y,v.y,q),zz=mul<wide>(v.z,v.z,q);
            U m=sub(3*xx%q,36*mul<wide>(zz,zz,q)%q,q);
            U s=4*mul<wide>(v.x,yy,q)%q;
            U x=sub(mul<wide>(m,m,q),2*s%q,q);
            U y=sub(mul<wide>(m,sub(s,x,q),q),8*mul<wide>(yy,yy,q)%q,q);
            v={x,y,2*mul<wide>(v.y,v.z,q)%q};
        } else v=O;
        if(!(n&(1u<<i))) continue;
        if constexpr(wide) assert(v.z%p);
        if(!v.z){ v={bx,by,1}; continue; }
        U zz=mul<wide>(v.z,v.z,q),h=sub(mul<wide>(bx,zz,q),v.x,q);
        U t=sub(by*mul<wide>(zz,v.z,q)%q,v.y,q);
        if constexpr(wide) assert(h%p || t%p);
        if(!h){
            // The equal point is the fixed generator, represented affinely by (bx,by).
            // Doubling G gives M=-9, S=-972, X=2025, Y=-25515, Z=18.
            v=t?O:Point{2025%q,(q-25515%q)%q,18%q};
            continue;
        }
        U hh=mul<wide>(h,h,q),hhh=mul<wide>(h,hh,q),s=mul<wide>(v.x,hh,q);
        U x=sub(sub(mul<wide>(t,t,q),hhh,q),2*s%q,q);
        U y=sub(mul<wide>(t,sub(s,x,q),q),mul<wide>(v.y,hhh,q),q);
        v={x,y,mul<wide>(v.z,h,q)};
    }
    return v;
}
bool kills(unsigned n,U p){return times_generator<false>(n,p).z==0;}
int main(int argc,char**argv){
    int bound=argc==2?std::atoi(argv[1]):31904497;
    if(bound<5||bound>40000000) return 1;
    int limit=bound+2*static_cast<int>(std::sqrt(bound))+5;
    std::vector<int> least(limit+1);
    for(int i=2;i<=limit;i++){
        if(least[i])continue;
        least[i]=i;
        if(i<=limit/i)for(int j=i*i;j<=limit;j+=i)if(!least[j])least[j]=i;
    }
    std::vector<short> odd_component(bound+1);
    for(int a=1;a*a<=bound;a+=2)for(int b=2;a*a+b*b<=bound;b+=2)
        odd_component[a*a+b*b]=(a+b)%4==1?a:-a;
    int total=0,odd=0,twice_odd=0,hits=0,prime_orders=0;
    U order_sum=0,lift_sum=0;
    for(int p=5;p<=bound;p+=2){
        if(least[p]!=p)continue;
        ++total;
        int r=p+1;
        if(p%4==1){
            int a=odd_component[p];
            assert(a);
            if(p%8==5)a=-a;
            r-=2*a;
            if(!kills(r,p))r=p+1+2*a;
        }
        assert(kills(r,p));
        while(r%4==0)r/=2;
        if(kills(r,p)){
            for(int k=r;k>1;){
                int ell=least[k];
                while(k%ell==0)k/=ell;
                while(r%ell==0&&kills(r/ell,p))r/=ell;
            }
            if(r%2)++odd;else ++twice_odd;
            if(r%2 && least[r]==r)++prime_orders;
            auto v=times_generator<true>(r,p);
            assert(v.x%p && v.y%p && v.z%p==0);
            if(!v.z){++hits;std::cout<<"hit p="<<p<<" r="<<r<<'\n'<<std::flush;}
            order_sum+=r;lift_sum+=v.z/p;
        }
        if(total%100000==0)std::cout<<"checkpoint primes="<<total<<" p="<<p<<" eligible="<<odd+twice_odd<<" hits="<<hits<<'\n'<<std::flush;
    }
    std::cout<<"bound="<<bound<<" good_primes="<<total<<" odd_order="<<odd<<" twice_odd_order="<<twice_odd<<" odd_prime_order="<<prime_orders<<" hits="<<hits<<" order_sum="<<order_sum<<" lift_sum="<<lift_sum<<'\n';
}
