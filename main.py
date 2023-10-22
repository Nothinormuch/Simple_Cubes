import SimpleCubes as sc
import CartesianSystem as csys
import streamlit as st
def temp_creation():
    c1=sc.cube("Testcube1")
    c2=sc.cube("Testcube2")
    sc.select_column(c1,1,1,1).colour='Blue'
    sc.select_column(c2,1,2,1).colour='Red'
def temp_show():
    sc.storage.update_storage()
    oncube=sc.chose_activecube('Testcube1',sc.storage.cubebag)
    sc.select_column(oncube,1,1,1).colour='Green'
    return(sc.storage.show_cubes(sc.storage.cubebag))

st.text(temp_show())