from tkinter import Tk, BOTH, Canvas
from turtle import width

class Window:
    def __init__(self, width, height, bg_color="white"):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("My Window")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False 

    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )



