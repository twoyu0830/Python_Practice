import threading
import time
from multiprocessing import Process
import pygame
import turtle
from random import randint

screen = turtle.Screen()

pygame.mixer.init()
screen.title("circulo_ritmo")

player  =  turtle.Turtle ()
player.color ( "black" )
player.shape ( "circle" )
player.pensize(3)

a  =  turtle.Turtle () #레일 그리는 객체
a.color ( "black" )
a.speed ( 0 )
a.pensize(5)

b1  =  turtle.Turtle () #장애물 객체
b1.color ( "red" )
b1.shape ( "triangle" )  # 정 오른쪽
b1.up ()
b1.speed ( 0 )
b1.pensize(5)

b2  =  turtle.Turtle ()  #정 위쪽
b2.color ( "red" )
b2.shape ( "triangle" )
b2.up ()
b2.speed ( 0 )
b2.pensize(5)
b2.ht()

b3  =  turtle.Turtle () #정 아래쪽
b3.color ( "red" )
b3.shape ( "triangle" )
b3.up ()
b3.speed ( 0 )
b3.pensize(5)
b3.ht()

b4  =  turtle.Turtle ()    # 정 왼쪽
b4.color ( "red" )
b4.shape ( "triangle" )
b4.up ()
b4.speed ( 0 )
b4.pensize(5)
b4.ht()

a.up()
a.goto(-290, 0)
a.down()
a.speed(0)
a.left(270)
a.circle(290)
a.ht()
player.down()
player.goto(-290, 0)
player.left(270)

player.circle( 290 , 140 )

b1.goto(300,0)
b1.setheading(90)

px = int(player.xcor())
py = int(player.ycor())

b1x = int(b1.xcor())
b1y = int(b1.ycor())

print(px,py)
print(b1x,b1y)

input()