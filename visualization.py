import plotly.graph_objects as go
import plotly.express as px

def plotBar(datapoints, title, xlabel, ylabel):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    for template in ["plotly_dark"]:
        fig.update_layout(template=template)
    fig.add_trace( go.Bar(x = datapoints.index,y= datapoints.values.flatten()))
    return fig

def plotBox(datapoints, names, title, xlabel, ylabel):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel, 
                    type = 'log',
        autorange = True)
    )
    fig = go.Figure(layout = layout)
    for template in ["plotly_dark"]:
        fig.update_layout(template=template)
    for datapoint, name in zip(datapoints, names):
        fig.add_trace( go.Box(y= datapoint.values, name = name))
    
    return fig

def plotHistogram(datapoints, title, xlabel, ylabel):
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)

    fig.update_layout(template="plotly_dark")
    fig.add_trace(go.Histogram(
        x = datapoints.values,
        # xbins = {'start': 1, 'size': 0.1, 'end' : 5}
    ))

    return fig

def plotScatter(df, cols, title, xlabel, ylabel):
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    fig = px.scatter(df, x=cols[0], y=col[1], color=cols[2],
                        hover_data=[cols[3]])

    fig.update_layout(template="plotly_dark")

    return fig


