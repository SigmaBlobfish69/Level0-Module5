"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':

    for i in range(101, 0, -1):
        print(i)

    for i in range(0, 101, 2):
        print(i)

    for i in range(1, 99, 2):
        print(i)

    for i in range(1, 501, 1):
        if i % 2 == 1:
            print(str(i) + " is odd")
        if i % 2 == 0:
            print(str(i) + " is even")
    for i in range(0, 778, 7):
        print(i)
    birth_year = 2012
    current_year = 2026

    for year in range(birth_year, current_year + 1):
        print("In " + str(year) + ", I was " + str(year-birth_year) + " years old.")

    for i in range(3):
        for n in range(3):
            print(str(i) + " " + str(n))

    for i in range(1, 10):
       for i in range():
           print(i, end=)
