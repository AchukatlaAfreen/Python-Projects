from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("🐢 Turtle Race with Betting")
screen.setup(width=700, height=400)
screen.bgcolor("lightyellow")


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-90, -60, -30, 0, 30, 60]
all_turtles = []


finish_line_x = 300
line_drawer = Turtle()
line_drawer.hideturtle()
line_drawer.penup()
line_drawer.goto(finish_line_x, -120)
line_drawer.setheading(90)
line_drawer.pensize(3)
line_drawer.pendown()
line_drawer.forward(250)

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-300, y=y_positions[i])
    all_turtles.append(new_turtle)


is_race_on = False
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > finish_line_x:
            is_race_on = False
            winning_color = turtle.pencolor()

            
            result = Turtle()
            result.hideturtle()
            result.penup()
            result.goto(0, 130)
            if winning_color.lower() == user_bet.lower():
                result.write(f"🎉 You WON! The {winning_color} turtle is the winner!",
                             align="center", font=("Arial", 16, "bold"))
            else:
                result.write(f"😢 You LOST! The {winning_color} turtle won the race!",
                             align="center", font=("Arial", 16, "bold"))
            break


screen.exitonclick()


