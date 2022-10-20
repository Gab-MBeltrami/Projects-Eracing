from Libraries.Write_Setup import writefile as wf
from Libraries.Logic_Building import logicbuild as lb
from Libraries.Dynamic_Plot import dp
from tkinter import messagebox as msg

""""Autor: Gabriel Moreira Beltrami
    Code developed as a tool to create simulation
    setups to Unicamp E-Racing groupe - 2022
    
    This code has the purpose of receive the desired angles and position of each airfoil and create the list of 
    points which they represent."""

if __name__ == "__main__":

    # Reading and Saving directory configuration
    airfoil_directory = "Airfoils/"
    saving_directory = "Multiairfoils"

    flap_configuration = []

    ground_effect = False
    height = 0.3

    # Space to choose the desired configuration of each flap
    flap_configuration.append(
        {'file': '2032c.txt', 'inversion': True, 'scale': 1,
         'aoai': -7, 'aoaf': 0, 'aoan': 2})

    flap_configuration.append(
        {'file': 's1223.txt', 'inversion': True, 'scale': 0.5,
         'aoai': -7, 'aoaf': 0, 'aoan': 2,
         'dxi': 0, 'dxf': 0.2, 'dxn': 2,
         'dyi': 0.1, 'dyf': 0.2, 'dyn': 2})

    flap_configuration.append(
        {'file': 'Ga1.txt', 'inversion': True, 'scale': 0.5,
         'aoai': -7, 'aoaf': 0, 'aoan': 2,
         'dxi': 0, 'dxf': 0.2, 'dxn': 2,
         'dyi': 0.1, 'dyf': 0.2, 'dyn': 2})

    setup_config, flap_data = lb(flap_configuration, airfoil_directory)

    # Creation of a dynamic plot due to evaluate if the proposed setups are acceptable.
    if len(setup_config) < 1000:
        dp(setup_config, flap_data)

    # If agreed, creates the setups' files
    if msg.askyesno('Create Profiles',
                    f'{len(setup_config)} setups are going to be written. Are you sure you wish to proceed?'):
        if ground_effect:
            wf(setup_config, flap_data, saving_directory, height)
        else:
            wf(setup_config, flap_data, saving_directory, 0)
