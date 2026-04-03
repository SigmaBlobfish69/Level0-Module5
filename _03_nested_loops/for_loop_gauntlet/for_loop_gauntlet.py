"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    for i in range(3):
        for j in range(1, 4):
            print(j+3*i, end=" ")
        print( )

    for i in range(10):
        for j in range(1, 11):
            print(j+10*i, end=" ")
        print( )

    for i in range(6):
        for j in range(1*i):
            print("*", end=" ")
        print( )
