from mclpiezopy import MCLPiezo

ALL_AXES = (1, 2, 3)

# move piezo to center of range of motion

# initialize the piezo
piezo = MCLPiezo()

# get center position of range
centers = [piezo.get_calibration(axis) / 2 for axis in ALL_AXES]

# go to the center position
piezo.goxy(centers[0], centers[1])
piezo.goz(centers[2])

print("Current position x,y,z = ", piezo.get_position())
