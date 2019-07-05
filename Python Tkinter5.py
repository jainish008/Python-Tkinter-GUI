import tkinter
#for jpg image
from PIL import Image, ImageTk

abc_root = tkinter.Tk()

abc_root.geometry("520x480")
w = tkinter.Label(text="Second Image")
#for jpg image
image = Image.open("abc.jpg")
photo = ImageTk.PhotoImage(image)
abc_label = tkinter.Label(image=photo)
w.pack()
abc_label.pack()


abc_root.mainloop()