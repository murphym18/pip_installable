import math
import numpy as np

def vec3d(x, y, z):
    return np.array([x, y, z], dtype=float)

def distance(a, b):
    c = a - b
    return math.sqrt(np.dot(c, c))