# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14

import heapq

import copy 
D = ((1,0),(-1,0),(0,1),(0,-1))
T = int(input())
for t in range(T):
    arr = []
    r, c = map(int, input().split())
    for i in range(r):
        temp = list(map(int, input().split()))
        arr.append(temp)
    q = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0:
                heapq.heappush(q, (-arr[i][j], (i,j)))
    visit = [[0 for _ in range(c)] for _ in range(r)]
    result = copy.deepcopy(arr)
    while q:
        element = heapq.heappop(q)
        value, x, y = -element[0], element[1][0], element[1][1]
        if visit[x][y] != 1:
            visit[x][y] = 1
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0<=nx<=r-1 and 0<=ny<=c-1 and visit[nx][ny] == 0:
                    result[nx][ny] = max(result[nx][ny], value-1)
                    heapq.heappush(q, (-result[nx][ny], (nx,ny)))
    cnt = 0
    for i in range(r):
        for j in range(c):
            cnt += result[i][j] - arr[i][j]
    print(f"Case #{t+1}: " + str(cnt))
    





