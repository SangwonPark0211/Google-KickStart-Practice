# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45

from math import sqrt
import sys
input = sys.stdin.readline

def prod(a,b):
    return a[0]*b[1] - a[1]*b[0]

def distance(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def perimeter(a,b,c):
    return distance(a,b) + distance(b,c) + distance(c,a)

def vec(a,b):
    return [b[0]-a[0], b[1]-a[1]]

def sol():
    N = int(input())
    white = []
    for _ in range(N):
        white.append(list(map(int, input().strip().split())))
    blue = list(map(int, input().strip().split()))

    if N <= 2:
        return "IMPOSSIBLE"
    ans = float('inf')
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                a, b, c = white[i], white[j], white[k]
                p = blue
                ap = vec(a,p)
                ab = vec(a,b)
                bp = vec(b,p)
                bc = vec(b,c)
                cp = vec(c,p)
                ca = vec(c,a)
                prod1, prod2, prod3 = prod(ap,ab), prod(bp,bc), prod(cp,ca)
                if (prod1>0 and prod2>0 and prod3>0) or (prod1<0 and prod2<0 and prod3<0):
                # if (prod1<0 and prod2<0 and prod3<0):
                    ans = min(ans, perimeter(a,b,c))
    return ans if ans!=float('inf') else "IMPOSSIBLE"

for t in range(int(input())):
    print(f"Case #{t+1}: "+str(sol()))