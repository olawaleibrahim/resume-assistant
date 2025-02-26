from resume_assistant.application.dataset.upload import upload_to_gcs
from resume_assistant.application.rag.retriever import get_langchain_docs
from resume_assistant.application.rag.utils import extract_content_from_documents


def extract_resume_pipeline(user_resume_path, content=None):
    public_url = upload_to_gcs(user_resume_path, content)
    documents = get_langchain_docs(user_resume_path)
    content = extract_content_from_documents(documents)
    return content
