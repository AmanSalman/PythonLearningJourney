from Graphics import *

def main():
    win = GraphWin("win", 300,300)

    aLine = Line(Point(0,0), Point(300,300))
    aLine.draw(win)

    win.getMouse()
    win.close()

main()