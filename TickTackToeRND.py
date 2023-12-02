import SimpleCubes as sc
import math
import CartesianSystem as csys
import itertools as itool

def update(cube,Player,row,column):
    if sc.select_column(cube,1,row,column).colour=="None":
        sc.select_column(cube,1,row,column).colour=Player
        sc.show_face(cube,1)
        return False
    else:
        print("That Space is already occupied!")
        print("Try again!")
        return True
    
    
def changePlayer(Player):
    if Player=="X":
        return "O"
    else:
        return "X"


def win_check(cube):
    points=[csys.point(x,y) for x in range(1,4) for y in range(1,4)]
    comb = list(itool.combinations(points,3))
    check = True
    for i in comb:
        if csys.line.equation(csys.line(i[0],i[1]),i[2]):
            if sc.select_column(cube,1,i[0].y,i[0].x).colour!='None' and sc.select_column(cube,1,i[1].y,i[1].x).colour!='None' and sc.select_column(cube,1,i[2].y,i[2].x).colour!='None' and sc.select_column(cube,1,i[0].y,i[0].x).colour==sc.select_column(cube,1,i[1].y,i[1].x).colour and sc.select_column(cube,1,i[1].y,i[1].x).colour==sc.select_column(cube,1,i[2].y,i[2].x).colour:
                check=False
                #backup testing perpouse print statement
                #print(sc.select_column(cube,1,i[0].y,i[0].x).colour+"\n"+sc.select_column(cube,1,i[1].y,i[1].x).colour+"\n"+sc.select_column(cube,1,i[2].y,i[2].x).colour)
    return check