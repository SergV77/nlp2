FROM python:3-onbuild

EXPOSE 5000

RUN mkdir /app
COPY . /app
WORKDIR /app 

CMD ["python", "./app.py"]
