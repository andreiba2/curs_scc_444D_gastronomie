FROM python:3.11-slim
WORKDIR /app
COPY gastronomie.py .
COPY app/ ./app/
RUN pip install --no-cache-dir flask
EXPOSE 5000
CMD ["python3", "gastronomie.py"]
