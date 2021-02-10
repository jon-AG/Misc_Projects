import os
import pygame as p
import random as r
import sys

sys.path.append(os.path.join(os.getcwd(), 'Support'))
from build import toolbox
from .config import play_Music

class title_Screen():
    def __init__(self, screen, config_Paths, screen_X, screen_Y, paths):
        self.screen = screen
        self.config_Paths = config_Paths
        self.screen_X = screen_X
        self.screen_Y = screen_Y
        self.delay_count = 0 
        self.GIF_count = 0

        #Get center of screen
        center_Coordinates = toolbox.get_Center(self.screen)
        [self.center_X, self.center_Y] = [center_Coordinates.x, center_Coordinates.y]

        self.start_Btn = toolbox.button((0,255,0), -250, -200, 220, 80, 95, 'START')
        m_flag = 0
        while True:     
             
            self.change_BG()
            self.start_Btn.draw(self.screen)
            for event in p.event.get():
                pos = p.mouse.get_pos()
                if event.type == p.QUIT:
                    sys.exit()
                if event.type == p.MOUSEBUTTONDOWN:
                    if self.start_Btn.isOver(pos):
                        print("Put Level 1 Here")

            if self.delay_count == 1000:
                self.delay_count = 0

            p.display.update() 
            p.display.flip()

    def change_BG(self):
        #Keep changing the background to give the user epilepsy
        delay_Multiplier = 85
        if self.delay_count%delay_Multiplier == 0:

            #Load title images
            title_Image = p.image.load(os.path.join(self.config_Paths.pic_Path, 'title_Support.png'))      
            
            glasses_GIF_Path = os.path.join(self.config_Paths.GIF_Path, 'Glasses')
            GIF_Files = os.listdir(glasses_GIF_Path)
            if self.GIF_count == len(GIF_Files):
                self.GIF_count = 0

            title_BG = p.image.load(os.path.join(self.config_Paths.pic_Path, os.path.join(glasses_GIF_Path, GIF_Files[self.GIF_count])))
            self.GIF_count+=1
                
            #Set Background
            title_BG = p.transform.scale(title_BG, (self.screen_X, self.screen_Y))
            self.screen.blit(title_BG, (0, 0))

            #Change title color and coordinates
            color_Title = title_Image.convert_alpha()            
            
            [min_X, max_X, min_Y, max_Y] = [-self.center_X,self.center_X*2,-self.center_Y,self.center_Y*2]
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