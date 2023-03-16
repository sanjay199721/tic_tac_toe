import pygame as pg
import random
import os
from enum import Enum

SCREENRECT = pg.Rect(0,0,640,480)
red_color = (200,20,30)
black_color = (20,20,20)
color_light = (170,170,170)
color_dark = (100,100,100)

class game_status(Enum):
    MAIN_MENU = 0
    GAME_PLAY = 1
    GAME_END = 2


pg.init()


font_1 = pg.font.SysFont('Corbel',50)
font_2 = pg.font.SysFont('Arial',20)
font_3 = pg.font.Font("BaiJamjuree-Bold.ttf",50)

clock = pg.time.Clock()
all = pg.sprite.RenderUpdates()

class GlobalState:
    GAME_STATE = game_status.MAIN_MENU
    SCREEN = None
    def __init__(self):
        screen = pg.display.set_mode(SCREENRECT.size)
        background = pg.Surface(SCREENRECT.size)
        background.fill(red_color)
        screen.blit(background,(0,0))
        title = font_3.render("Tic-Tac-Toe",True,black_color)
        title_rect = title.get_rect(center = (SCREENRECT.width//2,100))
        background.blit(title,title_rect)
        
        screen.blit(background,(0,0))
        pg.display.flip()
        smileyball.containers = all
        smileyball()
        GlobalState.BGD = background
        GlobalState.SCREEN = screen

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
        
def update_main_menu():

    clock.tick(40)
    all.clear(GlobalState.SCREEN,GlobalState.BGD)
    all.update()
    
    dirty = all.draw(GlobalState.SCREEN)
    pg.display.update(dirty)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            GlobalState.GAME_STATE = game_status.GAME_END
        elif event.type == pg.KEYDOWN:
            GlobalState.GAME_STATE = game_status.GAME_END
    return 

def main():

    logo = load_image("logo32x32.png")
    pg.display.set_icon(logo)
    pg.display.set_caption("Tic Tac Toe")
    GlobalState()
    while GlobalState.GAME_STATE == game_status.MAIN_MENU:
        update_main_menu()
    pg.quit()
if __name__=="__main__":
    main()