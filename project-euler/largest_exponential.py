import math

filename = "p099_base_exp.txt"
fo = open(filename)
pairs = fo.readlines()
fo.close()

max_logsolution = 0
max_ind = 0
i = 0
for raw_pair in pairs:
    i += 1
    pair = raw_pair.replace('\n', '').split(",")
    base = int(pair[0])
    exp = int(pair[1])
    # solution = base ** exp
    logsolution = exp * math.log10(base)
    # the higher the log(solution), the bigger the number

    if logsolution > max_logsolution:
        max_logsolution = logsolution
        max_ind = i


print(max_ind)
