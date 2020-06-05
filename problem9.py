import numpy as np
import time

A=np.array([[2, 1], [1, 0], [0, 1]])
B=np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])

ev1_a,U_a=np.linalg.eigh(np.dot(A,np.transpose(A)))
sev_1_a=ev1_a.argsort()[::-1]
U_a=U_a[:,sev_1_a]

ev2_a,V_a=np.linalg.eigh(np.dot(np.transpose(A),A))
sev_2_a=ev2_a.argsort()[::-1]
V_a=V_a[:,sev_2_a]

S_a=np.dot(np.dot(np.transpose(U_a),A),V_a)
print("UA:\n",U_a,"\n SA:\n",S_a,"\n VA:\n",V_a)

Up_a,Sp_a,Vp_a=np.linalg.svd(A)

print("SVD form of A using np.linalg.svd: \n")
print(Up_a)
print(Sp_a)
print(Vp_a)

ev1_b,U_b=np.linalg.eigh(np.dot(B,np.transpose(B)))
sev_1_b=ev1_b.argsort()[::-1]
U_b=U_b[:,sev_1_b]

ev2_b,V_b=np.linalg.eigh(np.dot(np.transpose(B),B))
sev_2_b=ev2_b.argsort()[::-1]
V_b=V_b[:,sev_2_b]

S_b=np.dot(np.dot(np.transpose(U_b),B),V_b)
print("UB:\n",U_b,"\n SB:\n",S_b,"\n VB:\n",V_b)

Up_b,Sp_b,Vp_b=np.linalg.svd(B)

print("SVD form of B using np.linalg.svd: \n")
print(Up_b)
print(Sp_b)
print(Vp_b)
