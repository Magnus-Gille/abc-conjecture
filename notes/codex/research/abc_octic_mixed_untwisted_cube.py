"""Certified number-field 2-descent for the mixed cube obstruction.

Pass a directory containing Denis Simon's ell.gp, qfsolve.gp and resultant3.gp
from Sage, commit 8de8dad7bcb38e1baa43508cbe944bf04a2d0401. Use GP with the
cypari or cypari2 bindings. The original files are hash checked, and the two
auxiliary bnfinit calls receive an unconditional certification assertion.
"""
from hashlib import sha256
from pathlib import Path
import sys
from tempfile import TemporaryDirectory

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()

dirpath = Path(sys.argv[1])
checks = {
    'qfsolve.gp':'739b6e06cb2c4b3e3adc7318bd327f3f5a3d9acef5fa2b52e68c34b85a0ac998',
    'resultant3.gp':'a195c027027ffd7e1134fbe1dfe88be2375e442a810c3ba51264701e885893b8',
    'ell.gp':'f137f61c596b4d86c72c294b46bccb8743beac55e5373d74ec7265baaf708800',
}
for name,expected in checks.items():
    content = (dirpath/name).read_bytes()
    assert sha256(content).hexdigest() == expected
    if name != 'ell.gp':
        pari.read(str(dirpath/name))
text = (dirpath/'ell.gp').read_text()
for bnf,defining_poly in [('bbbnf','solvepolabs'),('bbnf','rnfeq[1]')]:
    call = f'{bnf} = bnfinit({defining_poly},1);'
    assert text.count(call) == 1
    text = text.replace(call, call + f' if(!bnfcertify({bnf}),error("BNF certification failed"));'
                                     f' print("certified auxiliary discriminant ",{bnf}.disc);')
with TemporaryDirectory() as tmp:
    installed = Path(tmp)/'verified_ell.gp'
    installed.write_text(text)
    pari.read(str(installed))
pari('K=bnfinit(y^2-2,1); if(!bnfcertify(K),error("base field certification failed"))')
pari('d=Mod(y,y^2-2); c=2-2*d; ee=[0,6+6*d,0,6,c^2]; E=ellinit(ee,K); P=[0,c]')
pari('default_ell(0,5,50,5,20,0)')
pari('setrand(1)')
data = pari('bnfellrank(K,ee,[P])')
assert [int(data[i]) for i in range(2)] == [1,1]
assert pari('ellmul(E,P,2)==[3/4-3*d/2,(7*d-43)/8]')
print('rank and 2-Selmer dimension', data)
