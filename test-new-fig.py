import numpy as np
import plotly.graph_objects as go

# Function to generate data
def generate_data(n, L, grid_flag):
    if grid_flag == 0:  # Random Grid
        xx = np.random.uniform(-L, L, n**3)
        yy = np.random.uniform(-L, L, n**3)
        zz = np.random.uniform(-L, L, n**3)
    else:  # Even Grid
        x = np.linspace(-L, L, n)
        y = np.linspace(-L, L, n)
        z = np.linspace(-L, L, n)
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij', sparse=False)
        xx, yy, zz = X.flatten(), Y.flatten(), Z.flatten()
    return xx, yy, zz

def function_values(xx, yy, zz):
    # Custom function that could represent the interactions or scoring based on the axes
    ww = xx * yy * zz * np.exp(-(xx**2 + yy**2 + zz**2))
    ww[np.isinf(ww)] = np.nan
    return ww

# Generate data
n = 70
L = 1.35
xx, yy, zz = generate_data(n, L, grid_flag=1)
ww = function_values(xx, yy, zz)

fig = go.Figure()

# Add a black line to represent the z-axis, added first
fig.add_trace(go.Scatter3d(
    x=[0, 0],
    y=[0, 0],
    z=[-L, L],
    mode='lines',
    line=dict(color='black', width=10)
))

# Create a 3D scatter plot
fig.add_trace(go.Scatter3d(
    x=xx + 0.10,
    y=yy + 0.10,
    z=zz + 0.10, # Offset points slightly in z direction
    mode='markers',
    marker=dict(
        size=5,
        color=ww,  # Set color to the function values
        colorscale='jet',  # Choose a color scale
        opacity=0.5
    )
))

# Update the layout
fig.update_layout(
    title="3D Plot of Potential Motor-Cognitive Solutions",
    scene=dict(
        xaxis=dict(title='Executive Function Tempering', color='white', tickvals=[-L, L], ticktext=['Hot', 'Cool']),
        yaxis=dict(title='Metabolic Output', color='white', tickvals=[-L, L], ticktext=['Low', 'High']),
        zaxis=dict(title='Executive Function Engagement', color='white', tickvals=[-L, L], ticktext=['Low', 'High']),
        annotations=[
            dict(
                showarrow=False,
                x=0, y=0, z=-L,
                text="Low",
                xanchor="left",
                xshift=0,
                font=dict(family="Arial, sans-serif", size=16, color="black", weight="bold")
            ),
            dict(
                showarrow=False,
                x=0, y=0, z=0,
                text="Movement Complexity",
                xanchor="left",
                xshift=10,
                font=dict(family="Arial, sans-serif", size=16, color="black", weight="bold")
            ),
            dict(
                showarrow=False,
                x=0, y=0, z=L,
                text="High",
                xanchor="left",
                xshift=0,
                font=dict(family="Arial, sans-serif", size=16, color="black", weight="bold")
            )
        ],
        bgcolor='black'
    ),
    paper_bgcolor='black',
    font=dict(color='white'),
    margin=dict(l=0, r=0, b=0, t=30)
)

fig.show()
