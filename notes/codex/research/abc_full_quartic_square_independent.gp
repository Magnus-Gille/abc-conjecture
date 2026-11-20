\\ Independent checks of the rational-index sieve and the two split local heights.
E = ellinit([0,36,0,36,0]);
P = [-2,8];
Ep = ellinit(E[1..5]*Mod(1,577));
print("order mod 577 = ",ellorder(Ep,P));
print("rejected odd residues = ",select(n->kronecker(lift(8*(6-ellmul(Ep,P,n)[1])),577)==-1, [1,3,5,7,9,11,13,15,17,19,21,23]));
print("order mod 47 = ",ellorder(ellinit(E[1..5]*Mod(1,47)),P));
for(i=1,3,p=[13,23,47][i]; s=sqrt(Mod(3,p)); print(p," cardinalities ",vector(2,j,ellcard(ellinit([0,0,0,9*(2+(-1)^j*s),0])))));
for(i=1,2,t=sqrt(3+O(47^10)); if(lift(t)%47!=[12,35][i],t=-t); A=ellinit([0,0,0,9*(2+t),0]);D=[(21+12*t)/4,(-153-90*t)/8]; if(!ellisoncurve(A,D),error("invalid point")); R=ellmul(A,D,12); zm=lift((-R[1]/R[2])/47)%47; h=lift(t)%47^2; s=Mod(lift(t),47); B=ellinit([0,0,0,9*(2+s),0]);D0=[(21+12*s)/4,(-153-90*s)/8];print("root mod 47^2, D order, z(12D)/47 mod 47 = ",[h,ellorder(B,D0),zm]));
print("primitive genus-two points in height 100000 = ",hyperellratpoints(-2*(x^2+3)*(x^4-18*x^2+9),100000));
