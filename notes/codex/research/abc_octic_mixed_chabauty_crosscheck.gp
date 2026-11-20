\\ Independent PARI/GP cross-check of the five local disks at 11.
\\ Uses PARI's number-field residue maps, finite-field square roots and ellmul.

f = t^4-2*t^2-1;
nf = nfinit(f);
mp = nfmodprinit(nf, idealprimedec(nf,11)[1], 'r);
tt = Mod(t,f);
aa = 1+1/tt;
bb = aa*tt^2;
beta = -2*(1+tt);
gamma0 = 4*tt^3+2*tt^2-8*tt+2;
kk = -12*tt^3-4*tt^2+28*tt+4;
gg = 8*(tt^3+tt^2-tt);

pad(x) = Mod(lift(x)*(1+O(11^150)), f);
ec = ellinit([0,pad(-aa-bb),0,pad(aa*bb),0]);
residue_curve = ellinit([0,nfmodpr(nf,-aa-bb,mp),0,nfmodpr(nf,aa*bb,mp),0]);
ord = ellcard(residue_curve);
if (ord != 14596, error("Unexpected residue curve order"));

\\ Start Newton lifting with a residue-field square root of a fixed
\\ representative. Keeping this choice fixed identifies the sheet of the disk.
liftroot(x, initial) = {
  my(rep = lift(nfmodprlift(nf,sqrt(nfmodpr(nf,initial,mp)),mp)), v);
  for(j=0,3, if(polcoef(rep,j)%11, if(polcoef(rep,j)%11>5,rep=-rep); break));
  v = pad(rep);
  for(i=1,8, v=(v+x/v)/2);
  return(v);
};

to_curve(z,w) = {
  my(u=2*(w+z^2+beta*z+gamma0), v=2*u*z+beta*u-2*kk);
  return([(u+4*(1+tt)^2)/16,v/64]);
};

log_row(pt) = {
  my(q=ellmul(ec,pt,ord), u);
  if(#q==1, return([0,0,0,0]));
  u=lift(-q[1]/q[2])/11;
  for(j=0,3, if(valuation(polcoef(u,j),11)<0 || padicprec(polcoef(u,j),11)<2, error("Insufficient precision")));
  return(vector(4,j,lift(polcoef(u,j-1))%11));
};

project_row(v) = [(v[3]-7*v[2])%11,(v[4]-9*v[1]-10*v[2])%11];
factor_t(z) = z^2+2*beta*z+gg;

pole = [pad((1+tt)^2/4),pad(kk/32)];
seed = [pad((2*tt^3+5*tt^2+2*tt+2)/4),pad((-5*tt^3-11*tt^2-8*tt-5)/8)];
rows = [log_row(pole),log_row(seed)];
if(project_row(rows[1])!=[0,0] || project_row(rows[2])!=[0,0],error("Wrong log span"));
if((rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])%11==0,error("Dependent log directions"));

check_disk(d) = {
  my(z,v,w,b,r,h0,pt,vec, base, slope, keep=List());
  for(h=0,10,
    if(d==11,
      if(h==0, pt=pole,
        r=pad(11*h);
        w=liftroot((1+8*r^2)*(1+2*beta*r+gg*r^2),1);
        if(lift(polcoef(lift(w),0))%11 != 1, w=-w);
        pt=to_curve(1/r,-w/r^2)
      ),
      if(d==6,
        v=11*h;
        z=sqrt(v^2-8+O(11^150));
        if(lift(z)%11!=6, z=-z);
        z=pad(z);
        w=v*liftroot(factor_t(z),factor_t(6)),
        z=pad(d+11*h);
        w=liftroot((z^2+8)*factor_t(z),(d^2+8)*factor_t(d))
      );
      pt=to_curve(z,w)
    );
    vec=project_row(log_row(pt));
    if(h==0, base=vec);
    if(h==1, slope=vec-base);
    if(h>=2 && (vec-base-h*slope)%11 != [0,0], error("Nonlinear first digit"));
    if(vec==[0,0], listput(keep,h))
  );
  return(Vec(keep));
};

eligible=select(z->issquare(Mod(z^2+8,11)) && issquare(Mod((z^2-4*z-8)^2+16*z^2,11)),[0..10]);
if(eligible!=[1,6,9,10],error("Unexpected finite disks"));
disks=concat(eligible,[11]); \\ 11 denotes infinity.
surviving=apply(check_disk,disks);
if(surviving!=[[],[0],[],[10],[0]],error("Wrong disk survivors",surviving));
print("Residue group order ",ord,", log directions ",rows,", surviving digits ",surviving);
