import os
import pygame as p
import random as r
import sys

class run_Game():
    def __init__(self):
        #Initial Configurations
        p.init()
        self.get_Paths()
        self.create_Main_Screen()
        self.play_Music()

        while True:      
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()

        p.display.flip()

    def get_Paths(self):
        self.game_Path = os.path.dirname(os.path.realpath(__file__))
        self.music_Path = os.path.join(self.game_Path, 'Support', 'Music')
    
    def create_Main_Screen(self):
        p.display.set_mode((500,500))
        p.display.set_caption('Dumb Test')

    def play_Music(self):
        p.mixer.music.load(os.path.join(self.music_Path, 'opening_Theme.mp3'))
        p.mixer.music.play(-1) 

if __name__ == '__main__':
    run_Game()