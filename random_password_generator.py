#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shubham
#
# Created:     20/02/2019
# Copyright:   (c) Shubham 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import tkinter as tk
window=tk.Tk()
window.geometry("400x400")
window.title("Greetings ________")

def password_generator():
    chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password1 = ''
    name=int(entry1.get())
    for c in range(name):
        password1+=random.choice(chars)

    return password1

def phrase_display():
    greeting=password_generator()

    #This creates text field
    greeting_display=tk.Text(master=window,height=10,width=30)
    greeting_display.grid(column=1,row=3)
    greeting_display.insert(tk.END,greeting)


#label
label1=tk.Label(text="Welcome to My App")
label1.grid(column=0,row=0)
label2=tk.Label(text="Enter the length of password")
label2.grid()

#entry
entry1=tk.Entry()
entry1.grid(column=1,row=1)

#button
button1=tk.Button(text="Click here",command=phrase_display)
button1.grid(column=1,row=2)
window.mainloop()
