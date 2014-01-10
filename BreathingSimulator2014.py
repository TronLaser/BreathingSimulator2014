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
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

font = pygame.font.SysFont("Ariel", 30)

#SOUNDS
menu = pygame.mixer.Sound(os.path.join('sound','menu.ogg'))
playing = pygame.mixer.Sound(os.path.join('sound','menu.ogg'))
dead = pygame.mixer.Sound(os.path.join('sound','dead.ogg'))
print ("Sounds imported")

#IMAGES
background01 = pygame.image.load(os.path.join('images', 'background01.png'))
background02 = pygame.image.load(os.path.join('images', 'background02.png'))
button01 = pygame.image.load(os.path.join('images', 'button01.png'))
button02 = pygame.image.load(os.path.join('images', 'button02.png'))
print ("Images imported")

key = pygame.key.get_pressed()
screen = pygame.display.set_mode((1280, 720)) # STARTING THE SCREEN!!
pygame.display.set_caption("Breathing Simulator 2014")
global mousebutton
global score
global o2
global currentlevel
mousebutton = '0'

menu.play(-1)

#MAIN MENU
def menu():
	screen.blit(background01,(0, 0))
	screen.blit(button01,(340, 375))
	screen.blit(button02,(340, 550))

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
	screen.blit(background01,(0, 0))

#GAME OVER SCREEN
def death():
	screen.blit(background02,(0, 0))

# MAIN LOOP (RENDERING STUFF ALWAYS GOES AT TOP!)
while True:
	global mousebutton
	global currentlevel
	event = pygame.event.poll()
	if currentlevel == '0':
		menu()
		menubutton()
	if currentlevel == '1':
		game()
	if currentlevel == '2':
		death()
	for event in pygame.event.get():
            if event.type == pygame.QUIT:
		print ("Quitting game")
		pygame.mixer.stop()
		pygame.mixer.quit()
                sys.exit()
	    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
	            pygame.mixer.stop()
		    pygame.mixer.quit()
                    sys.exit()
	    if event.type == pygame.MOUSEBUTTONDOWN:
		global mousebutton
	        mousebutton = '1'
	    if event.type == pygame.MOUSEBUTTONUP:
		global mousebutton
		mousebutton = '0'
	if debug == '1':
		pygame.draw.rect(screen, BLACK,[0,0,105,25],0)
		mousepos = pygame.mouse.get_pos()
		mousepos = str(mousepos)
		mousepostext = font.render(mousepos, 1, WHITE)
		screen.blit(mousepostext,(0, 0))
	pygame.display.update()
	pygame.display.flip()

