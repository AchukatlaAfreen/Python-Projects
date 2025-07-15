from turtle import Turtle, Screen
def new_func():
    timmy_the_turtle = Turtle()
    timmy_the_turtle.shape("turtle")
    timmy_the_turtle.color("red")
new_func()

import turtle
dash_turtle = turtle.Turtle() 
dash_turtle.speed(1)
for _ in range(10):
    dash_turtle.forward(10)
    dash_turtle.penup()
    dash_turtle.forward(10)
    dash_turtle.pendown()

turtle.done()