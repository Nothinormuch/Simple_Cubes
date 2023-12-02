import TickTackToeRND as ttt
import SimpleCubes as sc
# import CartesianSystem as csys
import tkinter as tk

def when_pressed(x,y):
    global cube
    global Player
    Occupied=ttt.update(cube,Player,y,x)
    if Occupied == False:
        if ttt.win_check(cube) == False:
            window.destroy()
            print(f"The Player \"{Player}\" Wins. Good Job!")
        Player=ttt.changePlayer(Player)
    sc.select_column(cube,1,y,x).button["text"]=sc.select_column(cube,1,y,x).colour
    print(sc.show_face(cube,1))
    
    

def initialization(window,cube):
    for i in range(1,4):
        for j in range(1,4):
            selected_column=sc.select_column(cube,1,i,j)
            selected_column.button=tk.Button(window,text=selected_column.colour,command=lambda x=selected_column.point.x,y=selected_column.point.y: when_pressed(x,y))
            selected_column.button.grid(row=selected_column.point.y,column=selected_column.point.x)



Player="X"
window=tk.Tk()
window.geometry('100x100')
cube=sc.cube("cube")
initialization(window,cube)
window.mainloop()