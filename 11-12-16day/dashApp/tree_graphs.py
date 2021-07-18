import plotly.express as px

def tree_graphs (df):

    return px.treemap(df, path=['Country', 'City'], values='Year')