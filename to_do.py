from tkinter import *

inputTxt = ""
delOutTxt = ""

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

		#Add Text entry
		self.entryTxt = StringVar()
		self.myEntry = Entry(window,
						textvariable = self.entryTxt,
						width = 50)
		self.myEntry.pack(padx = 5,
					 	  pady = 5)

		#Add Button
		myButton = Button(text = "Enter",
						  width = 5,
						  height = 1,
						  bg = "white",
						  fg = "black",
						  command = self.clickHandle)
		myButton.pack(padx = 5,
					  pady = 5)
		myButton.bind("<Button-1>", self.clickHandle)

		#Delete Text entry
		self.delEntryTxt = StringVar()
		self.delEntry = Entry(window,
							  textvariable = self.delEntryTxt,
							  width = 50)
		self.delEntry.pack(padx = 5,
					 	   pady = 5)

		#Delete Button
		delButton = Button(text = "Delete",
						   width = 5,
						   height = 1,
						   bg = "white",
						   fg = "black",
						   command = self.delHandle)
		delButton.pack(padx = 5,
					   pady = 5)
		delButton.bind("<Button-2>", self.delHandle)

		#Output text label
		outputLabel = Label(window,
					   		text = "Not Done",
					   		bg = "#D7EAF7",
					   		font= "System 10 bold")
		outputLabel.pack(padx = 5,
						 pady = 5)

		#Output text
		self.outputTxt = StringVar()
		output = Label(window,
					   textvariable = self.outputTxt,
					   bg = "#D7EAF7")
		output.pack(padx = 5,
					pady = 5)

		#Done output text label
		delLabel = Label(window,
					   	 text = "Done",
					   	 bg = "#D7EAF7",
					   	 font= "System 10 bold")
		delLabel.pack(padx = 5,
					  pady = 5)

		#Done output text
		self.delTxt = StringVar()
		delOut = Label(window,
					   textvariable = self.delTxt,
					   bg = "#D7EAF7")
		delOut.pack(padx = 5,
					pady = 5)

		#Loop the program
		window.mainloop();

	#Button reaction event
	#Display text entered
	def clickHandle(self,event):
		global inputTxt 
		inputTxt = inputTxt + "\n" + self.entryTxt.get() #Get input
		outTxt = self.outputTxt.set(format(inputTxt)) #Copy input into output

		self.myEntry.delete(0, END) #Delete input
		return outTxt

	def delHandle(self,event):
		global delOutTxt
		delOutTxt = delOutTxt + "\n" + self.delEntryTxt.get() #Get input
		outTxt = self.delTxt.set(format(delOutTxt)) #Copy input into output
		return outTxt


to_do()
