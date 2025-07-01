from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='labels/user.png')

label = Label(window,
              text="Hello World!",
              font=('Times New Roman', 40, 'bold'),
              fg='#42f590',
              bg='#b042f5',
              relief=RAISED,  # SUNKEN
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
# label.lace(x=0,y=0)#place the label at a specific position

window.mainloop()
