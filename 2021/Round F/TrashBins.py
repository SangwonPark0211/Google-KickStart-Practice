T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, list(input())))
    trash_house = []
    if arr[0] != 1:
        trash_house.append(-100)
    for i in range(len(arr)):
        if arr[i]==1:
            trash_house.append(i)
    if trash_house[-1] != n-1:
        trash_house.append(n+100)

    k=0
    ans = 0
    for i in range(n):
        if arr[i]==1:
            k+=1
            if trash_house[k]==n+100:
                break
            continue
        ans += min(i-trash_house[k], trash_house[k+1]-i)
    for i in range(trash_house[k-1]+1, n):
        ans += arr[i] - trash_house[k-1]
    print(f"Case #{t+1}: {ans}")