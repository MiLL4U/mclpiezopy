from time import sleep

import numpy as np

from mclpiezopy import MCLPiezo

# simple scanning example

# intialize the piezo
piezo = MCLPiezo()
print([piezo.mcl_read(axis) for axis in (1, 2, 3)])
print([piezo.get_calibration(axis) for axis in (1, 2, 3)])
z_position = piezo.mcl_read(3)

# will scan over a rectangular area, from (x1, y1) to (x2, y2)
# with len_x steps in x-direction and len_y steps in y-direction

len_x = 16  # number of steps in x-direction
len_y = 16  # number of steps in y-direction
x1, x2 = 100., 200.  # x coordinates
y1, y2 = 100., 200.  # y coordinates
# z_position = 50.  # z position

# time to wait (seconds) after moving piezo to next position
wait_time = 0.02

# create a 2d grid of x and y scanning positions
x_pattern, y_pattern = np.meshgrid(np.linspace(
    x1, x2, len_x), np.linspace(y1, y2, len_y))
scan_shape = np.shape(x_pattern)

# create array to store the results of the measurements
results = np.zeros(scan_shape)

# go to the origin of the scan
piezo.goxy(x1, y1)
piezo.goz(z_position)

# move the piezo over the scan area
for index in np.ndindex(scan_shape):  # type: ignore
    # go to the next position
    piezo.goxy(x_pattern[index], y_pattern[index])
    sleep(wait_time)

    # do some measurements here by calling
    # measure_something() function and store the result
    # results(index) = measure_something()

    print("Current position x,y,z = ", piezo.get_position())
