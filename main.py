from graphics import *

def main():
    win = Window(800, 600)
    l = Line(Point(100, 100), Point(200, 200))
    win.draw_line(l, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()