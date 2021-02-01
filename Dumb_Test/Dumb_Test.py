import tkinter as tk

class main():
    def __init__(self):
        """Main Window Configuration"""
        self.root = tk.Tk()
        self.root.title('Dumb_Test')
        self.root.geometry('500x500')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)

        #Create Begin button
        self.begin_Btn = tk.Button(self.root,
                                       width = 15,
                                       height = 2,
                                       text = 'Click to Begin!')
    
        self.begin_Btn.grid(row = 0, column = 0)

        """Main Loop"""
        self.root.mainloop()
main()