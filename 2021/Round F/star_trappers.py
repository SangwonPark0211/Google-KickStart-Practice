# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45

from math import sqrt
import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    white = []
    for _ in range(N):
        white.append(list(map(int, input().strip().split())))
    blue = list(map(int, input().strip().split()))

    if N <= 2:
        return "IMPOSSIBLE"
    ans = float('inf')
    for i in range(N):
        for j in range(i+1,N):
            if i==j:
                continue
            for k in range(j+1,N):
                if i==k or j==k:
                    continue
                smaller, larger = 0, 0
                x1, y1 = white[i]
                x2, y2 = white[j]
                x3, y3 = white[k]
                if x1==x2:
                    if x1 < blue[0]:
                        larger += 1
                    elif x1 == blue[0]:
                        continue
                    else:
                        smaller += 1
                else:
                    temp1 = ((y1-y2)/(x1-x2))*blue[0] + y1-((y1-y2)/(x1-x2))*x1
                    if temp1 < blue[1]:
                        larger += 1
                    elif temp1 == blue[1]:
                        continue
                    else:
                        smaller += 1
                if x1==x3:
                    if x1 < blue[0]:
                        larger += 1
                    elif x1 == blue[0]:
                        continue
                    else:
                        smaller += 1
                else:
                    temp2 = ((y1-y3)/(x1-x3))*blue[0] + y1-((y1-y3)/(x1-x3))*x1
                    if temp2 < blue[1]:
                        larger += 1
                    elif temp2 == blue[1]:
                        continue
                    else:
                        smaller += 1
                if x2==x3:
                    if x2 < blue[0]:
                        larger += 1
                    elif x2 == blue[0]:
                        continue
                    else:
                        smaller += 1
                else:
                    temp3 = ((y2-y3)/(x2-x3))*blue[0] + y2-((y2-y3)/(x2-x3))*x2
                    # print(temp3)
                    if temp3 < blue[1]:
                        larger += 1
                    elif temp3 == blue[1]:
                        continue
                    else:
                        smaller += 1
                    # print("larger:", larger, "smaller:", smaller)
                if (smaller == 1 and larger == 2) or (smaller == 2 and larger == 1):
                    perimeter = sqrt((x1-x2)**2+(y1-y2)**2) + sqrt((x1-x3)**2+(y1-y3)**2) + sqrt((x3-x2)**2+(y3-y2)**2)
                    ans = min(ans, perimeter)
    if ans == float('inf'):
        ans = "IMPOSSIBLE"
    return ans

for t in range(int(input())):
    print(f"Case #{t+1}: "+str(sol()))