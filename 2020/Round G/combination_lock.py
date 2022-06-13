# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24
import sys
input = sys.stdin.readline

def sol():
    W, N = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ans = float('inf')
    target = arr[0]
    temp_ans = 0
    for i in range(len(arr)):
        temp_ans += min(abs(target-arr[i]), N-abs(target-arr[i]))
    ans = min(ans, temp_ans)
    target = arr[-1]
    temp_ans = 0
    for i in range(len(arr)):
        temp_ans += min(abs(target-arr[i]), N-abs(target-arr[i]))
    ans = min(ans, temp_ans)
    
    return ans
    
for case in range(int(input())):
    print(f"Case #{case+1}: "+str(sol()))