from tkinter import *


def TinhBMI():
    height = float(stringHeight.get())
    weight = float(stringWeight.get())
    BMI = weight / (height ** 2)
    stringBMI.set(BMI)

    if stringBMI.set(BMI) < 18.5:
        stringStatus.set("Thin")
        stringWarning.set("Thấp")
    elif stringBMI.set(BMI) <= 24.9:
        stringStatus.set("Normal")
        stringWarning.set("Trung bình")
    elif stringBMI.set(BMI) <= 29.9:
        stringStatus.set("Not too fat")
        stringWarning.set("High")
    elif stringBMI.set(BMI) <= 34.9:
        stringStatus.set("Fat LV1")
        stringWarning.set("High")
    elif stringBMI.set(BMI) <= 39.9:
        stringStatus.set("Fat LV2")
        stringWarning.set("Very High")
    else:
        stringStatus.set("Fat LV3")
        stringWarning.set("Very Dangerous")


root = Tk()

stringHeight = StringVar()
stringWeight = StringVar()
stringBMI = StringVar()
stringStatus = StringVar()
stringWarning = StringVar()

root.title("Chỉ số BMI")

label_height = Label(root, text="height (cm):", font=("Digital-7", 18)).grid(column=0, row=0)
entry_height = Entry(root, insertwidth=4, font=("Digital-7", 14, "bold"), bg="Light pink", justify=LEFT, bd=18,
                     textvariable=stringHeight).grid(columnspan=2, column=1, row=0)

label_weight = Label(root, text="weight (cm):", font=("Digital-7", 18)).grid(column=0, row=1)
entry_weight = Entry(root, insertwidth=4, font=("Digital-7", 14, "bold"), bg="black", fg="White", justify=LEFT, bd=18,
                     textvariable=stringWeight).grid(columnspan=2, column=1, row=1)

button_solve = Button(root, padx=10, pady=4, bd=5, text="Calculate your BMI", font=("Arial", 10,), command=TinhBMI).grid(column=1, row=2)

label_BMI = Label(root, text="Your BMI:", font=("Digital-7", 18)).grid(column=0, row=3)
entry_BMI = Entry(root, insertwidth=4, font=("Digital-7", 14, "bold"), bg="Red", justify=LEFT, bd=18,
                  textvariable=stringBMI).grid(columnspan=2, column=1, row=3)

label_status = Label(root, text="Your status:", font=("Digital-7", 18)).grid(column=0, row=4)
entry_status = Entry(root, insertwidth=4, font=("Digital-7", 14, "bold"), bg="Gold", justify=LEFT, bd=18,
                     textvariable=stringStatus).grid(columnspan=2, column=1, row=4)

label_warning = Label(root, text="Your ability:", font=("Digital-7", 18)).grid(column=0, row=5)
entry_warning = Entry(root, insertwidth=4, font=("Digital-7", 14, "bold"), bg="Light Green", justify=LEFT, bd=18,
                      textvariable=stringWarning).grid(columnspan=2, column=1, row=5)

button_exit = Button(root, padx=10, pady=4, bd=5, text="Exit", font=("Arial", 10), command=root.quit).grid(column=2, row=2)

root.mainloop()
