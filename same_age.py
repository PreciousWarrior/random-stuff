def digit_sum(n):
    total = 0
    for char in str(n):
        total += int(char)
    if len(str(total)) == 1:
        return total
    else:
        return digit_sum(total)

def check_pattern(y1, y2, n):
    youngest_y = max(y1, y2)
    for year in range(youngest_y+1, youngest_y+n):
        s1 = digit_sum(year-y1)
        s2 = digit_sum(year-y2)
        if s1 != s2:
            return False
    return True

def get_pattern(y, n):
    sums = []
    for year in range(y+1, y+n):
        age_sum = digit_sum(year-y)
        sums.append(age_sum)
    return sums

age_sum_map = {1:2 }



print(check_pattern(24, 34, 100))

