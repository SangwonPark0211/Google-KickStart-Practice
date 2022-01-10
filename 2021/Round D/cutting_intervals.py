# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b933

from collections import Counter

def find_intersect(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    common = s1.intersection(s2)
    return len(common)

def cuttingIntervals():
    N, C = map(int, input().split())
    intervals = []
    for _ in range(N):
        s, e = map(int, input().split())
        intervals.append((s,e))
    counter = {}
    for s, e in intervals:
        for i in range(s+1, e):
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
    counter = sorted(counter.items(), key=lambda x : x[1], reverse=True)
    cut_pos = []
    for i, c in enumerate(counter):
        if i+1 > C: break
        cut_pos.append(c[0])
    ans = 0
    for s, e in intervals:
        ans += find_intersect(cut_pos, range(s+1, e)) + 1
    return ans

for t in range(int(input())):
    print(f"Case #{t+1}: " + str(cuttingIntervals()))