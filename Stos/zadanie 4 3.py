class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty.")
            return None
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty.")
            return None
    def size(self):
        return len(self.items)
def oblicz_wartosc_postfix(wyrazenie):
    stos = Stack()
    for token in wyrazenie:
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') == 1):
            stos.push(float(token))
        elif token == '+':
            operand2 = stos.pop()
            operand1 = stos.pop()
            wynik = operand1 + operand2
            stos.push(wynik)
        elif token == '-':
            operand2 = stos.pop()
            operand1 = stos.pop()
            wynik = operand1 - operand2
            stos.push(wynik)
        elif token == '*':
            operand2 = stos.pop()
            operand1 = stos.pop()
            wynik = operand1 * operand2
            stos.push(wynik)
        elif token == '/':
            operand2 = stos.pop()
            operand1 = stos.pop()
            if operand2 != 0:
                wynik = operand1 / operand2
                stos.push(wynik)
            else:
                print("Error: Division by zero")
                return None
        elif token == '^':
            operand2 = stos.pop()
            operand1 = stos.pop()
            wynik = operand1 ** operand2
            stos.push(wynik)
        else:
            print("Error: Invalid operator")
            return None
    if stos.size() == 1:
        return stos.pop()
    else:
        print("Error: Invalid expression")
        return None
wyrazenie_postfix = input("Wprowadź wyrażenie w notacji postfiksowej: ").split()
wynik = oblicz_wartosc_postfix(wyrazenie_postfix)
if wynik is not None:
    print("Wynik:", wynik)
