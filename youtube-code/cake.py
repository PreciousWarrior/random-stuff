import random
import math

class Point():
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def __str__(self):
        return f"({self.X}, {self.Y})"
    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.hypot(dx, dy)
    def is_left(self, a, b):
        # https://stackoverflow.com/a/3461533
        # Calculates if the point is towards the left of a line with coordinates (ax, ay) and (bx, by) 
        c = self
        return ((b.X - a.X)*(c.Y-a.Y) - (b.Y-a.Y)*(c.X-a.X)) > 0


def random_point_in_circle():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x**2 + y**2 <= 1):
        return Point(x, y)
    return random_point_in_circle()

def random_point_on_circle():
    theta = random.uniform(0, 2*math.pi)
    return Point(math.cos(theta), math.sin(theta))

def circular_cake_were_candles_split():
    candle_one = random_point_in_circle()
    candle_two = random_point_in_circle()
    chord_p1 = random_point_on_circle()
    chord_p2 = random_point_on_circle()

    candle_1_left = candle_one.is_left(chord_p1, chord_p2)
    candle_2_left = candle_two.is_left(chord_p1, chord_p2)

    if candle_1_left and not candle_2_left:
        return True
    if candle_2_left and not candle_1_left:
        return True
    
    return False



def linear_cake_were_candles_split():
    candle_one_pos = random.random()
    candle_two_pos = random.random()
    cut_pos = random.random()

    if cut_pos > candle_one_pos and cut_pos < candle_two_pos:
        return True
    if cut_pos > candle_two_pos and cut_pos < candle_one_pos:
        return True
    return False

def simulate(f, trials):
    split_counter = 0
    for _ in range(0, trials):
        if f():
            split_counter += 1
    return split_counter/trials


print("Probability of candles being split on a circular cake", simulate(circular_cake_were_candles_split, 1000000))
print("Probability of candles being split on a linear cake", simulate(linear_cake_were_candles_split, 1000000))
