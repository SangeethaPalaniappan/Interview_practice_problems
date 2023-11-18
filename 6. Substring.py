# Substring

s1 = "testing1234"
s2 = "1234"
length = len(s2)
i = 0
j = 0
limit = len(s1) - length  
while i < limit + 1:
    if s2 == s1[i : length]:
        print(i)
        j = 1
        break
    i += 1
    length += 1
if j == 0:
    print(-1)    