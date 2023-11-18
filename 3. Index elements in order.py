# even index elements in ascending order
# odd index elements in descending order
arr = [13,2,4,15,12,10,5]
arr_1 = []
arr_2 = []
for i in range(0, len(arr), 2):
    arr_1.append(arr[i])
arr_1.sort()    


print(arr_1)
for k in range(1, len(arr), 2):
    arr_2.append(arr[k])
arr_2.sort(reverse = True) 
print(arr_2)
k = 0
arr_1.extend(arr_2)
arr = arr_1
print(arr_1)

print(arr)    
    