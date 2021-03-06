import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati', 'Houston'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.RadioItems(
        id='countries-dropdown',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='America'
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-dropdown'),

    html.Hr(),

    html.Div(id='display-selected-values')
])


@app.callback(
    Output('cities-dropdown', 'options'),
    [Input('countries-dropdown', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-dropdown', 'value'),
    [Input('cities-dropdown', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-dropdown', 'value'),
     Input('cities-dropdown', 'value')])
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )


if __name__ == '__main__':
    app.run_server(debug=True)


"""
The first callback updates the available options in the second RadioItems 
component based off of the selected value in the first RadioItems component.

The second callback sets an initial value when the options property changes:
 it sets it to the first value in that options array.

The final callback displays the selected value of each component. 
If you change the value of the countries RadioItems component, 
Dash will wait until the value of the cities component is updated 
before calling the final callback. This prevents your callbacks 
from being called with inconsistent state like with "America" and "Montréal".

"""