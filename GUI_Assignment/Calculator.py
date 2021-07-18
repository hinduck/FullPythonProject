from tkinter import *
from math import *


# Hàm bấm số
def press(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)


# Hàm Clear
def ClearDisplay():
    global expression
    expression = ""
    equation.set("")


# Hàm Xuất kết quả
def Equals():
    global expression
    sum_up = str(eval(expression))
    equation.set(sum_up)
    expression = ""


root = Tk()

# Tiêu đề
root.title("Calculator")
expression = ""
# Tính toán
equation = StringVar()
# Ô phép tính
textDisplay = Entry(root, insertwidth=4, textvariable=equation, font=("Digital-7", 20, 'bold'), bg="Powder blue",
                    justify=RIGHT, bd=30).grid(columnspan=4)
# Các số và phép toán
# Hàng 1:
btn7 = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="7", command=lambda: press(7)).grid(
    row=1, column=0)

btn8 = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="8", command=lambda: press(8)).grid(
    row=1, column=1)

btn9 = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="9", command=lambda: press(9)).grid(
    row=1, column=2)

btn_plus = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="+",
                  command=lambda: press("+")).grid(row=1, column=3)
# Hàng 2:
btn4 = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="4", command=lambda: press(4)).grid(
    row=2, column=0)

btn5 = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="5", command=lambda: press(5)).grid(
    row=2, column=1)

btn6 = Button(root, padx=16, pady=0, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="6",
              command=lambda: press(6)).grid(
    row=2, column=2)

btn_minus = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="-",
                   command=lambda: press("-")).grid(row=2, column=3)
# Hàng 3:
btn1 = Button(root, padx=20, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="1", command=lambda: press(1)).grid(
    row=3, column=0)

btn2 = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="2", command=lambda: press(2)).grid(
    row=3, column=1)

btn3 = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="3", command=lambda: press(3)).grid(
    row=3, column=2)

btn_multiply = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="*",
                      command=lambda: press("*")).grid(row=3, column=3)
# Hàng 4:
btn_dot = Button(root, padx=20, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text=".",
                 command=lambda: press(".")).grid(row=4, column=0)

btn0 = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="0", command=lambda: press(0)).grid(
    row=4, column=1)

btn_clear = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, "bold"), text="C",
                   command=ClearDisplay).grid(row=4, column=2)

btn_divide = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="/",
                    command=lambda: press("/")).grid(row=4, column=3)
# Hàng 5:
btn_equals = Button(root, padx=16, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="=", command=Equals).grid(
    row=5, column=3)
btn_exponent = Button(root, padx=12, bd=8, fg="Black", font=("Digital-7", 16, 'bold'), text="**",
                      command=lambda: press("**")).grid(
    row=5, column=2)

root.mainloop()
