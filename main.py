'''
Space Invaders

Auteur : Antoine-Alexis Bourdon
Licence 2 Mathématiques et Informatique
Université d'Artois
1 dec. 2018

Projet Space Invaders
Implémenter en Python3 avec module Pygame.
'''
# 1. Importe la bibliothèque Pygame.
import pygame

# Autres importations:


def main():
	'''
	None -> None.
	Fonction principale.
	'''
	# 2. Initialise Pygame.
	pygame.init()

	# 3. Initialise l'horloge.
	horloge = pygame.time.Clock()

	# 4. Ouvre la fenetre de l'application.
	L_FENETRE = 640
	H_FENETRE = 480
	surface = pygame.display.set_mode((L_FENETRE,H_FENETRE))
	pygame.display.set_caption("Space Invaders")
	bg_color = (0, 0, 0) #couleur de fond de la fenetre

	# 5. Initialisations des vues
	menu_items = ('Start', 'Settings', 'Quit')
	#gm = GameMenu(surface, menu_items)
	#gs = GameSettings(surface)
	g = None #pour redemarrage au début

	# 6. Tant que le programme n'est pas terminé :
	terminer = False
	while not terminer:

		# 6.1 traite les évènements.
		# Pour chaque évènements détecté :
		for event in pygame.event.get():

			#Si l'utilisateur a cliqué sur fermer fenetre :
			if event.type == pygame.QUIT :
				terminer = True

		# Démarre l'écran menu par défaut ou après ECHAP
		'''if menu_selected or g.escape_selected:
			gm.run()
			if g is not None:
				g.escape_selected = False
			gs.escape_selected = False

		# Démarre l'écran de jeu
		if gm.start_selected:
			g = Game(surface)
			g.run()
			gm.start_selected = False
			gm.quit_select = False

		# Démarre l'écran de configuration
		if gm.settings_selected:
			gs.run()
			gm.settings_selected = False

		# Ferme la fenêtre si Quit est séléctionnée
		if gm.quit_select is True:
			terminer = True
'''
		surface.fill(bg_color)

		# 6.4 mettre à jour l'écran
		pygame.display.update()
	pygame.quit()

if __name__ == 'main':
	main()
