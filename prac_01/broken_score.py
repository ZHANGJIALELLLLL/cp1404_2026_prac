"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("excellent")
elif score >= 50:
    print("pass")
else:
    print("bad")
