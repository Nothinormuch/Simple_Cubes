import side
def temp_creation():
    c1=side.cube("Testcube1")
    c2=side.cube("Testcube2")
    side.select_column(c1,1,1,1).colour='Blue'
    side.select_column(c2,1,2,1).colour='Red'
    side.storage.exportt(c1,'','Testcube1.log')
    side.storage.exportt(c2,'','Testcube2.log')


side.update_storage()
oncube=side.chose_activecube(cubename='Testcube1',cubebag=side.storage.cubebag)
side.select_column(oncube,1,1,1).colour='Green'
side.storage.show_cubes(side.storage.cubebag)