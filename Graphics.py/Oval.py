from Graphics import *

def main():
    win = GraphWin("win", 300,300)
    aOval = Oval(Point(50,50), Point(200,150))
    aOval.draw(win)
    win.getMouse()
    win.close()

main()