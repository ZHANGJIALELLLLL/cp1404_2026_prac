for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(0, 110, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
stars = int(input("Number of stars:"))
for i in range(stars):
    print('*', end='')
print()
# d. print lines of increasing stars.
# Ask the user for a number of lines, then print lines of increasing stars, starting at 1 with no blank line.
# E.g., if the user entered 4, your single loop should print:
lines = int(input("Enter number of lines:"))
for i in range(1, lines+1):
    print('*' * i)
