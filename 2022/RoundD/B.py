import sys
input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    arr1 = list(map(int, input().strip().split()))
    M = int(input())
    arr2 = list(map(int, input().strip().split()))
    K = int(input())

    dp1, dp2, dp3, dp4 = [0]*(N+1), [0]*(N+1), [0]*(M+1), [0]*(M+1)
    for i in range(1, N+1):
        dp1[i] = dp1[i-1] + arr1[i-1]
    for i in range(N-1, -1, -1):
        dp2[i] = dp2[i+1] + arr1[i]
    for i in range(1, M+1):
        dp3[i] = dp3[i-1] + arr2[i-1]
    for i in range(M-1, -1, -1):
        dp4[i] = dp4[i+1] + arr2[i]
    ans = 0
    for x in range(N+1):
        for y in range(N, -1, -1):
            if x+(N-y) > K or x+(N-y)>N:
                break
            for w in range(M+1):
                if x+(N-y)+w > K:
                    break
                for z in range(M, -1, -1):
                    if x+(N-y)+w+(M-z) > K or w+(M-z)>M:
                        break
                    if x+(N-y)+w+(M-z) == K:
                        # if x+(N-y)<=N and w+(M-z)<=M:
                        ans = max(ans, dp1[x]+dp2[y]+dp3[w]+dp4[z])
                        
    print(f"Case #{t+1}: "+str(ans))