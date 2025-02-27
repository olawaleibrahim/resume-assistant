import plotly.express as px
from dash import Dash, Input, Output, callback, html, dcc, no_update
import time
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


data_canada = px.data.gapminder().query("country == 'Canada'")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Button("Start", id="custom-spinner-button", n_clicks=0),
        html.Hr(),
        dcc.Loading(
            [dcc.Graph(id="custom-spinner-output",
                       figure=px.line(data_canada, x="year", y="pop"))],
            overlay_style={"visibility": "visible",
                           "opacity": .5, "backgroundColor": "white"},
            custom_spinner=html.H2(
                ["My Custom Spinner", dbc.Spinner(color="danger")]),
        ),
    ]
)


@callback(
    Output("custom-spinner-output", "figure"),
    Input("custom-spinner-button", "n_clicks"),
)
def load_output(n):
    if n:
        time.sleep(1)
        return px.bar(data_canada, x="year", y="pop")
    return no_update


if __name__ == "__main__":
    app.run(debug=True)


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
                                                'Click or Drag and Drop to ',
                                                html.A('Upload your resume')
                                            ], id="upload-file",
                                                style={
                                                'width': '100%',
                                                'height': '100%',
                                                'lineHeight': '100%',
                                                'borderWidth': '100%',
                                                'borderStyle': 'dashed',
                                                'borderRadius': '1%',
                                                'textAlign': 'center',
                                                'color': '#ffffff',
                                            }),
                                        ], style={"height": "20%", "width": "100%"}),
                                        dcc.Loading([dbc.Row([
                                            html.H5("Job Description",
                                                    className="default-font"),
                                            html.Div(
                                                [], id="extracted-job-description"),
                                        ], className="content", style={"height": "60vh"})],
                                            overlay_style={
                                                "visibility": "visible", "opacity": .5, "backgroundColor": "white"},
                                            custom_spinner=html.H6(["loading job description", dbc.Spinner(color="successss")], className="default-font"),)
                                    ]),
                                ], className="main-card"),
                            ], width=3, className=""),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody([
                                        dcc.Loading([
                                            html.H3("ATS ASSISTANT"),
                                            dbc.Row([
                                                dbc.Col([
                                                    html.H6(
                                                        "Summary", className="default-font"),
                                                    html.Div(
                                                        [], id="summary"),
                                                ], className="content", style={"height": "95%"}, width=3),
                                                dbc.Col([
                                                    html.H6(
                                                        "Experience", className="default-font"),
                                                    html.Div(
                                                        [], id="experience"),
                                                ], className="content", style={"height": "95%"}, width=8),
                                            ], style={"height": "60vh"}),
                                            dbc.Row([
                                                dbc.Col([
                                                    html.H6(
                                                        "Skills", className="default-font"),
                                                    html.Div([], id="skills"),
                                                ], className="content", style={"height": "60%"}, width=3),
                                                dbc.Col([
                                                    html.H6(
                                                        "Missing Keywords", className="default-font"),
                                                    html.Div(
                                                        [], id="missing-keywords"),
                                                ], className="content", style={"height": "60%"}, width=4),
                                                dbc.Col([
                                                    html.H6(
                                                        "Changes Made", className="default-font"),
                                                    html.Div(
                                                        [], id="changes-made"),
                                                ], className="content", style={"height": "60%"}, width=4),
                                            ], style={"height": "20vh"})
                                        ],
                                            overlay_style={
                                            "visibility": "visible", "opacity": .5, "backgroundColor": "white"},
                                            custom_spinner=html.H3(["ATS Reviewing...", dbc.Spinner(
                                                color="successss")], className="default-font"),
                                        ),
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
