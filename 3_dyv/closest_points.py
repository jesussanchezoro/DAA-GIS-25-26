import math
import random
import time


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def combine(strip, d):
    min_dist = d
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            d_i = euclidean_distance(strip[i], strip[j])
            min_dist = min(d_i, min_dist)
    return min_dist


def naive_closest_points(P):
    n = len(P)
    min_dist = 0x3f3f3f3f
    for i in range(n):
        for j in range(i+1, n):
            d = euclidean_distance(P[i], P[j])
            min_dist = min(d, min_dist)
    return min_dist


def dyv_closest_points(points_x, points_y):
    n = len(points_x)

    if n <= 3:
        return naive_closest_points(points_x)
    else:
        mid = n // 2
        points_x_l = points_x[ : mid]
        points_x_r = points_x[mid : ]

        mid_x = points_x_l[mid-1][0]

        points_y_l = []
        points_y_r = []

        for p in points_y:
            if p[0] <= mid_x:
                points_y_l.append(p)
            else:
                points_y_r.append(p)

        distance_l = dyv_closest_points(points_x_l, points_y_l)
        distance_r = dyv_closest_points(points_x_r, points_y_r)

        d = min(distance_l, distance_r)

        strip = []
        for p in points_y:
            if abs(p[0]-mid_x) < d:
                strip.append(p)

        d_strip = combine(strip, d)

        return d_strip



for n in range(10, 11, 10):


    points = [(random.randint(-n*10, n*10), random.randint(-n*10, n*10)) for _ in range(n)]
    print(n)
    for p in points:
        print(f"{p[0]} {p[1]}")
    print(n, end="\t")
    # DyV
    ini = time.time()
    points_x = sorted(points, key = lambda p : p[0])
    points_y = sorted(points, key = lambda p : p[1])
    dist_min_dyv = dyv_closest_points(points_x, points_y)
    print(dist_min_dyv)
    elapsed = time.time() - ini
    print(f"{elapsed:.2f}")
    # print(f"{elapsed:.2f}", end="\t")
    # Naive
    # ini = time.time()
    # dist_min_naive = naive_closest_points(points)
    # elapsed = time.time() - ini
    # print(f"{elapsed:.2f}")











