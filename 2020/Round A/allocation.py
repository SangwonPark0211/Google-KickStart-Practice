# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

def sol():
    N, B = map(int, input().split())
    house = list(map(int, input().split()))
    house.sort()
    cnt = 0
    total_cost = 0
    for cost in house:
        total_cost += cost
        if total_cost > B:
            break
        cnt += 1
    return cnt

for t in range(int(input())):
    print(f"Case #{t+1}: " + str(sol()))
