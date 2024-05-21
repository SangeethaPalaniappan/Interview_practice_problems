# Gap Sum

arr = [1,2,3,4,5,6,7,8,9]
sum_1 = 0
sum_2 = 0
sum_3 = 0
i, j, k = 0, 1, 2
while k < len(arr):
    sum_1 += arr[i]
    sum_2 += arr[j]
    sum_3 += arr[k]
    i += 3
    j += 3
    k += 3
print(sum_1, sum_2, sum_3)    