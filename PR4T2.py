import numpy as np

# input for 5x3 matrix
print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = input().split()
    row = [int(x) for x in row]
    A.append(row)

# input for 3x2 matrix
print("Enter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = input().split()
    row = [int(x) for x in row]
    B.append(row)

# convert to numpy arrays
A = np.array(A)
B = np.array(B)

# matrix multiplication
C = A @ B

print("Product Matrix:")
print(C)

