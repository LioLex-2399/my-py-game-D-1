import pygame
from gameDisplay import gameDisplay
import time
import random
from lvl import lvl1
clock = pygame.time.Clock()
def plyrmanage (skin1,skin2):
	#WIP
	ackskin2=""
	ackskin=""
	time3=0
	if skin1 == "plyrs/s1.png":
		ackskin="bullets/ein.gif"

	if skin1 == "plyrs/s2.png":
		ackskin="bullets/kleb.png"

	if skin1 == "plyrs/s3.png":
		ackskin="bullets/nya.png"

	if skin1 == "plyrs/s4.png":
		ackskin="bullets/skylor.png"

	if skin1 == "plyrs/s5.png":
		ackskin="bullets/zane.png"

	if skin1 == "plyrs/s6.png":
		ackskin="bullets/cole.png"

	if skin1 == "plyrs/s7.png":
		ackskin="bullets/kai.png"

	if skin1 == "plyrs/s8.png":
		ackskin="bullets/Lloyd.png"

	if skin1 == "plyrs/s9.png":
		ackskin="bullets/jay.png"


	#player 2 bullet control
	if skin2 == "plyrs/s1.png":
		ackskin2="bullet2/ein.gif"

	if skin2 == "plyrs/s2.png":
		ackskin2="bullet2/kleb.png"

	if skin2 == "plyrs/s3.png":
		ackskin2="bullet2/nya.png"

	if skin2 == "plyrs/s4.png":
		ackskin2="bullet2/skylor.png"

	if skin2 == "plyrs/s5.png":
		ackskin2="bullet2/zane.png"

	if skin2 == "plyrs/s6.png":
		ackskin2="bullet2/cole.png"

	if skin2 == "plyrs/s7.png":
		ackskin2="bullet2/kai.png"

	if skin2 == "plyrs/s8.png":
		ackskin2="bullet2/Lloyd.png"

	if skin2 == "plyrs/s9.png":
		ackskin2="bullet2/jay.png"


	time2=0
	while True:
		background_colour=0,200,55
		gameDisplay.fill(background_colour)
####################################################
#test things that might not be needed in the future#
####################################################
#		image1 = pygame.image.load(ackskin)		  ##			
#		gameDisplay.blit(image1, (100, 100))      ##
#		image1 = pygame.image.load(ackskin)		  ##
#		gameDisplay.blit(image1, (100, 100))      ##
####################################################
		
		pygame.draw.rect(gameDisplay, (0,100,205), (10,250,610,150),(2))
		time3 += 0.1
		time2+=1

		
		pygame.draw.rect(gameDisplay, (0,5,155), (10,250,100,150),(100))
		if time2 >= 100:
			pygame.draw.rect(gameDisplay, (0,5,155), (10,250,110,150),(2000))
		if time2 >= 250:
			pygame.draw.rect(gameDisplay, (0,5,155), (10,250,150,150),(2000))	
		if time2 >= 500:
			
			pygame.draw.rect(gameDisplay, (0,5,155), (10,250,200,150),(2000))	

		if time2 >= 650:			
			pygame.draw.rect(gameDisplay, (0,5,155), (10,250,310,150),(2000))	
		if time2 >= 700:
			pygame.draw.rect(gameDisplay, (0,5,155), (10,250,390,150),(2000))	
		if time2 >= 950:
			
			pygame.draw.rect(gameDisplay, (0,5,155), (10,250,610,150),(2000))	
	
		if time2 == 1000:
			lvl1(skin1,skin2,ackskin,ackskin2)

		
		font1 = pygame.font.Font('amatic-sc.bold.ttf', 50)
		img1 = font1.render("loading... (player initialize ="+str(int(time3))+"%)", True, (2,2,0))
		gameDisplay.blit(img1, (12, 253))

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key== pygame.K_q:
				
					pygame.quit()

		
		
		pygame.display.update()
		clock.tick(60)		
	