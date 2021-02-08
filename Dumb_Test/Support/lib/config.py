import os
import pygame as p

class get_Paths():
    def __init__(self, file):
        self.game_Path = os.path.dirname(os.path.realpath(file))
        self.music_Path = os.path.join(self.game_Path, 'Support', 'Media', 'Music')
        self.pic_Path = os.path.join(self.game_Path, 'Support', 'Media', 'Pictures')
        self.GIF_Path = os.path.join(self.game_Path, 'Support', 'Media', 'GIF')

class play_Music():
    def __init__(self, music_Path, song):
        p.mixer.music.load(os.path.join(music_Path, song))
        p.mixer.music.play(-1) 