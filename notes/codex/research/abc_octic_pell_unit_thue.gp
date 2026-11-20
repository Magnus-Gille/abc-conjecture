\\ Run with gp -q abc_octic_pell_unit_thue.gp
P = x^4+4*x^3-6*x^2-4*x+1;
if (!polisirreducible(P), error("unexpected reducible polynomial"));
sol = thue(thueinit(P,1),1);
expected = [[-3,-2],[-2,3],[-1,0],[0,-1],[0,1],[1,0],[2,-3],[3,2]];
if (Set(sol) != Set(expected), error("unexpected Thue solution list"));
print("PARI ",version(),"   F=1: ",sol);
