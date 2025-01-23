from tkinter import *
from PIL import Image , ImageTK

root = Tk()
root.title('image')
root.geometry('500x600')

upload = Image.open('dragun.jpg')

image = ImageTK.PhotoImage(upload)

label = Label(root , image= image , height = 400 , width = 500)
label.place(x=60 , y=20)
label2 = Label(root, text="This is how you add an image")
label2.place(x=90,y=340)

root.mainloop()