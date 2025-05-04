from turtle import Turtle
STARTING_POSTIONS = [(0,0),(0,-20),(0,-40)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
    def create_snake(self):
        for i in STARTING_POSTIONS:
            self.add_trutle(i)
    def add_trutle (self,position) :
        turtle = Turtle("square")
        turtle.color("black")
        turtle.penup()
        turtle.goto(position)
        self.turtle_list.append(turtle)
    def extend (self):
        self.add_trutle(self.turtle_list[-1].position())
    def snake_reset(self):
        for i in range(len(self.turtle_list)):
            self.turtle_list[i].goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
    def move (self):
        for i in range(len(self.turtle_list) - 1, 0, -1):
            x = self.turtle_list[i - 1].xcor()
            y = self.turtle_list[i - 1].ycor()
            self.turtle_list[i].goto(x,y)
        self.turtle_list[0].forward(MOVE)
    def right(self):
        if self.turtle_list[0].heading() != LEFT:
            self.turtle_list[0].setheading(RIGHT)
    def left(self):
        if self.turtle_list[0].heading() != RIGHT:
            self.turtle_list[0].setheading(LEFT)
    def up (self):
        if self.turtle_list[0].heading() != DOWN:
            self.turtle_list[0].setheading(UP)
    def down(self):
        if self.turtle_list[0].heading() != UP:
            self.turtle_list[0].setheading(DOWN)
