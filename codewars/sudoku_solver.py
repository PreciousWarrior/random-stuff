def solve(puzzle, row, column):
    already_used = set()
    
    # same row
    for box in puzzle[row]:
        already_used.add(box)
        
    # same column
    for row_2 in puzzle:
        box = row_2[column]
        already_used.add(box)
        
    # same matrix
    row_compartment = row//3
    column_compartment = column//3
    for row_3 in puzzle[row_compartment*3:(row_compartment+1)*3]:
        for box in row_3[column_compartment*3:(column_compartment+1)*3]:
            already_used.add(box)
    
    already_used.discard(0)
    if len(already_used) < 8:
        return puzzle
    
    digits = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    value = list((digits-already_used))[0]
    puzzle[row][column] = value
    return puzzle
        

def has_zeroes(puzzle):
    for row in puzzle:
        for box in row:
            if box == 0:
                return True
    return False


def sudoku(puzzle):
    while has_zeroes(puzzle):
        for row_id, row in enumerate(puzzle):
            for column_id, box in enumerate(row):
                if box == 0:
                    puzzle = solve(puzzle, row_id, column_id)
    return puzzle
