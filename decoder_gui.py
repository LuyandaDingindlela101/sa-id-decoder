from tkinter import *
from tkinter import messagebox


def get_details():
     import id_decode
     name = name_entry.get()
     id_number = id_number_entry.get()

     #    CHECK IF THE id_number IS EQUAL TO 13 NUMBERS 
     if len(id_number) == 13:
          #    CHECK IF THE id_number IS VALID, IF IT IS THEN RUNT TH EOTHER FUNCTIONS
          if id_decode.test_id_valid(id_number) == "valid":
               print(id_decode.get_dob(id_number[:6]))
               print(id_decode.get_gender(id_number[6:10]))
               print(id_decode.get_citizenship(id_number[10]))
               print(id_decode.get_age(id_decode.get_dob(id_number[:6])))
          #    IF THE id_number ISNT VALID, THEN INFORM THE USER
          else:
               messagebox.showerror("Id number", "Your id number id invalid")
     else:
               messagebox.showerror("Id number", "The provided id number does not meet the requirements")


window = Tk()
window.title("")
window.geometry("400x210")
window.title("SA Id Decoder")
window.config(bg="white")

heading_label = Label(window, text="Please enter your name and id number.", bg="white", font="15", fg="blue")
heading_label.place(x=50, y=15)

name_label = Label(window, text="Your Name: ", font="15", bg="white", fg="blue")
name_label.place(x=50, y=60)
name_entry = Entry(window, width=30, highlightthickness=0)
name_entry.place(x=150, y=60)

id_number_label = Label(window, text="Id Number: ", font="15", bg="white", fg="blue")
id_number_label.place(x=50, y=100)
id_number_entry = Entry(window, width=30, highlightthickness=0)
id_number_entry.place(x=150, y=100)

verify_button = Button(window, text="Verify Id", bg="white", highlightthickness=0, command=get_details)
verify_button.place(x=170, y=160)


window.mainloop()