from langchain_core.document_loaders.blob_loaders import Blob
from langchain_google_community import DocAIParser
import os
import time

from dotenv import load_dotenv
load_dotenv()


def get_langchain_docs(user_resume_path):

    GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
    DOC_PROCESSOR_NAME = os.getenv("DOC_PROCESSOR_NAME")

    parser = DocAIParser(location="us",
                         processor_name=DOC_PROCESSOR_NAME,
                         gcs_output_path="gs://{}/resume-assistant/data/output/dev/pdfs".format(GCS_BUCKET_NAME))
    inp_path = f"gs://{GCS_BUCKET_NAME}/resume-assistant/data/input/dev/pdfs/{user_resume_path}"
    blob = Blob(path=inp_path)
    operations = parser.docai_parse([blob])
    while parser.is_running(operations):
        time.sleep(0.5)
    results = parser.get_results(operations)
    docs = list(parser.parse_from_results(results))

    return docs
