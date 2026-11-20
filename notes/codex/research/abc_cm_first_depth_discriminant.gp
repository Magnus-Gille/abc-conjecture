\\ Verify first-layer different exponents at the two places above 11.
default(parisizemax,250000000);
K = nfinit(y^2 + 2);
tau = Mod(y, y^2 + 2);
E = ellinit([0,16,0,32,0]);
cubic = x^3 + 16*x^2 + 32*x;
tripling = ellxn(E,3);
u = tripling[1]/tripling[2];
v = -(x + 16 + 32/x)/2;
w = cubic*((deriv(u,x)/3 - deriv(v,x)/tau)/(u-v))^2 - 16 - u - v;
places_11 = idealprimedec(K,11);
connected = if(idealval(K,3+tau,places_11[1])==1,1,2);
other = 3-connected;

R = [-8,16];
reduction_order = ellorder(ellinit([0,16,0,32,0],11),R);
if(reduction_order!=9 || valuation(ellmul(E,R,reduction_order)[1],11)!=-2,error("first depth"));

F = numerator(w+8);
F = F/pollead(F);
if(poldegree(F)!=11 || matsize(nffactor(K,F))[1]!=1,error("simple orbit"));
disc = rnfdisc(K,F)[1];
if(idealval(K,disc,places_11[connected])!=11 || idealval(K,disc,places_11[other])!=0,error("simple discriminant"));

G = numerator(w-subst(w,x,-8))/(x+8);
G = G/pollead(G);
if(poldegree(G)!=10 || matsize(nffactor(K,G))[1]!=1,error("repeated orbit"));
disc = rnfdisc(K,G)[1];
if(idealval(K,disc,places_11[connected])!=9 || idealval(K,disc,places_11[other])!=0,error("repeated discriminant"));
print("p=11: connected-place discriminant exponents 11 (R) and 9 ([3+tau]R).");

\\ Compare the degree-121 fibres at the connected place for three depths.
tau_lift = sqrt(-2 + O(11^90));
tau_lift = if(valuation(tau_lift+3,11)>0,lift(tau_lift),lift(-tau_lift));
num = subst(lift(numerator(w)),y,tau_lift);
den = subst(lift(denominator(w)),y,tau_lift);
local_map = num/den;
num2 = subst(num,x,local_map)*den^11;
den2 = subst(den,x,local_map)*den^11;
target1 = subst(local_map,x,-8);
target2 = subst(local_map,x,target1);

local_different(g) = {
  my(d=poldegree(g), a=0, h);
  if(d==1,return(0));
  while(a<11 && valuation(subst(g,x,a),11)==0,a++);
  if(a==11,error("missing residue root"));
  h=subst(g,x,x+a);
  if(valuation(polcoef(h,0),11)!=1,error("nonuniformizer"));
  for(i=0,d-1,if(valuation(polcoef(h,i),11)<1,error("not Eisenstein")));
  vecmin(vector(d,i,d*valuation(i*polcoef(h,i),11)+i-1))
};

verify_fibre(target, degrees, differents) = {
  my(factors=factorpadic(num2-target*den2,11,7), n=matsize(factors)[1]);
  if(vector(n,i,poldegree(factors[i,1]))!=degrees,error("local degrees"));
  if(vector(n,i,local_different(factors[i,1]))!=differents,error("local differents"))
};

verify_fibre(-8,[121],[242]);
verify_fibre(target1,[11,110],[11,209]);
verify_fibre(target2,[1,10,110],[0,9,209]);
print("p=11: level-two local discriminant exponents 242, 220, 218.");
