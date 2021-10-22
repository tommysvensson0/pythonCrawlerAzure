FROM python:3.6

WORKDIR /app

#ADD requirements.txt /app/requirements.txt
RUN pip install typeshed-client
RUN pip install beautifulsoup4

ADD . /app

CMD ["python", "crawler.py"]