x = [[2,4,5],
     [4,5,6],
     [7,8,9]]
y = [[4,3,2],
     [9,7,5],
     [4,5,6]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
          
for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] += x[i][j]*y[i][j]

for r in result:
    print(r)
