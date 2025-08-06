import random
from turtle import Turtle,Screen
keshu=Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen", "Tomato", "Goldenrod"]
direction=[0,90,180,270]
keshu.pensize(10)

for _ in range(50):
    keshu.color(random.choice(colors))
    keshu.forward(45)
    keshu.setheading(random.choice(direction))

















screen=Screen()
screen.exitonclick()