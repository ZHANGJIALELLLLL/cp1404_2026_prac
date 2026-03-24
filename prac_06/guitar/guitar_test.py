from prac_06.guitar.guitar import Guitar

CURRENT_YEAR = 2017

def run_test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {95}. Got {guitar.get_age()}")
    print(f"My guitar: {name}, first made in {year}")
run_test()