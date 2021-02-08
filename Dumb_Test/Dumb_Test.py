import pygame as p
import os
from Support.lib import config, levels

class run_Game():
    def __init__(self):
        #Initial Configurations
        p.init()
        self.config_Paths = config.get_Paths(__file__)
        self.create_Main_Screen()
        self.play_Music()

        levels.title_Screen(self.screen, self.config_Paths, self.screen_X, self.screen_Y)
        
    def create_Main_Screen(self):
        self.screen_X = 800
        self.screen_Y = 500
        self.screen = p.display.set_mode((self.screen_X, self.screen_Y))
        p.display.set_caption('Dumb Test')

    def play_Music(self):
        p.mixer.music.load(os.path.join(self.config_Paths.music_Path, 'opening_Theme.mp3'))
        p.mixer.music.play(-1) 

if __name__ == '__main__':
    run_Game()