# -*- coding: utf-8 -*-
'''
Dessine le menu principal du jeu
'''
__author__ = 'Antoine-Alexis Bourdon <antoine-alexis_bourdon@ens.univ-artois.fr>'
__date__ = '02 decembre 2018'

# Importe Pygame.
import pygame

from couleur import *
import jeu

def init(DIM_FENETRE):
	''' None -> dict
	Initialise les élèments du menu principal
	'''
	att = {}
	att['credit']=0 #nombre de crédits
	att['hi_score']=int(open("hi_score","r").read()) #Score le plus elevé deja atteind
	att['score_1']=0 #Score du joueur 1
	att['score_2']=0 #Score du joueur 2
	att['act_coin']=0 #actualisation de l'affichage clignotant de "INSERT COIN" et "PLAY"
	att['mode_jeu']=0 #Savoir quel ecran mettre 0 -> accueil, 1->"règles de jeu" , 2-> le jeu
	att['joueur']=jeu.init((DIM_FENETRE[0]/2,DIM_FENETRE[1]-20))

	return att


def dessine_menu(surface,DIM_FENETRE,att):
	''' Dessine le Menu sur la surface passé en argument.
	Arguments:
		surface : Surface.
	Retour:
		None.
	'''
	# Dessine un fond noir
	surface.fill(NOIR)

	# Dessine le texte
	if att['act_coin'] <30:
		police = pygame.font.Font(None, 40)
		if att['credit'] == 0:
			texte = police.render('INSERT COIN', True, BLANC)
			surface.blit(texte, [DIM_FENETRE[0]/3,DIM_FENETRE[1]/3])
		else:
			texte = police.render('PLAY', True, BLANC)
			surface.blit(texte, [DIM_FENETRE[0]/3,DIM_FENETRE[1]/3])
	textescore = pygame.font.Font(None, 20).render('CREDIT '+str(att['credit']), True, BLANC)
	surface.blit(textescore, [DIM_FENETRE[0]-100,DIM_FENETRE[1]-20])
	att['act_coin']+=1
	att['act_coin']%=60
	
def dessine_score(surface,DIM_FENETRE,att):
	police = pygame.font.Font(None, 30)
	
	score1_titre = police.render('SCORE <1>', True, BLANC)
	score1_score = police.render(str(att['score_1']), True, BLANC)
	hi_score_titre = police.render('HI-SCORE', True, BLANC)
	hi_score_score = police.render(str(att['hi_score']), True, BLANC)
	score2_titre = police.render('SCORE <2>', True, BLANC)
	score2_score = police.render(str(att['score_2']), True, BLANC)
	
	surface.blit(score1_titre, [10,20])
	surface.blit(score1_score, [10,40])
	surface.blit(hi_score_titre, [10+DIM_FENETRE[0]/3,20])
	surface.blit(hi_score_score, [10+DIM_FENETRE[0]/3,40])
	surface.blit(score2_titre, [10+(DIM_FENETRE[0]/3)*2,20])
	surface.blit(score2_score, [10+(DIM_FENETRE[0]/3)*2,40])

def update(surface,DIM_FENETRE,att):
	if att['mode_jeu']==0:
		dessine_menu(surface,DIM_FENETRE,att)
	dessine_score(surface, DIM_FENETRE, att)
	if att['mode_jeu']==2:
		jeu.update(att['joueur'])
		jeu.dessine(att['joueur'],surface)
		jeu.dessine_tire(att['joueur'],surface)
		if att['joueur']['laser'][1] < 0:
			att['joueur']['visible'] = 0
		

