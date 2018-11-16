
N = int(input())
L = []
for i in range(N):
    Ltemp = list(map(int, input().split()))
    Ltemp.pop(len(Ltemp)-1)
    Ltemp.append(i+1)
    L.append(Ltemp)
L1 = []
while len(L) > 0:
    ltemp = L.pop()
    flag = True
    for i in range(len(L)):
        if len(set(ltemp).intersection(L[i])) != 0:
            L[i] = list(set(ltemp).union(set(L[i])))
            flag = False
            break
    if flag:
        L1.append(ltemp)

print(L1)
