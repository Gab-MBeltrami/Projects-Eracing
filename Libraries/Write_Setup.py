def writefile(setup, data, directory, height):
    import os
    import numpy as np
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Creates the file with each setup created and writes their configuration at the end of the file.
    for count, config in enumerate(setup):
        max_x = -100
        min_y = 100
        for i in range(len(config)):
            max_x = np.max([data[i][config[i]][0].max(), max_x])
            min_y = np.min([data[i][config[i]][1].min(), min_y])

        with open(f'{directory}/Setup-{str(count + 1).zfill(1 + len("%i" % len(setup)))}.txt', 'w+') as file:
            for flap, index in enumerate(config):
                if flap != 0:
                    file.write(f'-Inserting Flap {data[flap][index][2][0][:-4]}-\n')
                for x, y in zip(data[flap][index][0], data[flap][index][1]):
                    file.write(f'{round(x - max_x * 1.1, 5)},{round(y - min_y + height, 5)}\n')

            for flap, index in enumerate(config):
                file.write(f'*.*.Setup: {data[flap][index][2][0][:-4]} as Flap {flap + 1},'
                           f' Inverted: {data[flap][index][2][5]},'
                           f' Scale: {data[flap][index][2][4]},'
                           f' AoA: {data[flap][index][2][1]},'
                           f' Reposition from previous T.E. = : ({data[flap][index][2][2]}; {data[flap][index][2][3]})*.*.\n')
