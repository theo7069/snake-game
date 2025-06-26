from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
x = True
screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

def start_game():
    global snake, food, scoreboard, game_is_on  # Initialize game objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail.
        for segment in snake.segments:
            if segment != snake.head and snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                x = scoreboard.play_again()

    # After game over, ask to play again
if x:
    start_game()
# Exit the game


# Set up the screen

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Start the game for the first time
start_game()