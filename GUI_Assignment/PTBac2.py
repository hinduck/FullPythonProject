from math import *
from tkinter import *


def giaiAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    c = float(stringHSC.get())
    if a == 0:
        if b == 0 and c == 0:
            stringKQ.set("Vô số nghiệm")
        elif b == 0 and c != 0:
            stringKQ.set("Vô nghiệm")
        else:
            x = -c / b
            stringKQ.set("x =" + str(x))
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            stringKQ.set("Vô nghiệm")
        elif delta == 0:
            stringKQ.set("Nghiệm kép x1 = x2 =" + str(-b / (2 * a)))
        else:
            stringKQ.set("Nghiệm ở dưới!")
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            stringKQ1.set(str(x1))
            stringKQ2.set(str(x2))


def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")
    stringKQ1.set("")
    stringKQ2.set("")


root = Tk()
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()
stringKQ1 = StringVar()
stringKQ2 = StringVar()

root.title("PT bậc 2")
root.minsize(height=175, width=175)

Label(root, text="Phương trình bậc 2", fg="red", font=("Tahoma", 16)).grid(row=0, column=0, columnspan=2)
Label(root, text="Hệ số a:", font=11).grid(row=1, column=0)
Entry(root, width=20, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b:", font=11).grid(row=2, column=0)
Entry(root, width=20, textvariable=stringHSB).grid(row=2, column=1)

Label(root, text="Hệ số c:", font=11).grid(row=3, column=0)
Entry(root, width=20, textvariable=stringHSC).grid(row=3, column=1)

frameButton = Frame(root)
Button(frameButton, text="Giải", command=giaiAction, font=11, justify=CENTER).pack(side=LEFT)
Button(frameButton, text="Tiếp tục", command=tiepAction, font=11, justify=CENTER).pack(side=LEFT)
Button(frameButton, text="Thoát", command=root.quit, font=11, justify=CENTER).pack(side=LEFT)
frameButton.grid(row=4, columnspan=3)

Label(root, text="Kết quả:", font=14).grid(row=5, column=0)
Entry(root, width=20, textvariable=stringKQ).grid(row=5, column=1)
Label(root, text="Nghiệm x1:", font=11).grid(row=6, column=0)
Entry(root, width=20, textvariable=stringKQ1).grid(row=6, column=1)
Label(root, text="Nghiệm x2:", font=11).grid(row=7, column=0)
Entry(root, width=20, textvariable=stringKQ2).grid(row=7, column=1)

root.mainloop()