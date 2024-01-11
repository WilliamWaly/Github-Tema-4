temperaturer = [4, 7, 15]

def sum_over_5(temperaturer):
    total_sum = 0  # Initialiser total sum til 0

    # Loop gjennom hvert element i listen
    for temp in temperaturer:
        if temp > 5:
            forskjell = temp - 5  # Beregn differansen mellom temperaturen og 5
            total_sum += forskjell  # Legg til differansen til total sum

    return total_sum  # Returner den totale summen

resultat=sum_over_5(temperaturer)
print(resultat)
