import SimpleCubes as sc
def temp_creation():
    c1=sc.cube("Testcube1",(1,4,4))
    c2=sc.cube("Testcube2",(1,3,3))
    sc.select_column(c1,1,1,1).colour='Blue'
    sc.select_column(c2,1,2,1).colour='Red'
    sc.storage.exportt(c1, name='Testcube1.log')
    sc.storage.exportt(c2, name='Testcube2.log')

def temp_show():
    sc.storage.update_storage()
    oncube=sc.chose_activecube('Testcube1',sc.storage.cubebag)
    sc.select_column(oncube,1,1,1).colour='Green'
    return(sc.storage.show_cubes(sc.storage.cubebag))

temp_creation()
print(temp_show())