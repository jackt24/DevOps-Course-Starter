# FROM python:3.9.9-buster
FROM python:3.8-slim-buster as base-image
# setup poetry and environment
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    bash \
    curl \
    && mkdir /code
WORKDIR /code
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH = "${PATH}:/root/.poetry/bin"

# install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false --local && poetry install

FROM base-image as todo-prod
# copy app code and run gunicorn
COPY entrypoint-prod.sh gunicorn_config.py ./
COPY ./todo_app/*.py ./todo_app/
# statuses?
# COPY ./todo_app/statuses.json ./todo_app/
COPY ./todo_app/templates/ ./todo_app/templates/
EXPOSE 5000
ENV PORT=5000
RUN chmod +x ./entrypoint-prod.sh 
ENTRYPOINT ["sh", "entrypoint-prod.sh"]

# FROM base-image as todo-dev
# # copy entrypoint script and run
# COPY entrypoint-dev.sh ./
# EXPOSE 5000
# RUN chmod +x ./entrypoint-dev.sh
# ENTRYPOINT ["sh", "entrypoint-dev.sh"]