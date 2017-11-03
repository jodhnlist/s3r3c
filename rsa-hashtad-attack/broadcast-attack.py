from Crypto.Util.number import *
from gmpy2 import *
import sys
e = 3 
c1 = int(sys.argv[1])
n1 = int(sys.argv[2])
c2 = int(sys.argv[3])
n2 = int(sys.argv[4])
c3 = int(sys.argv[5])
n3 = int(sys.argv[6])

#Note that: C = pow(M,3,N1*N2*n3)
#Now we're trying to find C = (T1 + T2 + T3) mod (N1*N2*N3)

#T1 = C1*(N2*N3)*invert(N2*N3,N1)
t1 = c1*(n2*n3)*invert(n2*n3,n1)
print "T1 = ",t1

#T2 = C2*(N1*N3)*invert(N1*N3,N2)
t2 = c2*(n1*n3)*invert(n1*n3,n2)
print "T2 = ",t2

#T3 = C3*(N2*N1)*invert(N2*N1,N3)
t3 = c3*(n1*n2)*invert(n1*n2,n3)
print "T3 = ",t3

#Got T1,T2,T3 , Now calculate C 
c = (t1 + t2 + t3) % (n1*n2*n3)
print "C = ",c

#Got C, calculate M
m = str(iroot(c,3)).split('z(')[1].split('L)')[0]
print "M = ",m
print "M in plaintext: ",long_to_bytes(m)
