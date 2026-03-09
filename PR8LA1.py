# Program to read a text file and write its content in uppercase

# open source file in read mode
source = open("input.txt", "r")

# read content of file
data = source.read()

# convert content to uppercase
upper_data = data.upper()

# open new file in write mode
destination = open("output.txt", "w")

# write uppercase data to new file
destination.write(upper_data)

# close files
source.close()
destination.close()

# display contents
print("Original File Content:")
print(data)

print("\nUppercase File Content:")
print(upper_data)