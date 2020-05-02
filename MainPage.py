from tkinter import*

root = Tk()

theLabel = Label(root, text="Stay Focused")
theLabel.pack()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(text="My Schedule", fg="red")
button2 = Button(text="To Do List", fg="blue")
button3 = Button(text="Daily Schedule", fg="purple")

button1.pack()
button2.pack()
button3.pack()

root.mainloop()
root.maxsize(1000, 4000)
