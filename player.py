from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.reset_position()
        self.setheading(90)
        self.finish_line_y = FINISH_LINE_Y

    def go_up(self):
        """ This function is responsible for managing the upward movement of the player """
        return self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """ This function is responsible for set the starting position and to restoring the position of the player every time he hits the top edge of the screen """ 
        self.goto(STARTING_POSITION)