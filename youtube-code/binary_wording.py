from num2words import num2words

def get_binary_wording_count(n):
    bin_str = "{0:b}".format(n)
    counter = 0
    for char in bin_str:
        if char == "0":
            counter += len("ZERO")
        if char == "1":
            counter += len("ONE")
    return counter

def get_wording_count(n):
    word = num2words(n)
    return len(word)


def get_depth(n, maps, depth=0):
    if n != 4:
        nxt = maps[n]
        depth += 1
        return get_depth(nxt, maps, depth)
    return depth

max_depth = 0
max_depth_num = 4
maps = {1: 3, 2: 3, 3: 5, 4: 4}
for n in range(5, 10**6):
    count = get_wording_count(n)
    maps[n] = count
    depth = get_depth(count, maps) + 2
    if depth > max_depth:
        max_depth = depth
        max_depth_num = n

print(max_depth, max_depth_num)





#print(get_wording_count(192831))




