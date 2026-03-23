import pandas as pd

# Read CSV file
# noinspection PyArgumentList
df = pd.read_csv("books.csv")

# a) Print complete report
print("Complete Book Report:\n")
print(df)

# b) Books by a given author
author_name = "John Smith"
print("\nBooks by Author:", author_name)
print(df[df['author'] == author_name])

# c) Books by a given publisher
publisher_name = "XYZ"
print("\nBooks by Publisher:", publisher_name)
print(df[df['publisher'] == publisher_name])

# d) Cheapest and costliest book
cheapest = df.loc[df['price'].idxmin()]
costliest = df.loc[df['price'].idxmax()]

print("\nCheapest Book:")
print(cheapest['title'])

print("\nCostliest Book:")
print(costliest['title'])

# e) Sort by year
print("\nBooks Sorted by Year:")
print(df.sort_values(by='year'))