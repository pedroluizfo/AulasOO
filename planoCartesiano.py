
import tkinter as tk
from tk import *

from formas import *
class CartesianBoard():

    def __init__(self, root):
        self.root = root
        self.root.title("Plano Cartesiano")

        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()

        self.shapes = {}
        self.renderGrid()
    
    def renderGrid(self):
        for y in range(0, 600, 20):
            self.canvas.create_line(0, y, 600, y, fill="gray")

        for x in range(0, 600, 20):
            self.canvas.create_line(x, 0, x, 600, fill="gray")

        
        
    def inserShape(self, shape):
        
        self.shapes[shape.getType() + str(shape.getNumber())]= shape
        
        
    def removeShape(self, shape):
        
        del self.shapes[shape.getType() + str(shape.getNumber())]
        
        
    def showShapes(self):
        
        print('\nEste plano cartesiano possui as seguintes formas:\n')
        for shape in self.shapes.keys():
            print(shape)
    
    
    def printDetails(self):
        
        for key in self.shapes.keys():
            self.shapes[key].printCoord()
    
        
    def getShape(self,key):
        return self.shapes[key]
            
            