from tkinter import *

# button = you click it, then it does stuff

count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()

photo = PhotoImage(file='buttons/user.png')

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",  # font color
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,  # When the state is disable it won't be able to active
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()
