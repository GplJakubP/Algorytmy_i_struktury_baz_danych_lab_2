def merge(l, m, r, A, B):
    i, j, k = l, m, l
    while i < m and j <= r:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    while i < m:
        B[k] = A[i]
        i += 1
        k += 1
    while j <= r:
        B[k] = A[j]
        j += 1
        k += 1
def main():
    A = [1, 35, 42, 65, 68, 25, 55, 59, 70, 79]
    B = [0] * len(A)
    merge(0, 5, 9, A, B)
    for b in B:
        print(b, end=' ')
if __name__ == '__main__':
    main()
