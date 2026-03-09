# Program to copy python script without comments

# take file names from user
source_file = input("Enter source file name: ")
dest_file = input("Enter destination file name: ")

# open files
source = open(source_file, "r")
destination = open(dest_file, "w")

# read line by line
for line in source:

    # ignore lines starting with #
    if not line.strip().startswith("#"):
        destination.write(line)

# close files
source.close()
destination.close()

# print contents of both files
print("\nContent of Source File:")
source = open(source_file, "r")
print(source.read())

print("\nContent of Destination File (without comments):")
destination = open(dest_file, "r")
print(destination.read())

source.close()
destination.close()