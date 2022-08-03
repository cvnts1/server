# Run tests and linter
FROM python:3.10.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /server
ADD ./app /server
WORKDIR /server/app

RUN pip3 install -r requirements.txt 

# Run tests
RUN pip3 install pylint pytest requests
RUN pylint $(pwd)
RUN pytest -o log_cli=true
RUN pip3 uninstall pylint pytest requests -y

CMD uvicorn app:server --host 0.0.0.0
