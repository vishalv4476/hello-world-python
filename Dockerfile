FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt


COPY . .

CMD ["python", "hello-world.py"]
