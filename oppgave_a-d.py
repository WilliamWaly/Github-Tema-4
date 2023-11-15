# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:46:03 2023

@author: magnu
"""
from datetime import datetime
import matplotlib.pyplot as plt
 
def tell_storre_eller_lik_verdi(liste, verdi):
    liste2=[]
    for element in liste:
        if float(element)>=float(verdi) :
            liste2.append(element)
    return liste2


def trenden(liste_x,liste_y):
    
    liste_x_int=[]
    liste_y_int=[]
    startsum_x=0
    startsum_y=0
   
    for i in liste_x:
       startsum_x+=int(i)
       liste_x_int.append(int(i))
    gjennomsnitt_x=startsum_x/len(liste_x)
    for i in liste_y:
        startsum_y+=int(i)
        liste_y_int.append(int(i))
    gjennomsnitt_y=startsum_y/len(liste_y)
    
    teller=0
    nevner=0

    for index in range(len(liste_x)):
        x_uttrykk=float(liste_x_int[index]-gjennomsnitt_x)
        y_uttrykk=float(liste_y_int[index]-gjennomsnitt_y)
        teller_index=x_uttrykk*y_uttrykk
        teller+=teller_index
        nevner_index=x_uttrykk**2
        nevner+=nevner_index
    a=teller/nevner
    b=gjennomsnitt_y-a*gjennomsnitt_x
    return a,b
        


def tolk_vaerdata(filnavn):
     navn=[]
     stasjonstid=[]
     datoer=[]
     snødybde=[]
     nedbør=[]
     middeltemperatur=[]
     skydekke=[]
     hoyeste_middelvind=[]
     
     with open(filnavn, "r", encoding="UTF-8") as fila:
        dummy_verdi=fila.readlines()
        linjer=dummy_verdi[1:-1]
        for linje in linjer:
                linje.strip
                linjedel=linje.split(";")
                navn.append(linjedel[0])
                stasjonstid.append(linjedel[1])
                
                dato=datetime.strptime(linjedel[2],"%d.%m.%Y").date()
                datoer.append(dato)
                
                snødybde.append(linjedel[3])
                nedbør.append(linjedel[4])
                middeltemperatur.append(linjedel[5])
                skydekke.append(linjedel[6])
                hoyeste_middelvind.append(linjedel[7])
                
                
                
        vaerdata={"navn": navn,
             "navnstasjon": stasjonstid,
             "datoer": datoer,
             "snødybde":snødybde,
             "nedbør":nedbør,
             "middeltemperatur":middeltemperatur,
             "skydekke": skydekke,
             "hoyeste_middelvind":hoyeste_middelvind}
        
        return vaerdata
        

vaerdata=tolk_vaerdata("snoedybder_vaer_en_stasjon_dogn.csv")


        
#Oppgave B
datoer=vaerdata["datoer"]
snodybde=vaerdata["snødybde"]
def skidager(datoer,snodybde):
    skisesonger=dict()
    skisesong_str=[]
    variabel=False
    if datoer[0].month<10:
        aar=datoer[0].year-1
    else :
        aar = datoer.year
    
    for i, dato in enumerate(datoer):
        if(dato.year==aar and dato.month>=10) or (dato.year==aar+1 and dato.month < 6):
            if variabel:
                variabel=False
            skisesong_str.append(snodybde[i])
        else:
             if not variabel:
                skisesong=[]
                for n in skisesong_str:
                    try:
                        skisesong.append(float(n))
                    except ValueError:
                        pass
                
                skisesong=tell_storre_eller_lik_verdi(skisesong,20)
                if not len(skisesong)==0:
                    skisesonger[f"{aar}"]=len(skisesong)
                skisesong_str.clear()
                aar+=1
                variabel=True
                 
                
    return skisesonger
        
skidager=skidager(datoer,snodybde)

print(f"Oppg B: dictionary for skiføredager for sesongen til årene\n{skidager}\n\n")

#Oppg C
def trenden_dataset(skidager):
    listeskiføredager=[]
    liste_x=[]
    for i in skidager.values():
        listeskiføredager.append(i)
    for i in skidager:

       liste_x.append(int(i))
    trend=trenden(liste_x, listeskiføredager)
    a=round(trend[0], 4)
    b=round(trend[1], 2)
    
    return a,b

snøtrenden=trenden_dataset(skidager)
print(f"Oppg C: trenden for skiføredager er {snøtrenden}\n")


def plott_data(datoer,snodybde):
    skisesonger=dict()
    skisesong_str=[]
    variabel=False
    if datoer[0].month<10:
        aar=datoer[0].year-1
    else :
        aar = datoer.year
    
    for i, dato in enumerate(datoer):
        if(dato.year==aar and dato.month>=10) or (dato.year==aar+1 and dato.month < 6):
            if variabel:
                variabel=False
            skisesong_str.append(snodybde[i])
        else:
             if not variabel:
                skisesong=[]
                for n in skisesong_str:
                    try:
                        skisesong.append(float(n))
                    except ValueError:
                        pass
                
               
                if not len(skisesong)==0:
                    skisesonger[f"{aar}"]=len(skisesong)
                skisesong_str.clear()
                aar+=1
                variabel=True
    aarliste=[]
    ski_dict=skidager
    liste_x=[]
    liste_y=[]
    liste_y_trend=[]
    liste_x_int=[]
    for i in skisesonger.keys():
        aarliste.append(i)
    for n, data in enumerate(skisesonger.values()):   
        if data>=200:
            liste_x.append(aarliste[n])
    for j, verdier in enumerate(liste_x):
            liste_y.append(ski_dict[verdier])
    for k in liste_x:
        liste_x_int.append(int(k))
    tall=trenden(liste_x, liste_y)
    for i in liste_x_int:
        a=(float(tall[0])*float(i)+float(tall[1]))
        liste_y_trend.append(a)
    
    plt.plot(liste_x,liste_y,"-o", label="Skisesonger(lengde)")
    plt.plot(liste_x, liste_y_trend,"-o",label="trend")
    plt.xlabel("år")
    plt.ylabel("skiføredager")
    
    
    
plott_data(datoer,snodybde)
