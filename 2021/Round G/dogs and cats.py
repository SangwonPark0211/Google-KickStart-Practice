# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3771

T = int(input())
for t in range(T):
    N, D, C, M = list(map(int, input().split()))
    S = input()
    dog_max = -1   # max index of 'D'
    for i in range(N-1, -1, -1):
        if S[i] =='D':
            dog_max = i
            break
    if dog_max == -1:
        print(f"Case #{t+1}: YES")
        continue
    ans = "YES"
    for i in range(N):
        # two NO case
        if S[i]=='C' and C==0 and i<dog_max:
            ans = 'NO'
            break
        elif S[i]=='D' and D==0:
            ans = 'NO'
            break
        # update
        if S[i] == 'C':
            C -= 1
        elif S[i] == 'D':
            D -= 1
            C += M

    print(f"Case #{t+1}: " + ans)
        
