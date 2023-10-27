#import streamlit as st
#import TickTackToeRND as ttt
#import SimpleCubes as sc
#import CartesianSystem as csys
import tkinter as tk
def when_pressed(button):
    button['text']="hello"
window=tk.Tk()
window.geometry('100x100')
b1=tk.Button(window,text="ayoOOO")
b1['command']=lambda: when_pressed(b1)
b1.grid(row=1,column=1)
window.mainloop()


