import side
def temp_creation():
    c1=side.cube("Testcube1")
    c2=side.cube("Testcube2")
    side.select_column(c1,1,1,1).colour='Blue'
    side.select_column(c2,1,2,1).colour='Red'
    side.storage.exportt(c1,'','Testcube1.log')
    side.storage.exportt(c2,'','Testcube2.log')

def update_storage():
    imported_cubes=(side.storage.importt('','Testcube1.log'))
    for i in side.storage.importt('','Testcube2.log'):
        imported_cubes.append(i)
    for i in imported_cubes:
        if i.cbname in side.storage.cubebag:
            print('{} is already added!'.format(i.side.cbname))
        else:
            side.storage.cubebag.append(i)



update_storage()
oncube=side.chose_activecube(cubename='Testcube1',cubebag=side.storage.cubebag)
side.select_column(oncube,1,1,1).colour='Green'
side.storage.show_cubes(side.storage.cubebag)