"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD":"Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS":"Tasmania",
    "SA":"South Australia"
}
print(CODE_TO_NAME)

#显示字典
for code, name in CODE_TO_NAME.items():#.items()吧key, value分开。key=code, value=name
    print(f"{code:3} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    # if state_code in CODE_TO_NAME: #LBYL（Look Before You Leap）# → 先检查再做
    try:#EAFP（Easier to Ask Forgiveness than Permission）→ 直接做，错了再处理（Python推荐）
        print(state_code, "is", CODE_TO_NAME[state_code])
    # else:
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()