import SimpleCubes as sc
import CartesianSystem as csys
import itertools as itool
import tkinter as tk
from tkinter import ttk
class game:
    def update(instance,row,column):
        if sc.select_column(instance.cube,1,row,column).colour=='':
            sc.select_column(instance.cube,1,row,column).colour=instance.Player
            sc.show_face(instance.cube,1)
            return False
        else:
            print("That Space is already occupied!")
            print("Try again!")
            return True
        
        
    def changePlayer(instance):
        if instance.Player=="X":
            return "O"
        else:
            return "X"


    def win_check(instance):
        points=[csys.point(x,y) for x in range(1,4) for y in range(1,4)]
        comb = list(itool.combinations(points,3))
        check = True
        for i in comb:
            if csys.line.equation(csys.line(i[0],i[1]),i[2]):
                if sc.select_column(instance.cube,1,i[0].y,i[0].x).colour!=sc.square.default and sc.select_column(instance.cube,1,i[1].y,i[1].x).colour!=sc.square.default and sc.select_column(instance.cube,1,i[2].y,i[2].x).colour!=sc.square.default and sc.select_column(instance.cube,1,i[0].y,i[0].x).colour==sc.select_column(instance.cube,1,i[1].y,i[1].x).colour and sc.select_column(instance.cube,1,i[1].y,i[1].x).colour==sc.select_column(instance.cube,1,i[2].y,i[2].x).colour:
                    check=False
                    #backup testing perpouse print statement
                    #print(sc.select_column(self.cube,1,i[0].y,i[0].x).colour+"\n"+sc.select_column(self.cube,1,i[1].y,i[1].x).colour+"\n"+sc.select_column(self.cube,1,i[2].y,i[2].x).colour)
        return check
class instance:
    def __init__(self,window,cube):
        self.Player="X"
        self.window=window
        self.cube=cube
        self.buttonFrame=tk.Frame(window,bg="lightblue")
        self.textFrame=tk.Frame(window,bg="lightblue")
        self.style=ttk.Style()
        self.string=tk.Label(self.textFrame,text=f"It is player {self.Player}'s Turn: ",bd=2,relief="sunken",font=("Arial",int(self.window.winfo_screenwidth()*(18/1536))),bg="lightblue")
        self.buttons=instance.get_buttons(self)
    def config(self):
        self.window.configure(bg="lightblue",highlightbackground="lightblue", highlightcolor="lightblue")
        self.window.attributes("-alpha", 0.9)
        self.style.configure("Button", foreground="lightblue", background="blue")
        self.textFrame.pack()
        self.buttonFrame.pack()
        self.window.title("TickTackToe")
        self.string.pack()
        self.window.geometry(f'{int(self.window.winfo_screenwidth()*(115/768))}x{int(self.window.winfo_screenheight()*(95/288))}')#'230x285'
        self.Construction()
        self.window.resizable(False,False)
        self.window.mainloop()
    def when_pressed(self,x,y):
        Occupied=game.update(self,y,x)
        sc.select_column(self.cube,1,y,x).button["text"]=sc.select_column(self.cube,1,y,x).colour
        if Occupied == False:
            if game.win_check(self) == False:
                print(f"The Player \"{self.Player}\" Wins. Good Job!")
                self.string["font"]=("Arial",int(self.window.winfo_screenwidth()*(12/1536)))
                self.string["bd"]=0
                self.textFrame.pack(anchor="center",pady=(self.window.winfo_height() // 2, 0))
                self.string["text"]=f"The Player \"{self.Player}\" Wins. Good Job!"
                instance.Destruction(self)
            elif instance.tie_check(self) == True:
                print(f"The Player \"{self.Player}\" Wins. Good Job!")
                self.string["font"]=("Arial",int(self.window.winfo_screenwidth()*(10/1536)))
                self.string["bd"]=0
                self.textFrame.pack(anchor="center",pady=(self.window.winfo_height() // 2, 0))
                self.string["text"]=f"There was a tie between the players!"
                instance.Destruction(self)
            else:
                self.Player=game.changePlayer(self)
                self.string["text"]=f"It is player {self.Player}'s Turn: "
        # print(sc.show_face(self.cube,1))
        # print(game.win_check(self))

    def get_buttons(self) -> list:
        buttons=[]
        for i in range(1,len(sc.readable_pices(self.cube,1))+1):
            for j in range(1,len(sc.readable_pices(self.cube,1)[i-1])+1):
                selected_column=sc.select_column(self.cube,1,i,j)
                selected_column.button=tk.Button(self.buttonFrame,bg="lightblue",activebackground="lightblue",text=selected_column.colour,height=int(self.window.winfo_screenheight()*(5/864)),width=int(self.window.winfo_screenwidth()*(10/1536)),padx=0,pady=0,command=lambda x=selected_column.point.x,y=selected_column.point.y: instance.when_pressed(self,x,y))
                buttons.append(selected_column.button)
        return buttons

    def Construction(self):
        for i in range(1,len(sc.readable_pices(self.cube,1))+1):
            for j in range(1,len(sc.readable_pices(self.cube,1)[i-1])+1):
                selected_column=sc.select_column(self.cube,1,i,j)
                selected_column.button.grid(row=selected_column.point.y,column=selected_column.point.x)


    def Destruction(self):
        for i in self.buttons:
            i.grid_forget()

    def tie_check(self):
        check = True
        for i in self.buttons:
            if i["text"]=="":
                check = False
        return check