import math

def double_factorial(n):
    return math.prod(range(n, 0, -2))

def regular_partial_sum(n):
    s = 0
    for i in range(0, n):
        s += ((-1)**i)/(2*i+1)
    return s


def accelerated_partial_sum(n):
    s = 0
    for i in range(0, n):
        s += math.factorial(i)/double_factorial(2*i+1)
    return 0.5*s

def percentage_error(actual_value):
    expected_value = math.pi/4
    return str(abs((actual_value - expected_value)/expected_value)*100) + "%"

for n in [1, 2, 3, 4, 10, 50, 200, 1000]:
    print("n: " + str(n))
    print("error using regular sum: " + percentage_error(regular_partial_sum(n)))
    print("error using accelerated sum: " + percentage_error(accelerated_partial_sum(n)))
    print("------------")

