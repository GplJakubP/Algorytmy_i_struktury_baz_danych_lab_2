from collections import deque
def gra_goracy_ziemniak(uczestnicy, liczba_operacji):
    kolejka = deque(uczestnicy)
    while len(kolejka) > 1:
        for _ in range(liczba_operacji):
            kolejka.rotate(-1) 
        uczestnik = kolejka.popleft() 
        print(f"Uczestnik {uczestnik} odpada z gry.")
    zwyciezca = kolejka.pop()
    print(f"\nZwycięzca gry: {zwyciezca}")
uczestnicy = ['Kuba', 'Marek', 'Adrain', 'Damian', 'Jan', 'Filip']
liczba_operacji = 3
gra_goracy_ziemniak(uczestnicy, liczba_operacji)
