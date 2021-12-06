# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3a1c

# T = int(input())
# for t in range(T):
#     k = int(input())
#     obj = []
#     min_x, max_x, min_y, max_y = float('inf'), -float('inf'), float('inf'), -float('inf')
#     for i in range(k):
#         a, b, c, d = list(map(int, input().split()))
#         obj.append((a, b, c, d))
#         if a<min_x: min_x = a
#         if b<min_y: min_y = b
#         if c>max_x: max_x = c
#         if d>max_y: max_y = d
#     ans = float('inf')
#     for x in range(max_x, min_x-1, -1):
#         for y in range(max_y, min_y-1, -1):
#             dist = 0
#             for a, b, c, d in obj:
#                 # cacse 1
#                 if a<=x<=c and b<=y<=d:
#                     continue
#                 # case 2
#                 elif a<=x<=c:
#                     dist += min(abs(y-b), abs(y-d))
#                 # case 3
#                 elif b<=y<=d:
#                     dist += min(abs(x-a), abs(x-c))
#                 # case 4
#                 elif c<x and d<y:
#                     dist += (x-c) + (y-d)
#                 # case 5
#                 elif x<a and d<y:
#                     dist += (a-x) + (y-d)
#                 # case 6
#                 elif x<a and y<b:
#                     dist += (a-x) + (b-y)
#                 # case 7
#                 else:
#                     dist += (x-c) + (b-y)
#             if ans >= dist:
#                 ans = dist
#                 ans_x, ans_y = x, y
#     print(f"Case #{t+1}: "+str(ans_x)+' '+str(ans_y))

T = int(input())
for t in range(T):
    k = int(input())
    x = []
    y = []
    x_point = set()
    y_point = set()
    for i in range(k):
        x1, y1, x2, y2 = list(map(int, input().split()))
        x.append((x1,x2))
        y.append((y1,y2))
        x_point.add(x1)
        x_point.add(x2)
        y_point.add(y1)
        y_point.add(y2)
    x.sort()
    y.sort()
    x_point = sorted(list(x_point))
    y_point = sorted(list(y_point))
    for i in x_point:
        x_left, x_right = 0, 0
        for j in range(len(x)):
            if x[j][0]<=i<x[j][1]:
                continue
            if x[j][1]<=i:
                x_left += 1
            elif x[j][0]>i:
                x_right = k - j
                break
        if x_right - x_left <= 0:
            ans_x = i
            break
    for i in y_point:
        y_left, y_right = 0, 0
        for j in range(len(y)):
            if y[j][0]<=i<y[j][1]:
                continue
            if y[j][1]<=i:
                y_left += 1
            elif y[j][0]>i:
                y_right = k - j
                break
        if y_right - y_left <= 0:
            ans_y = i
            break

    print(f"Case #{t+1}: "+str(ans_x)+' '+str(ans_y))