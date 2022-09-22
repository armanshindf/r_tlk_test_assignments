FROM python:3.9


WORKDIR /app

COPY ./ /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN python3 -m poetry install --no-root
RUN python3 -m poetry update 