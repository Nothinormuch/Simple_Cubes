import SimpleCubes as sc
def temp_creation():
    c1=sc.cube("Testcube1")
    c2=sc.cube("Testcube2")
    sc.select_column(c1,1,1,1).colour='Blue'
    sc.select_column(c2,1,2,1).colour='Red'
    sc.storage.exportt(c1,'','Testcube1.log')
    sc.storage.exportt(c2,'','Testcube2.log')


sc.update_storage()
oncube=sc.chose_activecube(cubeName='Testcube1',cubeBag=sc.storage.cubeBag)
sc.select_column(oncube,1,1,1).colour='Green'
print(sc.storage.show_cubes(sc.storage.cubeBag))