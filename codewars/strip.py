def solution(string,markers):
    lines = string.split("\n")
    updated_lines = []
    for line in lines:
        lowest_ind = float('inf')
        for marker in markers:
            ind = line.find(marker)
            if ind < lowest_ind and ind != -1: lowest_ind = ind
        if lowest_ind != float('inf'):
            # comment marker was found
            updated_lines.append(line[0:lowest_ind].rstrip())
        else:
            updated_lines.append(line.rstrip())
    
    return '\n'.join(updated_lines)
