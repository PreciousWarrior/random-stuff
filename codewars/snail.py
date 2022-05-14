def recurse(map, pattern):
    if map == [[]]:
        return []
    if map == []:
        return pattern
    if len(map) == 1:
        pattern.append(map[0][0])
        return pattern
    
    # remove top
    print(map)
    pattern.extend([i for i in map[0]])
    del map[0]
    
    # remove right
    for row in map:
        pattern.append(row[len(row) - 1])
        del row[len(row) - 1]
        
    # remove bottom
    row = reversed(map[len(map) - 1])
    pattern.extend(row)
    del map[len(map) - 1]
    
    # remove left
    for row in reversed(map):
        pattern.append(row[0])
        del row[0]
    
    return recurse(map, pattern)

def snail(map):
    return recurse(map, [])
