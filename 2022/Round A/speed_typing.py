
def sol():
    I = input()
    P = input()
    I_dict, P_dict = {}, {}
    for a in I:
        if a not in I_dict:
            I_dict[a] = 0
        I_dict[a] += 1
    for a in P:
        if a not in P_dict:
            P_dict[a] = 0
        P_dict[a] += 1
    I_set, P_set = set(list(I)), set(list(P))
    if I_set - P_set:
        return "IMPOSSIBLE"
    for a in I_dict:
        if P_dict[a] < I_dict[a]:
            return "IMPOSSIBLE"
    i, j = 0, 0
    cnt = 0
    while i<len(I) and j<len(P):
        if I[i]==P[j]:
            i += 1
            j += 1
            cnt += 1
        else:
            j += 1
    if cnt != len(I):
        return "IMPOSSIBLE"
    else:
        return len(P)-len(I)

for t in range(int(input())):
    print(f"Case #{t+1}: "+str(sol()))