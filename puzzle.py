import itertools
import numpy as np

def is_valid(permutation):
    matrix = np.reshape(np.array(permutation), (3, 3))
    for row in matrix:
        if sum(row) != 15:
            return False
    for column in matrix.T:
        if sum(column) != 15:
            return False
    if sum(matrix.diagonal()) != 15:
        return False
    if sum(np.fliplr(matrix).diagonal()) != 15:
        return False
    print(matrix)


def get_permutations():
    numbers = list(range(1, 10))
    permutations = list(itertools.permutations(numbers))

    for permutation in permutations:
        is_valid(permutation)

    
get_permutations()
#is_valid([4, 3, 8, 9, 5, 1, 2, 7, 6])


