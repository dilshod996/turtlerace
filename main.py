from turtle import Turtle, Screen

belly = Turtle()
screen = Screen()
belly.speed("fastest")

def move_forward():
    belly.forward(20)


def turn_left():
    belly.left(20)


def turn_right():
    belly.right(20)


def backwards_key():
    belly.back(20)


def  clear_pass():
    belly.clear()
    belly.penup()
    belly.home()
    belly.pendown()



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=backwards_key)
screen.onkey(key="c", fun=clear_pass)
screen.exitonclick()