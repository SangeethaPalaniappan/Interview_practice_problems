# Convert the count into string

input = "s1a1n1g1e2t1h1a1"
output = ""
i = 1
j = 0
while i < len(input) - 1:
    if ord(input[i + 1]) >= 48 and ord(input[i + 1]) <= 57:
        output += (input[j] * int(input[i] + input[i + 1]))
        i += 3
        
    elif ord(input[i]) >= 48 and ord(input[i]) <= 57:    
        output += (input[j] * int(input[i]))
        i += 2
    j = i - 1
output += (input[len(input) - 2] * int(input[len(input) - 1]))        
print(output)        