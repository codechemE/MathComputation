import math


def distance2points(pt1, pt2):
    return math.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[0]) ** 2)


def pathlen(points):
    summer = 0
    for i in range(0,len(points)-1):
        summer = summer + distance2points(points[i], points[i+1])

    return summer

