# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec1cb

def AlienGenerator():
    G = int(input())
    n = 1
    cnt = 0
    while ((n+1)*n)//2 <= G:
        if (G-(n+1)*n//2) % n == 0:
            cnt += 1
        n += 1
    return cnt

for t in range(int(input())):
    print(f"Case #{t+1}: " + str(AlienGenerator()))