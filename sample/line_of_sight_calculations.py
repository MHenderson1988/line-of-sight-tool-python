import numpy as np


# Calculates the starting angle
def calc_start_angle(start_y, centre_y, start_x, centre_x):
    return np.arctan2(start_y - centre_y, start_x - centre_x)


# Calculates the ending angle
def calc_end_angle(end_y, centre_y, end_x, centre_x):
    return np.arctan2(end_y - centre_y, end_x - centre_x)