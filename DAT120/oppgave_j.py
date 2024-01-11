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
    return liste
        
        
def verdileser():
    liste=finn_forskjell(temperaturer)
    for i in range(len(finn_forskjell(temperaturer))):
        if liste[i-1]>0:
            print("stigende")
        elif liste[i-1]==0:
            print("Uforandret")
        elif liste[i-1]<0:
            print("synkende")
            


        
    

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]

print(finn_forskjell(temperaturer),"\n")


verdileser()

        
        
    
    
