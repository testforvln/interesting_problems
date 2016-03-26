def win_car(door_num, host_known):
    # initial prob of car in door
    car_in_door = [1/door_num]*door_num
    # prob of host open door last while car in i
    host_open = []
    if host_known == False:
        for i in range(door_num-1):
            host_open.append(1/(door_num-1))
        host_open.append(0)
    else:
        host_open = [1/(door_num-1)]
        for i in range(door_num-2):
            host_open.append(1/(door_num-2))
        host_open.append(0)
    open_last = 0
    # prob of sum open last door
    for i in range(door_num):
        open_last += car_in_door[i] * host_open[i]
    win_car_in_door = []
    # prob of car in i while open last door
    for i in range(door_num):
        win_car_in_door.append((car_in_door[i] * host_open[i]) / open_last)
    return win_car_in_door

if __name__ == '__main__':
    print(win_car(3, True))
    print(win_car(3, False))