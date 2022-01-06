FROM python:3.9.9-buster as base-image

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    bash \
    curl \
    && mkdir project
WORKDIR /project
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH = "${PATH}:/root/.poetry/bin"
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false --local && poetry install
RUN pip install gunicorn

FROM base-image as todo-prod
COPY entrypoint-prod.sh gunicorn_config.py ./
COPY ./todo_app/*.py ./project/todo_app
COPY ./todo_app/templates/ ./project/todo_app/templates/
EXPOSE 5000
ENV PORT=5000
RUN chmod +x ./entrypoint-prod.sh 
ENTRYPOINT ["sh", "entrypoint-prod.sh"]

FROM base-image as todo-dev
RUN cd todo_app
ENV FLASK_APP=app.py
RUN pip install flask
COPY entrypoint-dev.sh ./
EXPOSE 5000
ENTRYPOINT ["sh", "entrypoint-dev.sh"]
