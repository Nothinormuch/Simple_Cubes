import SimpleCubes as sc
import math
import CartesianSystem as csys
import itertools as itool
grid1=sc.cube("Grid1")
def temp_update(cube,Player):
    row=int(input("Enter the row number: "))
    column=int(input("Enter the column number: "))
    if sc.select_column(grid1,1,row,column).colour=="None":
        sc.select_column(grid1,1,row,column).colour=Player
        sc.show_face(cube,1)
    else:
        print("That Space is already occupied!")
        print("Try again!")
        temp_update(grid1,Player)
def changePlayer(Player):
    if Player=="X":
        return "O"
    else:
        return "X"
def main():
    Player="X"
    game=True
    while game:
        print(f"Player \"{Player}\"('s) Turn: ")
        temp_update(grid1,Player)
        print(sc.show_face(grid1,1))
        game=win_check()
        Player=changePlayer(Player)  
    print(f"Player {changePlayer(Player)}, You win!\n\nThe Final Grid: \n"+sc.show_face(grid1,1))

def win_check():
    points=[csys.point(x,y) for x in range(1,4) for y in range(1,4)]
    comb = list(itool.combinations(points,3))
    check = True
    for i in comb:
        if csys.line.equation(csys.line(i[0],i[1]),i[2]):
            if sc.select_column(grid1,1,i[0].y,i[0].x).colour!='None' and sc.select_column(grid1,1,i[1].y,i[1].x).colour!='None' and sc.select_column(grid1,1,i[2].y,i[2].x).colour!='None' and sc.select_column(grid1,1,i[0].y,i[0].x).colour==sc.select_column(grid1,1,i[1].y,i[1].x).colour and sc.select_column(grid1,1,i[1].y,i[1].x).colour==sc.select_column(grid1,1,i[2].y,i[2].x).colour:
                check=False
                #backup testing perpouse print statement
                #print(sc.select_column(grid1,1,i[0].y,i[0].x).colour+"\n"+sc.select_column(grid1,1,i[1].y,i[1].x).colour+"\n"+sc.select_column(grid1,1,i[2].y,i[2].x).colour)
    return check


main()