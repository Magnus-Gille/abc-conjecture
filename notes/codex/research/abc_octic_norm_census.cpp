// Exhaustive primitive square-full / cube-full census for the four octic quadratics.
// Build with g++ -std=c++17 -O3 and run with an integer height at most 10^9.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

using Integer = long long;
using Pair = std::pair<Integer, Integer>;
using Row = std::tuple<int,int,Integer,Integer,Integer,Integer>;
enum Form { D, Y, Minus, Plus };
const char* names[] = {"D","Y","U-","U+"};

Integer isqrt(Integer n) {
    Integer r = std::sqrt(static_cast<long double>(n));
    while ((r+1) <= n/(r+1)) ++r;
    while (r && r > n/r) --r;
    return r;
}
bool square(Integer n) {
    Integer r = isqrt(n);
    return r*r == n;
}
bool split_prime(int d, int p) {
    if (d == -1) return p%4 == 1;
    if (d == -2) return p%8 == 1 || p%8 == 3;
    return p%8 == 1 || p%8 == 7;
}
Pair generator(int d, int p) {
    // In the real quadratic ring a unit multiple has real embedding in
    // [sqrt(p),(1+sqrt(2))*sqrt(p)), so its nonnegative y is <= sqrt(p).
    for (int y=1; y*y<=p; ++y) {
        for (int sign : {1,-1}) {
            Integer x2 = sign*p + d*y*y;
            if (x2 < 0) continue;
            Integer x=isqrt(x2);
            if (x*x==x2 && (d!=-1 || x%2)) return {x,y};
        }
    }
    std::abort();
}
Pair multiply(Pair z, Pair w, int d) {
    return {z.first*w.first+d*z.second*w.second,z.first*w.second+z.second*w.first};
}
Pair real_representative(Pair z) {
    // Choose the unique sign and power of 1+sqrt(2) for which the positive
    // real embedding lies in [sqrt(abs(norm)),(1+sqrt(2))*sqrt(abs(norm))).
    auto [x,y] = z;
    if ((x<=0 && y<=0) || (x<0 && y>0 && (__int128)x*x>2*(__int128)y*y)
        || (x>0 && y<0 && (__int128)x*x<2*(__int128)y*y)) { x=-x; y=-y; }
    while (x<0 || y<0) std::tie(x,y)=Pair{x+2*y,x+y};
    while (2*y>=x && x>=y) std::tie(x,y)=Pair{2*y-x,x-y};
    return {x,y};
}
std::array<Integer,4> values(Integer s,Integer t) {
    Integer a=s*s, b=t*t, twice=2*s*t;
    return {std::abs(a-2*b),a+2*b,a+2*b-twice,a+2*b+twice};
}
struct Census {
    Integer h;
    int d;
    Integer limit;
    std::array<Integer,4> counts{};
    std::vector<Row> matches;
    std::vector<int> primes;
    std::vector<Pair> generators;
    std::array<std::vector<int>,4> target_primes;
    explicit Census(Integer height) : h(height) {
        Integer max_value=5*h*h;
        int last=1;
        while ((Integer)(last+1)*(last+1)*(last+1) <= max_value) ++last;
        std::vector<bool> prime(last+1,true);
        for(int p=2;p*p<=last;++p) if(prime[p])
            for(int q=p*p;q<=last;q+=p) prime[q]=false;
        for(int p=3;p<=last;p+=2) if(prime[p])
            for(int j=0;j<4;++j) if(split_prime(j==D?2:j==Y?-2:-1,p))
                target_primes[j].push_back(p);
    }
    bool squarefull(Integer n,int form) {
        if(square(n)) return true;
        for(int p:target_primes[form]) {
            if((Integer)p*p*p>n) break;
            if(n%p) continue;
            n/=p;
            if(n%p) return false;
            do {n/=p;} while(n%p==0);
        }
        return square(n);
    }
    void inspect(Integer s,Integer t,int cubefull,Integer norm) {
        if(s<1 || s>h || t<1 || t>h || t%2 || s%2==0) return;
        auto f=values(s,t);
        if (f[cubefull]!=norm || std::gcd(s,t)!=1) std::abort();
        ++counts[cubefull];
        for(int j=0;j<4;++j) if(j!=cubefull && squarefull(f[j],j))
            matches.emplace_back(cubefull,j,s,t,norm,f[j]);
    }
    void visit(std::size_t first,Integer norm,Pair z) {
        if(d==2) {
            auto [x,y]=z;
            while(x<=h && y<=h) {
                inspect(x,y,D,norm);
                std::tie(x,y)=Pair{x+2*y,x+y};
            }
        } else {
            auto x=std::abs(z.first), y=std::abs(z.second);
            if(d==-2) inspect(x,y,Y,norm);
            else {
                inspect(x-y,y,Plus,norm);
                inspect(x+y,y,Minus,norm);
                inspect(y-x,y,Minus,norm);
            }
        }
        for (std::size_t i=first;i<primes.size();++i) {
            Integer p=primes[i], cube=p*p*p;
            if(cube>limit/norm) break;
            Pair g=generators[i], power=multiply(multiply(g,g,d),g,d);
            Integer next=norm*cube;
            while(true) {
                if(d==2) power=real_representative(power);
                Pair out=multiply(z,power,d);
                visit(i+1,next,d==2?real_representative(out):out);
                if(first || d==2) {
                    out=multiply(z,{power.first,-power.second},d);
                    visit(i+1,next,d==2?real_representative(out):out);
                }
                if(next>limit/p) break;
                next*=p;
                power=multiply(power,g,d);
            }
        }
    }
    void run() {
        for(int ring : {-2,2,-1}) {
            d=ring;
            limit=(d==2?2:d==-2?3:5)*h*h;
            primes.clear(); generators.clear();
            for(int p:target_primes[d==2?D:d==-2?Y:Plus]) {
                if((Integer)p*p*p>limit) break;
                primes.push_back(p);
                generators.push_back(generator(d,p));
            }
            visit(0,1,{1,0});
        }
        std::sort(matches.begin(),matches.end());
    }
};
bool brute_full(Integer n,int k) {
    for(Integer p=2;p*p<=n;++p) if(n%p==0) {
        int e=0;
        do { n/=p; ++e; } while(n%p==0);
        if(e<k) return false;
    }
    return n==1;
}
void verify(int h) {
    Census c(h);
    c.run();
    std::array<Integer,4> counts{};
    std::vector<Row> matches;
    for(int s=1;s<=h;s+=2) for(int t=2;t<=h;t+=2) if(std::gcd(s,t)==1) {
        auto f=values(s,t);
        for(int i=0;i<4;++i) if(brute_full(f[i],3)) {
            ++counts[i];
            for(int j=0;j<4;++j) if(j!=i && brute_full(f[j],2))
                matches.emplace_back(i,j,s,t,f[i],f[j]);
        }
    }
    std::sort(matches.begin(),matches.end());
    if(counts!=c.counts || matches!=c.matches) std::abort();
}
int main(int argc,char** argv) {
    if(argc!=2) return 1;
    Integer h=std::stoll(argv[1]);
    if(h<=0 || h>1000000000LL) return 1;
    verify(300);
    Census c(h); c.run();
    std::cout<<"H "<<h<<"\n";
    for(int i=0;i<4;++i) std::cout<<"cubefull "<<names[i]<<" "<<c.counts[i]<<"\n";
    for(auto [a,b,s,t,x,y]:c.matches)
        std::cout<<names[a]<<" "<<names[b]<<" "<<s<<" "<<t<<" "<<x<<" "<<y<<"\n";
}
