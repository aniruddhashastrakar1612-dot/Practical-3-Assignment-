# Lab Assignment 2
# Prices of sold items stored in a Tuple

prices = tuple(map(int, input("Enter prices of sold items separated by space: ").split()))

# a) Total number of items sold
print("Total number of items sold:", len(prices))

# b) Cheapest item price
print("Cheapest item price:", min(prices))

# c) Costliest item price
max_price = max(prices)
print("Costliest item price:", max_price)

# d) Prices in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
print("Number of costliest items sold:", prices.count(max_price))
