import pygame as p

class get_Center():
    def __init__(self, screen):
        screen_Rect = screen.get_rect()
        screen_Center = screen_Rect.center
        [self.x, self.y] = screen_Center

class button():
    def __init__(self, color, x_Offset, y_Offset, width, height, font_Size, text):
        self.color = color
        self.x_Offset = x_Offset
        self.y_Offset = y_Offset
        self.width = width
        self.height = height
        self.font_size = font_Size
        self.text = text

    def draw(self,screen):
        #Call this method to draw the button on the screen

        self.screen_rect = screen.get_rect()
        self.btn_Bkgrnd = p.Rect(0, 0, self.width, self.height)
        self.btn_Bkgrnd.center = (self.screen_rect.center[0] + self.x_Offset, self.screen_rect.center[1] + self.y_Offset)
        p.draw.rect(screen, self.color, self.btn_Bkgrnd)
        
        font = p.font.SysFont('comicsans', self.font_size)
        text = font.render(self.text, 1, (0,0,0))
        text_Center = text.get_rect(center = screen.get_rect().center)
        screen.blit(text, (text_Center[0] + self.x_Offset, text_Center[1] + self.y_Offset))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.btn_Bkgrnd.center[0] - self.width/2 and pos[0] < self.btn_Bkgrnd.center[0] + self.width/2:
            if pos[1] > self.btn_Bkgrnd.center[1] - self.height/2 and pos[1] < self.btn_Bkgrnd.center[1] + self.height/2:
                return True
            
        return False

class pic_Button():
    def __init__(self, color, x, y, width, height, font_Size, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_Size
        self.text = text

    def draw(self,screen,outline=None):
        #Call this method to draw the button on the screen

        self.screen_rect = screen.get_rect()
        self.btn_Bkgrnd = p.Rect(0, 0, self.width, self.height)
        self.btn_Bkgrnd.center = self.screen_rect.center
        p.draw.rect(screen, self.color, self.btn_Bkgrnd)
        
        font = p.font.SysFont('comicsans', self.font_size)
        text = font.render(self.text, 1, (0,0,0))
        screen.blit(text, text.get_rect(center = screen.get_rect().center))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True