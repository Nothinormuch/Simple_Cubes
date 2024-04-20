import SimpleCubes as sc
sc.storage.storageMode="database"
def temp_creation():
    c1=sc.cube("Testcube1",(1,3,3))
    c2=sc.cube("Testcube2",(1,10,10))
    c3=sc.cube.create_Rubik_Cube()
    sc.select_column(c1,1,1,1).colour='Blue'
    sc.select_column(c2,1,2,1).colour='Red'
    sc.storage.exportt(c1, name='Testcube1.log')
    sc.storage.exportt(c2, name='Testcube2.log')
    sc.storage.exportt(c3, name='Testcube.log')

def temp_show():
    sc.storage.update_storage(file_path="")
    oncube=sc.chose_activecube("Rubik's Cube",sc.storage.cubebag)
    sc.select_column(oncube,1,1,1).colour='Green'
    return(sc.show_cubes(sc.storage.cubebag))

temp_creation()
print(temp_show())