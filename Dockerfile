FROM ubuntu:latest

RUN apt-get -y update
RUN apt install -y git
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv
ARG CACHEBUST=1
RUN git clone https://github.com/antontokm/Site.git
RUN python3 -m venv Site/env
RUN . ./Site/env/bin/activate
RUN pip3 install -r Site/requirements.txt
# RUN python3 Site/manage.py runserver