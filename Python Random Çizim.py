import turtle
import random
screen=turtle.Screen()
screen.bgcolor("blue")
screen.title("Python Turtle")
turtle_instance=turtle.Turtle()
turtle_instance.left(36)
turtle_instance.speed(0)
while True:
    x = random.randint(1, 2)
    turtle_instance.forward(random.randint(1,25))
    if x==1:
        turtle_instance.right(random.randint(0,180))
    elif x==2:
        turtle_instance.left(random.randint(0, 180))