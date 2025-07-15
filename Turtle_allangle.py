from turtle import Turtle, Screen
import turtle

def new_func():
    timmy_the_turtle = Turtle()
    timmy_the_turtle.shape("turtle")
    timmy_the_turtle.color("red")
    timmy_the_turtle.forward(100)  # Red turtle draws a line

new_func()

# Blue square
square = turtle.Turtle()
square.color("blue")
for _ in range(4):
    square.forward(100)
    square.right(90)

# Green triangle
triangle = turtle.Turtle()
triangle.color("green")
triangle.penup()
triangle.goto(150, 0)   
triangle.pendown()
for _ in range(3):
    triangle.forward(100)
    triangle.right(120)

turtle.done()

