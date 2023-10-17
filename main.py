import SimpleCubes as sc
cubebag=[]
def temp_creation():
    c1=sc.cube("Testcube1")
    c2=sc.cube("Testcube2")
    sc.select_column(c1,1,1,1).colour='Blue'
    sc.select_column(c2,1,2,1).colour='Red'
    global cubebag
    cubebag= sc.storage.cubeBag
def temp_show():
    oncube=sc.chose_activecube(cubebag,cubeName='Testcube1')
    sc.select_column(oncube,1,1,1).colour='Green'
    return(sc.storage.show_cubes(sc.storage.cubebag))