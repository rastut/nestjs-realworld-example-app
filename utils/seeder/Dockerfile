FROM python:3.9.7-slim-buster
WORKDIR /code
RUN apt update && apt install -y \
  libpq-dev \
  gcc \
  && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
COPY . .
CMD ["python", "main.py"]
