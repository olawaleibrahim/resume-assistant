import requests
from bs4 import BeautifulSoup

import resume_assistant.models.model as model
import resume_assistant.application.rag.templates as templates
import resume_assistant.application.processing.postprocess as postprocess



def scrape_webpage_content(url):
    """Scrapes the entire content of the given webpage."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch page, status code: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    page_content = soup.get_text(separator='\n', strip=True)
    
    return page_content


def extract_job_description(webpage_content):
    chat_model = model.get_model()
    chain = templates.JOB_DESCR_TEMPLATE | chat_model 
    result = chain.invoke({"webpage_content": webpage_content})
    
    content_json = postprocess.get_json_from_result(result)
    return content_json["job_description"]



