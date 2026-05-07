FROM python:3.9-slim
WORKDIR /app
COPY gastronomie.py .
RUN pip install flask
EXPOSE 5000
CMD ["python", "gastronomie.py"]
