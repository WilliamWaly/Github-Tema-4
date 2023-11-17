import numpy as np
import matplotlib.pyplot as plt

# Funksjonen for å beregne summen av temperaturer over 5 grader
def sum_over_5(temperaturer):
    total_sum = 0
    daily_sums = []  # Lagre summen for hver dag i året

    for temp in temperaturer:
        if temp > 5:
            total_sum += temp
        daily_sums.append(total_sum)

    return daily_sums

# Genererer tilfeldige temperaturer for hvert år, veit ikkje om vi fekk eksempel datasett
# Men dette funker
np.random.seed(42)  # For å gjøre resultatene gjentatte for testing
years = range(2020, 2023)
temperatur_datasett = {year: np.random.randint(-10, 20, 365) for year in years}

# Gå gjennom hvert år i datasettet
for year, temperatures in temperatur_datasett.items():
    # Sjekk om det er nok data for å gjøre beregningen (minst 300 dager)
    if len(temperatures) >= 300:
        # Kjør funksjonen og få listen med summen av temperaturer over 5 grader for hver dag
        daily_sums = sum_over_5(temperatures)
        
        # Plot resultatet
        plt.plot(range(1, len(daily_sums) + 1), daily_sums, label=str(year))

# Vis plottet
plt.xlabel('Dag i året')
plt.ylabel('Sum av temperaturer over 5 grader')
plt.legend()
plt.show()