import tkinter as tk

class mygui:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text = "Your message",font=('Times New Roman',16))
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root,height = 5, font=('Times New Roman',16))
        self.textbox.pack(padx=10,pady=10)

        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root,text = "Show MessageBox",font=('Times New Roman',16), variable = self.check_state)
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root, text = "Show message",font=('Times New Roman',16),command = self.showmessage)
        self.button.pack(padx=10,pady=10)

        self.root.mainloop()
    
    def showmessage(self):
        print(self.check_state.get()) 


mygui()