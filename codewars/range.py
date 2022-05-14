# this code is PAIN (pls help)
def solution(args):
    string = ""
    index = 0
    broke = False
    while index < len(args):
        try:
            if args[index] == args[index + 2] - 2:
                # needs to be written in range format
                trunc = args[index:]
                for ind in range(len(trunc)):
                    if ind+args[index] != trunc[ind]:
                        string += f"{args[index]}-{args[index + ind - 1]},"
                        index += ind
                        broke = True
                        break
                if not broke:
                    string += f"{args[index]}-{args[len(args) - 1]},"
                    break
                broke = False
            else: 
                # needs to be written in regular format
                string += str(args[index]) + ","
                index += 1
        except IndexError:
            try:
                string += f"{args[index]},{args[index+1]},"
            except IndexError:
                string += str(args[index]) + ","
            break
                              
    return string[:len(string)-1]
