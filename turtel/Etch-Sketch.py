from turtle import Turtle,Screen
jkl=Turtle()

screen=Screen()

def move_forward():
    jkl.forward(15)

def move_backward():
        jkl.backward(15)

def move_right():
        jkl.right(15)

def move_left():
        jkl.left(15)


def clear():
        jkl.clear()
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_right,"a")
screen.onkey(move_left,"d")
screen.onkey(clear,"c")
screen.exitonclick()