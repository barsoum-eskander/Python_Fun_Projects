from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)


game_on = True
while game_on:
    ball.move()
    screen.update()
    # detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # detect collision with the right paddle
    elif 340 >= ball.xcor() >= 330 and ball.distance(r_paddle) <= 61:
        ball.bounce_x()
        ball.setposition(329, ball.ycor())
    elif ball.xcor() > 340 and ball.distance(r_paddle) <= 61:
        ball.bounce_y()
    # detect collision with the left paddle
    elif ball.xcor() <= -330 and ball.distance(l_paddle) <= 61:
        ball.bounce_x()
    # detect a goal for the right paddle or the right player
    elif ball.xcor() < -400:
        score.r_score += 1
        score.display_score()
        ball.reset_position()
    elif ball.xcor() > 400:
        score.l_score += 1
        score.display_score()
        ball.reset_position()

screen.exitonclick()
