from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a user bet", prompt="Which turtle gonna win the race? Enter turtle name: ")
color_of_turtle = ["green", "blue", "black", "red", "yellow", "purple"]
y_postion = [-150, -100, -50, 0, 50, 100]


# def pick_color(number):
#     each_color = ""
#     index = -1
#     for color in color_of_turtle:
#         each_color = color_of_turtle[index + number]
#     return each_color
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_postion[turtle_index])
    new_turtle.color(color_of_turtle[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win the game! The {winning_color} is winner")
            else:
                print(f"You lost! The {winning_color} is winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)







screen.listen()
screen.exitonclick()