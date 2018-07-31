m = int(input("Enter rows of 1st matrix"))
n = int(input("Enter columns of 1st matrix"))
mat1 = []
for i in range(m):
    l = []
    for j in range(n):
        l.append(int(input()))
    mat1.append(l)
print(mat1)
p = int(input("Enter rows of 2nd matrix"))
q = int(input("Enter columns of 2nd matrix"))
mat2 = []
for i in range(p):
    l = []
    for j in range(q):
        l.append(int(input()))
    mat2.append(l)
print(mat2)
result = []
for i in range(m):
    l = []
    for j in range(q):
        l.append(0)
    result.append(l)
print(result)

for i in range(m):
    for j in range(q):
        for k in range(n):
            result[i][j] += mat1[i][k]*mat2[k][j]
print(result)            
