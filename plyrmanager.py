import pygame
from gameDisplay import gameDisplay
def plyrmanage (skin1,skin2):
	#WIP
	ackskin=""
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
		
	while True:
		gameDisplay.fill()
		image1 = pygame.image.load(ackskin)
		gameDisplay.blit(image1, (100, 100))
	