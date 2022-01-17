# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3
# 참고 : https://down-develope.tistory.com/2
# from collections import deque

# def init():
#     N = int(input())
#     A, B = [], []
#     for _ in range(N):
#         temp = list(map(int, input().split()))
#         A.append(temp)
#     for _ in range(N):
#         temp = list(map(int, input().split()))
#         B.append(temp)
#     R = list(map(int, input().split()))
#     C = list(map(int, input().split()))
#     cost_pos_pair = []
#     for i in range(N):
#         for j in range(N):
#             cost_pos_pair.append((B[i][j],(i,j)))
#     cost_pos_pair = sorted(cost_pos_pair)

#     return N, A, B, R, C, cost_pos_pair

# def row_col_extract(arr, i, j):
#     r = arr[i]
#     c = [arr[k][j] for k in range(len(arr))]
#     return r, c

# def checksum():
#     ans = 0
#     N, A, B, R, C, cost_pos_pair = init()
#     # print("cost_pos_pair : ", cost_pos_pair)
#     for cost, pos in cost_pos_pair:
#         row, col = pos
#         if A[row][col] != -1:
#             continue
#         A_row, A_col = row_col_extract(A, row, col)
#         if A_row.count(-1) >= 2 and A_col.count(-1) >= 2:
#             A[row][col] = 0 # restore
#             ans += B[row][col]
#             # print(f"restore ({row},{col})")
#             # consider affected element after restoring
#             q = deque()
#             q.append((row, col))
#             while q:
#                 r, c = q.popleft()
#                 row_list, col_list = row_col_extract(A, r, c)
#                 if row_list.count(-1) == 1:
#                     q.append((r,row_list.index(-1)))
#                     A[r][row_list.index(-1)] = 0
#                 if col_list.count(-1) == 1:
#                     q.append((col_list.index(-1), c))
#                     A[col_list.index(-1)][c] = 0
#         else:
#             A[row][col] = 0
#     for i in range(N):
#         print(A[i])
#     return ans

# for t in range(int(input())):
#     print(f"Case #{t+1}: "+str(checksum()))

'''
4
-1 -1 1 1
-1 -1 -1 1
1 1 -1 -1
1 1 -1 -1
2 2 0 0
2 2 1 0
0 0 2 2
0 0 2 2
0 0 0 0
0 0 0 0
ans : 4
output : 5
'''

def getParent(parent, x):
    if parent[x]==x:    
        return x
    else:
        return getParent(parent, parent[x])

def unionParent(parent, a, b):
    x = getParent(parent, a)
    y = getParent(parent, b)
    if x<y:
        parent[b] = x
    else:
        parent[a] = y

def findParent(parent, a, b):
    x = getParent(parent, a)
    y = getParent(parent, b)
    if x==y:
        return 1
    else:
        return 0

def checksum():
    mst_cost = 0
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]
    R = list(map(int, input().split()))
    C = list(map(int, input().split()))
    pos_cost_pair = []
    for i in range(N):
        for j in range(N):
            if A[i][j]==-1:
                pos_cost_pair.append(((i,j),B[i][j]))
    pos_cost_pair = sorted(pos_cost_pair, key=lambda x:x[1], reverse=True)

    # count nodes
    a, b = set(), set()
    for pos, cost in pos_cost_pair:
        a.add(pos[0])
        b.add(pos[1])
    nodes = len(a) + len(b)
    print(nodes)
    
    parent = [i for i in range(N)]
    edge = 0
    for pos, cost in pos_cost_pair:
        if edge==nodes-1:
            break
        x, y = pos
        # if not cycle
        if not findParent(parent, x, y):
            # union
            mst_cost += cost
            edge += 1
            unionParent(parent, x, y)
    print("mst cost:",mst_cost)
    # sum B
    sum_B = 0
    for i in range(N):
        sum_B += sum(B[i])

    return sum_B - mst_cost

for t in range(int(input())):
    print(f"Case #{t+1}: "+str(checksum()))

