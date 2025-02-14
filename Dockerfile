FROM python:3.11.7-slim-buster

WORKDIR /app

COPY ./app

RUN pip install -r requirements.txt

CMD ["python3","app.py"]