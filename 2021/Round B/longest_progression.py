# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a3a5

T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 2 or n == 3:
        print(f'Case #{t+1}: ' + str(n))
        continue
    start, end = [0 for _ in range(n)], [0 for _ in range(n)]
    for i in range(n-2):
        j = i + 1
        while arr[j] - arr[j-1] == arr[j+1] - arr[j]:
            j += 1
            if j == n-1:
                break
        start[i] = j - i + 1
    start[-1] = 1
    start[-2] = 2
    end[0] = 1
    end[1] = 2
    for i in range(2, n):
        j = i - 1
        while arr[j+1] - arr[j] == arr[j] - arr[j-1]:
            j -= 1
            if j == 0:
                break
        end[i] = i - j + 1
    ans = 0
    # when removing arr[0]
    d = arr[2] - arr[1]
    k = 3
    while k<n and arr[k]-arr[k-1] == d:
        k += 1
    ans = k
        
    # when removing arr[n-1]
    d = arr[n-2] - arr[n-3]
    k = n-4
    while k>=0 and arr[k+1] - arr[k] == d:
        k -= 1
    ans = max(ans, n-1-k)
    

    # when removing arr[1]
    if arr[2] - arr[0] == 2 * (arr[3] - arr[2]):
        ans = max(ans, end[0] + 1 + start[2])
    
    # when removing arr[n-2]
    if (arr[n-3] - arr[n-4]) * 2 == arr[n-1] - arr[n-3]:
        ans = max(ans, end[n-3] + 1 + start[-1])

    for i in range(2, n-2):
        if arr[i-1] - arr[i-2] == arr[i+2] - arr[i+1] and (arr[i-1] - arr[i-2]) * 2 == arr[i+1] - arr[i-1]:
            ans = max(ans, end[i-1] + 1 + start[i+1])
        elif arr[i-1] - arr[i-2] != arr[i+2] - arr[i+1] and (arr[i-1] - arr[i-2]) * 2 == arr[i+1] - arr[i-1]:
            ans = max(ans, end[i-1] + 2)
    print(f'Case #{t+1}: ' + str(ans))
    # print(start)
    # print(end)
    
    