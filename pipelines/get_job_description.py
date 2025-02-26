from resume_assistant.application.dataset.extraction import extract_job_description, scrape_webpage_content


def get_job_description_pipeline(url):
    webpage_content = scrape_webpage_content(url)
    job_description = extract_job_description(webpage_content)
    print(job_description)
    return job_description
