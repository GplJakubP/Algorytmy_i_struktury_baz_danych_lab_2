def oblicz_sume(tablica, lewy_indeks, prawy_indeks):
    if lewy_indeks == prawy_indeks:
        return tablica[lewy_indeks]
    else:
        srodek = (lewy_indeks + prawy_indeks) // 2
        lewa_suma = oblicz_sume(tablica, lewy_indeks, srodek)
        prawa_suma = oblicz_sume(tablica, srodek + 1, prawy_indeks)
        return lewa_suma + prawa_suma
tablica = []
n = int(input("Podaj liczbę elementów tablicy: "))
for i in range(n):
    element = int(input("Podaj element tablicy: "))
    tablica.append(element)
suma = oblicz_sume(tablica, 0, len(tablica) - 1)
print("Suma elementów w tablicy wynosi:", suma)
