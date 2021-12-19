import os, sys, numpy as np, matplotlib.pyplot as plt, mpl_toolkits.mplot3d  

with open(os.path.join(sys.path[0], "input.txt"),"r") as file:
    data = file.read().split()
for d in range(len(data)):
    data[d] = [int(s) for s in data[d] if s.isdigit]

grid = np.array(data)
X = np.arange(100)
Y = np.arange(100)
X, Y = np.meshgrid(X, Y)
Z = grid

# fig, [ax1,ax2] = plt.subplots(nrows=2, subplot_kw={"projection": "3d"})

# surf = ax1.plot_surface(X, Y, Z, rcount = 99, ccount = 99, cmap='winter', edgecolor='none')
# ax1.set_zlim(0,100)

# ax2.axes(projection = None)
# ax2.imshow(grid, cmap='winter', interpolation='nearest', origin="lower", aspect = "auto")
# fig.colorbar(surf)
# plt.show()

fig = plt.figure(figsize=(15,15))

fig.tight_layout()
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(X, Y, Z, rcount = 99, ccount = 99, cmap='viridis', edgecolor='none')
ax1.set_zlim(0,60)
fig.colorbar(surf, ticks = range(0,10),fraction=0.046, pad=0.04)
ax2 = fig.add_subplot(122)
heatmap = ax2.imshow(grid, cmap='viridis', interpolation='nearest', origin="lower", aspect = "equal")
fig.colorbar(heatmap, ticks = range(0,10),fraction=0.046, pad=0.04)
plt.show()

