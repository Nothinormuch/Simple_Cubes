#Imporing pickle for storage
#to get the paths and manage them
import pickle
import os
import CartesianSystem as csys


class square:
    defaultcolour='None'
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
        self.co_list={}
        for i in range(cbdata[2]):
            self.co_list[f'co{i+1}']=square(square.defaultcolour,square.co_no_perrow(square.co_no,row.ro_no),row.ro_no)
            self.no_of_columns=len(self.co_list)
        self.ro_no=row.ro_no
        row.ro_no+=1
        
# face contains 3 rows, one below the other with makes it contain 9 of those little squares
class face:
    fc_no=1
    def __init__(self,vector,cbdata):
        direction,axis=vector
        self.ro_list={}
        for i in range(cbdata[1]):
            self.ro_list[f'ro{i+1}']=row(cbdata)
        self.no_of_rows=len(self.ro_list)
        self.faceareavector=faceareavector(direction,axis)
        self.fc_no=face.fc_no
        face.fc_no+=1

#cube object(litreally) which will have 6 Faces, so it adds up to 54 of those small and cute squares 

class cube:
    cbno=1
    cbname='cube {}'.format(cbno)
    def __init__(self,cubename=cbname,cubedata=(6,3,3)):#(no_of_faces,no_of_rows,no_of_columns)=(6,3,3)
        self.cbdata=cubedata
        self.face_list={}
        for i in range(self.cbdata[0]):
            self.face_list[f'face{i+1}']=face(('noSign','noAxis'),self.cbdata)
        self.no_of_faces=len(self.face_list)
        #backup that i most probably won't need
        # self.face1=face(('+','x'),self.griddata)
        # self.face2=face(('+','y'),self.griddata)
        # self.face3=face(('+','z'),self.griddata)
        # self.face4=face(('-','x'),self.griddata)
        # self.face5=face(('-','y'),self.griddata)
        # self.face6=face(('-','z'),self.griddata)
        # #this might go wrong(i will know when i test it) - it didn't most probably -> yes it didn't
        self.cbname=cubename
        cube.cbno+=1
        cube.cbname='cube {}'.format(cube.cbno)
    
    def create_Rubik_Cube(properties=[(('+','x'),"Red"),(('+','y'),"White"),(('+','z'),"Blue"),(('-','z'),"Green"),(('-','x'),"Orange"),(('-','y'),"Yellow")],cubename="Rubik's Cube {}".format(cbno),cubedata=(6,3,3)):
        returncube=cube(cubename,cubedata)
        #properties=[(('+','x'),"Red"),(('+','y'),"White"),(('+','z'),"Blue"),(('-','z'),"Green"),(('-','x'),"Orange"),(('-','y'),"Yellow")]
        for property in properties:
            select_face(returncube,properties.index(property)+1).faceareavector=faceareavector(property[0][0],property[0][1])
            for i in range(1,returncube.cbdata[1]+1):
                for j in range(1,returncube.cbdata[2]+1):
                    select_column(returncube,properties.index(property)+1,i,j).colour=property[1]
        return returncube


#Class for storing the cube object and opening it
class storage:
    default_file_path=os.getcwd()
    cubebag=[]
    def exportt(cube,file=default_file_path,name='cube.log'):
        if not(file.endswith('\\') or file.endswith(':') or file==''):
            file+='\\'
        if file=='':
            file=storage.default_file_path
        fh= open(file+name,'wb')
        pickle.dump(cube,fh)
        fh.close()
        return("Sucessfully Exported to {name}!")
    
    def importt(file=default_file_path,name='cube.log'):
        if not(file.endswith('\\') or file.endswith(':') or file==''):
            file+='\\'
        if file=='':
            file=storage.default_file_path
        fh= open(file+name,'rb')
        imported_cubes=[]
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
    

    def update_storage(file_path=default_file_path):
        found=False
        if not(file_path.endswith('\\') or file_path.endswith(':') or file_path==''):
            file_path='\\'
        if file_path=='':
            file_path=storage.default_file_path
        # print(os.listdir(file_path))
        for i in os.listdir(file_path):
            if i.endswith('.log'):
                storage.cubebag+=storage.importt(name=i,file=file_path)
                found=True
        if found==False:
            print("No File with the Extension .log found!")



                
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
def select_face(cube,face_no) -> face:
    #backup if things screw up
    #selected_faces=[cube.face1,cube.face2,cube.face3,cube.face4,cube.face5,cube.face6]
    #selected_faces[face_no-1]
    try:
        return cube.face_list[f'face{face_no}']
    except AttributeError:
        print("Error encountered while selecting a face!")
def select_row(cube,face_no,row_no) -> row:
    try:
        return select_face(cube,face_no).ro_list[f'ro{row_no}']
    except AttributeError:
        print("Error encountered while selecting a row!")
#This is the final and most useable function which takes Cube Name(Variable),Face no.,row no. and column no. to give the object of that column to be used to get the co_no or the colour(Which are the only functions I have managed to code till now)
def select_column(cube,face_no,row_no,column_no) -> square:
    try:
        return select_row(cube,face_no,row_no).co_list[f'co{column_no}']
    except AttributeError:
        print("Error encountered while selecting a column!")



# This function gives me a formatted version of the cube
def printable_face(cube,face_no):
    try:
        return [[select_column(cube,face_no,i+1,j+1).colour for j in range(len(select_row(cube,face_no,i+1).co_list))] for i in range(len(select_face(cube,face_no).ro_list))]
    except AttributeError:
        print("Error encountered while selecting face to be printed!")

# This function gives me a the buttons from the columns
def readable_button(cube,face_no):
    try:
        return [[select_column(cube,face_no,i+1,j+1).button for j in range(len(select_row(cube,face_no,i+1).co_list))] for i in range(len(select_face(cube,face_no).ro_list))]
    except AttributeError:
        print("Error encountered while selecting a list of buttons!")

#Aggrigate of the above two functions
def readable_columns(cube,face_no):
    try:
        return [[select_column(cube,face_no,i+1,j+1) for j in range(len(select_row(cube,face_no,i+1).co_list))] for i in range(len(select_face(cube,face_no).ro_list))]
    except AttributeError:
        print("Error encountered while selecting a list of columns!")

#This function is very temperory will improve(soon)
# It shows the colours of the cube per face in the atribute
def show_face(cube, face_no):
        #returnlist=[[select_column(cube,face_no,i+1,j+1) for j in range(len(select_row(cube,face_no,i+1).co_list))] for i in range(len(select_face(cube,face_no).ro_list))]
        returnstr=""
        for i in range(select_face(cube,face_no).no_of_rows):
            returnstr+="\t\t"
            for j in range(select_row(cube,face_no,i+1).no_of_columns):
                returnstr+=printable_face(cube,face_no)[i][j]+"\t"
            returnstr+='\n\n'
        return(returnstr)




#Quick function to show all faces of the cube
def show_allFace(cube):
    returnstr=""
    for i in range(cube.no_of_faces):
        returnstr+="\tFace {}:\n".format(i+1)
        returnstr+=show_face(cube,i+1)
    return(returnstr)


#Updating Storage


def cubeAlreadyAdded(i):
    print('{} is already added!'.format(i.cbname))

#Tests
# Face=face(('+','x'),(3,3))

# print(Face.rows)
