a=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(a)):
    for j in range(len(a[0])):

        if i <j:
            a[i][j],a[j][i]=a[j][i],a[i][j]
print(a)


# matrix add,sub, mul using numpy

# import numpy as np

# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.array([[9,8,7],[6,5,4],[3,2,1]])

# print(a+b)
# print(a-b)
# print(np.matmul(a,b))
