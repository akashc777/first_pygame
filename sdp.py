import pygame
import time
import random
pygame.init()
game_width = 800
game_height = 600
gameDis = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption("WORNG WAY !!!!")
black = (0,0,0)
gray = (128,128,128)
red = (255,0,0)
clock = pygame.time.Clock()
carImg = [pygame.image.load("car/car1.png"), pygame.image.load("car/car2.png"), pygame.image.load("car/car3.png"),pygame.image.load("car/car4.png"), pygame.image.load("car/car5.png"), pygame.image.load("car/car6.png"), pygame.image.load("car/car7.png")]

def car(x,y):
    gameDis.blit(carImg[0],(x,y))

def obs(obsn,obsx, obsy):
    gameDis.blit(carImg[obsn],(obsx,obsy))

def message_display(text,size,l,a):
    textF = pygame.font.SysFont('timesnewroman', size, True, False)
    textS = textF.render(text, True, black)
    textA = textS.get_rect()
    if a == 1:
     textA.center = l
    gameDis.blit(textS, textA)
    pygame.display.update()

def score(count) :
     message_display('Score :'+str(count), 25, (0,0),0)

start = False
count = [3, 2, 1]
while not start :
    for n in count:
        for s in range(100,300):
            gameDis.fill((255,255,255))
            message_display(str(n),s,(400,300),1)
            pygame.display.update()
        time.sleep(0.3)

    start = True



def game_loop():
    x = (0)
    y = (game_height-160)
    y_change = 0
    w=0
    h = 100
    count=0
    obs_number = random.randrange(1, 7)
    obs_starty = random.randrange(0, game_height-h)
    obs_startx = game_width+600
    obs_speed = 5


    i=0
    while not False :

        event = pygame.event.poll()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                y_change = -5
            if event.key == pygame.K_DOWN :
                y_change = 5

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    y_change = 0

    #obs(obsn,obsx, obxy)
        gameDis.fill(gray)

        if obs_number == 1:
            w = carImg[1].get_width()
        if obs_number == 2:
            w = carImg[2].get_width()
        if obs_number == 3:
            w = carImg[3].get_width()
        if obs_number == 4:
            w = carImg[4].get_width()
        if obs_number == 5:
            w = carImg[5].get_width()
        if obs_number == 6:
            w = carImg[6].get_width()
        if x +144 > obs_startx and x < obs_startx + w:
            if y < obs_starty+70 and y+70 > obs_starty :
                message_display('CRASHED',100,(400,300),1)
                time.sleep(1)
                obs_startx = -300
                count=0
        if (y < 0 and y_change == -5) or (y > game_height-100 and y_change == 5):
            y_change = 0
            #message_display('end point!',100,(400,300))
        y+=y_change
        obs_startx -= obs_speed


        car(x,y)
        obs(obs_number, obs_startx, obs_starty)
        score(count)



        if obs_startx<-250 :
            obs_startx = game_width+268
            obs_number = random.randrange(1, 7)
            obs_starty = random.randrange(0, game_height-100)
            count +=5


        pygame.display.update()
        clock.tick(100)
game_loop()
pygame.quit()
quit()
