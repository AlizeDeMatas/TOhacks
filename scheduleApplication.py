from tkinter import*
#
import tk
# from self import self
#
#
# class SchedulePage(tk.Frame):
#     def __init__(self, parent, controller):
#     tk.Frame.__init__(self,parent)
#



# main frame
root = Tk()
root.title("Stay Focused")
root.configure(background="#D7EAF7")
root.geometry("400x600")

theLabel = Label(root, text="My Schedule for:", background= "#D7EAF7", font="System 40 bold italic")
theLabel.pack()

Label0 = Label(root, text="Monday, May 3, 2020", background="#D7EAF7", font="System 20 bold ")
Label0.pack()

Label1 = Label(root, text="1. Yoga at 2:00pm - 2:30pm", background= "red", font="Times 20 bold italic")
Label1.pack()

Label2 = Label(root, text="2. Calculus Lecture at 4:00pm - 6:00pm", background= "#D7EAF7", font="Times 20 bold italic")
Label2.pack()

Label3 = Label(root, text="3. Baking Sour Dough Bread at 6:30", background= "#D7EAF7", font="Times 20 bold italic")
Label3.pack()

Label4 = Label(root, text="4. Research Paper at 7:30pm - 9:30pm", background= "#D7EAF7", font="Times 20 bold italic")
Label4.pack()

Label5 = Label(root, text="5. Daily Coding Challenge from LeetCode at 10pm", background= "#D7EAF7", font="Times 18 bold italic")
Label5.pack()

Label5 = Label(root, text=" Schedule for this month", background= "#D7EAF7", font="Times 25 bold ")
Label5.pack()

photo = PhotoImage(file="Calendar.png")
labelP=Label(root,image=photo,background= "#D7EAF7")
labelP.place(x=40,y=280)


button1 = Button(text="Next Month", fg="blue")
button2 = Button(text="Previous Month", fg="blue")

button1.place(relx=0.8, rely=0.9, anchor=CENTER, width=120, height=40)
button2.place(relx=0.18, rely=0.9, anchor=CENTER, width=120, height=40)


root.mainloop()
root.maxsize(1000, 4000)