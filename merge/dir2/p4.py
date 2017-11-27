#!/usr/bin/python

from Tkinter import *
import MySQLdb
import tkFont
import webbrowser

def call_gui():	

	root = Tk()
	root.geometry("400x300")
	root.title("Details")
	
	url='http://www.google.com'
	# Use a set of lists to hold each field of data
	user_ID = []
	user_name=[]
	Domain=[]
	Role=[]

	# Function to destroy tkinter window on clicking quit
	def button_click():
		root.destroy()

	# Function to open browser on clicking google button
	def OpenUrl():
		webbrowser.open_new(url)

	# Let's open a connection to a MySQL database
		
	try:
		db = MySQLdb.connect ("localhost","root","password","users")
		print("Connected")
		try:
			s = "Select * from details"
			cursor = db.cursor()
			cursor.execute(s)
			rows = cursor.fetchall()
			numrows = cursor.rowcount  #calculating no of rows in the given table
			print("Query executed successfully")
			print ("no of rows= ", numrows)
		except:
			print("Table doesn't exist")
	except:
		print("Connectivity error!!!..Try Again")

	# Put the Header Information on the Page
	BigFont=tkFont.Font(family="Arial", size=14, weight="bold")

	# Font for Big Labels
	HeaderFont = tkFont.Font(family="Arial", size=12, weight="bold")
	HLabel1 = Label(root, text = "Employee_ID  ", fg = "blue", font=HeaderFont).grid(row = 1, column = 0)
	HLabel2 = Label(root, text = "Employee_name  ", fg = "blue", font=HeaderFont).grid(row = 1, column = 1)
	HLabel3 = Label(root, text = " Domain  ", fg = "blue", font=HeaderFont).grid(row = 1, column = 2)
	HLabel4 = Label(root, text = "Role", fg = "blue", font=HeaderFont).grid(row = 1, column = 3)
	HLabelTop = Label(root, text= "Fetching data from table", font=BigFont, fg="red").grid(row=0,columnspan = 7)

	for i in range(numrows):
		#data = rows[i][0]
		myLabel = Label(root, text = rows[i][0])
		user_ID.append(myLabel)
		myLabel2 = Label(root, text = rows[i][1])
		user_name.append(myLabel2)
		myLabel3 = Label(root, text = rows[i][2])
		Domain.append(myLabel3)
		myLabel4 = Label(root, text = rows[i][3])
		Role.append(myLabel4)
		
	btn = Button(root, text = "Quit", command=button_click,height=1,width=3)
		
	# Force the system to put all of the controls on the window.
	print("Fetching and displaying data from database")
	for a in range(0,numrows):
		print rows[a]
		
	print("Displaying data on tkinter window")
	for a in range(numrows):
		user_ID[a].grid(row=a+3, column=0,)
		user_name[a].grid(row=a+3, column=1,)
		Domain[a].grid(row=a+3, column=2,)
		Role[a].grid(row=a+3, column=3)

	btn.grid(row=a+4,columnspan=6)
	btn1=Button(root, text="Google", command=OpenUrl,height=1,width=3).grid(row=a+4,column=2)

	# stop this program by clicking "Quit" button
	root.mainloop()
	db.close()

def main():

	call_gui()
	
	
		
if __name__ == '__main__':
    main()


