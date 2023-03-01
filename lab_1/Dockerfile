## Create Image with small size
FROM python:3.10-slim-buster AS venv
RUN apt-get -y update \
    && apt-get install -y curl build-essential \
    && rm -rf /var/lib/apt/lists/*

## install poetry and setting the PATH
ENV POETRY_VERSION=1.1.13
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

## Working Directory inside container
## COPY everything over the new container
WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN python -m venv --copies /app/venv
RUN . /app/venv/bin/activate && poetry install --no-dev

CMD ["poetry","add", "fastapi uvicorn requests pytest httpx isort black"]
RUN pip install --no-cache-dir importlib_resources

## Production env.
## Install dependences to support POETRY env.
FROM python:3.10-slim-buster as prod

## Copying env. from the previous built image
COPY --from=venv /app/venv /app/venv/
ENV PATH /app/venv/bin:$PATH

WORKDIR /app
COPY . ./

#HEALTHCHECK --start-period=30s CMD python -c "import requests; requests.get('http://localhost:8000', timeout=2)"

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
