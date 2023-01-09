import turtle

ALLIGN = 'center'
FONT = ("Courier", 30, "normal")
class State(turtle.Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.x = x
        self.y = y
        self.hideturtle()
        self.speed(10)
        self.color('black')
        self.penup()
        self.setpos(self.x, self.y)
        self.state = state
        self.write(self.state, False, ALLIGN)

    def victory():
        victory = turtle.Turtle()
        victory.hideturtle()
        victory.speed(10)
        victory.color('black')
        victory.penup()
        victory.setpos(0, 0)
        victory.write('Congratulations, You won!', False, ALLIGN, FONT)


