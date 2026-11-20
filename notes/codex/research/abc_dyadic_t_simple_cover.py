"""Exact recurrence and power-character checks for t_{2^k}/17, k>=3."""

from math import gcd, isqrt

AUXILIARY = {
    2:7, 3:7, 5:31, 7:127, 11:199, 13:8087, 17:103, 19:191, 23:47,
    29:10847, 31:9239, 37:223, 41:5167, 43:4817, 47:473479, 53:892097,
    59:1070497, 61:9151, 67:196177, 71:2273, 73:1607, 79:2687, 83:6143,
    89:25633, 97:11447, 101:262399, 103:3202271, 107:30817, 109:31393,
    113:25087, 127:56897, 131:23057, 137:823, 139:(557,2503),
    149:1537681, 151:1511,
}


def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def next_state(a,b,p):
    aa,ab,bb = a*a%p, a*b%p, b*b%p
    return (aa-32*bb)**2%p, 4*ab*(aa+16*ab+32*bb)%p


def allowed(q,p):
    assert prime(p) and p!=17 and (p-1)%q==0
    a,b = 31**2%p,14**2%p
    inv = pow(17,-1,p)
    seen, bits = {}, []
    while (a,b) not in seen:
        seen[a,b]=len(bits)
        bits.append(pow((a+16*b)*inv%p,(p-1)//q,p) in (0,1))
        a,b=next_state(a,b,p)
    start=seen[a,b]
    return bits,start,len(bits)-start


# Modulus of the k condition and its simple cofactor prime.
COFACTOR_CLASSES={17:285190337, 3: 241, 5: 97, 7: 37313, 11: 6705793, 13: 2820977, 23: 22364161, 29: 433, 37: 42257, 41: 673, 47: 20161, 53: 7873, 59: 248401, 73: 167537, 83: 35569, 89: 1489, 97: 7681, 107: 246209, 113: 59729, 131: 25073, 137: 211217, 157: 3258529, 173: 92177, 181: 1172401, 233: 33889, 239: 8168561, 241: 174289, 263: 113041, 271: 58430609, 281: 76231153, 283: 2732993, 293: 4561, 311: 4615297, 337: 519089, 367: 773953, 373: 4354913, 397: 23161393}

def go(x,k,p):
 for j in range(k): x=(x*x-32)**2*pow(4*x*(x*x+16*x+32),-1,p)%p
 return x
def order(a,p):
 d=p-1; rest=d;q=2
 while q*q<=rest:
  if rest%q==0:
   while rest%q==0:rest//=q
   while d%q==0 and pow(a,d//q,p)==1:d//=q
  q+=1
 if rest>1:
  while d%rest==0 and pow(a,d//rest,p)==1:d//=rest
 return d
def check_class(q,k,p):
 assert prime(p) and prime(q) and 2*k-3==q
 x=1;cl=[]
 for j in range(q):
  if x==(-16)%p:cl.append((j+2)%q)
  x=go(x,1,p)
 assert x==1 and cl==[k%q],(q,p,cl)
 m=p*p
 w=go(-16,q,m); z=go(p-16,q,m)
 assert (w+16)%p==0 and (z-w)%p==0
 b=((w+16)//p)%p;a=((z-w)//p)%p
 h=(go(1,k-2,m)+16)//p%p
 assert h and a
 if a==1:assert b==0;return
 fix=b*pow(1-a,-1,p)%p
 if not fix or fix==h:return
 need=-fix*pow(h-fix,-1,p)%p
 assert pow(need,order(a,p),p)!=1,(q,k,p,a,b,h)


def check_deep_prime():
    p=12241
    assert prime(p)
    x=1
    hits=[]
    for k in range(2,9):
        if (x+16)%p==0:hits.append(k)
        x=go(x,1,p)
    assert x==1 and hits==[5]
    w=go(-16,7,p*p)
    z=go(p-16,7,p*p)
    assert ((w+16)//p,(z-w)//p%p)==(1556,12113)
    h=(go(1,3,p*p)+16)//p%p
    assert h==9115
    vals=[]
    for j in range(255):
        if h==0:vals.append(j)
        h=(12113*h+1556)%p
    assert h==9115 and vals==[127] and 5+7*127==894
    assert order(2,p)==510 and (pow(2,255,p*p)+1)//p==2714
    assert ((go(-16,1785,p**3)+16)//(p*p))%p==10714
    assert ((go(1,892,p**3)+16)//(p*p))%p==5357


def run():
    check_deep_prime()
    # Verify the unnormalized u²,v² recursion through the entire mod-17² orbit.
    a=b=1
    seen=set()
    while (a,b) not in seen:
        seen.add((a,b))
        assert gcd(b,17)==1 and (a+16*b)%17==0 and (a+16*b)%289!=0
        a,b=next_state(a,b,289)

    assert set(AUXILIARY)=={q for q in range(2,152) if prime(q)}
    for q,places in AUXILIARY.items():
        if isinstance(places,int):
            bits,start,period=allowed(q,places)
            assert not any(bits)
        else:
            (a,i,d),(b,j,e)=(allowed(q,p) for p in places)
            first=lambda seq,s,l,k: seq[k] if k<len(seq) else seq[s+(k-s)%l]
            assert not any(first(a,i,d,k) and first(b,j,e,k) for k in range(max(i,j)))
            g=gcd(d,e)
            c={k%g for k in range(i,len(a)) if a[k]}
            f={k%g for k in range(j,len(b)) if b[k]}
            assert not c.intersection(f)
    from fractions import Fraction
    from math import prod
    for q,p in COFACTOR_CLASSES.items():
        check_class(q,(q+3)//2,p)
    density=1-prod(Fraction(q-1,q) for q in COFACTOR_CLASSES)
    print('Density of the certified union for the cofactor:',density)
    print('17 is simple throughout; T=t/17 excludes all 36 prime exponents through 151.')


if __name__ == '__main__':
    run()
