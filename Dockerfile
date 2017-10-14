FROM python:3.6.3

WORKDIR /usr/src/app

RUN apt-get install -y build-essential postgresql-dev jpeg-dev zlib-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/python", "wgaccounting/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
