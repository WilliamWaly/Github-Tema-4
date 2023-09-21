# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:59:21 2023

@author: magnu
"""

import random

def finn_forskjell(listen):
    print("Den genererte listen er her", listen)
    liste=list()
    for element in range(len(listen)-1):
        forskjell=listen[element+1]-listen[element]
        liste.append(forskjell)
        
    print("Endringen fra første verdi blir slik", liste)
        
    
    
    
listen=[random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),
        random.randint(1, 20),random.randint(1, 20),random.randint(1, 20)]

finn_forskjell(listen)