# write the string and its count

input_1 = "sangeetha"
output = ""
count = 1
input = input_1.lower()
sum = 1
for i in range(len(input) - 1):
    if input[i] == input[i + 1]:
        if i == len(input) - 2:
            count += 1
            output += (input[i] + str(count))
            sum = 0
        count += 1
    else:
        output += (input[i] + str(count))
        count = 1
if sum != 0:
    output += (input[len(input) - 1] + str(1))
print(output)        