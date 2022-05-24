import numpy as np
import matplotlib; matplotlib.rcParams["savefig.directory"] = "."
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 18})
from math import pi
from meshpy.triangle import MeshInfo, build
from matplotlib.tri import Triangulation

mesh_info = MeshInfo()


outside_size = 15
circle_diameter = 3
N_circle = 10

dx = pi*circle_diameter/N_circle
dv = dx**3

# outer boundary
points = [(-outside_size, -outside_size),
          (-outside_size, outside_size),
          (outside_size, outside_size),
          (outside_size, -outside_size)]
segments = [(0,1), (1,2), (2,3), (3,0)]

# shaft
x = np.cos(np.linspace(0,2*pi,N_circle, endpoint=False))
y = np.sin(np.linspace(0,2*pi,N_circle, endpoint=False))

start = len(points)
for i, (xx,yy) in enumerate(zip(x,y)):
    points.append((xx,yy))
    if i<len(x)-1:
        segments.append((start+i,start+i+1))
segments.append((i+start,start))


mesh_info = MeshInfo()
mesh_info.set_points(points)
mesh_info.set_facets(segments)
mesh_info.set_holes([(0.0, 0.0)])

new_mesh = build(mesh_info,
                 allow_boundary_steiner=True,
                 max_volume=dv)

t = Triangulation(*np.array(new_mesh.points).T, new_mesh.elements)
plt.triplot(t)
plt.show()
