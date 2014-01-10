# Breathing Simulator 2014
# Made by Kieran Gould (TronLaser)

import pygame
import time
import sys
import os
import ConfigParser

print ("Everything imported fine")

# Reading from the config.ini
config = ConfigParser.ConfigParser()
config.read("config.ini")
fullscreen = config.get('video', 'fullscreen')
screen_width = config.get('video', 'width')
screen_height = config.get('video', 'height')
debug = config.get('debug', 'debug')
print ("Config file found and read")

currentlevel = '0'
x = y = 0

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.font.init()

#COLOURS AND STUFF
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,144,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

font = pygame.font.SysFont("Ariel", 30)

#SOUNDS
menu = pygame.mixer.Sound(os.path.join('sound','menu.ogg'))
playing = pygame.mixer.Sound(os.path.join('sound','menu.ogg'))
dead = pygame.mixer.Sound(os.path.join('sound','dead.ogg'))
print ("Sounds imported")
menu.play(-1)

#IMAGES
background01 = pygame.image.load(os.path.join('images', 'background01.png'))
background02 = pygame.image.load(os.path.join('images', 'background02.png'))
button01 = pygame.image.load(os.path.join('images', 'button01.png'))
button02 = pygame.image.load(os.path.join('images', 'button02.png'))
breathin = pygame.image.load(os.path.join('images', 'breathin.png'))
breathout = pygame.image.load(os.path.join('images', 'breathout.png'))
logo = pygame.image.load(os.path.join('images', 'logo.png'))
print ("Images imported")

key = pygame.key.get_pressed()
screen = pygame.display.set_mode((1280, 720)) # STARTING THE SCREEN!!
pygame.display.set_caption("Breathing Simulator 2014")
mousebutton = '0'
breath = '0'
print ("We seem to have loaded!")

#MAIN MENU
def menu():
	screen.blit(background01,(0, 0))
	screen.blit(button01,(340, 375))
	screen.blit(button02,(340, 550))
	screen.blit(logo,(500, 25))

def menubutton():
	global currentlevel
	global mousebutton
	x, y = mousepos = pygame.mouse.get_pos()
	if x > 340 and y > 375 and x < 940 and y < 475 and mousebutton == '1':
		print ("YES")
		currentlevel = '1'
	if x > 340 and y > 550 and x < 940 and y < 650 and mousebutton == '1':
		sys.exit()

#GAME
def game():
	global o2
	global breath
	global score

	score = score + 0.01 # Handle score
	scoredis = score
	scoredis = round (score, 1)
	scoredis = str(scoredis)
	print scoredis

	screen.blit(background01,(0, 0)) # Draw to screen
	pygame.draw.rect(screen, BLUE,[600,100,500,25],0)

	if breath == True:
		screen.blit(breathin,(0,0))

	if breath == False:
		screen.blit(breathout,(0,0))

	for event in pygame.event.get(): # Key presses
	    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:
		    breath = True
	    if event.type == pygame.KEYUP:
		if event.key == pygame.K_SPACE:
		    breath = False
	    if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            pygame.mixer.stop()
                    pygame.mixer.quit()
                    sys.exit()

#GAME OVER SCREEN
def death():
	screen.blit(background02,(0, 0))
	dead.play(1)

max_fps = 60
score = 0
# MAIN LOOP (RENDERING STUFF ALWAYS GOES AT TOP!)
while True:
	global mousebutton
	global currentlevel
	global score
	global breath
	max_fps = 60
	event = pygame.event.poll()
	if currentlevel == '0': # Level select
		menu()
		menubutton()
	if currentlevel == '1':
		game()
	if currentlevel == '2':
		death()
	for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit
		print ("Quitting game")
		pygame.mixer.stop()
		pygame.mixer.quit()
                sys.exit()
	    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
	            pygame.mixer.stop()
		    pygame.mixer.quit()
                    sys.exit()
	    if event.type == pygame.MOUSEBUTTONDOWN: # Mouse
		global mousebutton
	        mousebutton = '1'
	    if event.type == pygame.MOUSEBUTTONUP: # More mouse
		global mousebutton
		mousebutton = '0'
	if debug == '1': # Debug stuff
		pygame.draw.rect(screen, BLACK,[0,0,105,25],0)
		mousepos = pygame.mouse.get_pos()
		mousepos = str(mousepos)
		mousepostext = font.render(mousepos, 1, WHITE)
		screen.blit(mousepostext,(0, 0))
	pygame.display.update()
	pygame.display.flip()

