import sys
input = sys.stdin.readline

def sol():
    num = input().strip()
    num_sum = sum(list(map(int, list(num))))

    if num_sum % 9 == 0:
        return int(num[0]+'0'+num[1:])
    else:
        p = (num_sum // 9 + 1)*9 - num_sum
        # ans = min(int(str(p)+num), int(num+str(p)))
        # for i in range(1, len(num)):
        #     ans = min(ans, int(num[:i]+str(p)+num[i:]))
        ans = 0
        for i in range(len(num)):
            if p < int(num[i]):
                ans = int(num[:i] + str(p) + num[i:])
                break
        if ans == 0:
            ans = int(num+str(p))

        return ans

for t in range(int(input().strip())):
    print(f"Case #{t+1}: "+str(sol()))