#Matthew Choi
#CS 100 2022F Section 009
#HW 04, Oct 02, 2022


a= 3
b=4
c=5

if int(a)<int(b):
    print("OK")
if int(c)<int(b):
    print("OK")
if (int(a)+int(b)==int(c)):
    print("OK")
if (int(a)**2)+(int(b)**2)==(int(c)**2):
    print("OK")

if int(a)<int(b):
    print("OK")
if int(c)<int(b):
    print("OK")
else:
    print("Not OK")
if (int(a)+int(b)==int(c)):
    print("OK")
else:
    print("Not OK")
if (int(a)**2)+(int(b)**2)==(int(c)**2):
    print("OK")

Color = input('What is the color?')
print(Color)
Width = input('What is the width?')
print(Width)
Length = input('What is the length?')
print(Length)
Shape = input('What is the shape?')
print(Shape)

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.pencolor(Color)
t.pensize(int(Width))
if Shape == 'line':
    s = turtle.Screen()
    t = turtle.Turtle()
    t.pencolor(Color)
    t.pensize(int(Width))
    t.forward(int(Length))

elif Shape == 'triangle':
    s = turtle.Screen()
    t = turtle.Turtle()
    t.pencolor(Color)
    t.pensize(int(Width))
    t.forward(int(Length))
    t.right(120)
    t.forward(int(Length))
    t.right(120)
    t.forward(int(Length))

else:
    s = turtle.Screen()
    t = turtle.Turtle()
    t.pencolor(Color)
    t.pensize(int(Width))
    t.forward(int(Length))
    t.right(90)
    t.forward(int(Length))
    t.right(90)
    t.forward(int(Length))
    t.right(90)
    t.forward(int(Length))
    t.right(90)
