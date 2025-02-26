import base64
from pathlib import Path

from google.cloud import storage

import resume_assistant.consts as consts


def upload_to_gcs(user_resume_path, content=None):

    if content == None:
        root_dir = Path(__file__).resolve().parent.parent.parent.parent
        print("root_dir", root_dir)
        with open(f"{root_dir}/content_sample.txt", "r") as file:
            content = file.read()
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(consts.GCS_BUCKET_NAME)
    blob = bucket.blob(
        f"resume-assistant/data/input/dev/pdfs/{user_resume_path}")
    data_encode = content.encode("utf8").split(b";base64,")[1]
    data_decode = base64.decodebytes(data_encode)
    blob.upload_from_string(data_decode, content_type="application/pdf")
    return blob.public_url
