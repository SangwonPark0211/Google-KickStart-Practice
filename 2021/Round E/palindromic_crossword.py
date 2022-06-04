# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/0000000000859dcd

import sys
input = sys.stdin.readline
from collections import deque

def get_vertical_target_pos(arr, x, y):
    # up
    up = 0
    for i in range(x-1,-1,-1):
        if arr[i][y] == '#':
            up = i+1
            break
    #down
    down = len(arr)-1
    for i in range(x+1, len(arr)):
        if arr[i][y] == '#':
            down = i-1
            break
    return up+down-x    # this is palindromic row pos for arr[x][y]

def get_horizontal_target_pos(arr, x, y):
    # left
    left = 0
    for i in range(y-1,-1,-1):
        if arr[x][i] == '#':
            left = i+1
            break
    # right
    right = len(arr[0])-1
    for i in range(y+1, len(arr[0])):
        if arr[x][i] == '#':
            right = i-1
            break
    return left+right-y     # this is palindromic column pos for arr[x][y]

def sol():
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input().strip()))
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j].isalpha():
                q.append((arr[i][j],i,j))
    cnt = 0
    while q:
        num, x, y = q.popleft()
        nx1, ny1 = get_vertical_target_pos(arr,x,y), y
        nx2, ny2 = x, get_horizontal_target_pos(arr,x,y)
        for nx, ny in [[nx1,ny1], [nx2,ny2]]:
            if arr[nx][ny] == '.':
                arr[nx][ny] = arr[x][y]
                cnt += 1
                q.append((arr[nx][ny],nx,ny))
    return str(cnt)+'\n'+'\n'.join("".join(row) for row in arr)
    
for case in range(int(input())):
    print(f"Case #{case+1}: {sol()}")