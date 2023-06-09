def sprawdz_poprawnosc_symboli(symbole):
    stos = []
    opening_symbols = ['(', '[', '{', '<', '/']
    closing_symbols = [')', ']', '}', '>', '/']

    for symbol in symbole:
        if symbol in opening_symbols:
            stos.append(symbol)
        elif symbol in closing_symbols:
            if len(stos) == 0 or stos[-1] != opening_symbols[closing_symbols.index(symbol)]:
                return False
            stos.pop()
        else:
            return False
    return len(stos) == 0
symbole_input = input("Wprowadź symbole: ")
symbole = list(symbole_input)
wynik = sprawdz_poprawnosc_symboli(symbole)
if wynik:
    print("Symbole są poprawnie sparowane.")
else:
    print("Symbole nie są poprawnie sparowane.")
