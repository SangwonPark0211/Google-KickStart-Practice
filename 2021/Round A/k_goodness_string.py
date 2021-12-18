# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    former = S[:N//2]
    if N%2 == 0:
        latter = S[N//2:]
    else:
        latter = S[N//2+1:]
    latter = latter[::-1]
    for i in range(len(former)):
        if former[i]!=latter[i]:
            cnt += 1
    print(f"Case #{t+1}: " + str(abs(K-cnt)))
