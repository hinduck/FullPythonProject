from tkinter import *

def Convert():
    can = ['Canh', 'Tân', 'Nhâm,', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
    chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tí', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
    year = DuongLich.get()
    can_position = year % 10
    chi_position = year % 12
    AmLich.set(can[can_position] + " " + chi[chi_position])


root = Tk()
DuongLich = IntVar()
AmLich = StringVar()

root.title("Chuyển đổi năm")

DuongLich_Label = Label(root, text="Nhập năm dương lịch:").grid(column=0, row=1)
DuongLich_Entry = Entry(root, width=10, textvariable=DuongLich).grid(column=1, row=1)

DuongLich_Button = Button(root, padx=5, pady=2, bd=4, text="Chuyển", command=Convert).grid(column=1, row=2)

AmLich_Label = Label(root, text="Năm âm lịch:").grid(column=0, row=3)
AmLich_Entry = Entry(root, width=30, textvariable=AmLich).grid(column=1, row=3)

root.mainloop()
