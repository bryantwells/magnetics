import magpylib as magpy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# set font size
# plt.rcParams.update({'font.size':6})

# create a matplotlib figure
fig = plt.figure()
axs = [fig.add_subplot(2,2,i) for i in range(1,5)]

# create an observer grid in the xz-symettry plane
ts = np.linspace(-5,5,100)
grid = np.array([[(x,0,z) for x in ts] for z in ts]) # python loop

# source objects
s1 = magpy.magnet.Cylinder(magnetization=(0,0,500), dimension=(3,7))
s2 = magpy.magnet.Sphere(magnetization=(-200,0,500), diameter=5)
s3 = magpy.current.Line(current=10, vertices=[(0,-5,0),(0,5,0)])
s4 = magpy.current.Loop(current=10, diameter=5)

for i,s in enumerate([s1,s2,s3,s4]):


	B = s.getB(grid)
	log10_norm_B = np.log10(np.linalg.norm(B, axis=2))

	# Display the B-field with the streamplot using log10-scale
	# color function and linewidth
	splt = axs[i].streamplot(
		grid[:,:,0],
		grid[:,:,2],
		B[:,:,0],
		B[:,:,2],
		color='k',
		density=1,
	)
	#pclr = axs[i].pcolor(
	#	grid[:,:,0],
	#	grid[:,:,2],
	#	log10_norm_B,
	#	cmap="Greys"
	#)

	# remove arrows
	for art in axs[i].get_children():
		if not isinstance(art, matplotlib.patches.FancyArrowPatch):
			continue
		art.remove()


plt.tight_layout()
plt.show()
