COLOR_TO_HEX = {
    "absolute zero":"#0048ba",
    "acid green":"#b0bf1a",
    "aliceblue":"#f0f8ff",
    "alizarin crimson":"#e32636",
    "amber":"#ffbf00",
    "amethyst":"#9966cc",
    "banana yellow":"#ffe135",
    "blue green":"#0d98ba",
    "brilliant rose":"#ff55a3",
    "brink pink":"#fb607f"
}
color_name = input("Enter color name: ").strip().lower()
while color_name != "":
    try:
        print(color_name, "is", COLOR_TO_HEX[color_name])
    except KeyError:
        print("Invalid")
    color_name = input("Enter color name: ").strip().lower()