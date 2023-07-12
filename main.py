from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneaky snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game=True

while game:
    screen.update()

    time.sleep(0.17)
    snake.move()
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:

        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:

            scoreboard.reset()
            snake.reset()
#print("nom nom")

#moving snale
#second segment
# snake_sq2=Turtle()
# snake_sq2.shape("square")
# snake_sq2.color("coral")
# snake_sq2.goto(-20,0)
#
# #third segment
# snake_sq3=Turtle()
# snake_sq3.shape("square")
# snake_sq3.color("coral")
# snake_sq3.goto(-40,0)
screen.exitonclick()


