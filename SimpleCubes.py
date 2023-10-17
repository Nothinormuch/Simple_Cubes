#Imporing pickle for storage
#to get the paths and manage them
import pickle
import os

#changing the working directory
os.chdir("/home/nothin_mint/Documents/Code/Cube_0.01")


#square object (9 of these squares are there for each face)
class square:
    co_no=1
    def __init__(self,colour):
        self.colour=colour
        self.co_no=square.co_no
        square.co_no+=1
        
    #definition which i most probably would not need
    #it gives me the square number in one cube
    def conv_co_no(self,face,row,column):
        return(((face-1)*9)+((row-1)*3)+column)

# rows contain 3 squares in a straight line
class row:
    ro_no=1
    def __init__(self):
        self.co1=square('None')
        self.co2=square('None')
        self.co3=square('None')
        self.ro_no=row.ro_no
        row.ro_no+=1
        
# face contains 3 rows, one below the other with makes it contain 9 of those little squares
class face:
    fc_no=1
    def __init__(self):
        self.ro1=row()
        self.ro2=row()
        self.ro3=row()
        self.fc_no=face.fc_no
        face.fc_no+=1

#cube object(litreally) which will have 6 Faces, so it adds up to 54 of those small and cute squares 

class cube:
    cbno=1
    cbname='cube {}'.format(cbno)
    def __init__(self,cubeName=cbname):
        self.face1=face()
        self.face2=face()
        self.face3=face()
        self.face4=face()
        self.face5=face()
        self.face6=face()
        #this might go wrong(i will know when i test it)
        self.cbname=cubeName
        cube.cbno+=1
        cube.cbname='cube {}'.format(cube.cbno)


#Class for storing the cube object and opening it
class storage:
    cubeBag=[]
    filepath=(os.path.dirname(__file__))
    def exportt(cube,file=filepath,name='cube.log'):
        if file !='':
            file+='/'
        fh= open(file+name,'wb')
        pickle.dump(cube,fh)
        fh.close()
        return("Sucessfully Exported {}!")
    
    def importt(file=filepath,name='cube.log'):
        imported_cubes=[]
        if file !='':
            file+='/'
        try:
            fh= open(file+name,'rb')
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


    


#adding cubes in the list cube            
def chose_activecube(cubeName,cubeBag=storage.cubeBag):
    ck=False
    for i in cubeBag:
        if i.cbname==cubeName:
            ck=True
            return i
    if ck==False:
        cubeNotFound(cubeName)

def cubeNotFound(cubeName):
    print("No cube with the name {} Found!".format(cubeName))
        

# this series function make my life easier and There might be a way to compress this into one function but I dont want to overload my two small brain cells 
def select_face(cube,face):
    faces=[cube.face1,cube.face2,cube.face3,cube.face4,cube.face5,cube.face6]
    return faces[face-1]
def select_row(cube,face,row):
    rows=[select_face(cube,face).ro1,select_face(cube,face).ro2,select_face(cube,face).ro3]
    return rows[row-1]
#This is the final and most useable function which takes Cube Name(Variable),Face no.,row no. and column no. to give the object of that column to be used to get the co_no or the colour(Which are the only functions I have managed to code till now)
def select_column(cube,face,row,column):
    columns=[(select_row(cube,face,row).co1),(select_row(cube,face,row).co2),(select_row(cube,face,row).co3)]
    return columns[column-1]



# This function gives me a formatted version of the cube
def readable_face(cube,face):
    return [[select_column(cube,face,1,1).colour,select_column(cube,face,1,2).colour,select_column(cube,face,1,3).colour],[select_column(cube,face,2,1).colour,select_column(cube,face,2,2).colour,select_column(cube,face,2,3).colour],[select_column(cube,face,3,1).colour,select_column(cube,face,3,2).colour,select_column(cube,face,3,3).colour]]



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
        returnstr+=show_face(cube,i)
    return(returnstr)


#Updating Storage
def update_storage():
    imported_cubes=(storage.importt(storage.filepath,'Testcube1.log'))
    for i in storage.importt(storage.filepath,'Testcube2.log'):
        imported_cubes.append(i)
    for i in imported_cubes:
        if i.cbname in storage.cubeBag:
            cubeAlreadyAdded(i)
        else:
            storage.cubeBag.append(i)

def cubeAlreadyAdded(i):
    print('{} is already added!'.format(i.cbname))