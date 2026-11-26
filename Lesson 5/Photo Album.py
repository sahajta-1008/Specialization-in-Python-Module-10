from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window=Tk()
window.title("My Photo Album")
window.geometry("400x420")

title=Label(window,text="My Photo Album",bg="lightblue",fg="black")
img=Image.open("Blue Flower.jpeg")
img=img.resize((300,280))
photo=ImageTk.PhotoImage(img)
pic=Label(window,image=photo)
pic.pack(pady=5)

def ShowMessage():
    messagebox.showinfo("Great! ","You Clicked the photo")

btn=Button(window,text="Click to react",bg="darkblue",fg="white",command=ShowMessage)
btn.pack(pady=5)

def ShowDetails():
    top=Toplevel(window)
    top.title("Photo Details")
    top.geometry("200x120")
    info=Label(top,text="Taken from : Google")
    info.pack(pady=10)
    place=Label(top,text="These roses are very rare")
    place.pack()
    top.mainloop()

details=Button(window,text="See Details",bg="darkgreen",fg="white",command=ShowDetails)
details.pack(pady=5)

window.mainloop()