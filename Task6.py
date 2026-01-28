# Upper part (1 to 5 stars)
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower part (4 to 1 stars)
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
