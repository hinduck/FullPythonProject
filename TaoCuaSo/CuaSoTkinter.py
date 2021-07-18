from tkinter import *

from CenterLibrary import MakeCenter

root = Tk()
root.title("League of Legends")
root.resizable(height=True, width=True)
root.minsize(height=300, width=500)
root.mainloop()
MakeCenter(root)
root.mainloop()
