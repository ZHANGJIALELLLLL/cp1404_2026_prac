"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")
#
def main():
    score = float(input("Enter score:"))
    result = score_result(score)
    print(f"User score {score} is {result}.")

    if result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(1,100)
    random_result = score_result(random_score)
    print(f"Random: {random_score} = {random_result}")

def score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()