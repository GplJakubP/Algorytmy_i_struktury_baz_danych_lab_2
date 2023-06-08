Sn = {}
def calculate_nth_term(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n in Sn:
            return Sn[n]
    Sn[n-1] = calculate_nth_term(n-1)
    Sn[n-2] = calculate_nth_term(n-2)
    Sn[n] = 2 * Sn[n-1] - Sn[n-2]
    return Sn[n]
n = int(input("Podaj wartość n: "))
result = calculate_nth_term(n)
print(f"N-ty wyraz dla n={n}: {result}")
