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
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
lengde = lengste_null_sekvens(dogn_nedbor)
print(f"Lengden på den lengste sekvensen av nuller er: {lengde}")
