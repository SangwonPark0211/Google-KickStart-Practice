# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461

def min_op(a, b):
    a, b = ord(a), ord(b)
    return min(abs(a-b), min(a,b)+26-max(a,b))

T = int(input())
for t in range(T):
    op_num = 0
    s = input()
    f = set(list(input()))
    for i in range(len(s)):
        if s[i] not in f:
            min_path = 26
            for f_alpha in f:
                min_path = min(min_path, min_op(s[i], f_alpha))
            op_num += min_path
    print(f"Case #{t+1}: "+str(op_num))

