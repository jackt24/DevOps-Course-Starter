# setup
FROM python:3.9.9-buster as base-image

WORKDIR /project
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH = "${PATH}:/root/.poetry/bin"
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false --local && poetry install
RUN pip install gunicorn

# production build stage
FROM base-image as todo-prod
COPY entrypoint-prod.sh gunicorn_config.py ./
COPY ./todo_app ./todo_app
EXPOSE 5000
ENV PORT=5000
RUN chmod +x ./entrypoint-prod.sh 
ENTRYPOINT ["sh", "entrypoint-prod.sh"]

#ocal development stage 
FROM base-image as todo-dev
ENV FLASK_APP=app.py
COPY entrypoint-dev.sh ./
EXPOSE 5000
ENTRYPOINT ["sh", "entrypoint-dev.sh"]

# testing stage 
FROM base-image as test
# Install chrome and chromium webdriver
RUN apt-get update && \
    apt-get install -y gnupg wget curl unzip --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
    DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
    echo "Installing chromium webdriver version ${DRIVERVER}" &&\
    curl -sSL https://chromedriver.storage.googleapis.com/${DRIVERVER}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
    apt-get install unzip -y &&\
    unzip ./chromedriver_linux64.zip
COPY entrypoint-test.sh ./
COPY ./tests/ ./tests/
COPY ./tests_e2e/ ./tests_e2e/
COPY ./todo_app/ ./todo_app/
EXPOSE 5000
RUN chmod +x ./entrypoint-test.sh
ENTRYPOINT [ "poetry", "run", "pytest" ]