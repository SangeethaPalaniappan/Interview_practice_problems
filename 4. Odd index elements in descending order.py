# Odd index elements in descending order

arr = [13,2,4,15,12,10,5]
arr_1 = []
arr_2 = []
for i in range(0, len(arr), 2):
    arr_1.append(arr[i])
 
arr_1.sort(reverse = True) 

print(arr_1)
for k in range(1, len(arr), 2):
    arr_2.append(arr[k])
k = 0
print(arr_2)
for j in range(0, len(arr), 2):
    arr[j] = arr_1[k]
    k += 1
print(arr)    