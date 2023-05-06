from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(800,600)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    #Detect collision with the wall (Top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect ball goes beyond bounds
    if ball.xcor() > 350:
        ball.ball_reset()
        scoreboard.increase_l_score()

    if ball.xcor() < -350:
        ball.ball_reset()
        scoreboard.increase_r_score()


screen.exitonclick()

