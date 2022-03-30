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
RUN apt-get update -qqy && apt-get install -qqy wget gnupg unzip
# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -qqy \
    && apt-get -qqy install google-chrome-stable \
    && rm /etc/apt/sources.list.d/google-chrome.list \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
# Install Chrome driver that is compatible with the installed version of Chrome
RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+) (\.[0-9]+){3}.*/\1/") \
    && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$ {CHROME_MAJOR_VERSION}") \
    && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
    && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/ chromedriver_linux64.zip \
    && unzip /tmp/chromedriver_linux64.zip -d /usr/bin \
    && rm /tmp/chromedriver_linux64.zip \
    && chmod 755 /usr/bin/chromedriver
COPY entrypoint-test.sh ./
COPY ./tests/ ./tests/
COPY ./tests_e2e/ ./tests_e2e/
COPY ./todo_app/ ./todo_app/
EXPOSE 5000
RUN chmod +x ./entrypoint-test.sh
ENTRYPOINT [ "poetry", "run", "pytest" ]