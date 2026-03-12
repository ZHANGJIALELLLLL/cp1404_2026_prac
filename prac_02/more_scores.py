"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random
def main():
    # score = float(input("Enter score:"))
    # result = score_result(score)
    # print(f"User score {score} is {result}.")
    #
    # if result == "Excellent":
    #     print("You get a prize!")
    #
    # random_score = random.randint(1,100)
    # random_result = score_result(random_score)
    # print(f"Random: {random_score} = {random_result}")
    number_score = int(input("How many scores to generate?"))
    with open("result.txt", "w") as file:
        for i in range(number_score):
            score = random.randint(1, 100)
            result = score_result(score)
            file.write(f"{score} is {result}\n")
    print("Done")

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