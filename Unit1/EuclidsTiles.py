import turtle as t
def euclids(a,b):
	c =1
	while c!= 0:
		c= a% b
		a= b
		b= c
	return a

def square(squareSize):
	for i in range(4):
		t.forward(squareSize)
		t.right(90)

t.speed(0)
floorWidth = 345
floorLength = 150
numberOfTilesX = None
numberOfTilesY = None
startingPos = None
tilesX = 0
tilesY = 0
xPos = 0
yPos = 0
for i in range(2):
	t.forward(floorWidth)
	t.right(90)
	t.forward(floorLength)
	t.right(90)


squaresize = euclids(floorWidth,floorLength)
print(squaresize)
numberOfTilesX = int(floorWidth/squaresize)
numberOfTilesY = int(floorLength/squaresize)

while tilesY < numberOfTilesY:
	while tilesX < numberOfTilesX:
		square(squaresize)
		xPos += squaresize
		t.setx(xPos)
		tilesX = tilesX + 1
	tilesX = 0
	t.penup()
	t.goto(0,0)
	t.pendown()
	yPos += squaresize
	xPos = 0
	t.sety(-yPos)
	tilesY = tilesY + 1

