from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 0
        self.goto(-220, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """ This function updates the scoreboard entry but without cleaning the previous value, see increase_level() for the full scoreboard update function. """
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ Make the words game over appear when the user loses """
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """ Updating the user's level he hits the top edge of the screen """
        self.level += 1
        self.clear()
        self.update_scoreboard()