import numpy as np

# Take space-separated input numbers
nums = list(map(int, input().split()))

# Convert list into 3x3 array
arr = np.array(nums).reshape(3, 3)

# Print the matrix
print(arr)
