import tkinter 

james_root = tkinter.Tk()
james_root.title("Harrison GUI")
james_root.geometry("1020x920")

def function():
    pass

navigation_bar = tkinter.Menu(james_root)


menu_one = tkinter.Menu(navigation_bar, tearoff=0)

menu_one.add_command(label="New File", command=function)
menu_one.add_separator() #this keeps line between both of command in menu

menu_one.add_command(label="Open", command=function)
menu_one.add_command(label="Open Last Closed", command=function)
menu_one.add_separator() #this keeps line between both of command in menu

menu_one.add_command(label="Save", command=function)
menu_one.add_command(label="Save all", command=function)
menu_one.add_command(label="Save as", command=function)
menu_one.add_command(label="Revert", command=function)


menu_two = tkinter.Menu(navigation_bar, tearoff=0)
menu_two.add_command(label="Undo", command=function)
menu_two.add_command(label="Redo", command=function)
menu_two.add_separator() #this keeps line between both of command in menu
menu_two.add_command(label="Cut", command=function)
menu_two.add_command(label="Copy", command=function)
menu_two.add_command(label="Paste", command=function)
menu_two.add_command(label="Select All", command=function)
menu_two.add_separator() #this keeps line between both of command in menu
menu_two.add_command(label="Comment/Uncomment", command=function)
menu_two.add_command(label="Add block comment", command=function)
menu_two.add_command(label="Remove block comment", command=function)

james_root.config(menu=navigation_bar)
navigation_bar.add_cascade(label="File", menu=menu_one)

james_root.config(menu=navigation_bar)
navigation_bar.add_cascade(label="Edit", menu=menu_two)



james_root.mainloop()