FROM python:3.9

WORKDIR selenium_tests

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN mkdir allure-results

COPY conftest.py .
COPY /pages ./pages
COPY /tests ./tests


CMD ["pytest", "./tests"]
