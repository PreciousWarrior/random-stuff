def encode_rail_fence_cipher(string, n):
    if n == 1:
        return string
    
    rails = []
    for _ in range(n):
        rails.append("")
    is_incrementing = True
    rail_index = 0
    for ind,char in enumerate(string):
        if ind%(2*n-2) == 0: 
            # topmost rail 
            is_incrementing = True
        if (ind + n - 1) % (2*n-2) == 0:
            # bottom most rail (by checking the mod of the top rail)
            is_incrementing = False
        rails[rail_index] += char
        if is_incrementing:
            rail_index += 1
        else:
            rail_index -= 1
            
    strng = ""
    for rail in rails:
        strng += rail
    return strng
    
def decode_rail_fence_cipher(string, n):
    if n == 1:
        return string
    
    rails = []
    for _ in range(n):
        rails.append({})
        
    # same algorithm as decode (instead of char, appends index)
    is_incrementing = True
    rail_index = 0
    for ind in range(len(string)):
        if ind%(2*n-2) == 0: 
            # topmost rail 
            is_incrementing = True
        if (ind + n - 1) % (2*n-2) == 0:
            # bottom most rail (by checking the mod of the top rail)
            is_incrementing = False
        rails[rail_index][ind] = None
        if is_incrementing:
            rail_index += 1
        else:
            rail_index -= 1
    
    merged_dic = {}
    i = 0
    for rail in rails:
        for key in rail:
            merged_dic[key] = string[i]
            i += 1
            
    str = ""
    for key in sorted(merged_dic):
        str += merged_dic[key]
    
    return str
