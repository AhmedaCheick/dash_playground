import dash

# these two constitute the visual components of dash 
# and provide classes for each one
import dash_core_components as dcc 
import dash_html_components as html 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Dash is composed of two parts. 
# the first part is the "layout" of the app and it describes 
# what the application looks like.

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
   # equivelant to <h1>Hello Dash</h1> in html5
   # dash_html_components library or html here contains 
   # a class for every html tag as well as their keyword arguments 
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
# dcc describes higher-level components that are interactive 
# using js, html and css through react.js

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

# to turn of "hot-reloading" app.run_server(dev_tools_hot_reload=False)
if __name__ == '__main__':
    app.run_server(debug=True)