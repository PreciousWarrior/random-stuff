import numpy as np 

def v(n):
    # Example sequence (first n cubes)
    return n**3

def u(n):
    # Sequence given in problem
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10


#degree = 3
degree = 10


def OP(k, n):
    # Returns the nth term of the optimum polynomial generating function for the 1st k terms of u_n
    seq = []
    for i in range(1, k+1):
        seq.append(u(i))
    powers = []
    for row in range(0, k):
        powers.append([])
        for column in range(0, k):
            entry = (row+1)**column
            powers[row].append(entry)

    # https://stackoverflow.com/a/6789990
    coeffs = [round(i) for i in list(np.linalg.solve(np.array(powers), np.array(seq)))]

    term = 0
    for i in range(0, k):
        term += coeffs[i]*(n**i)

    return term



sum = 0
for k in range(1, degree+1):
    potential_FIT = OP(k, k+1)
    if potential_FIT != u(k+1):
        # the FIT is OP(k, k+1), hence it is a BOP
        sum += potential_FIT

print(sum)
