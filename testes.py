from formas import *
from planoCartesiano import *
import tkinter as tk

def workspace():
    root = tk.Tk()
    dashboard = CartesianBoard(root)
    
    p1 = Ponto(1, 195, 420, dashboard.canvas)

    p1.render_shape() 
    p1.printCoord()
    p1.updateCoord(253,315)

    c1 = Circle(1,120,230,250, dashboard.canvas)

    c1.printCoord()
    c1.area()
    c1.perimeter()
    c1.updateCoord(456,234,80)
    c1.render_circle()
    is_inside = c1.pointIn(p1)
    print(f'O ponto está dentro da área do circulo? {is_inside}')

    l1 = Line(15, 25, 200, 125, 100, dashboard.canvas)

    l1.printCoord()
    l1.updateCoord(35,45,95,105)
    l1.render_line()

    t1 = Triangle(1,15,25,87,105,99,200,dashboard.canvas)
    t1.printCoord()
    t1.updateCoord(95,105,87,12,19,280)
    t1.render_triangle()
    root.mainloop()

if __name__ == "__main__":
    workspace()
