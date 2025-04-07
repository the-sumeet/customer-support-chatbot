FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt



RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install "fastapi[standard]"


COPY ./src /app/src


CMD ["fastapi", "run", "src/main.py", "--port", "5000"]