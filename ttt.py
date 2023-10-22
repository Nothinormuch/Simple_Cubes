import streamlit as st
import TickTackToeRND as ttt
import SimpleCubes as sc
import CartesianSystem as csys

grid1=sc.cube("Grid1")
def main():
    Player="X"
    game=True
    while game:
        st.text(f"Player \"{Player}\"('s) Turn: ")
        ttt.temp_update(grid1,Player,int(st.text_input("Enter the row number: ")),int(st.text_input("Enter the column number: ")))
        st.text(sc.show_face(grid1,1))
        game=ttt.win_check()
        Player=ttt.changePlayer(Player)  
    st.text(f"Player {ttt.changePlayer(Player)}, You win!\n\nThe Final Grid: \n"+sc.show_face(grid1,1))