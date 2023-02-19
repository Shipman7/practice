def sort1(A, B):
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def rec_sort(A):
    if len(A) <= 1:
        return
    mid = len(A) // 2
    L, R = A[:mid], A[mid:]
    rec_sort(L)
    rec_sort(R)
    C = sort1(L, R)
    for i in range(len(A)):
        A[i] = C[i]
    return A
print(*rec_sort(list(map(int, input().split()))))