from tkinter import *

def Convert():
    DoF = float(Farenheit.get())
    Celcius.set((DoF - 32) / 1.8)

root = Tk()

Farenheit = StringVar()
Celcius = StringVar()

root.title("Chuyển đổi nhiệt độ")
# label_1 = Label(root, text="1. C --> F.", fg="black", font=("Digital-7", 14, "bold")).grid(column=0, row=1)
label_2 = Label(root, text="F --> C.", fg="Red", font=("Digital-7", 30, "bold")).grid(column=0, row=1)
# label_ask = Label(root, text="Choose 1 or 2?", fg="Red", font=("Digital-7", 18, "bold")).grid(column=0, row=3)
label_input = Label(root, text="F:", fg="black", font=("Digital-7", 11, "bold")).grid(column=0, row=2)
entry_input = Entry(root, insertwidth=2, textvariable=Farenheit, font=("Digital-7", 20, 'bold'), bg="Powder blue",
                    justify=LEFT, bd=18).grid(columnspan=3, column=1, row=2)

button_convert = Button(root, padx=8, pady=4, bd=3, text="Chuyển", command=Convert).grid(column=0, row=3)

label_output = Label(root, text="C", fg="black", font=("Digital-7", 11, "bold")).grid(column=0, row=4)
entry_output = Entry(root, insertwidth=2, textvariable=Celcius, font=("Digital-7", 20, 'bold'), bg="Powder blue",
                    justify=LEFT, bd=18).grid(columnspan=3, column=1, row=4)
# button_ask1 = Button(root, padx=5, pady=2, bd=4, text="1").grid(column=1, row=3)
# button_ask2 = Button(root, padx=5, pady=2, bd=4, text="2").grid(column=2, row=3)

root.mainloop()
