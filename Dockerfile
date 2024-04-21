FROM python:3.9-slim

WORKDIR /app

COPY main.py paragraphs.txt ./

RUN pip install --no-cache-dir nltk && \
    python -m nltk.downloader stopwords

CMD ["python", "main.py"]
