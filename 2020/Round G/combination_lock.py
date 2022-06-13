# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24
def combination_lock():
    W, N = map(int, input().strip().split())
    X = list(map(lambda x:int(x)-1, input().strip().split()))
    X.sort()
    for i in range(len(X)-1):  # make it as circular array
        X.append(X[i]+N)
    print(X)
    prefix = [0]
    for x in X:
        prefix.append(prefix[-1]+x)
    print(prefix)
    temp = ((prefix[(i+W-1)+1]-prefix[(i+(i+W-1)+1)//2])-(prefix[(i+(i+W-1))//2+1]-prefix[i]) for i in range(W))
    temp = list(temp)
    print(temp)
    return min((prefix[(i+W-1)+1]-prefix[(i+(i+W-1)+1)//2])-(prefix[(i+(i+W-1))//2+1]-prefix[i]) for i in range(W))  # find median of window with min number of moves

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, combination_lock()))