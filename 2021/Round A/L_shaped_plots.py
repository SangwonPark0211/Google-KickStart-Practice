# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509#analysis
import copy
T = int(input())
for t in range(T):
    arr = []
    r,c = map(int, input().split())
    for i in range(r):
        temp = list(map(int, input().split()))
        arr.append(temp)
    U, D, L, R = copy.deepcopy(arr), copy.deepcopy(arr), copy.deepcopy(arr), copy.deepcopy(arr)
    for i in range(1, r):
        for j in range(c):
            if arr[i][j] == 1:
                U[i][j] += U[i-1][j]
    for i in range(r-2, -1, -1):
        for j in range(c):
            if arr[i][j] == 1:
                D[i][j] += D[i+1][j]
    for i in range(r):
        for j in range(1,c):
            if arr[i][j] == 1:
                L[i][j] += L[i][j-1]
    for i in range(r):
        for j in range(c-2, -1, -1):
            if arr[i][j] == 1:
                R[i][j] += R[i][j+1]
    ans = 0
    for i in range(r):
        for j in range(c):
            ans += max(min(U[i][j]//2, R[i][j])-1, 0)
            ans += max(min(U[i][j]//2, L[i][j])-1, 0)
            ans += max(min(D[i][j]//2, R[i][j])-1, 0)
            ans += max(min(D[i][j]//2, L[i][j])-1, 0)
            ans += max(min(R[i][j]//2, D[i][j])-1, 0)
            ans += max(min(R[i][j]//2, U[i][j])-1, 0)
            ans += max(min(L[i][j]//2, D[i][j])-1, 0)
            ans += max(min(L[i][j]//2, U[i][j])-1, 0)
    print(f"Case #{t+1}: " + str(ans))

    
