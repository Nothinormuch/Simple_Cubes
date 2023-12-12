import TickTackToeRND as ttt
cube=ttt.sc.cube("Test")
window=ttt.tk.Tk()
client=ttt.instance(window, cube)
print(int(client.window.winfo_screenwidth()*(10/1536)))
client.config()