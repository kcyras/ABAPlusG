myAsm(a).
myAsm(b).
myAsm(c).
myAsm(d).
contrary(a, C(a)).
contrary(b, C(b)).
contrary(c, C(c)).
contrary(d, C(d)).
myRule(C(b), [c, d]). 
myRule(C(a), [c, d]).
myRule(C(c), [a, d]).
myRule(C(d), [d]).
myPrefLT(c, a). 