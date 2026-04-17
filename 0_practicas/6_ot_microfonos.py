import math


def euclidean_distance(p1, p2):
    # return int(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))
    return round(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2),2)


def combine(strip, d, closest_points):
    min_dist = d
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            d_i = euclidean_distance(strip[i], strip[j])
            if d_i < min_dist:
                min_dist = d_i
                closest_points.clear()
                closest_points.add(strip[i])
                closest_points.add(strip[j])
            elif d_i == min_dist:
                closest_points.add(strip[i])
                closest_points.add(strip[j])

    return min_dist


def naive_closest_points(P):
    n = len(P)
    min_dist = 0x3f3f3f3f
    closest_points = set()
    for i in range(n):
        for j in range(i+1, n):
            d = euclidean_distance(P[i], P[j])
            if d == min_dist:
                closest_points.add(P[i])
                closest_points.add(P[j])
            elif d < min_dist:
                min_dist = d
                closest_points = {P[i], P[j]}
    return min_dist, closest_points


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

        distance_l, closest_l = dyv_closest_points(points_x_l, points_y_l)
        distance_r, closest_r = dyv_closest_points(points_x_r, points_y_r)

        d = min(distance_l, distance_r)
        closest_points = set()
        if distance_l == d:
            closest_points.update(closest_l)
        if distance_r == d:
            closest_points.update(closest_r)

        strip = []
        for p in points_y:
            if abs(p[0]-mid_x) < d:
                strip.append(p)

        d_strip = combine(strip, d, closest_points)

        return d_strip, closest_points


if __name__ == '__main__':
    n = int(input().strip())
    points = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        points.append((x, y))
    points_x = sorted(points, key=lambda p: p[0])
    points_y = sorted(points, key=lambda p: p[1])
    min_dist, closest_points_set = dyv_closest_points(points_x, points_y)
    print(f"Distancia: {min_dist}")
    closest_points = list(closest_points_set)
    closest_points.sort(key = lambda p: p[0])
    for p in closest_points:
        print(f"({p[0]}, {p[1]})")



