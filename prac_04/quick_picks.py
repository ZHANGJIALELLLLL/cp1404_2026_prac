import random

NUMBER_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_lines = int(input("How many quick picks? "))
    for i in range(number_lines):
        line = []
        while len(line) < NUMBER_PER_LINE:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in line:
                line.append(number)
        line.sort()#将这一行数字按升序排列
        print(" ".join(f"{n:2}" for n in line))#[表达式 for 变量 in 列表 if 条件]
main()
