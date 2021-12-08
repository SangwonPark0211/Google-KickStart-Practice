# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3a1c

T = int(input())
for t in range(T):
    k = int(input())
    x, y = {}, {}
    for i in range(k):
        x1, y1, x2, y2 = list(map(int, input().split()))
        if x1 in x:
            x[x1] += 1
        else:
            x[x1] = 1
        if x2 in x:
            x[x2] += 1
        else:
            x[x2] = 1
        if y1 in y:
            y[y1] += 1
        else:
            y[y1] = 1
        if y2 in y:
            y[y2] += 1
        else:
            y[y2] = 1

    x = sorted(x.items())    
    y = sorted(y.items())
    
    ans_x, ans_y = 0, 0

    count = -1 * k
    for i in range(len(x)):
        count += x[i][1]
        if count >= 0:
            ans_x = x[i][0]
            break
    count = -1 * k
    for i in range(len(y)):
        count += y[i][1]
        if count >= 0:
            ans_y = y[i][0]
            break

    print(f"Case #{t+1}: "+str(ans_x)+' '+str(ans_y))