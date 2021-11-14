# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b813

T = int(input())
for t in range(T):
    A = []
    for i in range(3):
        temp = list(map(int, input().split()))
        if i==1:
            temp = [temp[0]] + ['N'] + [temp[1]]
        A.append(temp)
    avg = []
    if (A[0][0]+A[2][2])%2 == 0:
        avg.append((A[0][0]+A[2][2])//2)
    if (A[0][1]+A[2][1])%2==0:
        avg.append((A[0][1]+A[2][1])//2)
    if (A[0][2]+A[2][0])%2==0:
        avg.append((A[0][2]+A[2][0])//2)
    if (A[1][0]+A[1][2])%2==0:
        avg.append((A[1][0]+A[1][2])//2)
    avg_cnt = {}
    for k in avg:
        if k not in avg_cnt:
            avg_cnt[k] = 1
        else:
            avg_cnt[k] += 1
    # find max count
    max_cnt = 0
    for k in avg_cnt:
        max_cnt = max(max_cnt, avg_cnt[k])
    for k in avg_cnt:
        if avg_cnt[k]==max_cnt:
            max_cnt_num = k
    A[1][1] = max_cnt_num
    # 4 edge check
    edge_cnt = 0
    if A[0][1]-A[0][0] == A[0][2]-A[0][1]:
        edge_cnt += 1
    if A[1][2]-A[0][2] == A[2][2]-A[1][2]:
        edge_cnt += 1
    if A[2][1]-A[2][0] == A[2][2]-A[2][1]:
        edge_cnt += 1
    if A[1][0]-A[0][0] == A[2][0]-A[1][0]:
        edge_cnt += 1
    ans = max_cnt + edge_cnt
    print(f"Case #{t+1}: " + str(ans))