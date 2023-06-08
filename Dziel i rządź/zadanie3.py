def znajdz_najwiekszy_element(wektor, lewy_indeks, prawy_indeks):
    if lewy_indeks == prawy_indeks:
        return wektor[lewy_indeks]
    else:
        srodek = (lewy_indeks + prawy_indeks) // 2
        lewy_najwiekszy = znajdz_najwiekszy_element(wektor, lewy_indeks, srodek)
        prawy_najwiekszy = znajdz_najwiekszy_element(wektor, srodek + 1, prawy_indeks)
        return max(lewy_najwiekszy, prawy_najwiekszy)
wektor = []
n = int(input("Podaj liczbę elementów wektora: "))
for i in range(n):
    element = int(input("Podaj element wektora: "))
    wektor.append(element)
najwiekszy_element = znajdz_najwiekszy_element(wektor, 0, len(wektor) - 1)
print("Największy element wektora to:", najwiekszy_element)
