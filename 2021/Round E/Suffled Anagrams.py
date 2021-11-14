# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a152
import copy

T = int(input())
for t in range(T):
    s = list(input())
    n = len(s)
    
    # IMPORSSIBLE case check
    alpha_cnt = {}
    for i in range(n):
        if s[i] not in alpha_cnt:
            alpha_cnt[s[i]] = 1
        else:
            alpha_cnt[s[i]] += 1
    imp = 0
    for k,v in alpha_cnt.items():
        if v > n//2:
            imp = 1
            break
    if imp == 1:
        print(f"Case #{t+1}: IMPOSSIBLE")
        continue

    # find anagram
    temp = copy.deepcopy(s)
    for i in range(n):
        if temp[i] == s[i]:
            for j in range(n):
                if temp[i]!=s[j] and temp[j]!=s[i]:
                    temp[i], temp[j] = temp[j], temp[i]
                    break
    print(f"Case #{t+1}: " + ''.join(temp))
