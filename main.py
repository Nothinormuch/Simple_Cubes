import side
c1=side.cube("Testcube")
side.select_column(c1,1,2,1).colour='Red'
name=input('Enter the name of the cube- ')
side.storage.exportt(c1,'',name)