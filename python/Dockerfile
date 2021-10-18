FROM python:3.8.2

WORKDIR /opt/app/

ADD main.py /opt/app/
COPY requirements.txt /opt/app/

RUN pip install -r requirements.txt


ENTRYPOINT [ "python", "./main.py" ]