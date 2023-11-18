string = "abcdefghijklmnopqrs"

end = len(string) - 1

for i in range(len(string)):
    for j in range(len(string)):
        if j == i :
            print(string[j], end = " ")
            if end == j:
                end -= 1
        elif j == end:
            print(string[end], end = " ")
            end -= 1
        else:
            print(" ", end = " ")
    print("\n")        
            
            