# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b933

from collections import Counter

def cuttingIntervals():
    N, C = map(int, input().split())
    intervals = []
    for _ in range(N):
        s, e = map(int, input().split())
        intervals.append((s,e))

    pos_lines = {}
    for s, e in intervals:
        if s+1 not in pos_lines:
            pos_lines[s+1] = 0
        pos_lines[s+1] += 1
        if e not in pos_lines:
            pos_lines[e] = 0
        pos_lines[e] -= 1
    pos_lines = sorted(pos_lines.items())
    # print(pos_lines)

    cuts_lines = []
    affected_lines = 0
    for i in range(len(pos_lines)-1):
        affected_lines += pos_lines[i][1]
        possible_cuts = pos_lines[i+1][0] - pos_lines[i][0]
        cuts_lines.append((affected_lines, possible_cuts))
    cuts_lines = sorted(cuts_lines, reverse=True)
    
    ans = N
    for lines, cuts in cuts_lines:
        if cuts<=C:
            ans += lines * cuts
            C -= cuts
        else:
            ans += lines * C
            break
    return ans


for t in range(int(input())):
    print(f"Case #{t+1}: " + str(cuttingIntervals()))