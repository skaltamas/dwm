import numpy as np

n=int(input("Enter the no of pages: "))
d=0.85
eps=1.0e-8
mat = []
print("Enter the adjacency matrix: ")
print("Type 1 if link exist from i to j else type 0")
for i in range (0,n):
    L=[]
    for j in range (0,n):
        L.append(int(input('Page'+str(i+1)+' to Page'+str(j+1)+': ')))
    mat.append(L)

D=(1-d)/n
C=np.ones((n,1),dtype=int)
C=np.matrix(C)

outboundL=np.zeros((n,),dtype=int)
for i in range (0,n):
    for j in range (0,n):
        if mat[i][j]==1:
            outboundL[i]=outboundL[i]+1

M=np.zeros((n,n))
for i in range (0,n):
    for j in range (0,n):
        if mat[j][i]==1:
            M[i][j]=1/outboundL[j]

M=np.matrix(M)

rank=np.matrix(np.full((n,1),1/n))

while True:
    ranknext=d*np.dot(M,rank)+ D*C
    diff = np.subtract(ranknext,rank)
    if np.linalg.norm(diff) < eps:
        break
    rank=ranknext

    
