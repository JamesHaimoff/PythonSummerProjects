import tkinter as tk

root =tk.Tk()

root.geometry("500x500")
root.title("Final Grade Calculator") #this is what its called when you open it
label = tk.Label(root, text = "Welcome to my Program: ", font= ('Times New Roman',18)) # lable is just the heading or title basically 
label.pack(padx = 20, pady = 20) #sizing of the header

textbox = tk.Text(root, height = 3 , font=('Times New Roman',16)) #use root almost like self, allows to write 3 lines of code
textbox.pack(padx=10,pady=10)

#similar to a textbox
# myentry = tk.Entry(root)
# myentry.pack()

# button = tk.Button(root, text= "Click Me!", font=('Times New Roman',16))
# button.pack(padx=10,pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)


btn1 = tk.Button(buttonframe, text="1",font=('Times New Roman',16)) #now root isnt the master it is the buttonframe that is what were using this inside of 
btn1.grid(row =0,column= 0,sticky = tk.W+tk.E) #first row and column bc 0 is 1
#just pase this for as many rows as needed
#NEED TO DO THIS LIKE 6 TIMES AND JUST CHANGE THE VALUE TO CHANGE THE LOCATIONS
#but this is the basic for a grid layout
buttonframe.pack(fill='x')
#using the grid layout I can literally make a full calculator 

anotherbutton = tk.Button(root,text="test")
anotherbutton.place(x=200,y=200,height = 100,width=100)


root.mainloop()