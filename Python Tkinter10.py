import tkinter 


james_root = tkinter.Tk()
james_root.title("Harrison GUI")
james_root.geometry("1020x920")

#To make a function that can print a message while you click on button 

#Create a function
def welcome_to_coding_circle():
 tkinter.Label(text="Hello World").pack()
    

button = tkinter.Button(text="Click Me!!", command=welcome_to_coding_circle)
button.pack()

james_root.mainloop()