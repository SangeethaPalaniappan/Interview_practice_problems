# Backtracking

def backtrack(arr, i, n):
    if i == n:
        for i in arr:
            print(i, end = "")
        print("\n")
        return 
    arr[i] = 1
    backtrack(arr, i + 1, n)
    arr[i] = 2
    backtrack(arr, i + 1, n)
    arr[i] = 3
    backtrack(arr, i + 1, n)
    arr[i] = 4
    backtrack(arr, i + 1, n)


backtrack([0,0], 0, 2)


'''# Backtracking

def backtrack(arr, i, n):
    if i == n:
        for j in arr:
            print(j, end = "")
        print("\n")
        return
    for k in range(n):
        arr[k] = k
        backtrack(arr, i + 1, n)



backtrack([0,0], 0, 2)
'''