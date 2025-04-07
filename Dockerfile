FROM python:3.11

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock


RUN pip install poetry
RUN pip install "fastapi[standard]"
RUN poetry install --no-root


COPY ./src /code/src


CMD ["fastapi", "run", "src/main.py", "--port", "5000"]