from graphics import *

# Dibujamos el semaforo
interfaz = GraphWin('Semaforo', 250, 400)
rectangulo = Rectangle(Point(85, 15), Point(165, 250))
rectangulo.setFill('black')
rectangulo.draw(interfaz)
# Soporte del semaforo
pie = Rectangle(Point(115, 250), Point(135, 390))
pie.setFill('brown')
pie.draw(interfaz)
# Dibujamos el circulo rojo
circulo_rojo = Circle(Point(125, 70), 25)
circulo_rojo.setOutline('grey')
circulo_rojo.setFill('red')
circulo_rojo.draw(interfaz)
# Dibujamos color naranja
circulo_naranja = Circle(Point(125, 135), 25)
circulo_naranja.setOutline('grey')
circulo_naranja.setFill('orange')
circulo_naranja.draw(interfaz)
# Dibujamos color verde
circulo_verde = Circle(Point(125, 200), 25)
circulo_verde.setOutline('grey')
circulo_verde.setFill('green')
circulo_verde.draw(interfaz)
