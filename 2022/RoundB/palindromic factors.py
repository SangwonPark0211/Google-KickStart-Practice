# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acee89
import math 

def findFactors(a):
    factor_set = set()
    for i in range(1, int(math.sqrt(a))+1):
        if a % i == 0:
            factor_set.add(i)
            factor_set.add(a//i)
    return factor_set

def isPalindrome(s):
    if len(s)==1:
        return True
    if len(s) % 2 == 0:
        left = s[:len(s)//2]
        right = s[len(s)//2:]
    elif len(s) % 2 == 1:
        left = s[:len(s)//2]
        right = s[len(s)//2+1:]
    if left == right[::-1]:
        return True
    return False

for i in range(int(input())):
    n = int(input())
    factors = findFactors(n)
    cnt = 0
    for f in factors:
        if isPalindrome(str(f)):
            cnt += 1
    print(f"Case #{i+1}: " + str(cnt))