from dash import Dash, dcc, Output, Input, dash_table  
import dash_bootstrap_components as dbc  
from dash import html  
import plotly.express as px
import pandas as pd
from PIL import Image

# Import logos
pil_image1 = Image.open("cmu.png")
cmu_image = html.Img(src = pil_image1, height = '120', width = '180')
pil_image2 = Image.open("floor1.png")
floor_image = html.Img(src = pil_image2, height = '1200', width = '1200')

# Import data 
df = pd.read_csv('floor1.csv')

# Build components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytitle = dcc.Markdown(children = \
    '# **Real-time View of Rooms on the 1st Floor of Porter Hall**', 
    style={'textAlign': 'center'})

# Layouts
dashTable1 = dash_table.DataTable(
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'color': 'black',
        'backgroundColor': 'white'
    },
    style_cell={
        'width': '{}%'.format(len(df.columns)),
        'textOverflow': 'ellipsis',
        'overflow': 'hidden',
        'textAlign': 'center'
    },
    data = df.to_dict('records'), 
    columns= [{"name": i, "id": i} for i in df.columns],
    style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    }
    )

app.layout = html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col(cmu_image)
        ]),
    html.Br(),
    dbc.Row([mytitle]),
    html.Br(),
    dbc.Row([
        dbc.Col(floor_image),
        dbc.Col(dashTable1, width = 7)
        ])
    ])


# Run app
if __name__=='__main__':
    app.run_server(port=1609)