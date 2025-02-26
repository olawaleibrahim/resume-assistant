import os
from dotenv import load_dotenv
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
INDEX_NAME = os.getenv("INDEX_NAME")
INDEX_ID = os.getenv("INDEX_ID")
DB_USER= os.getenv("CLOUD_SQL_USER1")
DB_PASS = os.getenv("CLOUD_SQL_PASSWORD")
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
DOC_PROCESSOR_NAME = os.getenv("DOC_PROCESSOR_NAME")