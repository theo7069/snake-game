from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear previous score before updating
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()  # Call update_scoreboard directly

    def play_again(self):
        x = self.textinput("", 'Do you want to continue? (Y/N)').lower()
        if x == "y":
            return True
        elif x == "n":
            return False
        else:
            self.clear()  # Clear previous messages
            self.write("Please enter Y or N", align=ALIGNMENT, font=FONT)




