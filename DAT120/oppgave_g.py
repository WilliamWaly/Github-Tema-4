# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:41:15 2023

@author: magnu
"""

liste_1=[1,5,8]
liste_2=[9,1,3]

def trenden_x_y(liste_x,liste_y):

    gjennomsnitt_x=sum(liste_x)/len(liste_x)
    gjennomsnitt_y=sum(liste_y)/len(liste_y)
    a=0

    for index in range(len(liste_x)):
        x_uttrykk=(liste_x[index]-gjennomsnitt_x)
        y_uttrykk=(liste_y[index]-gjennomsnitt_y)
        a_index=x_uttrykk*y_uttrykk/x_uttrykk**2
        a+=a_index
    b=gjennomsnitt_y-a*gjennomsnitt_x
    print(f"\nDet lineære uttrykket for trenden er {a}x+{b}")
    if a>0:
        print("\nTrenden er stigende")
    if a<0:
        print("\nTrenden er synkende")
    if a==0:
        print("\nTrenden er uforandret")
        
    
trenden_x_y(liste_1, liste_2)

