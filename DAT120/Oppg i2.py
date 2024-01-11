from datetime import datetime
import matplotlib.pyplot as plt

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
            linje.strip()
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

# #Tar en liste som input og lager en ny liste med differansene mellom elementene
def finn_forskjell(listen):
    forskjeller = []
    for element in range(len(listen) - 1):
        forskjell = listen[element + 1] - listen[element]
        forskjeller.append(forskjell)
    return forskjeller

#Tar værdata som input, organiserer temperaturdataene per måned, beregner gjennomsnittstemperaturen for hver måned, og lagrer resultatene i en liste.
def gjennomsnittstemperatur_per_måned(vaerdata):
    månedlig_gjennomsnitt = {}
    
    for i in range(len(vaerdata["datoer"])):
        måned_år = vaerdata["datoer"][i].strftime("%m-%Y")
        temperatur_str = vaerdata["middeltemperatur"][i].replace(',', '.')

        if temperatur_str == '-':
            continue

        temperatur = float(temperatur_str) 
        
        if måned_år not in månedlig_gjennomsnitt:
            månedlig_gjennomsnitt[måned_år] = [temperatur]
        else:
            månedlig_gjennomsnitt[måned_år].append(temperatur)
    
    gjennomsnittstemperaturer = []
    
    for måned_år, temperaturer in månedlig_gjennomsnitt.items():
        gjennomsnitt_temperatur = sum(temperaturer) / len(temperaturer)
        gjennomsnittstemperaturer.append(gjennomsnitt_temperatur)
    
    return gjennomsnittstemperaturer

#Bruker de to funksjonene til å tolke værdata fra en CSV-fil, gjennomsnittstemperaturen per måned, differansene mellom påfølgende måneder, og plotte resultatene.
def main():
    vaerdata = tolk_vaerdata("snoedybder_vaer_en_stasjon_dogn.csv")
    gjennomsnittstemperaturer = gjennomsnittstemperatur_per_måned(vaerdata)
    differanser = finn_forskjell(gjennomsnittstemperaturer)
    
    # Plot gjennomsnittstemperaturer
    plt.subplot(2, 1, 1)
    plt.plot(gjennomsnittstemperaturer, marker='o')
    plt.title('Gjennomsnittstemperatur per måned')
    plt.xlabel('Måned og år')
    plt.ylabel('Temperatur (°C)')
    
    # Plot differanser
    plt.subplot(2, 1, 2)
    plt.plot(differanser, marker='o', color='r')
    plt.title('Differanser mellom gjennomsnittstemperaturer')
    plt.xlabel('Måned og år')
    plt.ylabel('Temperaturdifferanse (°C)')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
