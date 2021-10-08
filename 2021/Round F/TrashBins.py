T = int(input())
for t in range(T):
    n = int(input())
    arr = input()
    L, R = [500001 for _ in range(n)], [500001 for _ in range(n)]
    # select left only
    pos = -1
    for i in range(n):
        if arr[i]=='0' and pos==-1:
            continue
        if arr[i]=='1':
            L[i] = 0
            pos = i
        else:
            L[i] = i-pos
    # select right only
    pos = -1
    for i in range(n-1,-1,-1):
        if arr[i]=='0' and pos == -1:
            continue
        if arr[i]=='1':
            R[i] = 0
            pos = i
        else:
            R[i] = pos-i
    ans = 0
    for i in range(n):
        ans += min(L[i], R[i])
    
    print(f"Case #{t+1}: {ans}")