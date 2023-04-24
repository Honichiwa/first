import matematika
from geometrija.kvadratas import kvadrato_plotas as k_plotas
from geometrija.apskritimas import apskritimo_plotas as a_plotas
import random
import calendar

# print(matematika.daugyba(6, 6))
# print(matematika.dalyba(8, 4))

# print(a_plotas(20))
# print(k_plotas(80))


# def sort_random_skaicius():
#     random_skaiciai = []
#     for a in range(10):
#         random_skaicius = [random.randint(1, 100)]
#         random_skaiciai.append(random_skaicius)
#     print(sorted(random_skaiciai))


# sort_random_skaicius()
# kauliukai = []
# while len(kauliukai) < 3:
#     for a in range(3):
#         vaziuojam = input("metam kauliuka")
#         kauliukas = random.randint(1, 6)
#         print(kauliukas)
#         kauliukai.append(kauliukas)
#     if 5 in kauliukai:
#         print("pralaimejai")
#     else:
#         print("laimejai")


# def kalendorius(metai, menesis):
#     print(calendar.month(metai, menesis))
#     a = calendar.monthrange(metai, menesis)
#     abc = [4, 5]
#     if a[0] in abc and a[1] == 30:
#         print("menesyje yra 5 pilni savaitgaliai")
#     else:
#         print("menesyje yra 4 pilni savaitgaliai")


# kalendorius(2023, 6)


def kalendorius(metai, menesis):
    print(calendar.month(metai, menesis))
    menesio_ilgis = calendar.monthrange(metai, menesis)
    savaitgalio_dienos = 0
    print(menesio_ilgis)
    for diena in range(1, menesio_ilgis[1] + 1):
        savaites_diena = calendar.weekday(metai, menesis, diena)
        if savaites_diena == 5 or savaites_diena == 6:
            savaitgalio_dienos += 1

    print(f"Savaitgalio dienų skaičius šiame mėnesyje: {savaitgalio_dienos}")


kalendorius(2023, 8)
