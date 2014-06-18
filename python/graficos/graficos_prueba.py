import graphics
from graphics import *
g = GraphWin('Ejemplo graphics', 300, 180)
p = Point(150, 90)
p.draw(g)
p_1 = Point(290, 160)
p_1.draw(g)
p_2 = Point(10, 10)
p_2.draw(g)
r = Rectangle(p_1, p_2)
r.draw(g)
r.setFill('red')
r.setOutline('blue')
r2 = Rectangle(Point(20,20), Point(280, 150))
r2.draw(g)
r2.setFill('blue')
c = Circle(p, 20)
c.setFill('green')
c.draw(g)

g.getMouse()

