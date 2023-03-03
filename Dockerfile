FROM python:3.11

RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install Flask

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install elasticsearch

EXPOSE 5000

COPY . .

CMD ["python", "app.py"]