import sys
input = sys.stdin.readline

def getMedian(l):
    n = len(l)
    if n%2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

for t in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ans = float('inf')
    if N == M:
        ans = sum(arr)
    elif M == 1:
        ans = getMedian(arr)
    else:
        ans = getMedian(arr[:N-(M-1)]) + sum(arr[N-(M-1):])
    print(f"Case #{t+1}: "+str(ans))