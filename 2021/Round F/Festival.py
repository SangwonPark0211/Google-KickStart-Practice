T = int(input())
for t in range(T):
    D, N, K = list(map(int, input().split()))
    attraction = []
    for _ in range(N):
        temp = list(map(int, input().split()))  # input rating, start day, end day
        attraction.append(temp)
    # sort attraction by rating in decreasing order
    attraction.sort(key=lambda x:x[0], reverse=True)
    day_arr = [[] for _ in range(D + 1)]
    for i in range(N):
        r, s, e = attraction[i]
        for j in range(s,e+1):
            if len(day_arr[j])==K:
                continue
            day_arr[j].append(r)
            
    ans = -1
    for i in range(len(day_arr)):
        if day_arr[i]:
            ans = max(ans, sum(day_arr[i][:K]))
    print(f"Case #{t+1}: {ans}")


