# Lab Assignment 1
# Program using Tuple

# Taking input from user
nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(nums))

# b) Last item in the tuple
print("Last item in the tuple:", nums[-1])

# c) Tuple elements in reverse order
print("Tuple in reverse order:", nums[::-1])

# d) Check if integer 5 is present
if 5 in nums:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining items
if len(nums) > 2:
    remaining = nums[1:-1]
    sorted_remaining = tuple(sorted(remaining))
    print("After removing first & last and sorting:", sorted_remaining)
else:
    print("Not enough elements to remove first and last")
