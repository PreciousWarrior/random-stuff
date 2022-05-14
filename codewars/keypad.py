def adjacent_pins(number):
    if number == "1":
        return ["2", "4"]
    if number == "2":
        return ["1", "3", "5"]
    if number == "3":
        return ["2", "6"]
    if number == "4":
        return ["1", "5", "7"]
    if number == "5":
        return ["2", "4", "6", "8"]
    if number == "6":
        return ["3", "5", "9"]
    if number == "7":
        return ["4", "8"]
    if number == "8":
        return ["5", "9", "7", "0"]
    if number == "9":
        return ["6", "8"]
    if number == "0":
        return ["8"]
    
def possible_pins(number):
    pins = adjacent_pins(number)
    pins.append(number)
    return pins

def get_combinations(pattern, combinations):
    if pattern == "":
        # final digit
        return combinations
    if combinations == []:
        # first digit
        if len(pattern) == 1:
            return possible_pins(pattern[0])
        else:
            return get_combinations(pattern[1:], possible_pins(pattern[0]))
    
def get_pins(observed):
    combinations = get_combinations(observed, [])
    print(combinations)
   
get_pins('8')
