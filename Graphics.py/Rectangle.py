from Graphics import *

def main():
    win = GraphWin("win", 300,300)
    aRect = Rectangle(Point(50,50), Point(250,250))
    aRect.draw(win)

    win.getMouse()
    win.close()

main()