def tell_storre_eller_lik_verdi(liste, verdi):
    teller = 0
    for element in liste:
        if element >= verdi:
            teller += 1
    return teller

min_liste = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
verdi=float(input("Skriv inn verdien her: "))
antall_storre_eller_lik = tell_storre_eller_lik_verdi(min_liste, verdi)
print(f"Antall elementer større enn eller lik {verdi}: {antall_storre_eller_lik}")
