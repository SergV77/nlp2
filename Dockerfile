FROM python:3.7-slim-buster

WORKDIR /app

EXPOSE 5000

COPY ./my_test/requirements.txt requirements.txt
RUN pip install -r requirements.txt


ARG TENSORFLOW_VERSION=1.13.1
ARG TENSORFLOW_DEVICE=gpu
ARG TENSORFLOW_APPEND=_gpu
RUN pip3 --no-cache-dir install https://storage.googleapis.com/tensorflow/linux/${TENSORFLOW_DEVICE}/tensorflow${TENSORFLOW_APPEND}-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl

# install Keras for Python 3
ARG KERAS_VERSION=2.2.4
ENV KERAS_BACKEND=tensorflow
RUN pip3 --no-cache-dir install --no-dependencies git+https://github.com/fchollet/keras.git@${KERAS_VERSION}


COPY ./my_test .
RUN ls -l



CMD ["python3", "./app.py"]
