from Graphics import *

def main():
    win = GraphWin("win", 300,300)
    message = Entry(Point(100,100), 10)
    message.draw(win)

    win.getMouse()
    win.close()

main()