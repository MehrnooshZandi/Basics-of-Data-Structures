# -*- coding: utf-8 -*-
"""Distance between two points with tuples

Create a tuple called coordinates that contains the coordinates of point A on the plane ( (4, 3) = a).
Then write code that calculates the distance from this point to the origin (0, 0).

To calculate the distance between two points on the coordinate plane, use the Euclidean distance formula:

distance = √((x₂ - x₁)² + (y₂ - y₁)²)
"""

import math

# define A
coordinates = (4, 3)

# calculate
distance = math.sqrt((coordinates[0] - 0) ** 2 + (coordinates[1] - 0) ** 2)

print("Distance from origin:", distance)

