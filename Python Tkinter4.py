import tkinter

abc_root = tkinter.Tk()

abc_root.geometry("520x480")
w = tkinter.Label(text="First Image")
pic = tkinter.PhotoImage(file="2s3XhBY.png")
james = tkinter.Label(image=pic)
w.pack()
james.pack()

abc_root.mainloop()