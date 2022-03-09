import turtle as t
def mycircle(r,size):
    t.pendown()
    t.circle(r)
    t.write(f"{size}", font=style, align='center')
    t.penup()

t.screensize(4000,4000)
t.setup(1200,800)

style = ('Arial', 5, 'italic')
t.penup()
t.speed(0)
t.goto(-290,0)
t.pendown()
sum = 0
n1 = 0
n2 = 1
diameter = 0
numberOfBubbles = 0
while numberOfBubbles < 20:
    sum = n1+n2
    n1 = n2
    n2 = sum
    diameter = sum
    if diameter > 0:
        numberOfBubbles += 1
    t.setx(-300+diameter*2.2)
    mycircle(diameter/2,diameter)


t.ht() # hide turtle
t.Screen().exitonclick() # keep the canvas open until mouse click
