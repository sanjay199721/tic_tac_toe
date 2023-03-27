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
    CHECK_REPLAY = 1.5
    GAME_END = 2


pg.init()

SCREENRECT = pg.Rect(0,0,640,480)
font_1 = pg.font.SysFont('Corbel',50)
font_2 = pg.font.SysFont('Arial',20)
font_3 = pg.font.Font("BaiJamjuree-Bold.ttf",50)
font_4 = pg.font.Font("BaiJamjuree-Bold.ttf",25)
font_5 = pg.font.Font("BaiJamjuree-Bold.ttf",30)

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
        pwb_ = font_4.render("Play with bot",False,black_color)
        pwb_rect1 = pwb_.get_rect(center = (SCREENRECT.width//2-60,350))
        background.blit(pwb_,pwb_rect1)
        x_ = font_4.render("X",True,black_color)
        x_rect = x_.get_rect(center = (SCREENRECT.width//2-90,385))
        background.blit(x_,x_rect)
        or_ = font_4.render("or",True,black_color)
        or_rect = or_.get_rect(center = (SCREENRECT.width//2-60,385))
        background.blit(or_,or_rect)
        o_ = font_4.render("O",True,black_color)
        o_rect = o_.get_rect(center = (SCREENRECT.width//2-30,385))
        background.blit(o_,o_rect)
        one_v = font_5.render("1v1",True,black_color)
        one_vrect = one_v.get_rect(center = (SCREENRECT.width//2+80,370))
        background.blit(one_v,one_vrect)
        Main_Menu.x_press = x_rect.inflate(5,5)
        Main_Menu.o_press = o_rect.inflate(5,5)
        Main_Menu.onev_press = one_vrect.inflate(7,7)
        pg.draw.rect(background, "black",Main_Menu.x_press , 1, border_radius=7)
        pg.draw.rect(background, "black",Main_Menu.o_press , 1, border_radius=7)
        pg.draw.rect(background, "black",Main_Menu.onev_press , 2, border_radius=7)
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
                return 0
            elif event.type == pg.MOUSEBUTTONDOWN:
                if Main_Menu.x_press.collidepoint(mouse[0],mouse[1]):
                    GlobalState.GAME_STATE = game_status.GAME_PLAY
                    self.smiley.kill()
                    return 1
                elif Main_Menu.o_press.collidepoint(mouse[0],mouse[1]):
                    GlobalState.GAME_STATE = game_status.GAME_PLAY
                    self.smiley.kill()
                    return -1
                elif Main_Menu.onev_press.collidepoint(mouse[0],mouse[1]):
                    GlobalState.GAME_STATE = game_status.GAME_PLAY
                    self.smiley.kill()
                    return 0
        return 0





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
    image = pg.transform.scale(image,(640,480))
    image_x = load_image("x__1_-removebg-preview.png")
    image_x = pg.transform.scale(image_x,(140,110))
    image_o = load_image("o_image.png")
    image_o = pg.transform.scale(image_o,(140,110))
    point_1 = (44,44)
    y_offset = 190
    x_offset = 150
    grid_points = [(214,427),(160,320)]
    xo_points = [(10,224,437),(10,170,330)]

    def __init__(self,bot,xo):
        pg.sprite.Sprite.__init__(self,self.containers)
        background = pg.Surface(SCREENRECT.size)
        background.fill("blue")
        GlobalState.SCREEN.blit(background,(0,0))
        pg.display.update()
        self.rect = self.image.get_rect(midbottom = SCREENRECT.midbottom)
        #print(SCREENRECT.midbottom)
        dirty = all.draw(GlobalState.SCREEN)
        pg.display.update(dirty)
        self.array = np.array([[0,0,0],[0,0,0],[0,0,0]])
        self.xo = xo
        self.bot_ = bot
        self.turn = 1
        #self.Board = Board()
        #pg.display.update()

        #pg.time.wait(1000)
    def update(self):
        clock.tick(10)
        #pg.time.wait(500)
        if check_game(self.array)==1:
            GlobalState.GAME_STATE = game_status.CHECK_REPLAY
            won = font_3.render("X won",True,black_color)
            won_rect = won.get_rect(midbottom = SCREENRECT.midbottom)
            GlobalState.SCREEN.blit(won,won_rect)
            play_again = font_4.render("Main Menu",True,black_color)
            pa_rect = play_again.get_rect(bottomright = SCREENRECT.bottomright)
            pg.draw.rect(GlobalState.SCREEN, "black",pa_rect.inflate(5,5) ,3 , border_radius=10)
            GlobalState.SCREEN.blit(play_again,pa_rect)
            dirty = all.draw(GlobalState.SCREEN)
            pg.display.update(dirty)
            return pa_rect
            
        elif check_game(self.array)==-1:
            GlobalState.GAME_STATE = game_status.CHECK_REPLAY
            won = font_3.render("O won",True,black_color)
            won_rect = won.get_rect(midbottom = SCREENRECT.midbottom)
            GlobalState.SCREEN.blit(won,won_rect)
            play_again = font_4.render("Main Menu",True,black_color)
            pa_rect = play_again.get_rect(bottomright = SCREENRECT.bottomright)
            pg.draw.rect(GlobalState.SCREEN, "black",pa_rect.inflate(5,5) , 3, border_radius=10)
            GlobalState.SCREEN.blit(play_again,pa_rect)
            dirty = all.draw(GlobalState.SCREEN)
            pg.display.update(dirty)
            return pa_rect
        elif check_game(self.array)==0.5:
            GlobalState.GAME_STATE = game_status.CHECK_REPLAY
            won = font_3.render("Draw",True,black_color)
            won_rect = won.get_rect(midbottom = SCREENRECT.midbottom)
            GlobalState.SCREEN.blit(won,won_rect)
            play_again = font_4.render("Main Menu",True,black_color)
            pa_rect = play_again.get_rect(bottomright = SCREENRECT.bottomright)
            pg.draw.rect(GlobalState.SCREEN, "black",pa_rect.inflate(5,5) , 3, border_radius=10)
            GlobalState.SCREEN.blit(play_again,pa_rect)
            dirty = all.draw(GlobalState.SCREEN)
            pg.display.update(dirty)
            return pa_rect
            
        if self.bot_ and  GlobalState.GAME_STATE == game_status.GAME_PLAY and (self.turn != self.xo):
            self.bot_output()
            self.add_xo()
            self.turn = self.turn*-1

        events = pg.event.get()
        mouse = pg.mouse.get_pos()
        for event in events:
            if event.type == pg.QUIT:
                GlobalState.GAME_STATE = game_status.GAME_END
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.check_point(mouse[0],mouse[1])
                self.add_xo()
                self.turn = self.turn*-1
            
                

    def add_xo(self):
        if self.array[self.m][self.n]==0:
            self.x1 = self.xo_points[0][self.m]
            self.y1 = self.xo_points[1][self.n]
            self.array[self.m][self.n] = self.turn
            
            if self.turn==1:
                GlobalState.SCREEN.blit(self.image_x,(self.x1,self.y1))
                dirty = all.draw(GlobalState.SCREEN)
                pg.display.update(dirty)
                
            elif self.turn ==-1:
                GlobalState.SCREEN.blit(self.image_o,(self.x1,self.y1))
                dirty = all.draw(GlobalState.SCREEN)
                pg.display.update(dirty)
    def check_point(self,x,y):
        if x<(self.grid_points[0][0]):
            self.m = 0
        elif (self.grid_points[0][0])<x<(self.grid_points[0][1]):
            self.m = 1
        elif (self.grid_points[0][1])<x:
            self.m = 2
        if y<(self.grid_points[1][0]):
            self.n = 0
        elif (self.grid_points[1][0])<y<(self.grid_points[1][1]):
            self.n = 1
        elif (self.grid_points[1][1])<y:
            self.n = 2
    def bot_output(self):

        m = random.randint(0,2)
        n = random.randint(0,2)
        while(self.array[m][n]!=0):
            m = random.randint(0,2)
            n = random.randint(0,2)
        self.m = m
        self.n = n


def check_game(array):
    ar = np.append(np.sum(array,1),np.sum(array,0))
    ar = np.append(ar,[sum(np.diag(array)),sum(np.diag(np.fliplr(array)))])
    if 3 in ar:
        return 1
    elif -3 in ar:
        return -1
    elif 0 not in array:
        return 0.5
    else:
        return 0
            




def main():

    logo = load_image("logo32x32.png")
    pg.display.set_icon(logo)
    pg.display.set_caption("Tic Tac Toe")
    Play.containers = all
    
    while GlobalState.GAME_STATE != game_status.GAME_END:
        mm = Main_Menu()  
        while GlobalState.GAME_STATE == game_status.MAIN_MENU:
            c = mm.update()
        if GlobalState.GAME_STATE == game_status.GAME_PLAY:
            
            z = Play(abs(c),c)
            while GlobalState.GAME_STATE == game_status.GAME_PLAY:
                t = z.update()
                #print(t)
            while GlobalState.GAME_STATE == game_status.CHECK_REPLAY:
                events = pg.event.get()
                mouse = pg.mouse.get_pos()
                for event in events:
                    if event.type == pg.QUIT:
                        GlobalState.GAME_STATE = game_status.GAME_END
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        if t.collidepoint(mouse[0],mouse[1]):
                            GlobalState.GAME_STATE = game_status.MAIN_MENU


            z.kill()
            #pg.time.wait(1000)

    #while GlobalState.GAME_STATE == game_status.GAME_PLAY:

    pg.quit()
if __name__=="__main__":
    main()

    """pyinstaller --add-data "BaiJamjuree-Blod.ttf;." --add-data "hash-removebg-preview.png;." --add-data "logo32x32.png;." --add-data "o_image.png;." --add-data "x__1_-removebg-preview.png;." --add-data "Smiley.svg.png;."  start.py"""