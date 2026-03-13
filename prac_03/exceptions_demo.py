"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
User enter no in integers(floating letters and other things), because int().

2. When will a ZeroDivisionError occur?
If denominator=0 (Denominator(分母). Molecule(分子))

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
use if else or while loop.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # if denominator != 0:
    #     fraction = numerator / denominator
    #     print(fraction)
    # else:
    #     print("Cannot divide by zero!")
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
