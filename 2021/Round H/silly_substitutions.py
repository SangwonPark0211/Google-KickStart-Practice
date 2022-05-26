from collections import defaultdict

class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def sol():
    N = int(input())
    S = list(map(int, list(input())))
    tail = head = Node(S[0])
    lookup = defaultdict(set)
    cnt = 0
    for i in range(1, len(S)):
        node = Node(S[i], left=tail)
        node.left.right = node
        if (tail.val+1)%10 == node.val:
            lookup[tail.val].add(tail)
            cnt += 1
        tail = node
    i = 0
    while cnt:
        while lookup[i]:
            node = lookup[i].pop()
            cnt -= 1
            if node.left and node.left in lookup[node.left.val]:
                lookup[node.left.val].remove(node.left)
                cnt -= 1
            if node.right in lookup[node.right.val]:
                lookup[node.right.val].remove(node.right)
                cnt -= 1
            node = Node((i+2)%10, left=node.left, right=node.right.right)
            if node.left:
                node.left.right = node
            else:
                head = node
            if node.right:
                node.right.left = node
            if node.left and (node.left.val+1)%10 == node.val:
                lookup[node.left.val].add(node.left)
                cnt += 1
            if node.right and (node.val+1)%10 == node.right.val:
                lookup[node.val].add(node)
                cnt += 1
        i = (i+1)%10    
    cur = head
    result = []
    while cur:
        result.append(str(cur.val))
        cur = cur.right
    return ''.join(result)

for t in range(int(input())):
    print(f"Case #{t+1}: {sol()}")


# from collections import defaultdict

# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def silly_substitutions():
#     N = int(input())
#     S = list(map(int, list(input().strip())))
#     tail = head = Node(S[0])
#     lookup = defaultdict(set)
#     cnt = 0
#     for i in range(1, len(S)):
#         node = Node(S[i], left=tail)
#         node.left.right = node
#         if (tail.val+1)%10 == node.val:
#             lookup[tail.val].add(tail)
#             cnt += 1
#         tail = node
#     i = 0
#     while cnt:
#         while lookup[i]:
#             node = lookup[i].pop()
#             cnt -= 1
#             if node.left and node.left in lookup[node.left.val]:
#                 lookup[node.left.val].remove(node.left)
#                 cnt -= 1
#             if node.right in lookup[node.right.val]:
#                 lookup[node.right.val].remove(node.right)
#                 cnt -= 1
#             node = Node((i+2)%10, left=node.left, right=node.right.right)
#             if node.left:
#                 node.left.right = node
#             else:
#                 head = node
#             if node.right:
#                 node.right.left = node
#             # the number of inital nodes of interest is at most O(N).
#             # we will remove at most O(N) nodes.
#             # for each remove, at most 2 nodes of interest are added.
#             # the total number of added nodes of interest will be at most O(3N)
#             if node.left and (node.left.val+1)%10 == node.val:
#                 lookup[node.left.val].add(node.left)
#                 cnt += 1
#             if node.right and (node.val+1)%10 == node.right.val:
#                 lookup[node.val].add(node)
#                 cnt += 1
#         i = (i+1)%10
#     result = []
#     curr = head
#     while curr:
#         result.append(str(curr.val))
#         curr = curr.right
#     return "".join(result)

# for case in range(int(input())):
#     print(f"Case #{case+1}: {silly_substitutions()}")