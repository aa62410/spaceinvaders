# -*- coding: utf:8 -*-
#
# __main__.py
#
# Auteur : Bourdon Antoine-Alexis
# Institution : Université d'Artois
# Date : 02 decembre 2018
#
# Jeu : Space Invaders
#
import pygame
import menucoin
from couleur import *


def main():
	''' None -> None
	Fonction principale du programme. '''
	pygame.init()

	# La fenêtre de l'application.
	DIM_FENETRE = (640, 480)
	surface = pygame.display.set_mode(DIM_FENETRE)
	pygame.display.set_caption('Space Invaders ')
    
	# Initialise la police pour dessiner le score.
	police = pygame.font.Font(None, 25)
    
    
	# Initialise l'horloge.
	horloge = pygame.time.Clock()

	# Boucle principale.
	terminer = False

	# Initialisation du menu
	menu = menucoin.init(DIM_FENETRE)

	while not terminer :
		
       
		# Traite les evenements.
		for event in pygame.event.get() :
			
			

			if event.type == pygame.QUIT :
				terminer = True

			if event.type == pygame.KEYDOWN :
				
				if event.key == pygame.K_RIGHT:
					menu['joueur']['vit'][0] = 3
					
				if event.key == pygame.K_LEFT:
					menu['joueur']['vit'][0] = -3 
			
				if event.key == pygame.K_SPACE :
					if menu['mode_jeu']<2:
						menu['credit']+=1
					else:
						if menu['joueur']['visible'] == 0:
							menu['joueur']['laser'][0]=int(menu['joueur']['pos'][0])
							menu['joueur']['laser'][1]=int(menu['joueur']['pos'][1])
							menu['joueur']['visible'] = 1
					
				if event.key == pygame.K_RETURN :
					#print(menu['mode_jeu'])
					if menu['credit'] >=1 and menu['mode_jeu']<2:
						menu['mode_jeu']+=1
					
			if event.type == pygame.KEYUP :
				
				if event.key == pygame.K_RIGHT:
					menu['joueur']['vit'][0] = 0
					
				if event.key == pygame.K_LEFT:
					menu['joueur']['vit'][0] = 0
                    

        
		# Efface l'écran.
		surface.fill(NOIR)
        
		# Dessine les objects
		menucoin.update(surface,DIM_FENETRE,menu)

		# Met à jours l'ecran.
		pygame.display.update()
        
		# Ajuste la vitesse de la boucle.
		horloge.tick(30)

	# Termine Pygame.
	pygame.quit()

if __name__ == '__main__' :
	main()
