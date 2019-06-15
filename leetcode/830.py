from graphics import *
import math

spriaal = GraphWin("Joonistus", 1000, 1000)

a = 5
b = 4

while True:
    x = math.sin(a + math.pi() / 2)
    y = math.sin()

    pt = Point(x + 500, y + 500)
    pt.draw(spriaal)
