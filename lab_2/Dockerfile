ARG APP_DIR=/app

## Build env Image
FROM python:3.10-slim-buster AS build

ARG APP_DIR

RUN apt-get -y update \
    && apt-get install -y \
            curl \
            build-essential \
            libffi-dev \
    && rm -rf /var/lib/apt/lists/*

#RUN apk --no-cache add curl build-base libffi-dev


## install poetry and setting the PATH
ENV POETRY_VERSION=1.3.2
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH /root/.local/bin:$PATH

## Working Directory inside container
## COPY everything over the new container
WORKDIR ${APP_DIR}
COPY pyproject.toml poetry.lock ./

# copy over the venv and do not install dev/test libraries when we install poetry dependencies
RUN python -m venv --copies ${APP_DIR}/venv
RUN . ${APP_DIR}/venv/bin/activate 
#&& poetry install --no-dev

###################
## Dev Image
## Install dependences to support POETRY env.
FROM python:3.10-slim-buster as run
ARG APP_DIR

## Copying env. from the previous built image
COPY --from=build ${APP_DIR}/venv ${APP_DIR}/venv/
ENV PATH ${APP_DIR}/venv/bin:$PATH

WORKDIR ${APP_DIR}
COPY . ./

HEALTHCHECK --start-period=30s CMD python -c "import requests; requests.get('http://localhost:8000/health', timeout=2)"

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
