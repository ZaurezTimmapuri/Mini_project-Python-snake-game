from turtle import Turtle
import random

class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("Red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.x = 0
        self.y = 0
        self.refresh_location()

    def refresh_location(self):
        self.x = random.randint(-240,240)
        self.y = random.randint(-240,240)
        self.goto(self.x,self.y)