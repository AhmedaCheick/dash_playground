import dash 
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)

def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)


"""
1.The "inputs" and "outputs" of this application interface are described
 declaratively through the app.callback decorator.

2.In Dash, the inputs and outputs of this application are simply 
the properties 
of a particular component. In this example, our input is the "value" 
property of the component that has the ID "my-id". Our output is the 
"children" property of the component with the ID "my-div".

3.Whenever an input property changes, the function that the callback
decorator wraps will get called automatically. 
Dash provides the function with the new value of the input property
as an input argument and Dash updates the property of the output 
component with whatever was returned by the function.

4.The component_id and component_property keywords are optional 
(there are only two arguments for each of those objects). 
I have included them here for clarity 
but I will omit them from here on out for brevity and readability.

5.Notice how we don't set a value for the children property of the my-div
component in the layout. When the Dash app starts, it automatically calls 
all of the callbacks with the initial values of the input components in order
to populate the initial state of the output components. In this example, 
if you specified something like html.Div(id='my-div', children='Hello world'),
it would get overwritten when the app starts.

It's sort of like programming with Microsoft Excel: 
whenever an input cell changes, all of the cells that depend on that cell 
will get updated automatically. This is called "Reactive Programming".
"""
