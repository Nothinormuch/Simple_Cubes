import side
# c1=side.cube("Testcube")
# side.select_column(c1,1,2,1).colour='Red'
# name='Testcube.log'
# side.storage.exportt(c1,'',name)
def update_storage():
    imported_cubes=side.storage.importt('','testcube.log')
    for i in imported_cubes:
        if i.side.cbname in side.storage.cubebag:
            print('{} is already added!'.format(i.side.cbname))
        else:
            side.storage.cubebag.append(i)
update_storage
for i in side.storage.cubebag:
    side.show_allface(i)