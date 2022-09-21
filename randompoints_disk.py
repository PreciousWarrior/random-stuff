import random
import math


def get_random_point():
    r = math.sqrt(random.uniform(0, 1))
    theta = random.uniform(0, 2*math.pi)
    x = r*math.sin(theta)
    y = r*math.cos(theta)
    return (x, y)


def dist_two_points():
    x1, y1 = get_random_point()
    x2, y2 = get_random_point()
    return math.dist((x1, y1), (x2, y2))

def get_average_dist(n):
    total = 0
    for _ in range(0, n):
        total += dist_two_points()
    return total/n


print(get_average_dist(100000))
