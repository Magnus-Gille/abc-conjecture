\\ PARI/GP verifier. Run with gp -s 128M -q abc_octic_mixed_frey_bound.gp.

allowed(p) =
{
  my(out = List(), s, t, yy, vv, a2, a4);
  for(k = 0, p,
    if(k == p, s = 1; t = 0, s = k; t = 1);
    yy = (s^2 + 2*t^2) % p;
    vv = (yy - 2*s*t) % p;
    if(kronecker(yy,p) == -1 || kronecker(vv,p) == -1, next);
    a2 = 8*s*t;
    a4 = 16*s^2*t^2 - 6*yy^2;
    if(a4*(a2^2-4*a4) % p == 0, error("bad local reduction for this prime"));
    listput(out, -sum(x = 0, p-1, kronecker(x*(x^2+a2*x+a4),p)));
  );
  Set(Vec(out))
}

audit() =
{
  my(space = mfinit([2304,2],0), forms = mfeigenbasis(space));
  my(ps = [5,7,17,29], sets = [[-2,2],[0],[-6,4,8],[-6,-2,6,10]]);
  my(e = ellinit([0,0,0,-6,0]), live, tr, a, val, n, deg, cm, survivors);
  my(degrees = vector(#forms,j,poldegree(mfparams(forms[j])[4])));
  if(mfdim(space) != 38 || #forms != 26, error("unexpected dimension"));
  if(vecsum(degrees) != 38 || sum(j=1,#forms,degrees[j]==1) != 16 ||
     sum(j=1,#forms,degrees[j]==2) != 9 || sum(j=1,#forms,degrees[j]==4) != 1,
     error("unexpected coefficient-field degrees"));
  print("Coefficient-field degrees: ", degrees);
  live = vector(#forms,j,1);
  for(k = 1, #ps,
    tr = allowed(ps[k]);
    if(tr != sets[k], error("unexpected finite trace set"));
    for(j = 1, #forms,
      if(!live[j], next);
      a = mfcoef(forms[j],ps[k]);
      val = prod(i=1,#tr,a-tr[i]);
      if(val == 0, next);
      deg = degrees[j];
      n = if(type(val)=="t_POLMOD", abs(norm(val)), abs(val)^deg);
      if(n > 1 && vecmax(factor(n)[,1]) > 37, error("extra exponent divides norm"));
      live[j] = 0;
    );
    print("p=", ps[k], ": allowed ", tr, ", surviving orbit count ", vecsum(live));
  );
  if(vecsum(live) != 1, error("unexpected surviving count"));
  cm = select(j->live[j],vector(#forms,j,j))[1];
  if(ellglobalred(e)[1] != 2304, error("CM conductor"));
  if(mfcoefs(forms[cm],768) != concat(0,ellan(e,768)), error("Sturm comparison"));
  print("The survivor equals the newform of y^2=x^3-6x through coefficient 768.");
}

audit();
