from graphics import *
import time

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
circulo_rojo.draw(interfaz)

# Dibujamos color amarillo
circulo_amarillo = Circle(Point(125, 135), 25)
circulo_amarillo.setOutline('grey')
circulo_amarillo.draw(interfaz)

# Dibujamos color verde
circulo_verde = Circle(Point(125, 200), 25)
circulo_verde.setOutline('grey')
circulo_verde.setFill('green')
circulo_verde.draw(interfaz)

while True:
    time.sleep(4)
    circulo_verde.setFill('')
    circulo_amarillo.setFill('yellow')
    time.sleep(2)
    circulo_amarillo.setFill('')
    circulo_rojo.setFill('red')
    time.sleep(4)
    circulo_rojo.setFill('')
    circulo_verde.setFill('green')
