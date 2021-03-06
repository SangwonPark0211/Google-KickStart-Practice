# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def vector(a, b):
    return [a[0]-b[0], a[1]-b[1]]

def length(a):
    return (a[0]**2+a[1]**2)**0.5

def inner_product(a, b):
    return a[0]*b[0]+a[1]*b[1]

def is_strictly_inside_segment(t, a, b):
    return ccw(t, a, b) == 0 and inner_product(vector(a, t), vector(t, b)) > 0

def is_stricly_inside_triangle(t, a, b, c):
    d1, d2, d3 = ccw(t, a, b),  ccw(t, b, c),  ccw(t, c, a)
    return (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0)

def star_trappers():
    N = int(input())
    points = [list(map(int, input().strip().split())) for _ in range(N)]
    target = list(map(int, input().strip().split()))

    result = float("inf")
    for i in range(N-1):  # Time: O(N^3)
        for j in range(i+1, N):
            is_stricly_inside_edge = is_strictly_inside_segment(target, points[i], points[j])
            min_perimeters = [float("inf")]*2
            for k in range(N):
                if k == i or k == j:
                    continue
                if is_stricly_inside_triangle(target, points[i], points[j], points[k]):
                    result = min(result, length(vector(points[i], points[j]))+length(vector(points[j], points[k]))+length(vector(points[k], points[i])))  # possible triangle
                if is_stricly_inside_edge:
                    sign = ccw(points[i], points[j], points[k])
                    if sign != 0:  # keep min perimeters on each side of edge
                        min_perimeters[sign > 0] = min(min_perimeters[sign > 0], (length(vector(points[i], points[k]))+length(vector(points[j], points[k]))))
            if is_stricly_inside_edge:
                result = min(result, sum(min_perimeters))  # possible quadrilateral
    return result if result != float("inf") else "IMPOSSIBLE"

for case in range(int(input())):
    print(f'Case #{case+1}: ' + str(star_trappers()))