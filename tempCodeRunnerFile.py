import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def stripClosest(strip, d):
    min_dist = d
    strip.sort(key=lambda point: point[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))
            else:
                break
    return min_dist

def minDistUtil(points, left, right, level=0):
    if right - left <= 2:
        min_dist = float('inf')
        for i in range(left, right):
            for j in range(i + 1, right):
                d = distance(points[i], points[j])
                min_dist = min(min_dist, d)
        return min_dist
    mid = (left + right) // 2
    mid_x = points[mid][0]
    dl = minDistUtil(points, left, mid, level + 1)
    dr = minDistUtil(points, mid, right, level + 1)
    d = min(dl, dr)
    strip = []
    for i in range(left, right):
        if abs(points[i][0] - mid_x) < d:
            strip.append(points[i])
    stripDist = stripClosest(strip, d)
    return min(d, stripDist)

def minDistance(points):
    points.sort(key=lambda point: point[0])
    return minDistUtil(points, 0, len(points))

points = [
        [-72, -63], [29, -57], [-66, -25],
        
]
res = minDistance(points)

print(f'\nHasil jarak terdekat: {res:.6f}')
