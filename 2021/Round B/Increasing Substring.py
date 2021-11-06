# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882

T = int(input())

for t in range(T):
    n = int(input())
    s = input()
    dp = [1] * n
    for i in range(1, n):
        if ord(s[i]) > ord(s[i-1]):
            dp[i] = dp[i-1] + 1
    dp_str = list(map(str, dp))
    print(f"Case #{t+1}: " + " ".join(dp_str))