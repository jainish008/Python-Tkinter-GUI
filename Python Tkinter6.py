import tkinter 


james_root = tkinter.Tk()
james_root.title("Harrison GUI")
#Paragraph in Label and background color.
para_label = tkinter.Label(text ='''Some Tk widgets, like the label, text,\n and canvas widget, 
allow you to \n specify the fonts used to display text. This can be achieved by setting 
the attribute \n "font". typically via a "font" configuration option. You have to consider
that fonts are \n none of several areas that are not platform-independent. 
The attribute fg \n can be used to have the text in another colour and the attribute bg 
can be used to change \n the background colour of the label.''', bg="red", font=("times new roman", 20 ,"bold"), 
borderwidth=3
)
para_label.pack()

james_root.mainloop()