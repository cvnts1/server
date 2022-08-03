FROM python:3.10.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /server
ADD . /server
WORKDIR /server

RUN pip3 install -r requirements.txt 

CMD uvicorn app:server --host 0.0.0.0