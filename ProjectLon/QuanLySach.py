from tkinter import *
from tkinter import messagebox

from XuLyFile import *

def Add():
    line = stringMa.get() + ";" + stringTen.get() + ";" + stringNam.get()
    SaveFile(line)
    stringTen.set("")
    stringMa.set("")
    stringNam.set("")
    ShowBook()

def ShowBook():
    arrSach = ReadFile()
    listbox.delete(0, END)
    for item in arrSach:
        listbox.insert(END, item)

def Sort():
    arrSach = ReadFile()
    for i in range(len(arrSach)):
        for j in range(len(arrSach)):
            a = arrSach[i]
            b = arrSach[j]
            if a[2] > b[2]:
                arrSach[i] = b
                arrSach[j] = a
    listbox.delete(0, END)
    for item in arrSach:
        listbox.insert(END, item)

def Search():
    arrSach = ReadFile()
    ma = stringMa.get()
    found = False
    for sach in arrSach:
        if sach[0] == ma:
            found = True
            break
        if found:
            messagebox.showinfo("Tìm sách", "Tìm thấy sách bạn yêu cầu")
        else:
            messagebox.showwarning("Tìm sách", "Không tìm thấy sách bạn yêu cầu")

root = Tk()

stringMa = StringVar()
stringTen = StringVar()
stringNam = StringVar()

root.title("Quản lý sách")
root.minsize(height=300, width=320)
label_title = Label(root, text="Quản lý sách", fg="blue", font=("Cambria", 18)).grid(row=0, columnspan=2)
listbox = Listbox(root, width=60)
listbox.grid(row=1, columnspan=2)
ShowBook()

Label(root, text="Mã sách:").grid(row=2, column=0)
Entry(root, width=30, textvariable=stringMa).grid(row=2, column=1)

Label(root, text="Tên sách:").grid(row=3, column=0)
Entry(root, width=30, textvariable=stringTen).grid(row=3, column=1)

Label(root, text="Năm xuất bản:").grid(row=4, column=0)
Entry(root, width=30, textvariable=stringNam).grid(row=4, column=1)

frameButton = Frame(root)
button_Add = Button(frameButton, text="Thêm", command=Add).pack(side=LEFT)
button_Add = Button(frameButton, text="Tìm", command=Search).pack(side=LEFT)
button_Add = Button(frameButton, text="Sắp xếp", command=Sort).pack(side=LEFT)
button_Add = Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=5, column=1)

root.mainloop()