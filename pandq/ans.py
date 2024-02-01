import math
import random
import sympy
import numpy as np
from Crypto.Util.number import inverse, long_to_bytes

c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537

# phi = (p-1)*(q-1)
# ed = 1 % phi
# d = e**-1 % phi
# n = pq
# 

p = 475693130177488446807040098678772442581573
q = 1617549722683965197900599011412144490161
ntest = p*q
phi = (p-1)*(q-1)
ed = 1 % phi
d = ed/e
dtest = inverse(e, phi)
print(d)
print(dtest)

print()
# m=pow(c,d,n)
# print(m)
#print_factors(n)