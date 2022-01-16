# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3
from collections import Counter
from collections import deque

def init():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        temp = list(map(int, input().split()))
        A.append(temp)
    for _ in range(N):
        temp = list(map(int, input().split()))
        B.append(temp)
    R = list(map(int, input().split()))
    C = list(map(int, input().split()))
    cost_pos_pair = []
    for i in range(N):
        for j in range(N):
            cost_pos_pair.append((B[i][j],(i,j)))
    cost_pos_pair = sorted(cost_pos_pair)

    return N, A, B, R, C, cost_pos_pair

def row_col_extract(arr, i, j):
    r = arr[i]
    c = [arr[k][j] for k in range(len(arr))]
    return r, c

def checksum():
    ans = 0
    N, A, B, R, C, cost_pos_pair = init()
    # print("cost_pos_pair : ", cost_pos_pair)
    for cost, pos in cost_pos_pair:
        row, col = pos
        if A[row][col] != -1:
            continue
        A_row, A_col = row_col_extract(A, row, col)
        counter_1, counter_2 = Counter(A_row), Counter(A_col)
        if counter_1[-1] >= 2 and counter_2[-1] >= 2:
            A[row][col] = 0 # restore
            ans += B[row][col]
            # print(f"restore ({row},{col})")
            # consider affected element after restoring
            q = deque()
            q.append((row, col))
            while q:
                r, c = q.popleft()
                row_list, col_list = row_col_extract(A, r, c)
                row_list_count, col_list_count = Counter(row_list), Counter(col_list)
                if row_list_count[-1] == 1:
                    q.append((r,row_list.index(-1)))
                    A[r][row_list.index(-1)] = 0
                if col_list_count[-1] == 1:
                    q.append((col_list.index(-1), c))
                    A[col_list.index(-1)][c] = 0
    return ans

for t in range(int(input())):
    print(f"Case #{t+1}: "+str(checksum()))