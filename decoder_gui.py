from tkinter import *
from tkinter import messagebox

def get_details():
     print("something")


window = Tk()
window.title("")
window.geometry("400x210")
window["background"] = ["white"]
window.resizable(False, False)


heading_label = Label(window, text="Please enter your Name and ID number.", bg="white", font="15")
heading_label.place(x=50, y=15)

name_label = Label(window, text="Your Name: ", font="15", bg="white")
name_label.place(x=50, y=60)
name_entry = Entry(window, width=20, highlightthickness=0)
name_entry.place(x=150, y=60)

id_no_label = Label(window, text="ID Number: ", font="15", bg="white")
id_no_label.place(x=50, y=100)
id_no_entry = Entry(window, width=20, highlightthickness=0)
id_no_entry.place(x=150, y=100)

verify_button = Button(window, text="Verify", bg="white", highlightthickness=0, command=get_details)
verify_button.place(x=170, y=160)


window.mainloop()