# Projects-Eracing
Collection of codes developed with E-racing from 2019 to 2022. 

#Airfoil_Designer.py:
  To use this code, the Airfoil.rar must be unpacked as a source of airfoils avaliables to be worked with.
  This code has the purpose of taking samples of airfoils and combining them into multi-airfoils configurations. The parameters that are free to choose are:
    Angle of attack (AoA) - initial, final and number of angles.
      Eg. From 0° to 5° with 3 angles would result in 0°, 2.5° and 5°.
    Dx - Value to dislocate the flap in X-direction (initial, final and number of steps).
    Dy - Value to dislocate the flap in Y-direction (initial, final and number of steps).
  The number of flaps per setup is free to choose. To do so, just add another element in flap_configuration list as the example:
    flap_configuration.append(
          {'file': 's1223.txt', 'inversion': True, 'scale': 0.5,
           'aoai': -7, 'aoaf': 0, 'aoan': 2,
           'dxi': 0, 'dxf': 0.2, 'dxn': 2,
           'dyi': 0.1, 'dyf': 0.2, 'dyn': 2})
  A dynamic graph that displays the setups are avaiable if less than 1000 setups are requested (or proposed)
  A pop-up will appear as a safety button preventing the creation of undesired setups.
  
 
