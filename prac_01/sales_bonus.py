"""
<priming read - do something the loop will depend on, e.g., get/calculate a number>
while <condition based on something from above>
    <body of the loop - do the thing you want to repeat>
    <same as the priming read again>
<do next thing now that the loop is finished (condition was false)>

# SECRET = 6
# guess = int(input("? "))
# while guess != SECRET:
#     print("Guess again!")
#     guess = int(input("? "))
# print("You got it!")
"""

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

sales = float(input("Enter sales（enter'-1'stop: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * 0.15
    else:
        bonus = sales * 0.10
    print(f"Your bonus is ${bonus:.2f}")#:.2f小数点后两位

    sales = float(input("Enter sales: $"))