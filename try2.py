def turn_off_lamps_order():
    num_lamps = 13
    start = 0
    step = 5
    res = []
    lights = []
    for i in range(num_lamps):
        lights.append(1)
    
    counter = 1 # count the step
    ind = start # the index 
    c = 0 #how many lighs are turned off
    while True:
        if c == num_lamps:
            break
        else:
            if lights[ind] == 0:
                if ind == num_lamps - 1:
                    ind = 0
                else:
                    ind +=1
            else:
                if counter == step:
                    lights[ind] = 0
                    res.append(ind + 1)
                    counter = 1
                    if ind == num_lamps - 1:
                        ind = 0
                    else:
                        ind += 1
                    
                    c += 1
                else:
                    counter += 1
                    if ind == num_lamps - 1:
                        ind = 0
                    else:
                        ind +=1
    return res


