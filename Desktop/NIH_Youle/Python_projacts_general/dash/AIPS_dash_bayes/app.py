import dash_labs as dl
import json
import dash
from dash import ALL, callback_context
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Dash, Output, Input, State, ServersideOutput
import tifffile as tfi
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
from PIL import Image
import plotly.express as px
import pathlib
import base64
import pandas as pd
import io
from io import BytesIO
import re
from utils.controls import controls, controls_nuc, controls_cyto, upload_parm
from utils.Dash_functions import parse_contents
from utils import AIPS_functions as af
from utils import AIPS_module as ai
import pathlib
import dash_canvas
from dash_canvas.components import image_upload_zone
from dash_canvas.utils import (
    image_string_to_PILImage,
    array_to_data_url,
    parse_jsonstring_line,
    brightness_adjust,
    contrast_adjust,
)

UPLOAD_DIRECTORY = "/app_uploaded_files"

app = dash.Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.JOURNAL, dbc.icons.FONT_AWESOME],
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True
)

nav_bar = dbc.Nav([
                dbc.NavItem(dbc.NavLink('Bayes segmentation',id='Bayes', href=dash.page_registry['pages.Bayes_segmentation']['path']))
                    ])

app.layout = dbc.Container(
    [
        html.H1("Optical Pooled Cell Sorting Platform",className='header'),
        html.Hr(),
        html.Br(),
        nav_bar,
        dl.plugins.page_container,
     ],
fluid=True)


if __name__ == "__main__":
    app.run_server()



