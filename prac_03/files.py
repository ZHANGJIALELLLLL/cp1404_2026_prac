# Write code that asks the user for their name, then opens a file called name.
# txt and writes that name to it. Use open and close for this question.

name = input("Name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# In the same file, but as if it were a separate program, write code that opens "name.txt"
# and reads the name (as above) then prints (note the exact output),
# Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
# Use open and close for this question.

file = open("name.txt", "r")
name = file.read()
file.close()

print(f"Hi, {name}")

# Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens numbers.txt, reads only the first two numbers,
# adds them together then prints the result, which should be... 59.
# Use with instead of open and close for this question.

with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    calculation = number1 + number2
    print(calculation)

# Now write a fourth block of code that prints the total for all lines in numbers.txt.
# This should work for a file with any number of numbers.
# Use with instead of open and close for this question.
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)

print(total)
