import side
c1=side.cube("Testcube1")
c2=side.cube("Testcube2")
side.select_column(c1,1,1,1).colour='you can\'t see me'
side.select_column(c2,1,2,1).colour='Red'
side.storage.exportt(c1,'','Testcube1.log')
side.storage.exportt(c2,'','Testcube2.log')
def update_storage():
    imported_cubes=(side.storage.importt('','Testcube1.log')).extend(side.storage.importt('','Testcube2.log'))
    for i in imported_cubes:
        if i.cbname in side.storage.cubebag:
            print('{} is already added!'.format(i.side.cbname))
        else:
            side.storage.cubebag.append(i)

update_storage()
for i in side.storage.cubebag:
    side.show_allface(i)