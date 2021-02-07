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

        self.delay_count = 0 
        self.GIF_count = 0
        while True:     
             
            self.change_BG()
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()
            if self.delay_count == 1000:
                self.delay_count = 0

            p.display.update() 
            p.display.flip()

    def get_Paths(self):
        self.game_Path = os.path.dirname(os.path.realpath(__file__))
        self.music_Path = os.path.join(self.game_Path, 'Support', 'Music')
        self.pic_Path = os.path.join(self.game_Path, 'Support', 'Pictures')
        self.GIF_Path = os.path.join(self.game_Path, 'Support', 'GIF')
    
    def create_Main_Screen(self):
        self.screen_X = 800
        self.screen_Y = 500
        self.screen = p.display.set_mode((self.screen_X, self.screen_Y))
        p.display.set_caption('Dumb Test')

    def play_Music(self):
        p.mixer.music.load(os.path.join(self.music_Path, 'opening_Theme.mp3'))
        p.mixer.music.play(-1) 

    def change_BG(self):
        #Keep changing the background to give the user epilepsy
        delay_Multiplier = 85
        if self.delay_count%delay_Multiplier == 0:
            #Get center of screen
            screen_Rect = self.screen.get_rect()
            screen_Center = screen_Rect.center
            [center_X, center_Y] = screen_Center


            #Load title images
            title_Image = p.image.load(os.path.join(self.pic_Path, 'title_Support.png'))      
            
            glasses_GIF_Path = os.path.join(self.GIF_Path, 'Politician')
            GIF_Files = os.listdir(glasses_GIF_Path)
            if self.GIF_count == len(GIF_Files):
                self.GIF_count = 0

            title_BG = p.image.load(os.path.join(self.pic_Path, os.path.join(glasses_GIF_Path, GIF_Files[self.GIF_count])))
            self.GIF_count+=1
                
            #Set Background
            title_BG = p.transform.scale(title_BG, (self.screen_X, self.screen_Y))
            self.screen.blit(title_BG, (0, 0))

            #Change title color and coordinates
            color_Title = title_Image.convert_alpha()            
            
            [min_X, max_X, min_Y, max_Y] = [-center_X,center_X*2,-center_Y,center_Y*2]
            [title_X, title_Y] = self.random_Coordinates(min_X, max_X, min_Y, max_Y)
            [title_X2, title_Y2] = self.random_Coordinates(min_X, max_X, min_Y, max_Y)
            [title_X3, title_Y3] = self.random_Coordinates(min_X, max_X, min_Y, max_Y)

            color_Title = self.change_Color(color_Title, self.random_Color())
            self.screen.blit(color_Title, (title_X, title_Y))
            color_Title = self.change_Color(color_Title, self.random_Color())
            self.screen.blit(color_Title, (title_X2, title_Y2))
            color_Title = self.change_Color(color_Title, self.random_Color())
            self.screen.blit(color_Title, (title_X3, title_Y3))

        self.delay_count += 1   

    
    def random_Color(self):
        color_1 = r.randint(0,255)
        color_2 = r.randint(0,255)
        color_3 = r.randint(0,255)
        return (color_1, color_2, color_3)

    def change_Color(self, image, color):
        coloured_Image = p.Surface(image.get_size())
        coloured_Image.fill(color)
    
        finalImage = image.copy()
        finalImage.blit(coloured_Image, (0, 0), special_flags = p.BLEND_MULT)
        return finalImage
    
    def random_Coordinates(self, min_X, max_X, min_Y, max_Y):
        x = r.randint(min_X, max_X)
        y = r.randint(min_Y, max_Y)
        return [x,y]

if __name__ == '__main__':
    run_Game()