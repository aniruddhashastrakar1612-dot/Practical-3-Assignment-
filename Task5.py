rows = 5

for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end=" ")
    for star in range(2 * i - 1):
        print("*", end=" ")
    print()
