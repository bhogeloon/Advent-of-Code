MIN_X = 124

for velo_start_x in range(1000):
    x = 0
    velo_x = velo_start_x

    while True:
        if velo_x == 0:
            print("Velo_start_x: {}; x = {}".format(velo_start_x, x))
            break

        x += velo_x
        velo_x -= 1

    if x >= MIN_X:
        break
