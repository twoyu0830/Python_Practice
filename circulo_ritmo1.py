import threading
import time
from multiprocessing import Process
import pygame
import turtle
from random import randint

screen = turtle.Screen()

pygame.mixer.init()
music1 = pygame.mixer.music.load("1스테이지.mp3")
screen.title("circulo_ritmo")

def A(): #게임창 만들기
    a.up()
    a.goto(-750, -380)   #-750, 380    750, 380
    a.down()            #-750, -380   750, -380
    a.forward(1500)
    a.left(90)
    a.forward(760)
    a.left(90)
    a.forward(1500)
    a.left(90)
    a.forward(760)
    a.up()
    player.up()
    player.goto(-300, 0)
    player.left(270)
    a.goto(-290, 0)
    a.down()
    a.speed(0)      #             0, 300
    a.circle(290)   # -300, 0                 300, 0
    a.ht()          #             0, -300


player  =  turtle.Turtle ()
player.color ( "black" )
player.shape ( "circle" )
player.pensize(3)
player.speed(10)

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
b1.ht()

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

screen  =  player.getscreen ()

A()

screen.listen ()



def trun ():       #장애물의 라인 안팎 이동
    a1 =  b1.isvisible()
    a2 =  b2.isvisible()
    a3 =  b3.isvisible()
    a4 =  b4.isvisible()
    if a1 == True:
        screen.delay(0)
        b1.left(180)
        b1.forward(20)
    if a2 == True:
        screen.delay(0)
        b2.left(180)
        b2.forward(20)
    if a3 == True:
        screen.delay(0)
        b3.left(180)
        b3.forward(20)
    if a4 == True:
        screen.delay(0)
        b4.left(180)
        b4.forward(20)

def pattern (): #상하 1번 (2초)
    screen.delay(0)
    b3.setpos(0,-300)
    b2.setpos(0,280)
    b2.setheading(270)
    b3.setheading(270)
    b3.st()
    b2.st()
    threading.Timer(2.6, hide).start()

def  hide (): #좌우 1번 (4.6초)
    screen.delay(0)
    b2.ht()
    b3.ht()
    b2.setpos(0,0)
    b3.setpos(0,0)
    b1.setpos(300,0)
    b4.setpos(-280,0)
    b1.setheading(0)
    b4.setheading(0)
    b1.st()
    b4.st()
    threading.Timer(3.7 , pattern1).start()


def pattern1 ():  #상하 2번 (7.6초)
    screen.delay(0)
    b1.ht()
    b4.ht()
    b1.setpos(0,0)
    b4.setpos(0,0)
    b3.setpos(0,-280)
    b2.setpos(0,300)
    b2.setheading(90)
    b3.setheading(90)
    b2.st()
    b3.st()
    threading.Timer(4.5, pattern2).start()

def pattern2 (): #좌우 2번 (12.6초)
    screen.delay(0)
    b2.ht()
    b3.ht()
    b2.setpos(0,0)
    b3.setpos(0,0)
    b1.setpos(300,0)
    b4.setpos(-280,0)
    b1.setheading(0)
    b4.setheading(0)
    b1.st()
    b4.st()
    threading.Timer(4.6, pattern3).start()

def pattern3 (): #상하 2 번  (18.1초)
    screen.delay(0)
    b1.ht()
    b4.ht()
    b1.setpos(0,0)
    b4.setpos(0,0)
    b3.setpos(0,-300)
    b2.setpos(0,280)
    b2.setheading(270)
    b3.setheading(270)
    b2.st()
    b3.st()
    threading.Timer(6, pattern4).start()

def pattern4 (): #상하좌우 4번 (23.4초)
    screen.delay(0)
    b1.setpos(280,0)
    b4.setpos(-280, 0)
    b3.setpos(0,-300)
    b2.setpos(0,300)
    b1.setheading(180)
    b2.setheading(90)
    b3.setheading(270)
    b4.setheading(0)
    b1.st()
    b2.st()
    b3.st()
    b4.st()
    threading.Timer(11.0, pattern5).start()


def hit ():    #피격 판정
    threading.Timer(2, pattern).start()
    while True:
        screen.delay(3.7)
        player.circle ( 300 , 10 )
        px = int(player.xcor())
        py = int(player.ycor())
        b1x = int(b1.xcor())
        b1y = int(b1.ycor())
        b2x = int(b2.xcor())
        b2y = int(b2.ycor())
        b3x = int(b3.xcor())
        b3y = int(b3.ycor())
        b4x = int(b4.xcor())
        b4y = int(b4.ycor())
        if abs(px - b1x) <= 10 and abs(py - b1y) <= 10 :
            pygame.mixer.music.pause()
            player.goto(-300, 0)
            break
        if abs(px - b2x) <= 10 and abs(py - b2y) <= 10 :
            pygame.mixer.music.pause()
            player.goto(-300, 0)
            break
        if abs(px - b3x) <= 10 and abs(py - b3y) <= 10 :
            pygame.mixer.music.pause()
            player.goto(-300, 0)
            break
        if abs(px - b4x) <= 10 and abs(py - b4y) <= 10 :
            pygame.mixer.music.pause()
            player.goto(-300, 0)
            break



def start () :    #게임 시작 후 함수 실행
    pygame.mixer.music.play()
    hit()

def sethead ():
    screen.delay(0)
    b1.goto(280,0)
    b2.goto(0,300)
    b3.goto(0,-300)
    b4.goto(-280,0)
    player.setheading(270)
    b1.setheading(180)
    b2.setheading(90)
    b3.setheading(270)
    b4.setheading(0)

def restart () :    #재시작 함수 실행3
    pygame.mixer.music.play()
    sethead()
    hit()

screen.onkeypress(start, "space") #스페이스바 누르면 게임 시작

screen.onkeypress(trun , "Left") #왼쪽 방향키 누르면 장애물의 라인 안팎 이동

screen.onkeypress(restart , "Right")

turtle.mainloop()