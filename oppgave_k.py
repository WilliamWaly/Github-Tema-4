# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:16:33 2023

@author: magnu
"""



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
    f"Det lineære uttrykket for trenden i temperatur er {a}x+{b}"
    if a>0:
        print("\nTrenden er stigende")
    if a<0:
        print("\nTrenden er synkende")
    if a==0:
        print("+nTrenden er uforandret")
        

        
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]


    
temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)

    
trenden_x_y(temperaturer_tidspunkter, temperaturer)

