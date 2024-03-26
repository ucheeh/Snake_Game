from turtle import Turtle

ALIGN = "center"
FONT = ("Times New Roman", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.ht()
        self.score = 0
        with open('data.txt') as file:
            self.h_score = int(file.read())
        self.update_scoreboard()
        self.reset()

    def update_scoreboard(self):
        self.goto(0, 280)
        self.write(f"Score: {self.score} High Score: {self.h_score}", True, align= ALIGN, font= FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.goto(0, 280)
        self.update_scoreboard()

    def reset(self):
        if self.score > self.h_score:
            self.h_score = self.score
        self.score = 0
        with open('data.txt', 'w') as file:
            file.write(str(self.h_score))
        self.clear()
        self.update_scoreboard()

