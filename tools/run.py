from datetime import datetime as dt
from pathlib import Path

import click
from loguru import logger

from pipelines import (get_job_description_pipeline, 
                       extract_resume_pipeline)


@click.command(
    help="""
Resume Assistant project CLI v0.0.1. 

Main entry point for the pipeline execution. 
This entrypoint is where everything comes together.


Run a pipeline with the required parameters. 

Examples:

  \b
  # Run the pipeline with default options
  python run.py
               
  \b
  # Run the pipeline without cache
  python run.py --no-cache
  

"""
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable caching for the pipeline run.",
)
@click.option(
    "--run-get-job-description",
    is_flag=True,
    default=False,
    help="Whether to run the scrape job description pipeline.",
)
@click.option(
    "--run-extract-resume-content",
    is_flag=True,
    default=False,
    help="Whether to run the extract resume content pipeline.",
)
@click.option(
    "--url",
    default="https://job-boards.greenhouse.io/scaleai/jobs/4413274005",
    help="Filename of the ETL config file.",
)
@click.option(
    "--user-resume-path",
    default="Olawale_Machine_Learning_Engineer_Template.pdf",
    help="Filename of user resume",
)
def main(
    no_cache: bool = False,
    run_get_job_description: bool = False,
    run_extract_resume_content: bool = False,
    url: str = "https://job-boards.greenhouse.io/scaleai/jobs/4413274005",
    user_resume_path: str = "Olawale_Machine_Learning_Engineer_Template.pdf",
) -> None:
    assert (
        run_get_job_description
        or run_extract_resume_content
    ), "Please specify an action to run."


    root_dir = Path(__file__).resolve().parent.parent

    if run_get_job_description:
        job_description = get_job_description_pipeline(url)
        print(job_description)

    if run_extract_resume_content:
        resume_content = extract_resume_pipeline(user_resume_path)
        print(resume_content)


if __name__ == "__main__":
    main()