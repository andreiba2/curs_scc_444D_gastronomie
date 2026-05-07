FROM python:3.9-slim
WORKDIR /app
# Copiem TOT ce este in folderul curent (inclusiv folderul app)
COPY . .
RUN pip install flask
EXPOSE 5000
CMD ["python", "gastronomie.py"]
