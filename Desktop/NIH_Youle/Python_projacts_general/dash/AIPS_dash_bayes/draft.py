import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_canvas import DashCanvas
from dash_canvas.utils import (image_string_to_PILImage, array_to_data_url,
                               parse_jsonstring_line)
import urllib.request
from skimage import io,data
import tifffile as tfi

from controls.Bayes_nuc_control import Control_Channel_1
import os
import numpy as np

app = dash.Dash(__name__)

UPLOAD_DIRECTORY = "app_uploaded_files"


canvas_width = 250
img = io.imread(os.path.join(UPLOAD_DIRECTORY,'Composite.tif10.tif'))


app.layout = dbc.Container(
    [
    dbc.Row([
        dbc.Col([
                dbc.Label("Channel 1 detection"),
                Control_Channel_1
                ],width={"size": 4}),
        dbc.Col([
                DashCanvas(id='canvaas_image{}'.format(i),
                           tool='line',
                           lineWidth=5,
                           lineColor='red',
                           image_content=array_to_data_url(img[i,:,:]),
                           width=canvas_width)
                    for i in range(np.shape(img)[0])
                ],width={"size": 8})
        ])
    ],fluid=True)


if __name__ == '__main__':
    app.run_server()




