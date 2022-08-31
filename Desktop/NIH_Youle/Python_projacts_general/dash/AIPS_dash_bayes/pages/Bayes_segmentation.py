import dash
dash.register_page(__name__,path='/')
from dash_extensions.enrich import Dash, Output, Input, State, ServersideOutput
from dash import  html, dcc, callback
import dash_bootstrap_components as dbc
import dash_daq as daq
import json
from utils import AIPS_functions as af
from utils import AIPS_module as ai
import numpy as np
from PIL import Image
import plotly.express as px

import dash_canvas
from dash_canvas import DashCanvas
from dash_canvas.components import image_upload_zone
from dash_canvas.utils import (
    image_string_to_PILImage,
    array_to_data_url,
    parse_jsonstring_line,
    brightness_adjust,
    contrast_adjust,
)

UPLOAD_DIRECTORY = "/app_uploaded_files"

layout = html.Div([
    dbc.Alert(id='alert_display', is_open=False)
    ])

app = dash.Dash(__name__)

filename = 'https://github.com/gkanfer/AIPS_dash_final_old/blob/main/app_uploaded_files/Composite.tif10.tif'
canvas_width = 500


app.layout = html.Div([
    DashCanvas(id='canvaas_image',
               tool='line',
               lineWidth=5,
               lineColor='red',
               filename=filename,
               width=canvas_width)
    ])