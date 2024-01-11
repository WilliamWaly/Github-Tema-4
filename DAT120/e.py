import matplotlib.pyplot as plt

# Funksjonen for å beregne summen av temperaturer over 5 grader
def sum_over_5(temperaturer):
    total_sum = 0
    dag_sum = []  # Lagre summen for hver dag i året

    for temp in temperaturer:
        if temp > 5:
            total_sum += temp
        dag_sum.append(total_sum)

    return dag_sum

# Manuell inndata av temperaturer for hvert år
temperatur_datasett = {
    
    2022: [1, 6, 4, 7, 8, 3, 10, 2, 6, 8, 5, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8, 5, 3, 8, 2, 9, 4, 7, 1, 6, 8],
    2023: [5, 3, 8, 2, 9, 4, 7, 1, 6, 8, ]
    # Legg til flere år etter behov
}

# Gå gjennom hvert år i datasettet
for year, temperatures in temperatur_datasett.items():
    # Sjekker om det er nok data for å gjøre beregningen (minst 300 dager)
    if len(temperatures) >= 300:
        # Kjør funksjonen og få listen med summen av temperaturer over 5 grader for hver dag
        dag_sum = sum_over_5(temperatures)
        
        # Plot resultatet
        plt.plot(range(1, len(dag_sum) + 1), dag_sum, label=str(year))

# Vis plottet
plt.xlabel('Dag i året')
plt.ylabel('Sum av temperaturer over 5 grader')
plt.legend()
plt.show()