import pygame as pg
import random
import os
from enum import Enum
import numpy as np


red_color = (200,20,30)
black_color = (20,20,20)
color_light = (170,170,170)
color_dark = (100,100,100)

class game_status(Enum):
    MAIN_MENU = 0
    GAME_PLAY = 1
    GAME_END = 2


pg.init()

SCREENRECT = pg.Rect(0,0,640,480)
font_1 = pg.font.SysFont('Corbel',50)
font_2 = pg.font.SysFont('Arial',20)
font_3 = pg.font.Font("BaiJamjuree-Bold.ttf",50)
font_4 = pg.font.Font("BaiJamjuree-Bold.ttf",30)

clock = pg.time.Clock()
all = pg.sprite.RenderUpdates()

class GlobalState:
    GAME_STATE = game_status.MAIN_MENU
    SCREEN = None
    def __init__(Self):
        GlobalState.SCREEN = pg.display.set_mode(SCREENRECT.size)
GlobalState()

class Main_Menu:
    def __init__(self):
        background = pg.Surface(SCREENRECT.size)
        background.fill(red_color)
        title = font_3.render("Tic-Tac-Toe",True,black_color)
        title_rect = title.get_rect(center = (SCREENRECT.width//2,100))
        background.blit(title,title_rect)
        press_ = font_4.render("Play",True,black_color)
        press_rect1 = press_.get_rect(center = (SCREENRECT.width//2,400))
        background.blit(press_,press_rect1)
        Main_Menu.press_rect = press_rect1.inflate(20,15)
        pg.draw.rect(background, "black",Main_Menu.press_rect , 5, border_radius=10)
        GlobalState.SCREEN.blit(background,(0,0))
        pg.display.flip()
        smileyball.containers = all
        self.smiley = smileyball()
        Main_Menu.BGD = background
    def update(self):

        clock.tick(40)
        all.clear(GlobalState.SCREEN,Main_Menu.BGD)
        self.smiley.update()
        
        dirty = all.draw(GlobalState.SCREEN)
        pg.display.update(dirty)
        events = pg.event.get()
        mouse = pg.mouse.get_pos()
        for event in events:
            if event.type == pg.QUIT:
                GlobalState.GAME_STATE = game_status.GAME_END
            elif event.type == pg.MOUSEBUTTONDOWN:
                if Main_Menu.press_rect.collidepoint(mouse[0],mouse[1]):
                    GlobalState.GAME_STATE = game_status.GAME_PLAY
                    self.smiley.kill()



main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    file = os.path.join(main_dir,file)
    surface = pg.image.load(file)
    return surface#.convert()

def load_sound(file):
    file = os.path.join(main_dir,file)
    sound = pg.mixer.Sound(file)
    return sound
        
class smileyball(pg.sprite.Sprite):

    image = load_image("Smiley.svg.png")
    image_small = pg.transform.scale(image,(50,50))
    speed = 10
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self,self.containers)
        self.image = self.image_small
        self.rect = self.image.get_rect(midbottom = SCREENRECT.midbottom)
        self.top_facing = 1
        self.right_facing = 1
    
    def update(self):
        #print(self.rect.top,self.rect.bottom)
        self.rect.move_ip(self.speed*self.right_facing,self.speed*self.top_facing*(4/3))
        if self.rect.right>SCREENRECT.right or self.rect.left<SCREENRECT.left:
            self.right_facing = self.right_facing*-1
        if self.rect.top<SCREENRECT.top or self.rect.bottom>SCREENRECT.bottom:
            self.top_facing = self.top_facing*-1

class Play(pg.sprite.Sprite):
    image = load_image("hash-removebg-preview.png")
    image_small = pg.transform.scale(image,(640,480))


    def __init__(self):
        pg.sprite.Sprite.__init__(self,self.containers)
        background = pg.Surface(SCREENRECT.size)
        background.fill("blue")
        GlobalState.SCREEN.blit(background,(0,0))
        pg.display.update()
        self.image = self.image_small
        self.rect = self.image.get_rect(midbottom = SCREENRECT.midbottom)
        dirty = all.draw(GlobalState.SCREEN)
        pg.display.update(dirty)
        #pg.display.update()

        #pg.time.wait(1000)
    def update(self):
        clock.tick(40)
        #dirty = all.draw(GlobalState.SCREEN)
        #pg.display.update(dirty)
        events = pg.event.get()
        #mouse = pg.mouse.get_pos()
        for event in events:
            if event.type == pg.QUIT:
                GlobalState.GAME_STATE = game_status.GAME_END
            #elif event.type == pg.MOUSEBUTTONDOWN:
            #    if Main_Menu.press_rect.collidepoint(mouse[0],mouse[1]):
            #        GlobalState.GAME_STATE = game_status.GAME_PLAY



def check_game(array):
    ar = np.append(np.sum(array,1),np.sum(array,0))
    ar = np.append(ar,[sum(np.diag(y)),sum(np.diag(np.fliplr(y)))])
    if 3 in ar:
        return 1
    elif -3 in ar:
        return -1
    else:
        return 0
            


def main():

    logo = load_image("logo32x32.png")
    pg.display.set_icon(logo)
    pg.display.set_caption("Tic Tac Toe")
    mm = Main_Menu()
    while GlobalState.GAME_STATE == game_status.MAIN_MENU:
        mm.update()
    if GlobalState.GAME_STATE == game_status.GAME_PLAY:
        Play.containers = all
        Play()
        x = np.array([[0,0,0],[0,0,0],[0,0,0]])
        while GlobalState.GAME_STATE == game_status.GAME_PLAY:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    GlobalState.GAME_STATE = game_status.GAME_END

    #clock.tick(1)

    #while GlobalState.GAME_STATE == game_status.GAME_PLAY:

    pg.quit()
if __name__=="__main__":
    main()