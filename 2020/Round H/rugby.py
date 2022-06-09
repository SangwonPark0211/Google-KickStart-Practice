# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b027

def minimize(z):
    mid = z[len(z)//2]
    temp = 0
    for num in z:
        temp += abs(num-mid)
    return temp

def sol():
    N = int(input())
    x, y = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    y.sort()
    ans += minimize(y)
    x.sort()
    x = [x[i]-i for i in range(len(x))]
    x.sort()
    ans += minimize(x)
    return ans
    
for t in range(int(input())):
    print(f"Case #{t+1}: "+str(sol()))