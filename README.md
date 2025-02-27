# Resume Assistant

This is a sample project on building an LLM poc application using the langchain and google SDK.

### Installation

- Clone the repository

```bash
git clone git@github.com:olawaleibrahim/resume-assistant.git
cd resume-assistant
```

- Setup environment with poetry

```bash
poetry init
poetry install
```

### Setp up the following resources on Google Cloud Platform (GCP) and activate corresponding APIs

- **VertexAI**: For using Google's foundation models, in this case, Gemini-flash for the LLM logic https://console.cloud.google.com/vertex-ai
- **Google Cloud Storage**: https://console.cloud.google.com/ (used for creating storage buckets) https://console.cloud.google.com/storage
- **Cloud Build**: For building docker images and repositories https://console.cloud.google.com/cloud-build
- **Artifact Registry**: For storing built docker images and repositories https://console.cloud.google.com/artifacts
- **Cloud Run**: For deploying built docker image https://console.cloud.google.com/run
- **Document AI**: Used in the retrieval step for processing pdfs https://console.cloud.google.com/ai/document-ai

#### Setp up .env file with following GCP variables

- PROJECT_NAME=
- PROJECT_ID=
- REGION=
- INDEX_NAME=
- INDEX_ID=
- CLOUD_SQL_NAME=
- CLOUD_SQL_USER=
- CLOUD_SQL_PASSWORD=
- DATABASE_NAME=
- GCS_BUCKET_NAME=
- DOC_PROCESSOR_NAME=

### Pipelines and commands

There are two pipelines (with multi steps) in this project defined under the poe tasks in the pyproject.toml file

- **run-get-job-description**: which scrapes the job web page then makes an LLM call to extract just the exact job description

To run:

```bashrc
poetry poe run-get-job-description
```

- **run-extract-resume-content**: loads and ingest the resume context into langchain documents

To run:

```bashrc
poetry poe run-extract-resume-content
```

### Start application/frontend

**Locally**

To run:

```bashrc
poetry poe run-frontend
```

#### Deploy to Cloud Run

**Note** Ensure that port is set to default 8080 in index.py to run on CLoud Run

Configure Docker to use your Artifact Registry credentials when interacting with Artifact Registry. (You are only required to do this once.)

```bashrc
poetry poe run un-configure-registry
```

#### Build docker image

```bashrc
poetry poe run-build
```

Go to https://console.cloud.google.com/run to use built docker image for app deployment
