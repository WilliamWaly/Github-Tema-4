import numpy as np
import matplotlib.pyplot as plt

# Funksjonen for å finne høyeste middelvind og medianen for vindstyrke
def vindstatistikk(vindstyrker):
    middelvind = np.mean(vindstyrker)
    
    # Kopierer vindstyrker så man unngår endringer i den opprinnelige listen
    sorted_vindstyrker = sorted(vindstyrker)
    
    # Hvis lengden av listen er oddetall, er medianen midtelementet. Ellers gjennomsnittet av midteelementene.
    midt_indeks = len(sorted_vindstyrker) // 2
    if len(sorted_vindstyrker) % 2 == 1:
        median_vind = sorted_vindstyrker[midt_indeks]
    else:
        median_vind = (sorted_vindstyrker[midt_indeks - 1] + sorted_vindstyrker[midt_indeks]) / 2

    return middelvind, median_vind

# Manuell inndata av vindstyrker for hvert år
vindstyrke_datasett = {
    2019: [ 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11],
    2020: [12, 14, 11, 10, 13, 15, 9, 11, 14, 12, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 12, 14, 11, 10, 13, 15, 9, 11, 14, 12, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 12, 14, 11, 10, 13, 15, 9, 11, 14, 12, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 12, 14, 11, 10, 13, 15, 9, 11, 14, 12, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15, 8, 12, 10, 14, 18, 10, 9, 11, 10, 15],
    # Legg til flere år her
}

# Gå gjennom hvert år i datasettet
for year, vindstyrker in vindstyrke_datasett.items():
    # Sjekk om det er nok data for å gjøre beregningen (minst 300 dager)
    if len(vindstyrker) >= 300:
        # Kjør funksjonen og få høyeste middelvind og medianen for vindstyrke
        middelvind, median_vind = vindstatistikk(vindstyrker)
        
        # Skriv ut resultatet for hvert år
        print(f"År {year}: Høyeste middelvind er: {middelvind}, Median vindstyrke er: {median_vind}")

        # Plot resultatet
        plt.plot(range(1, len(vindstyrker) + 1), vindstyrker, label=str(year))

# Vis plottet
plt.xlabel('Dag i året')
plt.ylabel('Vindstyrke')
plt.legend()
plt.show()