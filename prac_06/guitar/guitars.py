from prac_06.guitar.guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("cost: $"))

        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add) #把guitar_to_add里的用.append()加入guitars = []列表
        print(guitar_to_add, "added.")#可以直接print(guitar_to_add)的原因是在guitar.py中我写的def __str__(self):内容
        name = input("Name: ")

    #即使没有输入，enter直接回车了，guitars = []里也有数据
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:#guitars = []空输出false
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):#enumerate()，从1开始编号guitars = []里的东西
            vintage_string = ""
            if guitar.is_vintage():#guitar.py里的is_vintage(self): （age >= 50)
                vintage_string = " (vintage)" #"="是赋值
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    # 在字符串前加f
    # {i} → 直接用变量i
    # {guitar.name: > 20} → 直接用guitar.name，右对齐20个字符
    #{guitar.year} → 直接用guitar.year
    #{guitar.cost: 10, .2f} → 直接用guitar.cost
    #{vintage_string} → 直接用变量vintage_string
            # print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    # {0} → 对应i
    # {1.name: > 20} → 对应guitar.name，右对齐20个字符
    # {1.year} → 对应guitar.year
    # {1.cost: 10, .2f} → 对应guitar.cost，10个字符宽，千位分隔符，保留2位小数
    # {2} → 对应vintage_string
    # 老师用.format()是为了兼容性或者教学演示, 你在Python3.6 + 可以直接用f - string，更直观

    #print("Guitar 1:  Fender Stratocaster (2014), worth $    765.40")
    # print(f"Fender Stratocaster (2014) : $765.40 added.")
    else:
        print("No guitars :( Quick, go and buy one!")

main()