from functools import partial
import tkinter as tk

class main():
    def __init__(self):
        self.winx = 6
        self.winy = 6
        self.root = tk.Tk()
        self.root.title('(HARD) Can you make it to the end?')
        
        self.grid_Frame = tk.Frame(self.root)
        self.grid_Frame.grid(row=0, column=0)
        self.reset_Frame = tk.Frame(self.root)
        self.reset_Frame.grid(row=1, column=0)

        action = partial(self.set_Spot, (0,0), ([(6,0),(0,6)]))
        self.reset_Btn = tk.Button(self.reset_Frame,
                                   text = 'Reset',
                                   command = action)

        self.reset_Btn.grid(row=0,column=1)
        self.create_Btn_Grid()
        self.create_Paths()
        self.set_Spot((0,0), ([(6,0),(0,6)]))
        self.root.mainloop()

    def create_Btn_Grid(self):

        # grid=[[4,2,2,3,3],
        #       [2,2,2,2,2],
        #       [3,2,2,2,2],
        #       [1,2,3,2,3],
        #       [3,2,2,2,0]]
        grid = [[6,3,2,4,6,2,5],
                [3,5,2,4,4,4,1],
                [3,3,2,3,3,4,2],
                [3,4,1,2,2,5,3],
                [4,4,4,2,3,2,4],
                [2,5,4,2,3,2,5],
                [3,5,2,1,4,4,0]]

        self.buttons = []

        for x in grid:
            row = []
            for y in x:
                row.append(tk.Button(self.grid_Frame,
                                         width=16,
                                         height=8,
                                         text = y))
            self.buttons.append(row)
        
        for x in range(len(self.buttons)):
            for y in range(len(self.buttons[x])):
                self.buttons[x][y].grid(row=x,column=y)

    def create_Paths(self):
        for x in range(len(self.buttons)):
            row_paths = []
            for y in range(len(self.buttons[x])):
                curr_locs = []
                neg_x = x - self.buttons[x][y]['text']
                pos_x = x + self.buttons[x][y]['text']
                neg_y = y - self.buttons[x][y]['text']
                pos_y = y + self.buttons[x][y]['text']

                poss_locs = [(neg_x,y),(pos_x,y),(x,neg_y),(x,pos_y)]
                for locs in poss_locs:
                    if locs[0] < 0 or locs[0] > len(self.buttons) or locs[1] < 0 or locs[1] > len(self.buttons[x]):
                        continue
                    else:
                        curr_locs.append(locs)
                action = partial(self.set_Spot, (x,y), curr_locs)
                self.buttons[x][y]['command'] = action

    def set_Spot(self, curr, idx): 
        self.buttons[self.winx][self.winy]['text'] = 0  
        if curr == (self.winx,self.winy):
            print('You Win!!!')
            self.buttons[self.winx][self.winy]['text'] = 'You Win!!'

        for x in range(len(self.buttons)):
            for y in range(len(self.buttons[x])):
                if (x,y) == curr:
                    self.buttons[x][y]['state'] = tk.DISABLED
                    self.buttons[x][y]['bg'] = 'lime green'
                elif (x,y) in idx:
                    self.buttons[x][y]['state'] = tk.NORMAL
                    self.buttons[x][y]['bg'] = 'grey'
                else:
                    self.buttons[x][y]['state'] = tk.DISABLED
                    self.buttons[x][y]['bg'] = 'white'

main()
