from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Paddle()
screen.update()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")


screen.exitonclick()