# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 2022

@author: Tahiri El Alaoui Youness & Julien Pheng & Hadj-Hamdri Amine
"""
# %%----------------------Import----------------------------------------------#

from Classes.entity import Entity


class EntityEnnemiSpecial(Entity):
    """Sous-classe pour les ennemis speciaux"""

    def slidingSpecial(self, pDirection, pCanevas):
        """
        Méthode permettant le déplacement des ennemis spéciaux.
        
        Parameters
        ----------
        pDirection : String
            'l' ou 'r' selon la direction choisie par createSpecialEntities.
        pCanevas : tkinter canevas
            Nécessaire pour l'interface graphique.
            
        Returns
        -------
        None.
        """

        if pDirection == 'r':
            pCanevas.move(self.imageOnCanvas, 5, 0) #déplacement des ennemis de 5 pixels sur la droite
            self.Position = [self.Position[0] + 5, self.Position[1]]
        else:
            pCanevas.move(self.imageOnCanvas, -5, 0)    #déplacement des ennemis de 5 pixels sur la gauche
            self.Position = [self.Position[0] - 5, self.Position[1]]