import dash_daq as daq
import dash
import dash.exceptions
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output, State

Control_Channel_1 = dbc.Card(
                    [html.Div
                        ([
                        dbc.Label("Object Size:"),
                        dcc.Slider(
                            id='Object_size',
                            min=0.01,
                            max=0.99,
                            step=0.01,
                            marks={i: '{}'.format(i) for i in [0.01,0.99]},
                            tooltip={"placement": "bottom", "always_visible": True},
                            value=0.9
                         ),
                        html.Br(),
                        html.Br(),
                        dbc.Label("Foreground Signal:"),
                        dcc.Slider(
                            id='Ch1_intensity',
                            min=0.000001,
                            max=0.9,
                            step=0.001,
                            marks={i: '{}'.format(i) for i in [0.000001, 0.9]},
                            tooltip={"placement": "bottom", "always_visible": True},
                            value=0.001
                        ),
                        html.Br(),
                        html.Br(),
                        dbc.Label("Remove small objects:"),
                        dcc.Slider(
                            id='rmv_object_nuc',
                            min=0.01,
                            max=0.99,
                            step=0.01,
                            marks={i: '{}'.format(i) for i in [0.01, 0.99]},
                            tooltip={"placement": "bottom", "always_visible": True},
                            value=0.9
                        ),
                        ]),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Label("Insert selected parameters:"),
                        dbc.Button(id = "load_Ch1_paramter",
                                  color="primary",
                                  className="mr-1")
                        ])