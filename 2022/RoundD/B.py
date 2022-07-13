import sys
input = sys.stdin.readline

def getMaxSum(cnt, ltr, rtl):
    case = [[i,cnt-i] for i in range(cnt+1)]
    ans = 0
    for f, b in case:
        temp = ltr[f] + rtl[len(ltr)-1-b]
        ans = max(temp, ans)
    return ans
    
for t in range(int(input())):
    N = int(input())
    A = list(map(int, input().strip().split()))
    M = int(input())
    B = list(map(int, input().strip().split()))
    K = int(input())

    A_ltr, A_rtl = [0]*(len(A)+1), [0]*(len(A)+1)
    B_ltr, B_rtl = [0]*(len(B)+1), [0]*(len(B)+1)
    for i in range(1, len(A_ltr)):
        A_ltr[i] = A_ltr[i-1] + A[i-1]
    for i in range(1, len(B_ltr)):
        B_ltr[i] = B_ltr[i-1] + B[i-1]
    for i in range(len(A_rtl)-2, -1, -1):
        A_rtl[i] = A_rtl[i+1] + A[i]
    for i in range(len(B_rtl)-2, -1, -1):
        B_rtl[i] = B_rtl[i+1] + B[i]
        
    case = [[i,K-i] for i in range(K+1)]
    ans = 0
    for f,b in case:
        if f>len(A) or b>len(B):
            continue
        else:
            ans = max(ans, getMaxSum(f, A_ltr, A_rtl)+getMaxSum(b, B_ltr, B_rtl))

    print(f"Case #{t+1}: "+str(ans))