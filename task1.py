#matrix mul using numpy
'''import numpy as np

a=np.identity(3)
b=np.array([[1,2,3],[4,5,6],[7,8,9]])

if a.shape[1]==b.shape[0]:
    result = np.matmul(a,b)
    print(result.astype(int))
else:
    print("matrix multiplication not possible")
'''
#matrix mul using list

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,0,0],[0,1,0],[0,0,1]]

if len(a[0])==len(b):
    result=[[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j]+=a[i][k]*b[k][j]
    print(result)
