import tkinter 


james_root = tkinter.Tk()
james_root.title("Harrison GUI")
james_root.geometry("1020x920")
james_root.configure(background="grey")

#Making of simple form with the help of grid
abc = tkinter.Label(text = "This is Harrison Form", fg = "white", bg = "purple").grid(row=0)
#Add title 
head = tkinter.Label(text = "First Name").grid(row = 1)
space = tkinter.Label(text = "Last Name").grid(row = 2)
email = tkinter.Label(text = "Email-ID").grid(row = 3)
#Then decide the value that will be input in that title 
headvalue = tkinter.StringVar()
spacevalue = tkinter.StringVar()
emailvalue = tkinter.StringVar()

#Making box for entering the user information
headentry = tkinter.Entry(james_root, textvariable="headvalue").grid(row = 1, column=1)
spaceentry = tkinter.Entry(james_root, textvariable="spacevalue").grid(row = 2, column=1)
emailentry = tkinter.Entry(james_root, textvariable="emailvalue").grid(row = 3, column=1)

keepup = tkinter.Checkbutton(james_root, text = "Keep Me Logged In").grid(columnspan = 2)

#Submit Button in the form
button = tkinter.Button(text="Submit").grid(row=5,column=1)

james_root.mainloop()