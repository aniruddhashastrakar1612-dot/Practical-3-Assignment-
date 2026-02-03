import numpy as np

# generate two 3x3 matrices with random numbers (1 to 9)
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

# matrix addition
add = A + B
print("Addition of matrices:")
print(add)

# matrix multiplication
mul = A @ B
print("Multiplication of matrices:")
print(mul)
