def extract_content_from_documents(documents):

    content = ""
    for document in documents:
        content+=document.page_content
    return content

