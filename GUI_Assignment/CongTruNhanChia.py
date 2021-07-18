from tkinter import *


def AdditionAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a + b)


def MinusAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a - b)


def MultiAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a * b)


def DivisionAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a / b)


root = Tk()
stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

root.title("4 phép tính cơ bản")
root.minsize(height=150, width=200)

Label(root, text="Cộng trừ nhân chia", fg="Blue", font=("tahoma", 18)).grid(row=0, columnspan=3)
frameButton = Frame(root)
Button(frameButton, text="Cộng", command=AdditionAction).pack(side=BOTTOM, fill=X)
Button(frameButton, text="Trừ", command=MinusAction).pack(side=BOTTOM, fill=X)
Button(frameButton, text="Nhân", command=MultiAction).pack(side=BOTTOM, fill=X)
Button(frameButton, text="Chia", command=DivisionAction).pack(side=BOTTOM, fill=X)
frameButton.grid(row=1, column=0, rowspan=4)

Label(root, text="A:").grid(row=1, column=1)
Entry(root, width=15, textvariable=stringA).grid(row=1, column=2)

Label(root, text="B:").grid(row=2, column=1)
Entry(root, width=15, textvariable=stringB).grid(row=2, column=2)

Label(root, text="Kết quả:").grid(row=3, column=1)
Entry(root, width=15, textvariable=stringKQ).grid(row=3, column=2)

Button(root, text="Thoát", command=root.quit).grid(row=4, column=2)

root.mainloop()
