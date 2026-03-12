# def main():
#     score = float(input("Enter score:"))
#     result = score_result(score)
#     print(f"User score {score} is {result}.")
#
#     if result == "Excellent":
#         print("You get a prize!")
#
#     random_score = random.randint(1,100)
#     random_result = score_result(random_score)
#     print(f"Random: {random_score} = {random_result}")
#
# def score_result(score):
#     if score < 0 or score > 100:
#         return "Invalid score"
#     elif score >= 90:
#         return "Excellent"
#     elif score >= 50:
#         return "Passable"
#     else:
#         return "Bad"
#
# main()

"""
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""
MENU = "\n(G)et a valid score (must be 0-100 inclusive)\n(P)rint result (copy or import your function to determine the result from score.py)\n(S)how stars (this should print as many stars as the score)\n(Q)uit"
def main():
    choice = ""
    while choice != "q":
        print(MENU)
        choice = input(">>> ").lower()
        if choice == "g":
            score = get_score()
        elif choice == "p":
            result = score_result(score)
            print(f"User score {score} is {result}.")
        elif choice == "s":
            show_stars(score)
        elif choice == "q":
            print("Goodbye! Thanks for using the score program.")
        else:
            print("Invalid")



def get_score():
    score = float(input("Enter score(1-100):"))
    while score <0 or score > 100:
        print("Invalid")
        score = float(input("Enter score(1-100):"))
    return score

def score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    for i in range(int(round(score))):
        print("*", end="")
    print()

main()
