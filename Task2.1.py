n = 5

i = 1
while i <= n:
    j = 1
    while j <= i:
        if j % 2 == 1:
            print("*", end=" ")
        else:
            print("#", end=" ")
        j = j + 1
    print()
    i = i + 1
