from tkinter import *

# all colors
c0 = "#ffffff"
c1 = "#000000"
c2 = "#4456f0"

# configure
win = Tk()
win.title('PhoneBook | Md Rayhan Munshi')
win.geometry('485x450')
win['bg'] = c0
win.resizable(width=False,height=False)

# frames
frame_up = Frame(win, width=485,height=50, bg=c2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(win, width=485,height=150, bg=c0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(win, width=485,height=100, bg=c2)
frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)

# frame_up content
soft_name = Label(frame_up, text="PhoneBook", height=1, font=('montserrat 17 bold'), fg=c0, bg=c2)
soft_name.place(x=5,y=5)

#frame_down content
lvl_name = Label(frame_down, text="Name *", font=('montserrat 10'), width=20, height=1, anchor=NW)
lvl_name.place(x=10,y=20)






win.mainloop()