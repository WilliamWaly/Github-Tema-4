def lengste_null_sekvens(liste):
    naavaerende_sekvens = 0
    lengste_sekvens = 0

    for num in liste:
        if num == 0:
            naavaerende_sekvens += 1
            if naavaerende_sekvens > lengste_sekvens:
                lengste_sekvens = naavaerende_sekvens
        else:
            naavaerende_sekvens = 0

    return lengste_sekvens

# Eksempel:
min_liste = [0, 1, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lengde = lengste_null_sekvens(min_liste)
print(f"Lengden paa den lengste sekvensen av nuller er: {lengde}")
