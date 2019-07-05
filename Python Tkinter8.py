import tkinter 


james_root = tkinter.Tk()
james_root.title("Harrison GUI")
james_root.geometry("1020x920") 
#Adding Button in the GUI

abc = tkinter.Label(text = "This is Harrison Button", fg = "white", bg = "purple")
button = tkinter.Button(text = "Button", fg = "red")
defg = tkinter.Label(text = "This left Y fill", fg="white", bg="black")

abc.pack()
button.pack()
defg.pack(fill="y", side="left")
james_root.mainloop()