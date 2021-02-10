import plotly.graph_objects as go
import plotly.io as pio

#%%
# Write plot to an html file and show it in the default browser
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.write_html('plots/first_figure.html', auto_open=True)

# %%
# Render plot directly in the default browser
pio.renderers.default = "browser"
fig = go.Figure(data=go.Bar(y=[2, 1, 3]))
fig.show()

