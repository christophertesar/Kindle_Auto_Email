from tkinter import *
import sys
import ezgmail
import os
from os import listdir
from os.path import isfile, join


email_list = []
book_list = [file for file in listdir('/home/ctesar/VisualStudioCode/email/bookfolder') if isfile(join('/home/ctesar/VisualStudioCode/email/bookfolder', file))]


def send_email():
    for address in email_list:
        for book in book_list:
            print(address)
            print(book)
            ezgmail.send(address,'','', os.sep.join(['/home/ctesar/VisualStudioCode/email/bookfolder', book]))

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

canvas = Canvas(root, height=400, width=600)
canvas.pack()

background_image = PhotoImage(file='background_app.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth = 1, relheight = 1)

#frames

frame = Frame(root, bg= '#E46448', bd = 5)
frame.place(relx = 0.5 , rely = 0.1 , relwidth=0.75, relheight = 0.1, anchor='n')

frame_listbox = Frame(root, bg= '#E46448', bd = 5)
frame_listbox.place(relx = 0.3 , rely = 0.3 , relwidth=0.4, relheight = 0.6, anchor ='n')

frame_sendbox = Frame(root, bg= '#E46448', bd = 5)
frame_sendbox.place(relx = 0.85 , rely = 0.85 , relwidth=0.2, relheight = 0.1, anchor ='n')

#buttons
button_enter = Button(frame, text="Enter", command = get_email)
button_enter.place(relx = 0.85, rely = 0, relheight = 1, relwidth = 0.15)

button_send = Button(frame_sendbox, text="Send", command = send_email)
button_send.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)

#entries
email_entry = Entry(frame)
email_entry.place(relx = 0.325, rely = 0, relheight = 1 , relwidth = 0.5)

#labels
email_entry_label = Label(frame, text = "Enter E-mail address", bg = '#E46448')
email_entry_label.place(relx = 0, rely = 0, relheight = 1, relwidth = 0.3)

email_listbox_label = Label(frame_listbox, text = "E-mail List", bg = '#E46448')
email_listbox_label.place(relx = 0.25, rely = 0, relheight = 0.1, relwidth = 0.5)

#listbox
email_listbox = Listbox(frame_listbox)
email_listbox.place(relx = 0, rely = 0.15, relheight = 0.85, relwidth = 1)

root.mainloop()





