from tkinter import *

root = Tk()
root.title("Học control cơ bản")
root.resizable(height=True, width=True)
root.minsize(height=200, width=300)

Label(root, text="Hello Tkinter", fg="green").pack()
Button(root, text="Click me", command=root.quit).pack()
e = StringVar()
e.set("https://community.com")
Entry(root, textvariable=e, width=30).pack()

root.mainloop()
