import glob as glob
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import flask


server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE,
                          dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
    server=server
)


app.title = "Beyond Abstracts"
title = app.title

main_content = dbc.Card(
    children=dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody([
                                        html.H6("Paste job ad link"),
                                        dbc.Row([
                                            dcc.Input(
                                                id="job-url",
                                                type="url",
                                            ),
                                            dbc.Row(),
                                            dcc.Upload([
                                                'Drag and Drop or ',
                                                html.A('Upload your resume')
                                            ], id="upload-file",
                                                style={
                                                'width': '100%',
                                                'height': '100%',
                                                'lineHeight': '100%',
                                                'borderWidth': '100%',
                                                'borderStyle': 'dashed',
                                                'borderRadius': '1%',
                                                'textAlign': 'center'
                                            }),
                                        ], style={"height": "20%", "width": "100%"}),
                                        dbc.Row([
                                            html.H5("Job Description"),
                                            html.Div(
                                                [], id="extracted-job-description"),
                                        ], className="content", style={"height": "55vh"}),
                                        html.Button(
                                            "Assist", id="assist-button", style={"width": "30%"}),
                                    ]),
                                ], className="main-card"),
                            ], width=3, className=""),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody([
                                        html.H3("ATS ASSISTANT"),
                                        dbc.Row([
                                            dbc.Col([
                                                html.H6("Summary"),
                                                html.Div(
                                                    [""""""], id="summary"),
                                            ], className="content", style={"height": "95%"}, width=3),
                                            dbc.Col([
                                                html.H6("Experience"),
                                                html.Div([], id="experience"),
                                            ], className="content", style={"height": "95%"}, width=8),
                                        ], style={"height": "60vh"}),
                                        dbc.Row([
                                            dbc.Col([
                                                html.H6("Skills"),
                                                html.Div([], id="skills"),
                                            ], className="content", style={"height": "60%"}, width=3),
                                            dbc.Col([
                                                html.H6("Missing Keywords"),
                                                html.Div(
                                                    [], id="missing-keywords"),
                                            ], className="content", style={"height": "60%"}, width=4),
                                            dbc.Col([
                                                html.H6("Changes Made"),
                                                html.Div(
                                                    [], id="changes-made"),
                                            ], className="content", style={"height": "60%"}, width=4),
                                        ], style={"height": "20vh"}),
                                    ]),
                                ], className="main-card"),], width=9, className=""),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ], style={"background-color": "#07141F"})
)


content = html.Div([html.H1(id='page-title', style={'padding-left': '1%', 'padding-top': '1%'}),
                    html.Div([html.Div([main_content], style={'padding': '1% !important', 'width': '100%'}),])],
                   className='app-content-div',
                   )


app.layout = html.Div(
    [
        # dcc.Store(id='timestamp', storage_type='memory', data=timestamp),
        dbc.Row([
            dbc.Col([
                html.Div(
                    [
                        dash.page_container,
                        main_content
                    ],
                    className="content",
                ),
            ], width=12)
        ],
            style={"background-color": "#07141F"})
    ])
