# Inner Reducing Pattern

n = 4
m = n * 2 - 1
start = 0
end = m - 1

mat = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]

i = 0
while n > 0:
    for i in range(start, end + 1):
        for j in range(start,end +1):
            if i == start or j == start or i == end or j == end:
                mat[i][j] = n

    n -= 1
    start += 1
    end -= 1
    
for i in mat:    
    for j in i:
        print(j, end = " ")
    print("\n")    
            