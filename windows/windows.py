from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("First GUI Program")

icon = PhotoImage(file='windows/logo.png')
window.iconphoto(True, icon)
window.config(background="#42f590")  # set background color

window.mainloop()  # place window on computer screen, listen for events
