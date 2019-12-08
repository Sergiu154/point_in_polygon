from graphics import *

win = GraphWin("My Polygon", 800, 800)
# set the coordinate system of the window , lower-left and upper-right
win.setCoords(0, 0, 800, 800)
win.plot(100, 10, "blue")
points = [Point(100, 100), Point(400, 400), Point(400, 800), Point(100, 800)]
laturi = []
for i in range(0, len(points) - 1):
    line = Line(points[i], points[i + 1])
    time.sleep(0.5)
    laturi.append(line)
    line.draw(win)

time.sleep(1)
line = Line(points[len(points) - 1], points[0])
laturi.append(line)
line.draw(win)

for i in range(0, len(laturi)):
    laturi[i].setOutline("red")
    time.sleep(1)
    laturi[i].setOutline("black")

point = Point(100, 100)
message = Text(point, "Hello")
message.setSize(20)
message.draw(win)

# for i in range(0, len(laturi)):
#     # line = Line(points[i], points[i + 1])
#     laturi[i].undraw()
# poligon.draw(win)
win.getMouse()
win.close()
