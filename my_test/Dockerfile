FROM python:3

EXPOSE 5000

RUN apt-get clean && apt-get update

ADD app.py /

CMD ["python", "./app.py"]