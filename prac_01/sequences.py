# 1. Show the even numbers from x to y
# 2. Show the odd numbers from x to y
# 3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
# 4. Exit the program

MENU = "\n1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)\n4. Exit the program"

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
if x > y:
    x, y = y, x

choice = 0
while choice != 4:
    print(MENU)
    choice = int(input("Enter choice:"))
    if choice == 1:
        for i in range(x , y+1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    elif choice == 2:
        for i in range(x , y+1):
            if i % 2 != 0:
                print(i, end=" ")
        print()
    elif choice == 3:
        for i in range(x , y+1):
            print(i ** 2, end=" ")
        print()
print("bye")




