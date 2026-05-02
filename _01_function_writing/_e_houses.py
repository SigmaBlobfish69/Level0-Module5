"""
Have the turtle draw a row of houses.
"""
import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

def draw_pointy_roof(width):
    t.begin_fill()
    t.left(45)
    t.forward(width * 0.707)
    t.right(90)
    t.forward(width * 0.707)
    t.right(135)
    t.forward(width)
    t.end_fill()
    t.setheading(0)

def draw_flat_roof(width):
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(10)
    t.end_fill()
    t.setheading(0)

def draw_house(size_str):
    if size_str == "small":
        height = 60
    elif size_str == "medium":
        height = 120
    elif size_str == "large":
        height = 250
    else:
        height = 100

    width = 60

    t.pendown()
    t.color("black", "lightgrey")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(height)
    t.right(90)

    t.color("black", "brown")
    t.pendown()
    if size_str == "large":
        draw_flat_roof(width)
    else:
        draw_pointy_roof(width)

    t.penup()
    t.setheading(270)
    t.forward(height)
    t.setheading(0)
    t.forward(width)

    t.color("green")
    t.pensize(5)
    t.pendown()
    t.forward(30)
    t.penup()
    t.pensize(1)
    t.color("black")
    t.forward(10)

t.penup()
t.goto(-350, -200)

sizes = ["small", "medium", "large"]
for _ in range(9):
    random_size = random.choice(sizes)
    draw_house(random_size)

screen.exitonclick()
