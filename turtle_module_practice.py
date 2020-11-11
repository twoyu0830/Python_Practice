import turtle

screen = turtle.Screen()
screen.bgcolor('lightgreen')

p = turtle.Turtle()
p.shape('turtle')
p.turtlesize(2, 2)
p.color('blue')
speed = 1

def turnleft():
    p.left(30)

def turnright():
    p.right(30)

def speedup():
    global speed
    speed += 1

def speeddown():
    global speed
    speed -= 1

screen.listen()
screen.onkey(turnleft, 'Left')
screen.onkey(turnright, 'Right')
screen.onkey(speedup, 'Up')
screen.onkey(speeddown, 'Down')

while True:
    p.forward(speed)

screen.mainloop()