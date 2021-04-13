FROM python:3

EXPOSE 5000

RUN apt-get update -y
RUN apt-get install -y python-pip

RUN pip install -r requirements.txt

ADD app.py /

CMD ["python", "./app.py"]