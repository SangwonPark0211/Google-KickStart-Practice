# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082bffc
from collections import deque

def sol():
    ans = []
    N, M = map(int, input().split())
    p_set = []
    for _ in range(N):
        a, b = map(int, input().split())
        p_set.append([a,b])
    p_set.sort()
    q = deque()
    for a,b in p_set:
        q += range(a,b+1)
    students = list(map(int, input().split()))

    for key in students:
        # binary search
        l, r = 0, len(q)-1
        diff = float('inf')
        idx = -1
        difficulty = 0
        while l<=r:
            if key in set(q):
                idx = q.index(key)
                difficulty = key
                break
            mid = (l+r)//2
            if q[mid] < key:
                l = mid+1
            else:
                r = mid-1
            if diff > abs(q[mid]-key):
                diff = abs(q[mid]-key)
                difficulty = q[mid]
                idx = mid
            elif diff == abs(q[mid]-key):
                if difficulty > q[mid]:
                    difficulty = q[mid]
                    idx = mid
        ans.append(difficulty)
        del q[idx]
        
    return ans

for t in range(int(input())):
    print(f"Case #{t+1}: " + ' '.join(list(map(str, sol()))))