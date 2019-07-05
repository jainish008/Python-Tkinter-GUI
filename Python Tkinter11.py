import tkinter 


james_root = tkinter.Tk()
james_root.title("Harrison GUI")
james_root.geometry("1020x920")


#For creating an event where you left click, right click and midddle click on mouse 
#There will message printed on the screen

#Create function for each click
def left_click(event):
    tkinter.Label(text = "Left Click!!!").pack()

def middle_click(event):
    tkinter.Label(text = "Middle Click!!!!").pack()

def right_click(event):
    tkinter.Label(text = "Right Click!!!").pack()

#Now bind it 
james_root.bind("<Button-1>", left_click)
james_root.bind("<Button-2>", middle_click)
james_root.bind("<Button-3>", right_click)



james_root.mainloop()