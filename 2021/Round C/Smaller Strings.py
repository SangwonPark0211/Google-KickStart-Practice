# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e

T = int(input())
for t in range(T):
    n, k = list(map(int, input().split()))
    s = input()

    ans = 1
    for i in range(n//2):
        ans *= min(ord(s[i])-ord('a')+1, ord(s[n-1-i])-ord('a')+1)

    # length is odd
    if n % 2 == 1:
        ans *= k
        ans -= k - (ord(s[n//2])-ord('a')+1)
    
    # if s in palindrome we should subtrat 1 from ans
    s_inverse = s[::-1]
    if s == s_inverse:
        ans -= 1

    ans %= 1000000007

    print(f"Case #{t+1}: "+str(ans))
        

