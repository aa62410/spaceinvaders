# -*- coding: utf-8 -*-
''' Implémente le vaiseau joueur et les ennemis. '''
__author__ = 'Bourdon Antoine-Alexis <antoine-alexis_bourdon@ens.univ-artois.fr>'
__date__ =  '04 decembre 2018'

# Import Pygame.
import pygame

# Bibliotèques pour trouver les fichiers.
import sys
import os

import pygame

from couleur import *

def init(pos):
    ''' Initialise un vaisseau spatial.
    Arguments:
        pos : (int, int) -- les coordonnées du vaisseau.
    Retour:
        dict -- les attributs du vaisseau.
    '''
    att = {}
    
    # Trouve le fichier d'image du vaisseau.
    dossier = os.path.dirname(sys.argv[0])
    fichier_image = os.path.join(dossier, 'space_ship.bmp')

    # Charge l'image du vaisseau.
    att['image'] = pygame.image.load_basic(fichier_image)
    # Converti l'image du vaisseau.
    att['image'].convert()
    # Rend le fond de l'image transparent.
    att['image'].set_colorkey((0, 0, 0))
       
    # Coordonées initiales du vaisseau.
    att['pos'] = [pos[0], pos[1]]
    # Vitesses initiales.
    att['vit'] = [0, 0]
    att['laser']= [100,240]
    att['vit_laser']=10
    att['visible']=0
    
    return att

def dessine(att, surface):
    ''' Dessine un vaisseau spatial.
    Arguments:
        att : dict --  les attributs d'un vaisseau.
        surface : Surface -- la surface de l'application.
    Retour:
        None
    '''
    surface.blit(att['image'], att['pos'])

def dessine_tire(att,surface):
    ''' Dessine un rayon laser.
    Arguments:
        att : dict -- les attributs d'un rayon laser.
        surface : Surface -- la surface de l'application.
    Retour:
        None
    '''
    if att['visible'] > 0:
        pygame.draw.circle(surface, (255, 255, 255), (int(att['laser'][0]),int(att['laser'][1]-att['vit_laser'])),5,0)
        att['laser'][1]-=att['vit_laser']


def update(att):
    ''' Met à jours la position du vaisseau.
    Arguments:
        att : dict -- les attributs d'un vaisseau.
    Retour:
        None
    '''
    # Change la position du vaisseau.
    att['pos'][0] += att['vit'][0]
    att['pos'][1] += att['vit'][1]
    
