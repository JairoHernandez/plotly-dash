import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Generate data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# Specifies plot type of Scatter and specifies marker points for our scatter plot.
data = [go.Scatter(
    x=random_x, 
    y=random_y, 
    mode='markers',
    marker=dict(
        size=12,
        color='rgb(51,204,153)',
        symbol='pentagon',
        line={'width': 2}
    )
)] 

layout = go.Layout(
    title='Hello First Plot', 
    xaxis={'title': 'MY X AXIS'},
    yaxis=dict(title='MY Y AXIS'), # personal preferance for creating dictionary, but ploty docs use dict(). It does make it easier to see over mutliple lines.
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)

#pyo.plot(data, filename='scatter.html') # If no filename specified default name 'temp-plot.html' is generated.
pyo.plot(fig, filename='scatter.html')