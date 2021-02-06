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

        delay_count = 0 
        while True:     
             
            self.change_BG(delay_count)
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()
            delay_count+=1
            if delay_count == 1000:
                delay_count = 0

            p.display.update() 
            p.display.flip()

    def get_Paths(self):
        self.game_Path = os.path.dirname(os.path.realpath(__file__))
        self.music_Path = os.path.join(self.game_Path, 'Support', 'Music')

        self.pic_Path = os.path.join(self.game_Path, 'Support', 'Pictures')
    
    def create_Main_Screen(self):
        self.screen = p.display.set_mode((500,500))
        p.display.set_caption('Dumb Test')

    def play_Music(self):
        p.mixer.music.load(os.path.join(self.music_Path, 'opening_Theme.mp3'))
        p.mixer.music.play(-1) 

    def change_BG(self, delay_count):
        if delay_count%10 == 0:
            color_1 = r.randint(0,255)
            color_2 = r.randint(0,255)
            color_3 = r.randint(0,255)

            self.screen.fill((color_1, color_2, color_3))

            title_image = p.image.load(os.path.join(self.pic_Path, 'title.png'))
            main_title_mage = p.image.load(os.path.join(self.pic_Path, 'title_Main.png'))
            title_x = r.randint(-500,500)
            title_y = r.randint(-500,500)
        
            self.screen.blit(title_image, title_image.get_rect(center = self.screen.get_rect().center))
            self.screen.blit(main_title_mage, (title_x,title_y))

            
        return False
if __name__ == '__main__':
    run_Game()