# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24

def getSum(i,j,pre):
    return pre[j+1] - pre[i]

def combination_lock():
    W, N = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    presum = [0]
    for x in arr:
        presum.append(presum[-1]+x)
    ans = float('inf')
    for i in range(len(arr)):
        if arr[i] < N/2:
            l, r = 0, W-1
            while l <= r:
                mid = (l+r)//2
                if arr[mid]-arr[i] < N-arr[mid]+arr[i]:
                    l = mid + 1
                elif arr[mid]-arr[i] > N-arr[mid]+arr[i]:
                    if arr[mid-1]-arr[i] <= N-arr[mid-1]+arr[i]:
                        break
                    else:
                        r = mid - 1
                else:
                    break
            first, second = i, mid
            ans = min(ans, arr[i]*first - getSum(0,first-1,presum) + getSum(first,second-1,presum) - arr[i]*(second-first) + (N+arr[i])*(W-second) - getSum(second,W-1,presum))
        elif arr[i] > N/2:
            l, r = 0, W-1
            while l <= r:
                mid = (l+r)//2
                if arr[mid]+N-arr[i] > arr[i]-arr[mid]:
                    r = mid - 1
                elif arr[mid]+N-arr[i] < arr[i]-arr[mid]:
                    if arr[mid+1]+N-arr[i] >= arr[i]-arr[mid+1]:
                        break
                    else:
                        l = mid + 1
                else:
                    break
            first, second = mid, i
            ans = min(ans, (N-arr[i])*(first+1)+getSum(0,first,presum) + arr[i]*(second-first)-getSum(first+1,second,presum) + getSum(second+1,W-1,presum)-arr[i]*(W-1-second))
        else:
            ans = min(ans, arr[i]*i - getSum(0,i,presum) + getSum(i+1,W-1,presum) - arr[i]*(W-1-i))
        print(ans)
    return ans
for t in range(int(input())):
    print(f"Case #{t+1}: "+str(combination_lock()))

# def combination_lock():
#     W, N = map(int, input().strip().split())
#     X = list(map(lambda x:int(x)-1, input().strip().split()))
#     X.sort()
#     for i in range(len(X)-1):  # make it as circular array
#         X.append(X[i]+N)
#     print(X)
#     prefix = [0]
#     for x in X:
#         prefix.append(prefix[-1]+x)
#     print(prefix)
#     temp = ((prefix[(i+W-1)+1]-prefix[(i+(i+W-1)+1)//2])-(prefix[(i+(i+W-1))//2+1]-prefix[i]) for i in range(W))
#     temp = list(temp)
#     print(temp)
#     return min((prefix[(i+W-1)+1]-prefix[(i+(i+W-1)+1)//2])-(prefix[(i+(i+W-1))//2+1]-prefix[i]) for i in range(W))  # find median of window with min number of moves

# for case in range(int(input())):
#     print('Case #%d: %s' % (case+1, combination_lock()))