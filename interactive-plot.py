import numpy as np
import plotly.graph_objects as go

# Function to generate data
def generate_data(n, L, grid_flag):
    if grid_flag == 0:
        xx = np.random.uniform(-L, L, n**3)
        yy = np.random.uniform(-L, L, n**3)
        zz = np.random.uniform(-L, L, n**3)
    else:
        x = np.linspace(-L, L, n)
        y = np.linspace(-L, L, n)
        z = np.linspace(-L, L, n)
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij', sparse=False)
        xx, yy, zz = X.flatten(), Y.flatten(), Z.flatten()
    return xx, yy, zz

def function_values(xx, yy, zz):
    return xx * yy * zz * np.exp(-(xx**2 + yy**2 + zz**2))

# Generate data
n = 50
L = 1
xx, yy, zz = generate_data(n, L, grid_flag=1)
ww = function_values(xx, yy, zz)

# Normalize the color values to range [0, 1]
ww_normalized = (ww - np.min(ww)) / (np.max(ww) - np.min(ww))

# Define a custom colorscale
custom_colorscale = [
    [0, 'blue'], [0.5, 'white'], [1, 'red']
]

fig = go.Figure(data=[
    go.Scatter3d(
        x=xx,
        y=yy,
        z=zz,
        mode='markers',
        marker=dict(
            size=5,
            color=ww_normalized,  # Color by normalized function values
            colorscale=custom_colorscale,
            opacity=0.8,
            colorbar=dict(title='Value')
        )
    )
])

# Update layout to match matplotlib style
fig.update_layout(
    title='3D Plot of Potential Motor-Cognitive Solutions',
    scene=dict(
        xaxis=dict(title='X', backgroundcolor='black'),
        yaxis=dict(title='Y', backgroundcolor='black'),
        zaxis=dict(title='Z', backgroundcolor='black'),
        xaxis_showspikes=False,
        yaxis_showspikes=False,
        zaxis_showspikes=False
    ),
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)

fig.show()
