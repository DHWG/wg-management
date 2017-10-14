FROM python:3.6.3

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y build-essential libpq-dev libjpeg-dev zlib1g-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/python", "wgaccounting/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
