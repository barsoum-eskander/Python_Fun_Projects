from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # Main Point: The Tracer Method Makes The Program Updates Invisible From The User
# And In That Time We Can Do Something With The Turtle Or The Screen!

snake = Snake()
scoreboard = ScoreBoard()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_on = True
x = 0.1
while game_on:
    scoreboard.write_score()
    screen.update()
    '''And After Using The turtle.tracer()
    And Doing Something With The Turtle And Screen
    Or Anything Else We Can Go 
    And Actually Use The turtle.update() Method
    To Show The New Result To The User!. '''
    time.sleep(x)  # delays the execution of the python code for x num of secs
    scoreboard.high_score()
    snake.move()
    # detect collision with food
    if snake.turtles[0].distance(food) < 17:
        scoreboard.calculate_score()
        food.refresh()
        snake.extend_snake()
        x -= 0.001  # this to make the snake faster each time it eats

    # detect collision with wall

    if snake.turtles[0].xcor() > 298 or snake.turtles[0].xcor() < -298 \
            or snake.turtles[0].ycor() > 299 or snake.turtles[0].ycor() < -298:
        game_on = False
        scoreboard.game_over()

    # detect collision with tail
    # for snake_part in snake.turtles:
    #     if snake_part == snake.turtles[0]:
    #         pass
    #     elif snake.turtles[0].distance(snake_part) < 10:
    #         game_on = False
    #         scoreboard.game_over()
    for snake_part in snake.turtles[1:]:
        if snake.turtles[0].distance(snake_part) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
