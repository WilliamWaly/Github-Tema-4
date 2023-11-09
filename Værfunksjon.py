# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 22:20:56 2023

@author: magnu
"""
from datetime import datetime

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
        linjer1=fila.readlines()
        linjer=linjer1[1:-1]
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
        print(datoer[2])
        return vaerdata
        

værdata=tolk_vaerdata("snoedybder_vaer_en_stasjon_dogntest.csv")



                     
                    
                
            
                    
                    
                   
                
            

            
            
    
    