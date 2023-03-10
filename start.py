	
# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen_width = 640
    screen_height = 480
    red_color = (200,20,30)
    black_color = (20,20,20)
    color_light = (170,170,170)
    color_dark = (100,100,100)
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(red_color)
    image = pygame.image.load("Smiley.svg.png")
    image_small = pygame.transform.scale(image,(50,50))
    #screen.blit(image_small,(50,50))
    #pygame.display.flip()
    x1 = 50
    y1 = 50
    step_x = 50
    step_y = 50 
    font_1 = pygame.font.SysFont('Corbel',50)
    text_1 = font_1.render('Tic-Tac-Toe',True,black_color)
    font_2 = pygame.font.SysFont('Arial',20)
    text_2 = font_2.render('Play with computer',True,black_color)


    print(screen.get_height())
    # define a variable to control the main loop
    running = True
     
    # main loop
    i = 0
    while running:
        i += 1
        screen.blit(text_1,(screen_width/2-100,screen_height/2-100))
        screen.blit(text_2,(screen_width/2-60,screen_height/2))
        pygame.display.update()
        if i%1000==0:
            if x1>screen_width-64 or x1<0:
                step_x = -step_x
            if y1>screen_height-64 or y1<0:
                step_y = -step_y
            x1 += step_x
            y1 += step_y
            screen.fill(red_color)
            screen.blit(image_small,(x1,y1))
            pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        if screen_width/2-60<mouse[0]<screen_width/2+80 and screen_height/2<mouse[1]<screen_height/2+30:
            pygame.draw.rect(screen,color_light,[screen_width/2-60,screen_height/2,140,30])
        else:
            pygame.draw.rect(screen,color_dark,[screen_width/2-60,screen_height/2,140,30])

        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_width/2-60<mouse[0]<screen_width/2+80 and screen_height/2<mouse[1]<screen_height/2+30:
                    running = False



            
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()