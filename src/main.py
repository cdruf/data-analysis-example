import os

import numpy as np
import pandas as pd
import pandas_profiling as pp

import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px

import seaborn as sns
import matplotlib.pyplot as plt


# %%

print(os.getcwd())
df = pd.read_csv('data/diabetes.csv')
df.head(4)

# %%
"""
Create detailed profile of dataset
"""
profile = pp.ProfileReport(df)
profile.to_file('data/profile.html')

# %%
"""
Piechart with plotly
"""
dist = df['Outcome'].value_counts()
trace = go.Pie(values=(np.array(dist)), labels=dist.index)
layout = go.Layout(title='Diabetes Outcome')
fig = go.Figure(trace, layout)
fig.update_traces(marker=dict(colors=['mediumturquoise', 'darkorange'], line=dict(color='#000000', width=2)))
fig.write_html('plots/outcome.html', auto_open=True)

# %%
"""
Correlation matrix with plotly
"""
pio.renderers.default = "browser"


def df_to_plotly(df):
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist()}


df_new = df.corr()
fig = go.Figure(data=go.Heatmap(df_to_plotly(df_new)))
fig.show()

# %%
"""
Scatter plot with plotly
"""
fig = px.scatter(df, x='Glucose', y='Insulin')
fig.update_traces(marker_color="turquoise",
                  marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Glucose and Insulin')
fig.write_html('plots/outcome.html', auto_open=True)

# %%
"""
Boxplot with plotly
"""
fig = px.box(df, x='Outcome', y='Age')
fig.update_traces(marker_color="midnightblue",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Age and Outcome')
fig.write_html('plots/outcome.html', auto_open=True)
#%%
"""
Boxplot with seaborn
"""
sns.boxplot(x='Outcome', y="BMI", data=df)
plt.show()
