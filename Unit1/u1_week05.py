import turtle as t
t.speed(0)
t.pensize(3)
# Task: Create a
# Draw HEAD
# Draw EYES
# Draw NOSE
# Draw RED CHEEKS
# Draw MOUTH
# MOVE function
def myMove(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def myCircle(size,col):
    t.fillcolor(col)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
def myNose(radius):
    for i in range(2):
        t.circle(30,90)
        t.circle(20//2,90)


t.circle(120) # face
myMove(-40,90)
myCircle(35,"black") # left eye
myMove(-40,120)
myCircle(10,"white") # left pupil
myMove(40,90)
myCircle(35,"black") # right eye
myMove(40,120)
myCircle(10,"white")
myMove(0,50)
myCircle(35,"grey")
myMove(-21,85)
t.seth(-40)
myNose(30)
myMove(-20,80)
t.seth(-90)
t.circle(10,180)

t.ht() # hide turtle
t.Screen().exitonclick() # keep the canvas open until mouse click
