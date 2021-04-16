FROM python:3.7-slim-buster

WORKDIR /app

EXPOSE 5000

COPY ./my_test/requirements.txt requirements.txt
RUN pip install -r requirements.txt



COPY ./my_test .
RUN ls -l



CMD ["python3", "./app.py"]
