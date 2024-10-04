import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import ListedColormap


# Function to plot the conceptual cube
def plot_conceptual_cube(n, grid_flag):
    # Function to create the figure plotting
    def MakePlot(xx, yy, zz, ww, cmapO=cm.jet):
        my_cmapN = cmapO(np.arange(cmapO.N))

        # Pre-allocate and modify the alpha channel
        nA = cmapO.N
        xA = np.linspace(-7, 7, nA)
        epsilon = 1
        x_0 = 1

        def f_AlphaControl(x):
            u = (x - x_0) / epsilon
            return 1 - np.exp(-u ** 2 / (1 - u ** 2)) * (np.abs(u) < 1.)

        yA = f_AlphaControl(xA)
        my_cmapN[:, 3] = yA  # Modify alpha channel

        # Create custom colormap
        my_cmap = ListedColormap(my_cmapN)
        colors = xx + yy + zz + ww
        vmin, vmax = -max(abs(colors)), max(abs(colors))

        # Normalize color values
        norm = cm.colors.Normalize(vmin=-1, vmax=1)
        colors_scaled = norm(colors)

        # Adjust colors based on conditions
        for i in range(len(xx)):
            if xx[i] < 0 and yy[i] < 0 and zz[i] < 0:
                colors_scaled[i] = -0.5 * abs(colors_scaled[i])

        # Create the plot
        plt.style.use('dark_background')
        fig = plt.figure(dpi=200)
        ax = fig.add_subplot(projection='3d')
        ax.scatter(xx, yy, zz, c=colors_scaled, cmap=my_cmap, vmin=vmin, vmax=vmax)

        ax.set_title('Plot of Potential Motor-Cognitive Solutions')

        # Set viewing angle
        ax.view_init(25, -45)

        # Set axis limits
        ax.set_xlim([-(1.3) * L, (1.3) * L])
        ax.set_ylim([-(1.3) * L, (1.3) * L])
        ax.set_zlim([-(1.3) * L, (1.3) * L])
        ax.invert_yaxis()  # Reverse the y-axis

        # Hide axis labels
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])

        ax.tick_params(labelbottom=False, labeltop=False, labelleft=False,labelright=False)

        # Add grid
        ax.grid(True)

    # Set the grid dimensions
    L = 1
    x_C = 0.0
    y_C = 0.0
    z_C = 0.0
    a1, b1 = x_C - L, x_C + L
    a2, b2 = y_C - L, y_C + L
    a3, b3 = z_C - L, z_C + L

    NT = n ** 3  # Total number of points

    if grid_flag == 0:
        # Random grid
        xx = np.random.uniform(a1, b1, NT)
        yy = np.random.uniform(a2, b2, NT)
        zz = np.random.uniform(a3, b3, NT)
    else:
        # Even grid
        x = np.linspace(a1, b1, n)
        y = np.linspace(a2, b2, n)
        z = np.linspace(a3, b3, n)
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij', sparse=False)
        xx, yy, zz = X.flatten(), Y.flatten(), Z.flatten()

    # Define the function to visualize
    def f(x, y, z):
        return x * y * z * np.exp(-(x ** 2 + y ** 2 + z ** 2))

    ww = f(xx, yy, zz)
    ww[np.isinf(ww)] = np.nan

    # Plot the result
    MakePlot(xx, yy, zz, ww)
    plt.show()


# Example usage
plot_conceptual_cube(n=10, grid_flag=1)

# Original Cube = plot_conceptual_cube(n=100, grid_flag=0)  ## Caution, this requires high compute!
# Higher-Skilled = plot_conceptual_cube(n=50, grid_flag=0)
# Lower-Skilled = plot_conceptual_cube(n=20, grid_flag=0)
