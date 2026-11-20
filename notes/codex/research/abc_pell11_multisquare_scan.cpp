// Enumerate all indices in an interval having at least three lifted square primes.
// Input lines have p, projective period m, and residues modulo p*m.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using i64=int64_t;
using i128=__int128_t;
struct Prime {int p; i64 period; std::vector<i64> residues;};
struct Event {i64 n; int a,b; bool operator<(const Event& other) const {return n<other.n;}};
i64 inverse(i64 a,i64 mod) {
    i64 b=mod,s=1,t=0;
    while(b) {i64 q=a/b; i64 r=a-q*b; a=b;b=r; r=s-q*t;s=t;t=r;}
    if(a!=1) std::abort();
    return (s%mod+mod)%mod;
}
void add(std::vector<Event>& events,i128 first,i128 period,i64 lo,i64 hi,int a,int b) {
    if(first<lo) first+=((lo-first+period-1)/period)*period;
    for(i128 n=first;n<=hi;n+=period) events.push_back({(i64)n,a,b});
}
int main(int argc,char**argv) {
    if(argc!=5){std::cerr<<"classes file, inclusive lower bound, inclusive upper bound, hot count\n";return 1;}
    std::ifstream input(argv[1]); i64 lo=std::stoll(argv[2]),hi=std::stoll(argv[3]); int hot=std::stoi(argv[4]);
    if(!input||lo<1||hi<lo) return 1;
    std::vector<Prime> rows;
    for(std::string line;std::getline(input,line);) {
        std::istringstream s(line); Prime row; i64 m,r; s>>row.p>>m; row.period=row.p*m;
        while(s>>r) row.residues.push_back(r);
        if(!std::is_sorted(row.residues.begin(),row.residues.end())||std::adjacent_find(row.residues.begin(),row.residues.end())!=row.residues.end()) return 1;
        rows.push_back(row);
    }
    std::sort(rows.begin(),rows.end(),[](const Prime& a,const Prime& b){
        return (i128)a.residues.size()*b.period>(i128)b.residues.size()*a.period;
    });
    hot=std::min(hot,(int)rows.size());
    std::vector<Event> events;
    for(size_t i=hot;i<rows.size();i++) for(i64 r:rows[i].residues)
        add(events,r,rows[i].period,lo,hi,rows[i].p,0);
    size_t cold_events=events.size();
    for(int i=0;i<hot;i++) for(int j=0;j<i;j++) {
        const auto& a=rows[i];const auto& b=rows[j];
        i64 d=std::gcd(a.period,b.period), v=b.period/d;
        i64 inv=inverse(a.period/d%v,v);
        i128 period=(i128)a.period*v;
        for(i64 r:a.residues) for(i64 s:b.residues) {
            if((s-r)%d)continue;
            i64 k=(i128)((s-r)/d)*inv%v;
            if(k<0)k+=v;
            add(events,r+(i128)a.period*k,period,lo,hi,a.p,b.p);
        }
    }
    std::cerr<<"primes "<<rows.size()<<" hot "<<hot<<" cold incidences "<<cold_events<<" hot pairs "<<events.size()-cold_events<<"\n";
    std::sort(events.begin(),events.end());
    for(size_t i=0;i<events.size();) {
        size_t j=i+1;
        while(j<events.size()&&events[i].n==events[j].n) j++;
        if(j>i+1) {
            std::set<int> primes;
            for(size_t k=i;k<j;k++){primes.insert(events[k].a);if(events[k].b)primes.insert(events[k].b);}
            for(int k=0;k<hot;k++) {
                const auto& a=rows[k];
                if(std::binary_search(a.residues.begin(),a.residues.end(),events[i].n%a.period)) primes.insert(a.p);
            }
            if(primes.size()>=3){std::cout<<events[i].n;for(int p:primes)std::cout<<" "<<p;std::cout<<"\n";}
        }
        i=j;
    }
}
