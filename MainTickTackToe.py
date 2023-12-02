import TickTackToeRND as ttt
cube=ttt.sc.cube("Test")
window=ttt.tk.Tk()
client=ttt.instance(window, cube)
client.config()