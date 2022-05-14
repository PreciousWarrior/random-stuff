def even_middle(string):
    n = len(string)
    first_char = string[int(n/2-1)]
    mid_str = first_char
    string = string.replace(first_char, "")
    mid_str += string[::-1]
    return mid_str

def odd_middle(string):
    n = len(string)
    first_char = string[int(n/2-0.5)]
    mid_str = first_char
    string = string.replace(first_char, "")
    second_char = string[int((n-1)/2-1)]
    mid_str += second_char
    string = string.replace(second_char, "")
    mid_str += string[::-1]
    return mid_str
    
def middle_permutation(string):
    sorted_str = ''.join(sorted(string))
    if len(string) % 2 == 0:
        return even_middle(sorted_str)
    return odd_middle(sorted_str)
