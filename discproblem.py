import math

def get_final_disk(num_disks):
    # populate disks
    disks = []
    for x in range(1, num_disks + 1):
        disks.append(x)

    # set initial variables
    move_to_index = 0
    last_disk_removed = False
    
    while len(disks) != 1:
        # print(move_to_index)
        if (not last_disk_removed):
            disks.remove(disks[move_to_index])
            last_disk_removed = True
            move_to_index = (move_to_index) % len(disks)
        else:
            last_disk_removed = False
            move_to_index = (move_to_index + 1) % len(disks)

    return disks[0]

def get_final_disk_mathematically(num_disks):
    closest_power_of_two = math.floor(math.log2(num_disks))
    last_power_of_two = 2 ** closest_power_of_two
    if last_power_of_two == num_disks:
        return last_power_of_two
    return (num_disks - last_power_of_two) * 2


def verify_theory():    
    num_disks = 0
    while True:
        num_disks += 1
        if (get_final_disk(num_disks) -  get_final_disk_mathematically(num_disks) != 0):
            print(num_disks)

print(get_final_disk_mathematically(65))

    