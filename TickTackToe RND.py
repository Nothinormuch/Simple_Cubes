import SimpleCubes as sc
import math
import CartesianSystem as csys
import itertools as itool
grid1=sc.cube("Grid1")
def temp_update(face):
    sc.select_column(grid1,face,1,1).colour="x"
    sc.select_column(grid1,face,2,2).colour="x"
    sc.select_column(grid1,face,3,3).colour="x"
temp_update(1)


def triplets():
    points=[csys.point(x,y) for x in range(1,4) for y in range(1,4)]
    comb = list(itool.combinations(points,3))
    for i in comb:
        if csys.line.equation(csys.line(i[0],i[1]),i[2]):
            if i 
print(triplets())