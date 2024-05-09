'''
Created on April 25, 2024

@author: Rushikesh
'''
import turtle  # allows us to use the turtles library

wn = turtle.Screen()  # creates a graphics window
wn.bgcolor('black')
a=turtle.Turtle()

def pattern_1(a):
    a.color('Green')
    for i in range(100):
        a.backward(i+100)
        a.left(145)
        a.backward(i+100)
        a.speed(0)
def pattern_2(a):
    for i in range(100):
        a.color('purple')
        a.backward(10)
        a.left(105)
        a.forward(i+10)
        a.color('white')
        a.left(105)
        a.backward(i+10)
        a.left(105)
def pattern_3(a):
    a.color('blue')
    for i in range(100):
        a.left(30)
        a.forward(i+50)
        a.left(75)
        a.forward(i+25)
def pattern_4(a):
    a.color('green')
    for i in range(50):
        a.circle(i+50)
        a.left(60)
        a.circle(i+50)
def pattern_5(object):
    a.color('red')
    for i in range(14):
        a.up()
        a.width(2)
        a.forward(30)
        a.left(90)
        a.forward(30)
        a.right(120)
        a.down()
        a.left(90)
        a.forward(30)
        a.left(90)
        a.forward(30)
def swastik(a):
    a.color('red')
    for i in range(5):
        a.width(2)
        a.up()
        a.fd(100)
        a.left(90)
        a.fd(100)
        a.down()
        a.left(90)
        a.fd(100)
        a.left(90)
        a.fd(100)

def pattern_7(a):
    a.color('white')
    for i in range(100):
        a.forward(50-i)
        a.left(45)
        a.forward(50-i)
        a.left(45)

if __name__ == "__main__":
    def sketch():
        pattern_1(a)
        a._clear()
        pattern_2(a)
        a._clear()
        pattern_3(a)
        a._clear()
        pattern_4(a)
        a._clear()
        pattern_5(a)
        a._clear()
        swastik(a)
        a._clear()
        pattern_7(a)


    sketch()
    wn.exitonclick()
