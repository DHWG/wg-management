FROM python:3.6.3-alpine3.6

WORKDIR /usr/src/app

RUN apk add --update build-base postgresql-dev jpeg-dev zlib-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["/bin/sh", "start.sh"]
