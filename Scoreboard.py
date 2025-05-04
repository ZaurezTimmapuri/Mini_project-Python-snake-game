from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.highscore = 0
        self.score = 0
        self.value = 0
        self.read_score()
        self.write(f"  Score:  {self.score}  Highscore :    {self.value} ", align="center",
                   font=('Courier', 24, 'bold'))

    def read_score(self):
        with open("Highscore.txt", "r") as file:
            self.value = file.read()

    def update_score(self):
        self.clear()
        self.read_score()
        self.write(f"  Score:  {self.score}   Highscore :  {self.value} ", align="center",
                   font=('Courier', 24, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("Highscore.txt","w") as file:
            file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def gameover(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"  Game Over ", align="center", font=('Courier', 20, 'bold'))
