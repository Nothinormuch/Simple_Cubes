#Imporing pickle for storage
#to get the paths and manage them
import pickle
import os
import math
import CartesianSystem as csys
import tkinter as tk


class square:
    default=''
    co_no=1
    def __init__(self,colour,x,y):
        self.colour=colour
        self.co_no=square.co_no
        self.point=csys.point(x,y)
        self.button=None
        square.co_no+=1
        
    #not so important functions
    #making a definition to convert co_no to column number per row
    def co_no_perrow(co_no,ro_no):
        if ro_no==1:
            return co_no
        elif ro_no==2:
            return co_no-3
        elif ro_no==3:
            return co_no-6
        else:
            return("Error while using column number for each row!")
        
    #definition which i most probably would not need
    #it gives me the square number in one cube
    def conv_co_no(self,face,row,column):
        return(((face-1)*9)+((row-1)*3)+column)

# rows contain 3 squares in a straight line
class row:
    ro_no=1
    def __init__(self,cbdata):
        # self.co1=square(square.default,square.co_no_perrow(square.co_no,row.ro_no),row.ro_no)
        # self.co2=square(square.default,square.co_no_perrow(square.co_no,row.ro_no),row.ro_no)
        # self.co3=square(square.default,square.co_no_perrow(square.co_no,row.ro_no),row.ro_no)
        self.columns={}
        for i in range(cbdata[1]):
            self.columns[f'co{i+1}']=square(square.default,square.co_no_perrow(square.co_no,row.ro_no),row.ro_no)
        self.ro_no=row.ro_no
        row.ro_no+=1
        
# face contains 3 rows, one below the other with makes it contain 9 of those little squares
class face:
    fc_no=1
    def __init__(self,vector,cbdata):
        direction,axis=vector
        # direction,axis=vector
        # self.ro1=row()
        # self.ro2=row()
        # self.ro3=row()
        # self.faceareavector=faceareavector(direction,axis)
        # self.fc_no=face.fc_no
        # face.fc_no+=1
        # self.ro1={}
        # for i in range(cbdata[0]):
        #     self.ro_list[f'ro{i+1}']=row(cbdata)
        self.faceareavector=faceareavector(direction,axis)
        self.fc_no=face.fc_no
        face.fc_no+=1

#cube object(litreally) which will have 6 Faces, so it adds up to 54 of those small and cute squares 

class cube:
    cbno=1
    cbname='cube {}'.format(cbno)
    def __init__(self,cubename=cbname,cubedata=(6,3,3)):#(no_of_faces,no_of_rows,no_of_columns)=(6,3,3)
        self.cbdata=cubedata
        self.griddata=(self.cbdata[1],self.cbdata[2])
        self.face1=face(('+','x'),self.griddata)
        self.face2=face(('+','y'),self.griddata)
        self.face3=face(('+','z'),self.griddata)
        self.face4=face(('-','x'),self.griddata)
        self.face5=face(('-','y'),self.griddata)
        self.face6=face(('-','z'),self.griddata)
        #this might go wrong(i will know when i test it) - it didn't most probably -> yes it didn't
        self.cbname=cubename
        cube.cbno+=1
        cube.cbname='cube {}'.format(cube.cbno)


#Class for storing the cube object and opening it
class storage:
    cubebag=[]
    def exportt(cube,file="",name='cube.log'):
        if file !='':
            file+='/'
        fh= open(file+name,'wb')
        pickle.dump(cube,fh)
        fh.close()
        return("Sucessfully Exported {}!")
    
    def importt(file="",name='cube.log'):
        fh= open(file+name,'rb')
        imported_cubes=[]
        if file !='':
            file+='/'
        try:
            while True:
                imported_cubes.append(pickle.load(fh))

        except FileNotFoundError:
            storage.fileNotFound(file,name)
        finally:
            fh.close()
            return imported_cubes
        
    def fileNotFound(file,name):
        print("No file with the name \"{}\" found in \"{}\" folder!".format(name,file))

    def show_cubes(cubes):
        returnstr=""
        for i in cubes:
            returnstr+=i.cbname+':\n'
            returnstr+=show_allFace(i)+'\n'
        return(returnstr)
    

    def update_storage():
        for i in os.listdir():
            if i.endswith('.log'):
                storage.cubebag+=storage.importt(name=i)



                
class faceareavector:
    def __init__(self,direction,axis):
        self.axis=axis
        self.direction=direction

    def __str__(self):
        return str(self.direction)+str(self.axis)

#adding cubes in the list cube            
def chose_activecube(cubename,cubegag=storage.cubebag):
    ck=False
    for i in cubegag:
        if i.cbname==cubename:
            ck=True
            return i
    if ck==False:
        cubeNotFound(cubename)

def cubeNotFound(cubename):
    print("No cube with the name {} Found!".format(cubename))
        

# this series function make my life easier and There might be a way to compress this into one function but I dont want to overload my two small brain cells 
def select_face(cube,face) -> face:
    selected_faces=[cube.face1,cube.face2,cube.face3,cube.face4,cube.face5,cube.face6]
    return selected_faces[face-1]
def select_row(cube,face,row) -> row:
    selected_rows=[select_face(cube,face).ro1,select_face(cube,face).ro2,select_face(cube,face).ro3]
    return selected_rows[row-1]
#This is the final and most useable function which takes Cube Name(Variable),Face no.,row no. and column no. to give the object of that column to be used to get the co_no or the colour(Which are the only functions I have managed to code till now)
def select_column(cube,face,row,column) -> square:
    selected_columns=[(select_row(cube,face,row).co1),(select_row(cube,face,row).co2),(select_row(cube,face,row).co3)]
    return selected_columns[column-1]



# This function gives me a formatted version of the cube
def readable_face(cube,face):
    return [[select_column(cube,face,1,1).colour,select_column(cube,face,1,2).colour,select_column(cube,face,1,3).colour],[select_column(cube,face,2,1).colour,select_column(cube,face,2,2).colour,select_column(cube,face,2,3).colour],[select_column(cube,face,3,1).colour,select_column(cube,face,3,2).colour,select_column(cube,face,3,3).colour]]

# This function gives me a the buttons from the columns
def readable_button(cube,face):
    return [[select_column(cube,face,1,1).button,select_column(cube,face,1,2).button,select_column(cube,face,1,3).button],[select_column(cube,face,2,1).button,select_column(cube,face,2,2).button,select_column(cube,face,2,3).button],[select_column(cube,face,3,1).button,select_column(cube,face,3,2).button,select_column(cube,face,3,3).button]]

#Aggrigate of the above two functions
def readable_pices(cube,face):
    return [[select_column(cube,face,1,1),select_column(cube,face,1,2),select_column(cube,face,1,3)],[select_column(cube,face,2,1),select_column(cube,face,2,2),select_column(cube,face,2,3)],[select_column(cube,face,3,1),select_column(cube,face,3,2),select_column(cube,face,3,3)]]


#This function is very temperory will improve(soon)
# It shows the colours of the cube per face in the atribute
def show_face(cube, face):
    returnstr=""
    for i in range(0,3):
        for j in range(0,3):
            returnstr+=readable_face(cube,face)[i][j]+"\t"
        returnstr+='\n'
    return(returnstr)




#Quick function to show all faces of the cube
def show_allFace(cube):
    returnstr=""
    for i in range(6):
        returnstr+="Face {}:\n".format(i+1)
        returnstr+=show_face(cube,i+1)
    return(returnstr)


#Updating Storage


def cubeAlreadyAdded(i):
    print('{} is already added!'.format(i.cbname))

#Tests
# Face=face(('+','x'),(3,3))

# print(Face.rows)