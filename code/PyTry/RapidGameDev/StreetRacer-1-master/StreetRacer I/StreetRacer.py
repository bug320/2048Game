import pygame
import time
import random

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (66, 134, 244)

car_width = 31

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('StreetRacer I')
clock = pygame.time.Clock()

carImg = pygame.image.load('Sprites/Player.png')
OtherCarImg = pygame.image.load('Sprites/Other Car.png')
BackgroundImg = pygame.image.load('Backgrounds/Background.png')

pygame.mixer.music.load('Sounds/Music.mp3')
CrashEffect = pygame.mixer.Sound('Sounds/Crash.wav')
pygame.mixer.music.set_volume(0.5)

def cars_dodged(count):
        font = pygame.font.Font('Fonts/joystix monospace.ttf', 27)
        text = font.render('Score: ' + str(count), True, blue)
        gameDisplay.blit(text, (0, 0))

def Background():
        gameDisplay.blit(BackgroundImg, (0, 0))

def stuff(x, y):
        gameDisplay.blit(OtherCarImg, (x, y))

def car(x, y):
        gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
        textSurface = font.render(text, True, blue)
        return textSurface, textSurface.get_rect()

def message_display(text):
        largeText = pygame.font.Font('Fonts/joystix monospace.ttf', 72)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

        GameLoop()
        
def crash():
        message_display('You Crashed!')

def GameLoop():
        
        x = (display_width * 0.45)
        y = (display_height * 0.8)

        x_change = 0

        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        thing_speed = 4
        thing_width = 32
        thing_height = 58

        score = 0

        paused = False
        GameExit = False

        while not GameExit:
                for event in pygame.event.get():
                        print(event)
                        
                        if event.type == pygame.QUIT:
                                print('Quitting...')
                                pygame.quit()
                                quit()

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        x_change = -5
                                if event.key == pygame.K_RIGHT:
                                        x_change = 5

                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                        x_change = 0

                x += x_change

                gameDisplay.fill(white)


                Background()
                stuff(thing_startx, thing_starty)
                thing_starty += thing_speed
                car(x, y)
                cars_dodged(score)

                if x > display_width - car_width or x < 0:
                        CrashEffect.play()
                        crash()

                if thing_starty > display_height:
                        thing_starty = 0 - thing_height
                        thing_startx = random.randrange(0, display_width)
                        score += 1
                        thing_speed += 1

                if y < thing_starty + thing_height:
                        print('y crossover')

                        if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                                CrashEffect.play()
                                print('x crossover')
                                crash()
                
                pygame.display.update()
                clock.tick(30)

pygame.mixer.music.play(0)
GameLoop()
pygame.quit()
quit()
