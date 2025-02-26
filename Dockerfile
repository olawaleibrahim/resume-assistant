FROM python:3.11-slim-bullseye AS release

ENV WORKSPACE_ROOT=/app/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3
ENV DEBIAN_FRONTEND=noninteractive
ENV POETRY_NO_INTERACTION=1

# Install other system dependencies.
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends build-essential \
    gcc \
    python3-dev \
    build-essential \
    libglib2.0-dev \
    libnss3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry using pip and clear cache
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"
RUN poetry config installer.max-workers 20

WORKDIR $WORKSPACE_ROOT

# Copy the poetry lock file and pyproject.toml file to install dependencies
COPY pyproject.toml requirements.txt $WORKSPACE_ROOT


# RUN poetry run pip install -r requirements.txt
RUN poetry install

# Copy the rest of the code.
COPY . $WORKSPACE_ROOT

CMD ["sh", "entrypoint.sh"]
