FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /Disc_forum
WORKDIR /Disc_forum
ADD requirements.txt /Disc_forum/
RUN pip install -r requirements.txt
ADD .. /Disc_forum/