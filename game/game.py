import binascii
from functools import partial
import tkinter as tk

class main():
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title('(EASY) Can you make it to the end?')
        
        self.grid_Frame = tk.Frame(self.root)
        self.grid_Frame.grid(row=0, column=0)
        self.reset_Frame = tk.Frame(self.root)
        self.reset_Frame.grid(row=1, column=0)

        action = partial(self.set_Spot, (4,2), ([(4,1),(4,3),(3,2)]))
        self.reset_Btn = tk.Button(self.reset_Frame,
                                   text = 'Reset',
                                   command = action)

        self.reset_Btn.grid(row=0,column=1)
        self.create_Btn_Grid()
        self.create_Paths()
        self.set_Spot((4,2), ([(4,1),(4,3),(3,2)]))
        self.root.mainloop()

    def create_Btn_Grid(self):

        # grid=[[4,2,2,3,3],
        #       [2,2,2,2,2],
        #       [3,2,2,2,2],
        #       [1,2,3,2,3],
        #       [3,2,2,2,0]]
        grid = [[2,2,4,1,3],
                [3,3,1,3,2],
                [1,2,0,2,3],
                [3,2,3,2,4],
                [4,2,1,3,2]]

        self.buttons = []

        for x in grid:
            row = []
            for y in x:
                row.append(tk.Button(self.grid_Frame,
                                         width=20,
                                         height=10,
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
                    if locs[0] < 0 or locs[0] > 4 or locs[1] < 0 or locs[1] > 4:
                        continue
                    else:
                        curr_locs.append(locs)
                action = partial(self.set_Spot, (x,y), curr_locs)
                self.buttons[x][y]['command'] = action

    def set_Spot(self, curr, idx): 
        self.buttons[2][2]['text'] = 0  
        if curr == (2,2):
            user_input = '1029384756'
            z= 0x31303239333834373536
            answer = binascii.unhexlify('{:x}'.format(z))
            answer = answer.decode('ascii')
            if user_input == answer:
                print('You Win!!')
            self.buttons[2][2]['text'] = 'You Win!!'

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
