from z3 import *

opt = Optimize()
s = BitVec('s', 64)
a, b, c = s, 0, 0
for x in [2,4, 1,6, 7,5, 4,4, 1,7, 0,3, 5,5, 3,0]:
    b = a & 7
    b = b ^ 6
    c = a >> b
    b = b ^ 7
    b = b ^ c
    a = a >> 3
    opt.add((b & 7) == x)
opt.add(a == 0)
opt.minimize(s)
assert str(opt.check()) == 'sat'
print(opt.model().eval(s))