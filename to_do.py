from tkinter import *
from tkinter import ttk

class to_do:

	def __init__(self):
		#Window
		window = Tk()
		window.title("Stay Focused")
		window.configure(background = "#D7EAF7")
		window.geometry("400x600")

		#Label
		myLabel = Label(window,
						text = "To Do List",
						fg = "black",
						bg = "#D7EAF7",
						font= "System 40 bold italic")

		myLabel.pack(padx = 5,
					 pady = 5)

		#Text entry
		self.entryTxt = StringVar()
		myEntry = Entry(window,
						textvariable = self.entryTxt,
						width = 50)
		myEntry.pack(padx = 5,
					 pady = 5)

		#Button
		myButton = Button(text = "Enter",
						  width = 5,
						  height = 1,
						  bg = "white",
						  fg = "black",
						  command = self.clickHandle)
		myButton.pack(padx = 5,
					  pady = 5)
		myButton.bind("<Button-1>", self.clickHandle)

		#Output text
		self.outputTxt = StringVar()
		output = Label(window,
					   	   textvariable = self.outputTxt,
					   	   bg = "#D7EAF7")
		output.pack(padx = 5,
					pady = 5)

		#Main the program
		window.mainloop();

	#Button reaction event
	#Display text entered
	def clickHandle(self,event):
		inputTxt = self.entryTxt.get() #Get input
		outTxt = self.outputTxt.set(format(inputTxt))
		return outTxt



to_do()