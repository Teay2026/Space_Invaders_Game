# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 2022

@author: Tahiri El Alaoui Youness & Julien Pheng & Hadj-Hamdri Amine
"""

# %%----------------------Import----------------------------------------------#

from tkinter import PhotoImage
import math, random
from Classes.entity import Entity


class EntityTirJoueur(Entity):
    """Sous-classe pour les tirs du joueur"""

    def afficherTirJoueur(self, pWindow, pCanevas):
        """
        Méthode d'affichage des Entitys. Les parametres pWindow et pCanevas
        sont respectivement la fenêtre et le canvas.
        
        Parameters
        ----------
        pWindow : tkinter window
            Nécessaire pour l'interface graphique
        pCanevas : tkinter canevas
            Idem
            
        Returns
        -------
        None.
        """
        self.PixelArt = PhotoImage(master=pWindow,
                                   file='PixelArts/' + self.Frame1)
        pCanevas.create_image(self.Position[0], self.Position[1],
                              image=self.PixelArt)

    def hitbox1(self, pListeDesEnnemis):
        """
        Méthode pour la détection des hitboxs. Le parametre pListeDesEnnemis
        est une liste dont chaque élément est une liste contenant tous les
        ennemis d'une ligne, EN COMMENCANT PAR LE LIGNE LA PLUS BASSE
        
        Parameters
        ----------
        pListeDesEnnemis : Liste de Liste de d'élement EntityEnnemiClassique
            Liste des ennemis en jeu.
            
        Returns
        -------
        bool
            True si un le projectile du joueur à touché un ennemi (pour le
                                                                   supprimer).
        Int
            Nombre de point gagné lors du kill.
        """
        for i, item in enumerate(pListeDesEnnemis):  # Pour chacune des lignes
            for j, ennemi in enumerate(item):
                distance = math.sqrt((ennemi.Position[0] - self.Position[0]) ** 2 +
                                     (ennemi.Position[1] - self.Position[1]) ** 2)  #CALCUL DE NORME ENTRE LE PROJECTILE ET LE CENTRE DE L'ENNEMI pour vérifier la distance avec l'ennemi
                if distance <= 10:  #les ennemis ayant une taille de 20x20 pixels minimum, 10 permet d'être sûr de toucher
                    item.remove(ennemi) 

                    if i == 0:  #On ajoute le nombre de point approprié selon l'ennemi touché
                        Points = 40     #40 pour la dernière ligne
                    elif i in [1, 2]:
                        Points = 20     #20 pour la 4ème et 3ème
                    elif i in [3, 4]:
                        Points = 10     #10 pour la 2nd et 1ère
                    elif i == 5:
                        Points = random.choice([50, 100, 150, 200]) #Un nombre de point aléatoire pour l'ennemi rouge

                    return True, Points
        return False, 0