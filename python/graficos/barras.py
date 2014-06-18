# -*- coding: cp1252 -*-
from graphics import *

mywin = GraphWin('Grafico', 600, 400)
Text(Point(300,50), 'Gráfico del Empleo en España').draw(mywin)
mywin.setCoords(-5,-5,40,25)
lx = Line(Point(0,0), Point(38,0))
lx.draw(mywin)
r = Rectangle(Point(1,0),Point(6,20))
r.setFill('#000')
r.draw(mywin)

r2 = Rectangle(Point(8,0),Point(13,15))
r2.setFill('#FF00FF')
r2.draw(mywin)

r3 = Rectangle(Point(15,0),Point(20,10))
r3.setFill('#FFFF00')
r3.draw(mywin)

r4 = Rectangle(Point(22,0),Point(27,5))
r4.setFill('#CCC')
r4.draw(mywin)

r5 = Rectangle(Point(29,0),Point(34,2))
r5.setFill('#FFF056')
r5.draw(mywin)

year = ['2009', '2010', '2011', '2012', '2013']

x = 3.5
for y in year:
    Text(Point(x,-2), y ).draw(mywin)
    x += 7


mywin.getMouse()
