FROM python:3.11

RUN apt update || apt upgrade

RUN mkdir /telebot

WORKDIR /telebot

COPY ./core ./core
COPY ./bot.py ./bot.py
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]
