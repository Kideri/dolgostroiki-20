FROM python:3.8-buster
WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

RUN useradd user

COPY . /app

# works like "cp scripts/* ."
COPY scripts .
RUN chown -R user:user /app
USER user
RUN chmod -R 777 /app
