#python project exibition game - maze
import turtle
wn = turtle.Screen()
wn.bgcolour("black")
wn.title("Maze Game") 
wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.colour("yellow")
        self.penup()
        self.speed()
#speed doesnt mean object speed, it means animation ki speed

levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXX",
"XX   XXXXXXXXXXXXXXX",
"XX   XXXXXX    XX  X",
"XX       XX        X",
"XXXXXX   XXXX   X  X",
"XX  XX   XXXX   XXXX",
"XX              XXXX",
"XXXXXXXXX    XXXX  X",
"XXX   XXX    XXXX  X",
"XXX   XXX    XXXX  X",
"XXX          XXXX  X",
"XXXXXXXXX          X",
"XXXX           XXXXX",
"XXXX    XXXXXXXXXXXX",
"XXXX    XXXX   XX  X",
"XX             XX  X",
"XXXXXXXXXXXX       X",
"XXXXXX           XXX",
"XX       XX    XXXXX",
"XXXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character =="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()

pen = Pen()

setup_maze(levels[1])

#main game loop
while True:
    pass
