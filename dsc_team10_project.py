from multiprocessing import Process
import pygame
import turtle
from random import randint

pygame.mixer.init()
music1 = pygame.mixer.music.load("1스테이지.mp3")

def A():
    a.up()
    a.goto(-600,-350)   #-600,300    650,300
    a.down()            #-600,-350   650,-350
    a.forward(1250)
    a.left(90)
    a.forward(650)
    a.left(90)
    a.forward(1250)
    a.left(90)
    a.forward(650)
    a.up()
    player.up()
    player.goto(-210,-20)
    player.left(270)
    a.goto(-200,-20)
    a.down()
    a.speed(0)
    a.circle(290)
    a.ht()


player1  =  turtle.Turtle ()
player1.color ( "black" )
player1.shape ( "circle" )
player1.pensize(3)
player1.speed(3)


a  =  turtle.Turtle () #레일 그리
a.color ( "black" )
a.speed ( 0 )
a.pensize(5)

b  =  turtle.Turtle ()
b.color ( "red" )
b.shape ( "triangle" )
b.up ()
b.speed ( 0 )
b.pensize(5)

screen  =  player1.getscreen ()
screen  =  player2.getscreen ()

A() #게임창 만들기

screen.listen ()

def play () :            #플레이어의 움직임 제현
    while True:
        player1.circle ( 300 )

def start () :    #게임 시작후 함수 실행
    pygame.mixer.music.play()
    play()

screen.onkeypress(start, "space") #스페이스 누르면 게임 시작

turtle.mainloop()