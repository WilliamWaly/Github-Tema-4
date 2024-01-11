def tell_temperaturdager(temperaturer):
    antall_sommerdager = 0
    antall_hoysommerdager = 0
    antall_tropedager = 0

    for temperatur in temperaturer:
        if temperatur > 20:
            antall_sommerdager += 1
        if temperatur > 25:
            antall_hoysommerdager += 1
        if temperatur > 30:
            antall_tropedager += 1

    return antall_sommerdager, antall_hoysommerdager, antall_tropedager

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]
antall_sommerdager, antall_hoysommerdager, antall_tropedager = tell_temperaturdager(temperaturer)

print("Antall sommerdager (over 20 grader):", antall_sommerdager)
print("Antall hoysommerdager (over 25 grader):", antall_hoysommerdager)
print("Antall tropedager (over 30 grader):", antall_tropedager)
