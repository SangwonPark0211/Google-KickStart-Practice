# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/0000000000859dcd

import sys
input = sys.stdin.readline
from collections import deque

def sol():
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input().strip()))
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j].isalpha():
                q.append((arr[i][j], i, j))
    while q:
        letter, x, y = q.popleft()
        

for t in range(int(input())):
    print(f"Case #{t+1}: "+str(sol()))
