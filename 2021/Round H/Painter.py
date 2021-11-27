# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9a88

import copy

d = {'R':['R'], 'B':['B'], 'Y':['Y'], 'O':['R', 'Y'], 'P':['R', 'B'], 'G':['Y', 'B'], 'A':['R', 'Y', 'B'], 'U':[]}
T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    job = []
    for i in range(n):
        job.append(copy.deepcopy(d[s[i]]))
    cnt = 0
    R_list, B_list, Y_list = [0]*n, [0]*n, [0]*n
    for i in range(len(job)):
        if 'R' in job[i]:
            R_list[i] = 1
        if 'B' in job[i]:
            B_list[i] = 1
        if 'Y' in job[i]:
            Y_list[i] = 1
    if R_list[0] == 1:
        cnt += 1
    for i in range(1,n):
        if R_list[i-1]==0 and R_list[i]==1:
            cnt += 1
    if B_list[0] == 1:
        cnt += 1
    for i in range(1,n):
        if B_list[i-1]==0 and B_list[i]==1:
            cnt += 1 
    if Y_list[0] == 1:
        cnt += 1
    for i in range(1,n):
        if Y_list[i-1]==0 and Y_list[i]==1:
            cnt += 1
    print(f'Case #{t+1}: '+str(cnt))

    
