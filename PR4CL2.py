votes = [0, 0, 0, 0, 0]
spoil = 0

for i in range(5):
    n = int(input("Enter vote (1 to 5): "))
    if 1 <= n <= 5:
        votes[n-1] = votes[n-1] + 1
    else:
        spoil = spoil + 1

print("Votes of candidates:", votes)
print("Spoilt ballots:", spoil)
