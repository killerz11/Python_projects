from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 20, 'normal')
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score_data:
            self.highscore = int(score_data.read())
        self.color("White")
        self.penup()
        self.goto(0, 273)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE : {self.score}  High score : {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as score_data:
                score_data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Baby! it's game over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()