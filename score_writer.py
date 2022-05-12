from turtle import Turtle
FONT = ('Arial', 10, 'normal')

class Score_Writer(Turtle):

    def __init__(self) -> None:
        super().__init__()

    def type(self, x: int, y: int, answer: str) -> None:
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(arg=answer, move=False, align='center',
                   font=FONT)
