FROM python:3.8-slim

WORKDIR /consumer
COPY . /consumer

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/consumer"
ENV PATH "${PATH}:${PYTHONPATH}"

##############################################
RUN apt-get update 
# RUN apt-get install build-essential gcc g++ musl-dev unixodbc-dev -y
# RUN apt-get install libc-dev libxslt-dev libxml2-dev libffi-dev -y
RUN apt-get install build-essential -y
RUN pip install --upgrade pip
RUN pip install -r consumer/requirements.txt
##############################################


EXPOSE 5000

CMD ["python", "consumer/consumer.py"]