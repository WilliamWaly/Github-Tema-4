# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:08:30 2023

@author: magnu
"""


def finn_forskjell(listen):
    liste=list()
    for element in range(len(listen)-1):
        forskjell=listen[element+1]-listen[element]
        liste.append(forskjell)
        
    print("Temperaturforskjellen er slik fra dag 1\n", liste)
        
    

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]

finn_forskjell(temperaturer)

        
        
    
    
