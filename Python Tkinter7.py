import tkinter 

james_root = tkinter.Tk()
james_root.title("Harrison GUI")
james_root.geometry("1020x920")
f1 = tkinter.Frame(james_root, bg="blue", borderwidth= 3)
f1.pack()

para = tkinter.Label(f1, text="Hello World")

para.pack()

james_root.mainloop()


