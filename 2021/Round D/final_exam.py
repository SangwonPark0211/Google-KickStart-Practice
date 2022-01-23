# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082bffc

def sol():
    ans = []
    N, M = map(int, input().split())
    problems = []
    for _ in range(N):
        a, b = map(int, input().split())
        problems += range(a,b+1)
    problems.sort()
    students = list(map(int, input().split()))
    for key in students:
        # binary search
        l, r = 0, len(problems)-1
        diff = float('inf')
        idx = -1
        difficulty = 0
        while l<=r:
            if key in set(problems):
                idx = problems.index(key)
                difficulty = key
                break
            mid = (l+r)//2
            if problems[mid] < key:
                l = mid+1
            else:
                r = mid-1
            if diff > abs(problems[mid]-key):
                diff = abs(problems[mid]-key)
                difficulty = problems[mid]
                idx = mid
            elif diff == abs(problems[mid]-key):
                if difficulty > problems[mid]:
                    difficulty = problems[mid]
                    idx = mid
        ans.append(difficulty)
        problems.pop(idx)
    return ans

for t in range(int(input())):
    print(f"Case #{t+1}: " + ' '.join(list(map(str, sol()))))