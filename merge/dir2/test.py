from Tkinter import *
top=Tk()
#top1=Tk()
Label(top, text="UserId").grid(row=0)
Label(top, text="User Name").grid(row=1)
Label(top, text="Domain").grid(row=2)
Label(top, text="Role").grid(row=3)
e1=Entry(top,bd=5)
e2=Entry(top,bd=5)
e3=Entry(top,bd=5)
e4=Entry(top,bd=5)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e4.grid(row=3,column=1)
e5.grid(row=5,column=1)
e6.grid(row=6,column=1)
e6.grid(row=6,column=1)
e6.grid(row=6,column=1)
e7.grid(row=7,column=1)
print("HELLO")
# print ("hello python")
top.mainloop()