import turtle
import random

screen = turtle.Screen() #배경
screen.bgcolor('lightgreen')
screen.tracer(2)

limit = turtle.Turtle() #울타리
limit.penup()
limit.setposition(-300, 300)
limit.pendown()
limit.pensize(3)
limit.speed(50)

for i in range(4):
    limit.forward(600)
    limit.right(90)

limit.hideturtle()

p = turtle.Turtle() #거북이
p.shape('turtle')
p.turtlesize(2, 2)
p.color('blue')
p.penup()
speed = 1

bugs_num = 20 #벌레들(먹이들)
bugs = []
colors = ['red', 'blue', 'green', 'white', 'black']
shapes = ['circle', 'classic', 'triangle']

for i in range(bugs_num):
    c = random.randint(0, 4)
    s = random.randint(0, 2)
    rx = random.randint(-300, 300)
    ry = random.randint(-300, 300)
    ra = random.randint(0, 360)
    bugs.append(turtle.Turtle())
    bugs[i].color(colors[c])
    bugs[i].shape(shapes[s])
    bugs[i].penup()
    bugs[i].speed(0)
    bugs[i].setposition(rx, ry)
    bugs[i].right(ra)

def turnleft(): #키 입력받아 거북이가 움직이기 위한 함수
    p.left(30)
 
def turnright():
    p.right(30)
   
def speedup():
    global speed
    speed += 1

def speeddown():
    global speed
    speed -= 1

screen.listen() #키 입력 받기
screen.onkey(turnleft, 'Left')
screen.onkey(turnright, 'Right')
screen.onkey(speedup, 'Up')
screen.onkey(speeddown, 'Down')

while True:
    p.forward(speed) #거북이 항시 이동하는 것
    if p.xcor() > 300 or p.xcor() < -300: #울타리 실현
        p.right(180)
    if p.ycor() > 300 or p.ycor() < -300:
        p.right(180)

    for i in range(bugs_num):
        bugs[i].forward(5) #벌레 항시 이동하는 것
        if bugs[i].xcor() > 300 or bugs[i].xcor() < -300: #울타리 실현
            bugs[i].right(180)
        if bugs[i].ycor() > 300 or bugs[i].ycor() < -300:
            bugs[i].right(180)

screen.mainloop()