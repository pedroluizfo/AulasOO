import math
from tkinter import *
root = Tk()
class Ponto():

    def __init__(self, n, x, y, canvas):
        self._n = n
        self._x = x
        self._y = y
        self.canvas = canvas

    def render_shape(self):
        python_green = "#476042"
        x1, y1 = (self._x - 2), (self._y - 2)
        x2, y2 = (self._x + 2), (self._y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=python_green)

    def updateCoord(self, x, y):
        self._x = x
        self._y = y
        print(f"As coordenadas do ponto {self._n} foram atualizadas para: ({self._x}, {self._y})")

    def getType(self):
        return 'Ponto_'

    def getNumber(self):
        return self._n

    def printCoord(self):
        print(f'\nO ponto {self._n} possui as coord: ({self._x}, {self._y}).')

class Circle(Ponto):

    def __init__(self, n, x, y, radius, canvas):
        super().__init__(n, x, y, canvas)
        self.radius = radius

    def getType(self):
        return 'Circle_'

    def updateCoord(self, x, y, radius):
        super().updateCoord(x, y)
        self.radius = radius
        print(f"As coordenadas de origem do circulo {self._n} foram atualizadas para: ({self._x}, {self._y})\ne o raio foi atulaizado para: ({self.radius})")

    def printCoord(self):
        print(f'\nO círculo {self._n} possui origem em: ({self._x}, {self._y})')
        print(f'E o seu raio é {self.radius}')

    def pointIn(self, pt):
        """ Verifica se o ponto está dentro deste círculo"""
        distance = math.sqrt((self._x - pt._x) ** 2 + (self._y - pt._y) ** 2)
        return distance <= self.radius

    def area(self):
        """ Calcula a área deste círculo e mostra no terminal"""
        area = math.pi * self.radius ** 2
        print(f'A área do círculo {self._n} é: {area}')

    def perimeter(self):
        """ Calcula o perímetro deste círculo e mostra no terminal"""
        perimeter = 2 * math.pi * self.radius
        print(f'O perímetro do círculo {self._n} é: {perimeter}')

    def render_circle(self):
        radius = self.radius
        python_black = "#000000"
        x1, y1 = (self._x - radius), (self._y - radius)
        x2, y2 = (self._x + radius), (self._y + radius)
        self.canvas.create_oval(x1, y1, x2, y2, fill=python_black)

class Line():
    def __init__(self, n, x1, y1, x2, y2, canvas):
        self._n = n
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.canvas = canvas

    def render_line(self):
        self.canvas.create_line(self._x1, self._y1, self._x2, self._y2)

    def updateCoord(self, x1, y1,x2,y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        print(f"As coordenadas de formação da linha {self._n} foram atualizadas para: ({self._x1}, {self._y1}) e ({self._x2}, {self._y2})")

    def printCoord(self):
        print(f'\nA linha {self._n} possui as coord: ({self._x1}, {self._y1})e ({self._x2}, {self._y2})')

class Triangle(Line):
    def __init__(self, n, x1, y1, x2, y2, x3, y3, canvas):
        super().__init__(n, x1, y1, x2, y2, canvas)
        self._x3 = x3
        self._y3 = y3

    def render_triangle(self):
        # Draw the three lines to form the triangle
        super().render_line()
        self.canvas.create_line(self._x2, self._y2, self._x3, self._y3)
        self.canvas.create_line(self._x3, self._y3, self._x1, self._y1)

    def updateCoord(self, x1, y1, x2, y2, x3, y3):
        # Update the coordinates of the three points
        super().updateCoord(x1, y1, x2, y2)
        self._x3 = x3
        self._y3 = y3

        print(f"Coordenadas do triângulo {self._n} atualizadas para: "
              f"({self._x1}, {self._y1}), ({self._x2}, {self._y2}), ({self._x3}, {self._y3})")

    def printCoord(self):
        # Print the coordinates of the three points of the triangle
        super().printCoord()
        print(f"Coordenadas do terceiro ponto do triângulo {self._n}: ({self._x3}, {self._y3})")
