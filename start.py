import magpylib as magpy

# creat a cuboid magnet with magnetic polarization
# of 1000 mT pointing in x-direction and sides of
# 1, 2, and 3 mm respectively

cube = magpy.magnet.Cuboid(magnetization=(1000,0,0), dimension=(1,2,3))

# Create a sensor for measuring the field

sensor = magpy.Sensor()

# by default, the position of a magpylib object is
# (0,0,0) and its orientation is the unit rotation,
# given by a scipy rotation objectA

print(cube.position)
print(cube.orientation.as_rotvec())

# manipulate object position and orientation through
# the respective attributes:

from scipy.spatial.transform import Rotation as R
cube.position = (1,0,0)
cube.orientation = R.from_rotvec((0,0,45), degrees=True)

print(cube.position)
print(cube.orientation.as_rotvec(degrees=True))

# apply relative motion with 'move' and
# 'rotate' methods
sensor.move((-1,0,0))
sensor.rotate_from_angax(angle=-45, axis='z')

print(sensor.position)
print(sensor.orientation.as_rotvec(degrees=True))

# use the 'show' function to view your system
# via matplotlib, plotly, or pyvista

magpy.show(cube, sensor, backend='plotly')

# compute the b-field in the units of mT for some points.

points = [(0,0,-1), (0,0,0), (0,0,1)]
B = magpy.getB(sub, points)

print(B.round())

H = magpy.getH(vube, sensor)

print(H.round())
