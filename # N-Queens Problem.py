# N-Queens Problem

def nqueen(mat, i, n):
    if i == n:
        print("Possibility")
        for arr in mat:
            for k in arr:
                if k == 1:
                    print("Q", end = " ")
                else:
                    print("_", end = " ")    
            print("\n")
        return    

    for j in range(n):
        if check(mat, i, j, n) == 1:    
            mat[i][j] = 1            
            nqueen(mat, i + 1, n)
            mat[i][j] = 0

def check(mat, row, column, n):
    prev_row = row - 1
    prev_column = column
    while prev_row >= 0:
        if mat[prev_row][prev_column] == 1:
            return 0
        prev_row -= 1

    prev_row = row - 1    
    prev_column = column - 1
    while prev_row >= 0 and prev_column >= 0:
        if mat[prev_row][prev_column] == 1:
            return 0
        prev_row -= 1
        prev_column -= 1    

    prev_row = row - 1
    prev_column = column + 1  
    while prev_row >= 0 and prev_column < n:
        if mat[prev_row][prev_column] == 1:
            return 0
        prev_row -= 1
        prev_column += 1          

    return 1

mat = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]    
nqueen(mat, 0, 4)
                

