FROM python:latest
WORKDIR /usr/src/sreality-scraper
COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .
CMD ["scrapy", "crawl", "sreality"]
