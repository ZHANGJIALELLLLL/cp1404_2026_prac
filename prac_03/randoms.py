import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
I saw the random integers between 5 to 20
What was the smallest number you could have seen, what was the largest?
smallest number: 5 ; largest number: 20

What did you see on line 2?
I saw the random numbers like 3,5,7,9
What was the smallest number you could have seen, what was the largest?
smallest number: 3 ; largest number: 9
Could line 2 have produced a 4?
no, because step is 2, start is 3, so only odd numbers

What did you see on line 3?
floating numbers between 2.5 to 5.5
What was the smallest number you could have seen, what was the largest?
smallest number: 2.5 ; largest number: 5.5

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
print(random.randint(1, 100))
