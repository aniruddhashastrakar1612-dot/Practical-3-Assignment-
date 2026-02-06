n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

max_diff = 0
min_diff = abs(arr[0] - arr[1])

for i in range(n):
    for j in range(i+1, n):
        diff = abs(arr[i] - arr[j])
        if diff > max_diff:
            max_diff = diff
        if diff < min_diff:
            min_diff = diff

print("Maximum difference:", max_diff)
print("Minimum difference:", min_diff)
