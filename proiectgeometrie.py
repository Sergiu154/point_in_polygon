from dataclasses import dataclass
from graphics import *


@dataclass
class Punct:
    x: float
    y: float


x = Punct(0, 0)


def read_input():
    points = []
    with open("citire", "r") as fin:
        row = [float(x) for x in fin.readline().split()]
        n = int(row[0])
        for i in range(0, n):
            row = [float(x) for x in fin.readline().split()]
            points.append(Punct(float(row[0]), float(row[1])))
        row = [float(x) for x in fin.readline().split()]
        A = Punct(float(row[0]), float(row[1]))
    return n, A, points


def cross_product(p1, p2):
    return p1.x * p2.y - p2.x * p1.y


def direction(p1, p2, p3):
    return cross_product(Punct(p3.x - p1.x, p3.y - p1.y), Punct(p2.x - p1.x, p2.y - p1.y))


def point_on_segment(p1, p2, p3):
    if min(p1.x, p2.x) <= p3.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= p3.y <= max(p1.y, p2.y):
        return 1
    return 0


def print_msg(win, msg, pmax):
    point = Point((pmax[0] + 700) / 2, pmax[1] + 600)
    message = Text(point, msg)
    message.setSize(10)
    message.draw(win)
    win.getMouse()
    win.close()


def point_position(P1, P2, A, win, pmax):
    cross_prod = direction(P1, P2, A)
    if cross_prod > 0:
        print_msg(win, "Punctul A este situat in afara poligonului convex", pmax)
        return 0
    elif cross_prod == 0:
        if point_on_segment(P1, P2, A):
            print_msg(win, "Punctul A este situat pe latura \n" + str(P1) + '\n' + str(P2) + "\na poligonului convex",
                      pmax)
            return 0
    return -1


def find_point():
    n, A, points = read_input()
    p = [(max(points, key=lambda A: A.x)).x, (max(points, key=lambda A: A.y)).y]
    print("p=", p)
    l = p[0] + 700
    L = p[1] + 700
    offsetX, offsetY, mult = l / 4, L / 4, 4

    if 0 <= p[0] <= 9 and 0 <= p[1] <= 9:
        offsetX, offsetY, mult = l / 4, L / 4, 35
    elif 100 <= p[0] <= 999 and 100 <= p[1] <= 999:
        offsetX, offsetY, mult = l / 3.5, L / 3.5, 1

    win = GraphWin("My Polygon", l, L)
    win.setCoords(-l, -L, l, L)
    pct = Circle(Point(A.x * mult + offsetX, A.y * mult + offsetY), 5)
    pct.setFill("blue")
    # pct.setWidth(3)

    Ox = Line(Point(-l, 0), Point(l, 0))
    Oy = Line(Point(0, -L), Point(0, L))
    Ox.draw(win)
    Ox.setArrow('last')
    Oy.setArrow('last')
    Oy.draw(win)
    pct.draw(win)
    print(offsetY, offsetX, mult)
    laturi = []
    for i in range(0, len(points) - 1):
        line = Line(Point(points[i].x * mult + offsetX, points[i].y * mult + offsetY),
                    Point(points[i + 1].x * mult + offsetX, points[i + 1].y * mult + offsetY))
        time.sleep(0.5)
        laturi.append(line)
        line.draw(win)

    time.sleep(0.5)
    line = Line(Point(points[len(points) - 1].x * mult + offsetX, points[len(points) - 1].y * mult + offsetY),
                Point(points[0].x * mult + offsetX, points[0].y * mult + offsetY))
    laturi.append(line)
    line.draw(win)
    time.sleep(1)

    for i in range(0, n - 1):
        laturi[i].setOutline("red")
        pct.setFill("red")
        time.sleep(1)
        laturi[i].setOutline("black")
        pct.setFill("black")

        if point_position(points[i], points[i + 1], A, win, p) == 0:
            return
    laturi[n - 1].setOutline("red")
    pct.setFill("red")
    time.sleep(1)
    laturi[n - 1].setOutline("black")
    pct.setFill("black")
    if point_position(points[n - 1], points[0], A, win, p) == 0:
        return
    print_msg(win, "Punctul A este in interiorul poligonului convex", p)
    return 0


if __name__ == "__main__":
    find_point()
