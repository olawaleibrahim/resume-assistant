import glob as glob
import dash
import dash_bootstrap_components as dbc
from dash import callback, no_update, dcc, html, Input, Output, State
import flask
from waitress import serve

from resume_assistant.application.dataset.extraction import (extract_job_description,
                                                             scrape_webpage_content)
from resume_assistant.application.dataset.upload import upload_to_gcs
import resume_assistant.application.processing.postprocess as postprocess
from resume_assistant.application.rag.retriever import get_langchain_docs
import resume_assistant.application.rag.templates as templates
from resume_assistant.application.rag.utils import extract_content_from_documents
from resume_assistant.models.model import get_model

from . import app as home_app


server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE,
                          dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
    server=server
)


index_page = home_app.content

app.title = "ATS Assistant"
app_states = html.Div([
    dcc.Store(id='node-questions', data=[]),
])


app.layout = dbc.Row([
    app_states,
    dcc.Location(id='url', refresh=False),
    dbc.Col([
        dbc.Row([

        ])
    ], width=12, id='page-content'),
])

page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(['Orange', 'Blue', 'Red'], 'Orange', id='page-2-radios'),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])


@app.callback(
    Output("extracted-job-description", "children"),
    Input("job-url", "value")
)
def update_job_description(url):

    if url:
        webpage_content = scrape_webpage_content(url)
        job_description = extract_job_description(webpage_content)
        return job_description
    else:
        return no_update


@app.callback(
    Output('summary', 'children'),
    Output('experience', 'children'),
    Output('skills', 'children'),
    Output('missing-keywords', 'children'),
    Output('changes-made', 'children'),
    Input('upload-file', 'contents'),
    Input('extracted-job-description', 'value'),
    State('upload-file', 'filename'),
)
def triggerATSApi(file_content, job_description, filename):

    ctx = dash.callback_context
    if filename and "upload-file" in ctx.triggered[0]["prop_id"]:
        public_url = upload_to_gcs(filename, file_content)
        documents = get_langchain_docs(filename)
        content = extract_content_from_documents(documents)
        chat_model = get_model()
        ats_chain = templates.ATS_TEMPLATE | chat_model
        ats_result = ats_chain.invoke({"job_description": job_description,
                                       "resume_content": content})

        json_ats_result = postprocess.get_json_from_result(ats_result)
        summary = json_ats_result["Summary"]
        experience = json_ats_result["Experience"]
        skills = json_ats_result["Skills"]
        missing_kws = json_ats_result["Missing Keywords"]
        changes_made = json_ats_result["Changes Made"]

        return summary, experience, skills, missing_kws, changes_made
    else:
        return no_update


@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    print("pathname", pathname)
    if pathname == '/home':
        return index_page
    elif pathname == "/page2":
        return page_2_layout
    else:
        return index_page


PORT = str(8080)

if __name__ == '__main__':
    print("start")
    serve(app.server, host='0.0.0.0', port=PORT,
          channel_timeout=500, threads=8)
