from tkinter import *


def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")


def giaiAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    if a == 0 and b == 0:
        stringKQ.set("Vô số nghiệm")
    elif a == 0 and b != 0:
        stringKQ.set("Vô nghiệm")
    else:
        stringKQ.set("x =" + str((-b / a)))


root = Tk()

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

root.title("Giải phương trình bậc 1")
root.minsize(height=130, width=200)
root.resizable(height=True, width=True)

Label(root, text="Giải phương trình bậc 1 nè mấy thằng ngu", fg="Violet", font=("Bahnschrift SemiBold", 20),
      justify=CENTER).grid(row=0, columnspan=2)
Label(root, text="Hệ số a: ", font=14, justify=CENTER).grid(row=1, column=0)
Entry(root, width=45, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b: ", font=14, justify=CENTER).grid(row=2, column=0)
Entry(root, width=45, textvariable=stringHSB).grid(row=2, column=1)

frameButton = Frame()
Button(frameButton, text="Giải", command=giaiAction, font=11, justify=CENTER).pack(side=LEFT)
Button(frameButton, text="Tiếp tục", command=tiepAction, font=11, justify=CENTER).pack(side=LEFT)
Button(frameButton, text="Thoát", command=root.quit, font=11, justify=CENTER).pack(side=LEFT)
frameButton.grid(row=3, columnspan=2)

Label(root, text="Kết quả", font=14).grid(row=4, column=0)
Entry(root, width=45, textvariable=stringKQ).grid(row=4, column=1)

root.mainloop()
