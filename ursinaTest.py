import ursina as engine
import math


def update():
    stats.text="Position: {}\n Rotation_x: {}\n Rotation_y: {}".format(cube1.y,math.cos((engine.time.time()*2*math.pi*omega[0])+math.pi*3/2)*a[1][0],cube1.rotation_y%180)
    # Backup: cube1.rotation=(math.cos(math.pi*(engine.time.time()/1.5))*20,cube1.rotation[1]+1.5,math.cos(math.pi*(engine.time.time()/1.5))*20)
    cube1.rotation=(math.cos((engine.time.time()*2*math.pi*omega[0])+math.pi)*a[1][0],cube1.rotation[1]+6*omega[1],-((engine.time.time()*2*math.pi*omega[2])+math.pi*3/2)*a[1][2])
    cube2.rotation=(math.cos(-math.pi*(engine.time.time()/1.5))*20,cube1.rotation[1]+1.5,-math.cos(math.pi*(engine.time.time()/1.5))*20)
    cube3.rotation=(math.cos(-math.pi*(engine.time.time()/1.5))*20,cube1.rotation[1]+1.5,math.cos(math.pi*(engine.time.time()/1.5))*20)

    cube1.y=((math.cos((engine.time.time()*neu)))*a[0])
    cube2.x=((math.cos((engine.time.time()*neu)-math.pi/3))*a[0])
    cube3.z=((math.cos((engine.time.time()*neu)+math.pi/3))*a[0])
    

app=engine.Ursina()

#Scene
Platform=engine.Entity(model="cube",scale=(15,0,15), position=(0,-3,0),rotation=(0,0,0),color=engine.color.rgb(11, 41, 66))
Wall1=engine.Entity(model="cube",scale=(15,15,0), position=(-7.5,4.5,0),rotation=(0,-90,0),color=engine.color.rgb(95, 126, 151))
Wall2=engine.Entity(model="cube",scale=(15,15,0), position=(7.5,4.5,0),rotation=(0,90,0),color=engine.color.rgb(95, 126, 151))
Wall3=engine.Entity(model="cube",scale=(15,15,0), position=(0,4.5,7.5),rotation=(0,0,0),color=engine.color.rgb(95, 126, 151))

#Main Objects
cube1=engine.Entity(model="cube",color=engine.color.cyan,texture='white_cube',rotation=(0,0,0),position=(0,0,0))
cube2=engine.Entity(model="cube",color=engine.color.lime,texture='white_cube',rotation=(0,0,0),position=(0,0,0))
cube3=engine.Entity(model="cube",color=engine.color.azure,texture='white_cube',rotation=(0,0,0),position=(0,0,0))


#Camera's Position
engine.camera.rotation=(0,0,0)
engine.camera.position=(0,0,-20)

#Angular Velocity
omega=(0.0625,0.0625,0)
#Frequency
neu=2
#Amplitude(linear,rotational(x,y,z))
a=(2,(30,0,0))
stats=engine.Text(text="Position: 0",position=(-0.6,-0.3,0))
app.run()