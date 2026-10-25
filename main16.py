
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

name = Tk()
name.title("Shadow Fight 4: The Arena!")
name.configure(bg='purple')
name.geometry('750x500')

upload = Image.open('Shadow Fight 4.png')
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(name, image=image, bg="#eb61e6")
label.place(x=180, y=20)

label1 = Label(
    name,
    text='when I was found people used me\n'
         'they experimented on me\n'
         'they tried to control me\n'
         'but now with all that knowledge I evolved\n'
         'for I am the shadow',
    bg='#ee82ee'
)
label1.place(x=0.5, y=340)

fight_started = False

def msg():
    global fight_started
    fight_started = True
    messagebox.showwarning("Read", "Shadow boss is coming lvl 200")

def kethan2():
    if fight_started == False:
        messagebox.showwarning("Warning!", "You must click 'See Danger' first!")
    else:
        messagebox.showinfo("Congratulations", "You have defeated the shadow boss!!")

button1 = Button(
    name,
    text="See Danger",command=msg,bg='#dda0dd',fg='#6a5acd')
button1.place(x=260, y=360)

button2 = Button(
    name,text="Click to fight boss",command=kethan2,bg='#dda0dd',fg='#6a5acd')
button2.place(x=260, y=395)

name.mainloop()