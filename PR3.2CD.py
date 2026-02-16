# write your code here
n = int(input("Enter a positive integer: "))

if (n < 1):
    print("Please enter a number greater than 0")
else:
    s = 0
    for i in range(1, n + 1):
        s = s + i
    print("The sum of numbers from 1 to", n, "is:", s)
