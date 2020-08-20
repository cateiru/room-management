FROM  python:3.8

COPY src /src
COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock

RUN pip install pipenv
RUN pipenv install --system --deploy
