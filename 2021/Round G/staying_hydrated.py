# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3a1c

T = int(input())
for t in range(T):
    k = int(input())
    obj = []
    min_x, max_x, min_y, max_y = float('inf'), -float('inf'), float('inf'), -float('inf')
    for i in range(k):
        a, b, c, d = list(map(int, input().split()))
        obj.append((a, b, c, d))
        if a<min_x: min_x = a
        if b<min_y: min_y = b
        if c>max_x: max_x = c
        if d>max_y: max_y = d
    ans = float('inf')
    for x in range(max_x, min_x-1, -1):
        for y in range(max_y, min_y-1, -1):
            dist = 0
            for a, b, c, d in obj:
                # cacse 1
                if a<=x<=c and b<=y<=d:
                    continue
                # case 2
                elif a<=x<=c:
                    dist += min(abs(y-b), abs(y-d))
                # case 3
                elif b<=y<=d:
                    dist += min(abs(x-a), abs(x-c))
                # case 4
                elif c<x and d<y:
                    dist += (x-c) + (y-d)
                # case 5
                elif x<a and d<y:
                    dist += (a-x) + (y-d)
                # case 6
                elif x<a and y<b:
                    dist += (a-x) + (b-y)
                # case 7
                else:
                    dist += (x-c) + (b-y)
            if ans >= dist:
                ans = dist
                ans_x, ans_y = x, y
    # print("ans :", ans)
    # print(ans_x, ans_y)
    print(f"Case #{t+1}: "+str(ans_x)+' '+str(ans_y))

    