# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf079

import sys
input = sys.stdin.readline
from math import pi

for t in range(int(input())):
    R, A, B = map(int, input().split())
    r = R
    radius_list = [r]
    while True:
        r *= A
        radius_list.append(r)
        r = r//B
        if r == 0:
            break
        else:
            radius_list.append(r)
    ans = 0
    for rad in radius_list:
        ans += pi * rad**2
    print(f"Case #{t+1}: "+str(ans))