import random

with open("temps_input.txt", "w") as file:
    temp = random.uniform(-200,200)
    file.write(f"{temp}\n")

def fahrenheit_to_celsius(f):
    return 5 / 9 * (f - 32)
# print(fahrenheit_to_celsius(32))  # 输出应该是0
# print(fahrenheit_to_celsius(212)) # 输出应该是100

with open("temps_input.txt", "r") as infile, open("temps_output.txt", "w") as outfile:
    for line in infile:
        f = float(line.strip())
        c = fahrenheit_to_celsius(f)
        outfile.write(f"{c}\n")