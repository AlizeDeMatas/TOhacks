#import csv (later)
#popup that takes place every time a new habit is added

from tkinter import * #import for tkinder GUI
from tkinter import ttk #used for text and other options

#Boiler plate
class Root(Tk):
  def __init__(self):
    super(Root, self).__init__()
    #self.title("New habit") #Name yours accordingly
    #self.minsize(600, 400)  #Like that it doesn't need to be expanded
    #You'll need this to show options
    self.initUI()
    self.spinBox()

  def initUI(self):
    self.name = StringVar() #Collects input
    #Info, just text
    self.label = ttk.Label(self, text = "New habit")
    self.label.grid(column = 0, row = 0)
    #Text box that sends info to StringVar
    self.textbox = ttk.Entry(self, width = 40, textvariable = self.name)
    self.textbox.grid(column = 0, row = 1)
    #To deal with less chance of user error I used a spinbox
    #Will finish later
    #Button
    self.button = ttk.Button(self, text = "Done", command = self.done)
    self.button.grid(column = 0, row = 4)

  def spinBox(self):
    self.name = IntVar()
    self.label = ttk.Label(self, text= "Time (in minutes) dedicated to it")
    self.label.grid(column = 0, row = 2)
    self.spin = ttk.Spinbox(self, from_ = 15, to = 180, increment = 15.0)
    #I need help retrieving the value in the Spinbox
    self.spin.grid(column = 0, row = 3)

  def done(self):
    self.root.destroy()

root = Tk()
root.title("Stay Focused")
root.configure(background="#D7EAF7")
root.geometry("400x600")
theLabel = Label(root, text="Add new habit", background= "#D7EAF7", font="System 40 bold italic")
theLabel.pack()
root.mainloop()