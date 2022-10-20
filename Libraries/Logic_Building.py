import numpy as np

""""Autor: Gabriel Moreira Beltrami
    Code developed as a tool to create simulation
    setups to Unicamp E-Racing groupe - 2022

    This library has the purpose of receive the desired angles and position of each airfoil 
    and structure each setup. This includes reading, rotating, scaling, translating each airfoil and arranging them."""


# Function to read the coordinates of a flap from a file.
# Returns two lists, each with the X or Y coordinates.
def read_coord(file):
    x = []
    y = []

    with open(file) as line:
        for coord in line:
            try:
                coord_x = float(coord.split()[0])
                coord_y = float(coord.split()[1])
                x.append(coord_x)
                y.append(coord_y)
            except:
                pass
    x = np.array(x)
    y = np.array(y)

    return x, y


# Function to rotate an airfoil at an angle alpha
# Returns two lists, each with the X or Y coordinates
def rotation(x, y, alpha):
    alpha = np.deg2rad(alpha)
    rotation_matrix = np.array([[np.cos(alpha), - np.sin(alpha)],
                                [np.sin(alpha), np.cos(alpha)]], dtype='float64')

    for index, coords in enumerate(zip(x, y)):
        new_coords = np.matmul(rotation_matrix, np.array(coords))

        x[index] = new_coords[0]
        y[index] = new_coords[1]

    return x, y


# Function to translate an airfoil at a distance dx in X and dy in Y
# Returns two lists, each with the X or Y coordinates
def translation(x, y, dx, dy):
    x = x + dx
    y = y + dy

    return x, y


# Function to scale an airfoil at a factor beta. Also inverts the Y coordinates if programmed.
# Returns two lists, each with the X or Y coordinates
def scaling(x, y, beta, inversion):
    if inversion:
        y = y * beta * (-1)
    else:
        y = y * beta

    x = x * beta

    return x, y


# Function to apply all transformations in due order.
# Returns two lists and two floats, each list with the X or Y # coordinates
# and each float with the first coordinate of the airfoil.
def airfoil_geometrics(x, y, alpha, dx, dy, beta, inversion=True):
    [x, y] = scaling(x, y, beta, inversion)
    [x, y] = rotation(x, y, alpha)
    [x, y] = translation(x, y, dx, dy)
    return x, y, x[0], y[0]


# Function that organizes the configurations of each airfoil in respect of another
# Returns two lists:
# Setup_config: a list with seize total setups x number of flaps per setup
# Each element correspond to a setup, and each element of the setup correspond
# to the index by which the flap is identified.
# Flap_data: a list with the transformed airfoil coordinates, with an index by which the flap is identified.
def logicbuild(flap_configuration, reading_directory):
    number_flaps = len(flap_configuration)

    flap_data = []

    # Fixing Main Flap at (x,y) = (0,0)
    flap_configuration[0]['dxi'] = 0
    flap_configuration[0]['dxn'] = 1
    flap_configuration[0]['dyi'] = 0
    flap_configuration[0]['dyn'] = 1

    # Building flap_data list
    for count, flap in enumerate(flap_configuration):
        flap_data.append([])

        x_init, y_init = read_coord(f'{reading_directory}{flap["file"]}')

        # Defining the angle of attack
        for angle_config in range(flap["aoan"]):
            if flap["aoan"] != 1:
                angle = flap["aoai"] + (flap["aoaf"] - flap["aoai"]) * angle_config / (flap["aoan"] - 1)
            else:
                angle = [flap["aoai"]]

            # Defining the dx
            for dx_config in range(flap["dxn"]):
                if flap["dxn"] != 1:
                    dx = flap["dxi"] + (flap["dxf"] - flap["dxi"]) * dx_config / (flap["dxn"] - 1)
                else:
                    dx = flap["dxi"]

                # Defining the dy
                for dy_config in range(flap["dyn"]):
                    if flap["dyn"] != 1:
                        dy = flap["dyi"] + (flap["dyf"] - flap["dyi"]) * dy_config / (flap["dyn"] - 1)
                    else:
                        dy = flap["dyi"]

                    # Creating the setup with due configuration, and referring it to the last flap created.
                    if count != 0:
                        for old_flap in flap_data[count - 1]:
                            [x, y, xf, yf] = airfoil_geometrics(x_init, y_init, angle, dx + old_flap[2][6],
                                                                dy + old_flap[2][7], flap["scale"],
                                                                flap["inversion"])

                            flap_data[count].append(
                                [x, y, [flap["file"], angle, dx, dy, flap["scale"], flap["inversion"], xf, yf]])

                    else:
                        [x, y, xf, yf] = airfoil_geometrics(x_init, y_init, angle, dx, dy, flap["scale"],
                                                            flap["inversion"])

                        flap_data[count].append([x, y, [flap["file"], angle, dx, dy,
                                                        flap["scale"], flap["inversion"], xf, yf]])

    number_configurations = len(flap_data[-1])
    setup_config = []

    # Building setup_config list
    for flap in range(number_flaps):
        for index, config in enumerate(flap_data[flap]):
            for repetition in range(number_configurations // len(flap_data[flap])):
                current_setup_index = (len(flap_data[-1]) // len(flap_data[flap])) * index + repetition

                if flap == 0:

                    setup_config.append([index])

                else:
                    setup_config[current_setup_index].append(index)

    return setup_config, flap_data
