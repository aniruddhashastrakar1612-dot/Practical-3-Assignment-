start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

while start <= end:
    if start > 1:
        count = 0
        for i in range(1, start + 1):
            if start % i == 0:
                count += 1
        if count == 2:
            print(start)
    start += 1
