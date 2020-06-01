import math
import numpy as np

# Calculates the starting angle
def calc_start_angle(start_y, centre_y, start_x, centre_x):
    start_angle = np.arctan2(start_y - centre_y, start_x - centre_x)
    return start_angle

# Calculates the ending angle
def calc_end_angle(end_y, centre_y, end_x, centre_x):
    end_angle = np.arctan2(end_y - centre_y, end_x - centre_x)
    return end_angle

# Calculates the interval between the starting coordinates and the ending coordinates.
# No use when using the 'path' parameter of the google elevation api
def calculate_interval(pos_2, pos_1, number_of_samples):
    interval = (pos_2 - pos_1) / number_of_samples
    return interval