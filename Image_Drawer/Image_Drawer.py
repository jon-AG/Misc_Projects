import numpy as np
from PIL import Image
import pyautogui
import time
import pygame as p
import sys
import keyboard
import win32api, win32con
import random

# def pygame_Draw():
#     p.init()
#     gim = Image.open('rock.png').convert('1')
#     gim=gim.convert('RGB')
#     a=[]
#     b=[]

#     s=((gim.size))
#     #plt.ion()
#     #plt.show() 
#     screen = p.display.set_mode((s[0], s[1]))
#     p.display.set_caption('Lets Draw')

#     screen.fill((255,255,255))
#     while True:     
#         for x in range(0,s[0]):
#             for y in range(0,s[1]):
#                 c = gim.getpixel((x,y))
#                 if c == (255,255,255):
#                     continue
#                 screen.set_at((x, y), c)
#                 p.display.update() 

#         for event in p.event.get():
#             if event.type == p.QUIT:
#                 sys.exit()
#         p.display.update() 

# def paint():
#     pyautogui.pause=0.01
#     gim = Image.open('rock.png').convert('1')
#     gim = gim.convert('RGB')
#     gim.save('testrock.png')
#     a=[]
#     b=[]

#     s=((gim.size))
#     time.sleep(2)


#     for x in range(0,s[0]):
#         for y in range(0,s[1]):
#             if keyboard.is_pressed('q'):
#                 sys.exit()
#             c = gim.getpixel((x,y))
#             if c == (255,255,255):
#                 continue
#             #pyautogui.click(x=x+200,y=y+200)
#             x1=x+200
#             y1=y+200
#             win32api.SetCursorPos((x1,y1))
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x1,y1,0)
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x1,y1,0,0)
#             time.sleep(0.0001)

def rand_paint():
    gim = Image.open('face.png').convert('1')
    gim = gim.convert('RGB')

    s=((gim.size))
    
    while True:
        if keyboard.is_pressed('s'):
            break
    all_Coords = []
    for x in range(0,s[0]):
        for y in range(0,s[1]):
            all_Coords.append((x,y))

    random.shuffle(all_Coords)
    b=0
    w=0

    for coord in all_Coords:
        c = gim.getpixel((x,y))
        if c == (255,255,255):
            w+=1
        elif c == (0,0,0):
            b+=1
    if w >= b:
        skipC= (255,255,255)
    elif b > w:
        skipC= (0,0,0)

    for coord in all_Coords:
        (x,y) = coord
        if keyboard.is_pressed('q'):
            sys.exit()
        c = gim.getpixel((x,y))
        if c == skipC:
            continue
        #pyautogui.click(x=x+200,y=y+200)
        x1=x+200
        y1=y+200
        win32api.SetCursorPos((x1,y1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x1,y1,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x1,y1,0,0)
        time.sleep(0.0001)

rand_paint()