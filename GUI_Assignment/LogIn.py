from tkinter import *
from tkinter import messagebox


def MessageBox():
    OldPassword = stringOld.get()
    NewPassword = stringNew.get()
    EnterPassword = stringEnter.get()
    if NewPassword != EnterPassword:
        messagebox.showerror("Change Password Failed", "Your enter password is different from new password")
    if len(NewPassword) < 8 or len(NewPassword) > 24:
        messagebox.showerror("Change Password Failed", "Your password is too short! Please change password bigger than 8 - 24 characters")
    if NewPassword == EnterPassword and len(NewPassword) >= 8 and len(NewPassword) <= 24:
        messagebox.showinfo("Change Password Completed", "You have changed your password successful")


root = Tk()

stringOld = StringVar()
stringNew = StringVar()
stringEnter = StringVar()

root.title("Change Password")

Label(root, text="Old Password:").grid(row=1, column=0)
Entry(root, width=30, textvariable=stringOld, show="*").grid(row=1, column=1)

Label(root, text="New Password:").grid(row=2, column=0)
Entry(root, width=30, textvariable=stringNew, show="*").grid(row=2, column=1)

Label(root, text="Enter New Password:").grid(row=3, column=0)
Entry(root, width=30, textvariable=stringEnter, show="*").grid(row=3, column=1)

buttonOK = Button(root, padx=10, pady=2, bd=4, fg="Black", text="OK", command=MessageBox).grid(row=4, column=0,
                                                                                               rowspan=1)
buttonCancel = Button(root, padx=10, pady=2, bd=4, fg="Black", text="Cancel", command=root.quit).grid(row=4, column=1,
                                                                                                      rowspan=1)

root.mainloop()
