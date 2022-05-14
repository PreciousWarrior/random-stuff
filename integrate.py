def f(x): return 2*x*x - 3*x - 19

def integrate(f, a, b, n=10000):
    # Integrates a function f via midpoint Reimann Summation, on the interval [a, b] using n partitions.
    delta_x = (b-a)/n
    heights = []
    for i in range(n):
        midpoint_offset = ((2*i+1)*delta_x)/2
        height = f(a+midpoint_offset)
        heights.append(height)
    return delta_x*sum(heights)

def differenciate(f, x, h=0.00001, max_diff=0.01):
    # Differenciates f at x via limit definition using h close to 0.
    h_neg = -h
    positive_derivative = (f(x+h)-f(x))/h
    negative_derivative = (f(x+h_neg)-f(x))/h_neg
    diff = abs(positive_derivative - negative_derivative)
    if diff > max_diff: return None
    return positive_derivative

def newtons_method(f, guess, iterations=100):
    # Approximates roots for f using Newton's method
    root = guess
    for _ in range(iterations):
        root = root - f(root)/differenciate(f, root)
    return root
