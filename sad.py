
N = int(input())
L = [0]*1000
L[1] = 10
L[2] = 100
if N > 2:
    for i in range(3, N+1):
        L[i] = (L[i-1]*12+L[i-2]) % 1000000007
print(L[N])