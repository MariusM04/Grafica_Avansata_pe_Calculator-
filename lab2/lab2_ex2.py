from graphics import * 
def main():
    win = GraphWin('My Graphics', 300, 250)   # fereastra de 300 x 250 pixeli
    g   = Circle(Point(150, 125), 50)         # primul cerc apare la coordonatele x,y = 150,125 marime 50
    g.setFill('purple')                       # primul cerc este mov
    g1   = Circle(Point(225, 125),  25)       # al doilea cerc apare la coordonatele x,y = 225,125  marime 25
    g1.setFill('green')                       # al doilea cerc este verde
    g.draw(win)     
    g1.draw(win)                              # cele 2 cercuri apar in fereastra win
    win.getMouse()
    win.close()
main()
