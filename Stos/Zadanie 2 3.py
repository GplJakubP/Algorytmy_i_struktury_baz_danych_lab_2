from Zadanie13 import Stack
def SPR(symbolString):
    s= Stack()
    index = 0
    error = True
    while index <len(symbolString) and error:
        symbol = symbolString[index]
        if symbol == "(":s.push(symbol)
        else:
            if s.isEmpty(): error=False
            else: s.pop()
        index = index+1
    if error and s.isEmpty(): return True
    else : return False
print(SPR('(()()()())'))
print(SPR('((((())))'))
print(SPR('(()()()())')) 
