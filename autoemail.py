from tkinter import *
import sys
import ezgmail,os

email_list = []

def send_email(address, header, message, attatchment):
    ezgmail.send(address,header,message,attatchment)

def confirm():
    print("Sent Email(s).")

def get_email():
    email_address = email_entry.get()
    if (email_address != ""):
        email_list.append(email_address)
        email_entry.delete(first = 0,last = END)
        email_listbox.insert(email_listbox.size() + 1,email_address)
    else:
        print("Empty Message")

#ctesarautoemail@gmail.com

os.chdir(r'/home/ctesar/VisualStudioCode/email')
ezgmail.init()

root = Tk()

frame = Frame(root, width = 1000, height = 600)
frame.pack()

#buttons
button_enter = Button(frame, text="Enter", command = get_email)
button_enter.grid(row = 2, column = 1)

#entries
email_entry = Entry(frame)
email_entry.grid(row = 0, column = 1 ,columnspan = 3)

#labels
email_entry_label = Label(frame, text = "Enter E-mail address")
email_entry_label.grid(row = 0, column = 0)

email_listbox_label = Label(frame, text = "E-mail List")
email_listbox_label.grid(row = 3, column = 0)

#listbox
email_listbox = Listbox(frame)
email_listbox.grid(row = 4, rowspan = 2, column = 0)


#packing
#button_enter.pack(side = BOTTOM)
#email_entry.pack(side = TOP)

root.mainloop()





