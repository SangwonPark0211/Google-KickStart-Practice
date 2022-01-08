# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def CP():
    Z = int(input())
    for first in range(int(Z**0.5), 1, -1):
        if isPrime(first):
            second = first + 1
            while not isPrime(second):
                second += 1
            if first * second <= Z:
                return first * second

for t in range(int(input())):
    print(f'Case #{t+1}: ', CP())