FROM python:3.8-slim

WORKDIR /producer/
COPY . /producer

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/producer:/producer/base"
ENV PATH "${PATH}:${PYTHONPATH}"

##############################################
RUN apt-get update 
# RUN apt-get install build-essential gcc g++ musl-dev unixodbc-dev -y
# RUN apt-get install libc-dev libxslt-dev libxml2-dev libffi-dev -y
RUN apt-get install build-essential -y
RUN pip install --upgrade pip
RUN pip install -r producer/requirements.txt
##############################################


EXPOSE 5000

CMD ["gunicorn", "-w", "2", "--bind", "0.0.0.0:5000", "producer.producer:app"]