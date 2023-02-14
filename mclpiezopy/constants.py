from typing import Literal

AxisName = Literal["X", "Y", "Z", "AUX"]
AxisID = Literal[1, 2, 3, 4]

AXIS_ID: dict[AxisName, AxisID] = {
    "X": 1, "Y": 2, "Z": 3, "AUX": 4}

AXIS_ID_X = 1
AXIS_ID_Y = 2
AXIS_ID_Z = 3
AXIS_ID_AUX = 4
