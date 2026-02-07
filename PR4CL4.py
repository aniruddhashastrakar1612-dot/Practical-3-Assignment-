import numpy as np

a1 = np.array([0, 10, 20, 40, 60, 80])
a2 = np.array([10, 30, 40, 50, 70, 90])

result = np.setdiff1d(a1, a2)

print("Set difference:", result)
